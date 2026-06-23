from pathlib import Path
from PySide6.QtWidgets import QMessageBox
import sys
import math

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.gp import gp_Pln, gp_Pnt, gp_Dir,gp_Trsf
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Section
from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopAbs import TopAbs_EDGE
from OCC.Core.TopoDS import TopoDS_Shape, topods
from OCC.Core.BRepAdaptor import BRepAdaptor_Curve
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Core.GCPnts import GCPnts_AbscissaPoint

ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = ROOT.parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.python.config.dataclass import GUIData
from pages.message_box import MessageBox

class Cutprocess_step():
    def __init__(self, ui, data : GUIData):
        self.ui = ui
        self.data = data
        self.ui.cut_process_btn.clicked.connect(self.run_cut_process)
        self.ui.create_traj_btn.clicked.connect(self.create_traj)
        self.step = self.data.sken_step
        self.half_points = np.empty((0, 3))
    def create_traj(self):
        if not hasattr(self, "half_points") or self.half_points is None or len(self.half_points) == 0:
            MessageBox.show(
                parent=self.ui.centralwidget,
                title="Chyba",
                text="Nejdříve je potřeba vygenerovat body řezu.",
                icon=QMessageBox.Warning
            )
            return

        self.plot_section_points_2d_xy(show_line=True)
    def load_step_shape(self):
        self.model_path = self.data.model_path
        if not Path(self.model_path).is_file():
            MessageBox.show(
                parent=self.ui.centralwidget,
                title="Nesprávný vstup",
                text=f"Soubor nenalezen: {self.model_path}",
                icon=QMessageBox.Critical
            )
            raise FileNotFoundError(f"Soubor nenalezen: {self.model_path}")

        base, _ = os.path.splitext(self.model_path)
        self.step_path = base + ".step"

        if not Path(self.step_path).is_file():
            MessageBox.show(
                parent=self.ui.centralwidget,
                title="Nesprávný vstup",
                text=f"STEP soubor nenalezen: {self.step_path}",
                icon=QMessageBox.Critical
            )
            raise FileNotFoundError(f"STEP soubor nenalezen: {self.step_path}")

        reader = STEPControl_Reader()
        status = reader.ReadFile(str(self.step_path))

        if status != IFSelect_RetDone:
            MessageBox.show(
                parent=self.ui.centralwidget,
                title="Chyba",
                text=f"STEP soubor se nepodařilo načíst: {self.step_path}",
                icon=QMessageBox.Critical
            )
            raise RuntimeError(f"STEP soubor se nepodařilo načíst: {self.step_path}")

        reader.TransferRoots()
        shape = reader.OneShape()

        if shape.IsNull():
            MessageBox.show(
                parent=self.ui.centralwidget,
                title="Chyba",
                text=f"Načtený STEP model je prázdný: {self.step_path}",
                icon=QMessageBox.Critical
            )
            raise RuntimeError("Načtený STEP model je prázdný.")

        shape = self.transform_shape(shape)

        print("shape po transformaci:", shape)
        print("type(shape):", type(shape))
        print("is TopoDS_Shape:", isinstance(shape, TopoDS_Shape))
        print("shape.IsNull():", shape.IsNull())

        return shape
    def transform_shape(self,shape):
        """
        Transformace shapu pomocí matice 4x4 z classy LoadModel()
        """
        self.model_transform_matrix = self.data.transform_matrix
        self.model_position = self.data.position_model
        transform = np.asarray(self.model_transform_matrix,dtype=float)
        if transform.shape !=(4,4):
            MessageBox.show(parent=self.ui.centralwidget,title="Chyba",text="Chyba při tvorvě userframu na předchozí stránce",icon=QMessageBox.Warning)

        step_trans = gp_Trsf()

        step_trans.SetValues(
            float(transform[0,0]), float(transform[0,1]), float(transform[0,2]), float(transform[0,3]),
            float(transform[1,0]), float(transform[1,1]), float(transform[1,2]), float(transform[1,3]),
            float(transform[2,0]), float(transform[2,1]), float(transform[2,2]), float(transform[2,3])
        )   

        transformed = BRepBuilderAPI_Transform(shape,step_trans,True)
        transformed_shape = transformed.Shape()

        if transformed_shape.IsNull():
            MessageBox.show(parent=self.ui.centralwidget,title="Chyba",text="Transformace řezu selhala",icon=QMessageBox.critical)

        return transformed_shape
    def section_shape_with_plane(
        self,
        shape,
        origin,
        normal
    ):
        """
        Provede řez STEP shape rovinou.
        Vrací TopoDS_Shape obsahující hrany řezu.
        """

        origin = np.asarray(origin, dtype=float)
        normal = np.asarray(normal, dtype=float)

        normal_norm = np.linalg.norm(normal)

        if normal_norm <= 1e-12:
            raise ValueError("Normála roviny má nulovou délku.")

        normal = normal / normal_norm

        plane = gp_Pln(
            gp_Pnt(float(origin[0]), float(origin[1]), float(origin[2])),
            gp_Dir(float(normal[0]), float(normal[1]), float(normal[2]))
        )

        section = BRepAlgoAPI_Section(shape, plane,False)
        section.ComputePCurveOn1(True)
        section.Approximation(True)
        section.Build()

        if not section.IsDone():
            MessageBox.show(parent=self.ui.centralwidget,title="Chyba",text="Řez se nepodařilo vytvořit.",icon=QMessageBox.Critical)
            raise RuntimeError("Řez se nepodařilo vytvořit.")

        result_shape = section.Shape()

        if result_shape.IsNull():
            return None

        return result_shape

    def extract_edges_from_section(self, section_shape):
        """
        Z výsledku řezu vytáhne jednotlivé TopoDS_Edge.
        """

        edges = []

        explorer = TopExp_Explorer(
            section_shape,
            TopAbs_EDGE
        )

        while explorer.More():
            edge = topods.Edge(explorer.Current())
            edges.append(edge)
            explorer.Next()

        return edges
    def point_to_array(self, pnt):
        return np.array([pnt.X(), pnt.Y(), pnt.Z()], dtype=float)
    def get_edge_endpoints(self, edge):
        """
        Vrátí počáteční a koncový bod edge.
        """

        curve = BRepAdaptor_Curve(edge)

        first_param = curve.FirstParameter()
        last_param = curve.LastParameter()

        p_start = self.point_to_array(curve.Value(first_param))
        p_end = self.point_to_array(curve.Value(last_param))

        return p_start, p_end
    def approx_edge_length(self, edge, samples: int = 100):
        """
        Spočítá se délka jedné křivky na celé kontuře nalezne se přibližně 200 bodů 
        """

        curve = BRepAdaptor_Curve(edge)

        first_param = curve.FirstParameter()
        last_param = curve.LastParameter()

        params = np.linspace(first_param, last_param, samples)

        points = []

        for u in params:
            pnt = curve.Value(float(u))
            points.append([
                pnt.X(),
                pnt.Y(),
                pnt.Z()
            ])

        points = np.asarray(points, dtype=float)

        if len(points) < 2:
            return 0.0

        diffs = points[1:] - points[:-1]
        lengths = np.linalg.norm(diffs, axis=1)

        return float(np.sum(lengths))
    def edge_to_polyline(
        self,
        edge,
        reversed_edge: bool = False,
        tolerance: float = 1e-7
    ):
        """
        Převede jednu CAD edge na body po kroku self.step.

        Důležité:
        - vždy zachová začátek edge,
        - vždy zachová konec edge,
        - body mezi nimi rozmístí podle délky edge,
        - tím pádem nezmizí rohy kontury.
        """

        if self.step <= 0:
            raise ValueError("Krok musí být větší než 0.")

        adaptor = BRepAdaptor_Curve(edge)

        first_param = adaptor.FirstParameter()
        last_param = adaptor.LastParameter()

        try:
            edge_length = GCPnts_AbscissaPoint.Length(adaptor)
        except Exception:
            return np.empty((0, 3))

        if edge_length <= tolerance:
            p = adaptor.Value(first_param)
            pts = np.array([[p.X(), p.Y(), p.Z()]], dtype=float)

            if reversed_edge:
                pts = pts[::-1].copy()

            return pts

        # Počet úseků na hraně.
        # ceil zajistí, že skutečný rozestup nebude větší než self.step.
        n_segments = max(1, int(math.ceil(edge_length / self.step)))

        # Skutečný krok po této konkrétní hraně.
        # Bude <= self.step a konec edge vždy vyjde přesně.
        actual_step = edge_length / n_segments

        points = []

        for i in range(n_segments + 1):
            if i == 0:
                param = first_param

            elif i == n_segments:
                param = last_param

            else:
                distance = i * actual_step

                try:
                    param = GCPnts_AbscissaPoint(
                        adaptor,
                        distance,
                        first_param
                    ).Parameter()
                except Exception:
                    continue

            p = adaptor.Value(param)

            points.append([
                p.X(),
                p.Y(),
                p.Z()
            ])

        pts = np.asarray(points, dtype=float)

        if reversed_edge:
            pts = pts[::-1].copy()

        return pts
    def build_contours_from_edges(self, edges, tolerance: float = 1e-5):
        """
        Složí jednotlivé edge do souvislých kontur podle návaznosti koncových bodů.

        Vrací list kontur.
        Každá kontura je list položek:
        {
            "edge": edge,
            "reversed": bool
        }
        """

        remaining = []

        for edge in edges:
            p_start, p_end = self.get_edge_endpoints(edge)

            remaining.append({
                "edge": edge,
                "start": p_start,
                "end": p_end
            })

        contours = []

        while remaining:
            first_item = remaining.pop(0)

            contour = [
                {
                    "edge": first_item["edge"],
                    "reversed": False
                }
            ]

            contour_start = first_item["start"]
            contour_end = first_item["end"]

            closed = False

            while remaining:
                best_idx = None
                best_reverse = False
                best_dist = None

                for i, item in enumerate(remaining):
                    dist_start = np.linalg.norm(item["start"] - contour_end)
                    dist_end = np.linalg.norm(item["end"] - contour_end)

                    if dist_start <= tolerance:
                        candidate_dist = dist_start
                        candidate_reverse = False
                    elif dist_end <= tolerance:
                        candidate_dist = dist_end
                        candidate_reverse = True
                    else:
                        continue

                    if best_dist is None or candidate_dist < best_dist:
                        best_idx = i
                        best_reverse = candidate_reverse
                        best_dist = candidate_dist

                if best_idx is None:
                    break

                next_item = remaining.pop(best_idx)

                contour.append({
                    "edge": next_item["edge"],
                    "reversed": best_reverse
                })

                if best_reverse:
                    contour_end = next_item["start"]
                else:
                    contour_end = next_item["end"]

                if np.linalg.norm(contour_end - contour_start) <= tolerance:
                    closed = True
                    break

            contours.append({
                "edges": contour,
                "closed": closed,
                "start": contour_start,
                "end": contour_end
            })

        return contours
    def contour_to_step_polyline(
        self,
        contour,
        tolerance: float = 1e-5,
        remove_closing_duplicate: bool = True
    ):
        """
        Převede složenou konturu na body po kroku self.step.

        Na rozdíl od globálního resamplingu vzorkuje každou edge zvlášť,
        takže zůstanou zachované rohy.
        """

        all_pts = []

        for edge_item in contour["edges"]:
            edge = edge_item["edge"]
            reversed_edge = edge_item["reversed"]

            edge_pts = self.edge_to_polyline(
                edge=edge,
                reversed_edge=reversed_edge,
                tolerance=tolerance
            )

            if edge_pts.size == 0:
                continue

            if len(all_pts) == 0:
                all_pts.extend(edge_pts)

            else:
                last_point = np.asarray(all_pts[-1], dtype=float)
                first_new = edge_pts[0]

                # Pokud je první bod nové edge stejný jako poslední bod předchozí edge,
                # nepřidáme ho znovu.
                if np.linalg.norm(last_point - first_new) <= tolerance:
                    all_pts.extend(edge_pts[1:])
                else:
                    all_pts.extend(edge_pts)

        if len(all_pts) < 2:
            return np.empty((0, 3))

        pts = np.asarray(all_pts, dtype=float)

        # U uzavřené kontury může být poslední bod stejný jako první.
        # Pro trajektorii ho většinou nechceš dvakrát.
        if contour["closed"] and remove_closing_duplicate:
            if np.linalg.norm(pts[0] - pts[-1]) <= tolerance:
                pts = pts[:-1]

        return pts
    def resample_polyline_by_step(
        self,
        polyline: np.ndarray,
        closed: bool = True,
        tolerance: float = 1e-5
    ):
        """
        Převzorkuje celou konturu podle skutečné kumulativní délky polyline.

        Tady už se nevzorkuje každá edge zvlášť.
        Vzorkuje se celá složená kontura najednou.
        """

        if self.step <= 0:
            raise ValueError("Krok musí být větší než 0.")

        pts = np.asarray(polyline, dtype=float)

        if len(pts) < 2:
            return np.empty((0, 3))

        if closed:
            if np.linalg.norm(pts[0] - pts[-1]) > tolerance:
                pts = np.vstack([pts, pts[0]])

        segment_vectors = pts[1:] - pts[:-1]
        segment_lengths = np.linalg.norm(segment_vectors, axis=1)

        valid = segment_lengths > 1e-12

        segment_vectors = segment_vectors[valid]
        segment_lengths = segment_lengths[valid]
        pts_start = pts[:-1][valid]

        if len(segment_lengths) == 0:
            return np.empty((0, 3))

        total_length = float(np.sum(segment_lengths))

        if total_length <= 1e-12:
            return np.empty((0, 3))

        distances = np.arange(0.0, total_length, self.step)

        cumulative_lengths = np.insert(
            np.cumsum(segment_lengths),
            0,
            0.0
        )

        sampled_points = []

        for d in distances:
            seg_idx = np.searchsorted(cumulative_lengths, d, side="right") - 1

            if seg_idx >= len(segment_lengths):
                seg_idx = len(segment_lengths) - 1

            seg_len = segment_lengths[seg_idx]

            if seg_len <= 1e-12:
                continue

            local_t = (d - cumulative_lengths[seg_idx]) / seg_len

            new_point = pts_start[seg_idx] + local_t * segment_vectors[seg_idx]
            sampled_points.append(new_point)

        return np.asarray(sampled_points, dtype=float)
    def generate_section_contour_points(
        self,
        planes: list[dict],
        export_csv_path: str | Path | None = None,
        contour_tolerance: float = 1e-5,
        dense_factor: int = 5
    ):
        """
        Načte STEP model, provede řezy rovinami, složí edge do kontur
        a vygeneruje body po celé kontuře podle kroku.

        planes example:
        [
            {
                "origin": [0, 0, 50],
                "normal": [0, 0, 1]
            }
        ]
        """

        if self.step <= 0:
            raise ValueError("Krok musí být větší než 0.")

        shape = self.load_step_shape()
        print("shape:", shape)
        print("type(shape):", type(shape))
        print("is TopoDS_Shape:", isinstance(shape, TopoDS_Shape))
        # if apply_transform and self.model_transform_matrix is not None:
        #     shape = self.transform_shape_by_matrix(
        #         shape=shape            )

        all_points = []

        for plane_id, plane in enumerate(planes):
            origin = np.asarray(plane["origin"], dtype=float)
            normal = np.asarray(plane["normal"], dtype=float)

            normal_norm = np.linalg.norm(normal)

            if normal_norm <= 1e-12:
                raise ValueError(f"Normála roviny {plane_id} má nulovou délku.")

            normal = normal / normal_norm

            section_shape = self.section_shape_with_plane(shape,origin,normal)

            if section_shape is None:
                print(f"Rovina {plane_id}: řez je prázdný.")
                continue

            edges = self.extract_edges_from_section(section_shape)

            if len(edges) == 0:
                print(f"Rovina {plane_id}: řez neobsahuje žádné hrany.")
                continue

            contours = self.build_contours_from_edges(
                edges=edges,
                tolerance=contour_tolerance
            )

            if len(contours) == 0:
                print(f"Rovina {plane_id}: nepodařilo se složit žádné kontury.")
                continue

            for contour_id, contour in enumerate(contours):
                sampled_points = self.contour_to_step_polyline(
                contour=contour,
                tolerance=contour_tolerance,
                remove_closing_duplicate=True)

                if sampled_points.size == 0:
                    continue
                ### zde vezmeme pouze jednu polovinu bodů, kvůli symetrii
                self.half_points = sampled_points[sampled_points[:, 0] < 0]
                for point_id, p in enumerate(self.half_points):
                    all_points.append({
                        "plane_id": plane_id,
                        "contour_id": contour_id,
                        "point_id": point_id,
                        "x": p[0],
                        "y": p[1],
                        "z": p[2],
                        "nx": normal[0],
                        "ny": normal[1],
                        "nz": normal[2],
                        "closed": contour["closed"],
                    })

        df = pd.DataFrame(all_points)

        if export_csv_path is not None:
            export_csv_path = Path(export_csv_path)

            if not export_csv_path.is_absolute():
                export_csv_path = PROJECT_ROOT / export_csv_path

            export_csv_path.parent.mkdir(parents=True, exist_ok=True)
            df.to_csv(export_csv_path, index=False)

        return df,self.half_points
    def index_points(self):
        half_points = self.half_points
        matice_bodu = []
        for bod_id,bod in enumerate(half_points):
            matice_bodu.append([bod_id,bod[0],bod[2]])
        return matice_bodu
    def show_traj(self, show_line=False):
        matice_bodu = np.array(self.index_points(), dtype=float)

        if len(matice_bodu) == 0:
            return np.empty((0, 3)), None, None,matice_bodu

        if not show_line:
            return matice_bodu, None, None,matice_bodu

        start_text = self.ui.start_traj_text.text().strip()
        finish_text = self.ui.cil_traj_text.text().strip()

        if start_text == "" or finish_text == "":
            MessageBox.show(
                parent=self.ui.centralwidget,
                title="Chyba",
                text="Není zadaný startovní nebo cílový bod.",
                icon=QMessageBox.Warning
            )
            return np.empty((0, 3)), None, None

        try:
            start_bod = int(start_text)
            finish_bod = int(finish_text)
        except ValueError:
            MessageBox.show(
                parent=self.ui.centralwidget,
                title="Chyba",
                text="Startovní a cílový bod musí být celé číslo.",
                icon=QMessageBox.Warning
            )
            return np.empty((0, 3)), None, None

        if start_bod == finish_bod:
            MessageBox.show(
                parent=self.ui.centralwidget,
                title="Chyba",
                text="Start a finish je stejný bod.",
                icon=QMessageBox.Critical
            )
            return np.empty((0, 3)), None, None

        max_id = len(matice_bodu) - 1

        if not (0 <= start_bod <= max_id) or not (0 <= finish_bod <= max_id):
            MessageBox.show(
                parent=self.ui.centralwidget,
                title="Chyba",
                text=f"Body musí být v rozsahu 0 až {max_id}.",
                icon=QMessageBox.Warning
            )
            return np.empty((0, 3)), None, None

        if start_bod < finish_bod:
            traj_points = matice_bodu[start_bod:finish_bod + 1]
        else:
            traj_points = matice_bodu[start_bod:finish_bod - 1:-1]

        return traj_points, start_bod, finish_bod, matice_bodu
    def plot_section_points_2d_xy(self, show_line: bool = False):
        points, start, finish, matice_bodu = self.show_traj(show_line)

        if points.size == 0:
            return

        fig, ax = plt.subplots()
        x_full = matice_bodu[:, 1]
        z_full = matice_bodu[:,2]

        x = points[:, 1]
        z = points[:, 2]
        ids = points[:, 0].astype(int)

        ax.plot(x_full, z_full, "o-", color="blue", linewidth=1.5)
        if show_line:
            ax.plot(x,z,"o-",color="green",linewidth = 1.5)
            for i, bod_id in enumerate(matice_bodu):
                if start<=i<=finish:
                    i += 1
                    continue
                if start >= i >= finish:
                    i -= 1
                    continue
                ax.text(x_full[i],z_full[i],f"{i}",fontsize=8,color="red")
        else:
            for i, bod_id in enumerate(ids):
                ax.text(
                    x[i],
                    z[i],
                    f"{bod_id}",
                    fontsize=8,
                    color="red"
                )

        ax.set_xlabel("X")
        ax.set_ylabel("Z")
        ax.set_title("Scan points on contour")
        ax.axis("equal")
        ax.grid(True)

        plt.show()
    def run_cut_process(self):
        planes = [
            {
                "origin": [0, 0, 0],
                "normal": [0, 1, 0]
            }
        ]
        df_points = self.generate_section_contour_points(
            planes=planes,
            export_csv_path=PROJECT_ROOT / "export" / "step_rez_body.csv"
        )

        sken_data = self.plot_section_points_2d_xy(show_line=False)

        self.data.scan_points = sken_data

if __name__ == "__main__":
    planes = [
        {
            "origin": [0, 0, 50],
            "normal": [0, 0, 1]
        }
    ]

    cut_process = Cutprocess_step(ui=None, data=GUIData())
    data = GUIData()

    df_points,half_points = cut_process.generate_section_contour_points(
        step_path=PROJECT_ROOT / "STL_modely" / "test2step.step",
        planes=planes,
        export_csv_path=PROJECT_ROOT / "export" / "step_rez_body.csv"
    )

    data.half_points = half_points
    
    cut_process.plot_section_points_2d_xy(
        df_points=df_points,
        plane_id=0)