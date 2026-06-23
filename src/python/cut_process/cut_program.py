from PySide6.QtWidgets import QWidget, QFileDialog
import pyvista as pv
import numpy as np
import pandas as pd
from scipy.spatial.transform import Rotation as R
from pathlib import Path
from matplotlib import pyplot as plt
import sys

ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = ROOT.parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.python.config.dataclass import GUIData


class Cutprocess():
    def __init__(self,ui,data: GUIData):
        self.ui = ui
        self.data = data
        self.mesh = self.data.active_mesh
        self.position_model = self.data.position_model
        self.transform_matrix = self.data.transform_matrix

    def _extract_polylines_from_section(self,section: pv.PolyData):
        """
        Z PyVista řezu vytáhne jednotlivé polyline křivky.

        section.lines má strukturu:
        [n, id1, id2, ..., idn, n, id1, id2, ..., idn, ...]
        """
        lines = section.lines
        points = section.points

        polylines = []
        i = 0

        while i < len(lines):
            n = lines[i]
            ids = lines[i + 1:i + 1 + n]
            polyline = points[ids]
            polylines.append(polyline)
            i += n + 1

        return polylines


    def _resample_polyline(self,polyline: np.ndarray, step: float, closed: bool = True):
        """
        Převzorkuje jednu polyline křivku na body s přibližně konstantním krokem.

        Parameters
        ----------
        polyline : np.ndarray
            Body křivky ve tvaru (N, 3).
        step : float
            Požadovaný krok mezi body.
        closed : bool
            Jestli se má poslední bod spojit zpět s prvním.

        Returns
        -------
        np.ndarray
            Převzorkované body ve tvaru (M, 3).
        """

        if len(polyline) < 2:
            return np.empty((0, 3))

        pts = np.asarray(polyline, dtype=float)

        if closed:
            # Pokud křivka není uzavřená, přidáme první bod na konec
            if np.linalg.norm(pts[0] - pts[-1]) > 1e-9:
                pts = np.vstack([pts, pts[0]])

        segment_vectors = pts[1:] - pts[:-1]
        segment_lengths = np.linalg.norm(segment_vectors, axis=1)

        total_length = np.sum(segment_lengths)

        if total_length <= 1e-12:
            return np.empty((0, 3))

        # Vzdálenosti, kde chceme nové body
        distances = np.arange(0, total_length, step)

        resampled_points = []

        cumulative_lengths = np.insert(np.cumsum(segment_lengths), 0, 0.0)

        for d in distances:
            seg_idx = np.searchsorted(cumulative_lengths, d, side="right") - 1

            if seg_idx >= len(segment_lengths):
                seg_idx = len(segment_lengths) - 1

            seg_start = pts[seg_idx]
            seg_vec = segment_vectors[seg_idx]
            seg_len = segment_lengths[seg_idx]

            if seg_len <= 1e-12:
                continue

            local_t = (d - cumulative_lengths[seg_idx]) / seg_len
            new_point = seg_start + local_t * seg_vec
            resampled_points.append(new_point)

        return np.array(resampled_points)


    def generate_section_contour_points(self,
        mesh_path: str | Path,
        planes: list[dict],
        step: float,
        export_csv_path: str | Path | None = None,
        closed_contours: bool = True,
    ):
        """
        Načte STL mesh, provede řezy zadanými rovinami a vygeneruje body na konturách.

        Parameters
        ----------
        mesh_path : str | Path
            Cesta ke STL souboru.

        planes : list[dict]
            Seznam rovin řezu.

            Každá rovina má tvar:
            {
                "origin": [x, y, z],
                "normal": [nx, ny, nz]
            }

            Například:
            planes = [
                {
                    "origin": [0, 0, 10],
                    "normal": [0, 0, 1]
                },
                {
                    "origin": [0, 0, 20],
                    "normal": [0, 0, 1]
                }
            ]

        step : float
            Krok generovaných bodů po kontuře.

        export_csv_path : str | Path | None
            Pokud je zadáno, uloží body do CSV.

        closed_contours : bool
            Jestli se mají kontury brát jako uzavřené.

        Returns
        -------
        pd.DataFrame
            Tabulka s body kontur.
        """

        mesh_path = Path(mesh_path)

        if not mesh_path.exists():
            raise FileNotFoundError(f"Soubor nebyl nalezen: {mesh_path}")

        if step <= 0:
            raise ValueError("Krok musí být větší než 0.")

        mesh = pv.read(mesh_path)

        all_points = []

        for plane_id, plane in enumerate(planes):
            origin = np.asarray(plane["origin"], dtype=float)
            normal = np.asarray(plane["normal"], dtype=float)

            normal_norm = np.linalg.norm(normal)

            if normal_norm <= 1e-12:
                raise ValueError(f"Normála roviny {plane_id} má nulovou délku.")

            normal = normal / normal_norm

            section = mesh.slice(
                origin=origin,
                normal=normal
            )

            if section.n_points == 0:
                print(f"Rovina {plane_id}: řez neobsahuje žádné body.")
                continue
            
            polylines = self._extract_polylines_from_section(section)

            if len(polylines) == 0:
                print(f"Rovina {plane_id}: nebyly nalezeny žádné polyline kontury.")
                continue

            for contour_id, polyline in enumerate(polylines):
                resampled = self._resample_polyline(
                    polyline=polyline,
                    step=step,
                    closed=closed_contours
                )

                for point_id, p in enumerate(resampled):
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
                    })

        df = pd.DataFrame(all_points)
        if export_csv_path is not None:
            export_csv_path = Path(export_csv_path)
            export_csv_path.parent.mkdir(parents=True, exist_ok=True)
            df.to_csv(export_csv_path, index=False)

        return df
    
    def plot_section_points_2d_xy(self,df_points, plane_id=0):
        df = df_points[df_points["plane_id"] == plane_id]

        fig, ax = plt.subplots()

        for contour_id, contour_df in df.groupby("contour_id"):
            ax.scatter(
                contour_df["x"],
                contour_df["y"],
                s=5,
                label=f"contour {contour_id}"
            )

            ax.plot(
                contour_df["x"],
                contour_df["y"],
                linewidth=1
            )

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title(f"Kontura řezu v XY - plane_id = {plane_id}")
        ax.axis("equal")
        ax.grid(True)
        ax.legend()

        plt.show()

if __name__ == "__main__":
    planes = [
        {
            "origin": [0, 0, 1],
            "normal": [0, 0, 1]
        }
    ]

    data = GUIData()

    cut_process = Cutprocess(
        ui=None,
        data=data
    )


    df_points = cut_process.generate_section_contour_points(
        mesh_path=PROJECT_ROOT/"STL_modely"/"test_vnitrni_skenovani_mm.STL",
        planes=planes,
        step=0.5,
        export_csv_path="export/rez_body.csv"
    )

    print(df_points)

    cut_process.plot_section_points_2d_xy(
        df_points,
        plane_id=0
    )

    


