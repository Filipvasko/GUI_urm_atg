import sys
from pathlib import Path

import trimesh
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = ROOT.parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.python.config.dataclass import GUIData


class Cutprocess:
    def __init__(self, ui=None, data: GUIData | None = None):
        self.ui = ui
        self.data = data

        if self.data is not None:
            self.mesh = getattr(self.data, "active_mesh", None)
            self.position_model = getattr(self.data, "position_model", None)
            self.transform_matrix = getattr(self.data, "transform_matrix", None)
        else:
            self.mesh = None
            self.position_model = None
            self.transform_matrix = None

    def load_mesh_trimesh(self, mesh_path: str | Path) -> trimesh.Trimesh:
        """
        Načte STL/OBJ/PLY mesh pomocí trimesh.
        """

        mesh_path = Path(mesh_path)

        if not mesh_path.is_absolute():
            mesh_path = PROJECT_ROOT / mesh_path

        if not mesh_path.exists():
            raise FileNotFoundError(f"Soubor nebyl nalezen: {mesh_path}")

        mesh = trimesh.load_mesh(mesh_path, force="mesh")

        if not isinstance(mesh, trimesh.Trimesh):
            raise TypeError("Načtený objekt není trimesh.Trimesh.")

        if mesh.is_empty:
            raise ValueError("Mesh je prázdný.")

        return mesh

    def _resample_polyline(
        self,
        polyline: np.ndarray,
        step: float,
        closed: bool = True
    ) -> np.ndarray:
        """
        Převzorkuje polyline na body s přibližně konstantním krokem.
        """

        if step <= 0:
            raise ValueError("Krok musí být větší než 0.")

        if len(polyline) < 2:
            return np.empty((0, 3))

        pts = np.asarray(polyline, dtype=float)

        if closed:
            if np.linalg.norm(pts[0] - pts[-1]) > 1e-9:
                pts = np.vstack([pts, pts[0]])

        segment_vectors = pts[1:] - pts[:-1]
        segment_lengths = np.linalg.norm(segment_vectors, axis=1)

        total_length = np.sum(segment_lengths)

        if total_length <= 1e-12:
            return np.empty((0, 3))

        distances = np.arange(0.0, total_length, step)
        cumulative_lengths = np.insert(np.cumsum(segment_lengths), 0, 0.0)

        resampled_points = []

        for d in distances:
            seg_idx = np.searchsorted(cumulative_lengths, d, side="right") - 1

            if seg_idx >= len(segment_lengths):
                seg_idx = len(segment_lengths) - 1

            seg_len = segment_lengths[seg_idx]

            if seg_len <= 1e-12:
                continue

            seg_start = pts[seg_idx]
            seg_vec = segment_vectors[seg_idx]

            local_t = (d - cumulative_lengths[seg_idx]) / seg_len
            new_point = seg_start + local_t * seg_vec

            resampled_points.append(new_point)

        return np.asarray(resampled_points)

    def generate_section_contour_points(
        self,
        mesh_path: str | Path,
        planes: list[dict],
        step: float,
        export_csv_path: str | Path | None = None,
        closed_contours: bool = True,
        apply_transform: bool = False,
    ) -> pd.DataFrame:
        """
        Načte mesh, provede řezy rovinami a vygeneruje body na konturách.

        Parameters
        ----------
        mesh_path:
            Cesta ke STL souboru.

        planes:
            Seznam rovin. Každá rovina má tvar:

            {
                "origin": [x, y, z],
                "normal": [nx, ny, nz]
            }

        step:
            Krok generovaných bodů po kontuře.

        export_csv_path:
            Pokud je zadáno, výsledek se uloží do CSV.

        closed_contours:
            Jestli se kontury berou jako uzavřené.

        apply_transform:
            Pokud True a existuje self.transform_matrix, aplikuje transformaci na mesh.

        Returns
        -------
        pd.DataFrame
            Tabulka bodů.
        """

        if step <= 0:
            raise ValueError("Krok musí být větší než 0.")

        mesh = self.load_mesh_trimesh(mesh_path)

        if apply_transform:
            if self.transform_matrix is None:
                raise ValueError("apply_transform=True, ale self.transform_matrix není nastavená.")

            mesh = mesh.copy()
            mesh.apply_transform(np.asarray(self.transform_matrix, dtype=float))

        all_points = []

        for plane_id, plane in enumerate(planes):
            origin = np.asarray(plane["origin"], dtype=float)
            normal = np.asarray(plane["normal"], dtype=float)

            normal_norm = np.linalg.norm(normal)

            if normal_norm <= 1e-12:
                raise ValueError(f"Normála roviny {plane_id} má nulovou délku.")

            normal = normal / normal_norm

            section = mesh.section(
                plane_origin=origin,
                plane_normal=normal
            )

            if section is None:
                print(f"Rovina {plane_id}: řez neobsahuje žádné body.")
                continue

            polylines = section.discrete

            if len(polylines) == 0:
                print(f"Rovina {plane_id}: nebyly nalezeny žádné kontury.")
                continue

            for contour_id, polyline in enumerate(polylines):
                polyline = np.asarray(polyline, dtype=float)

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

            if not export_csv_path.is_absolute():
                export_csv_path = PROJECT_ROOT / export_csv_path

            export_csv_path.parent.mkdir(parents=True, exist_ok=True)
            df.to_csv(export_csv_path, index=False)

        return df

    def plot_section_points_2d_xy(
        self,
        df_points: pd.DataFrame,
        plane_id: int = 0
    ):
        """
        Vykreslí jeden řez v rovině XY.
        Vhodné hlavně pro řezy s normálou [0, 0, 1].
        """

        if df_points.empty:
            print("DataFrame je prázdný, není co vykreslit.")
            return

        df = df_points[df_points["plane_id"] == plane_id]

        if df.empty:
            print(f"Pro plane_id={plane_id} nejsou žádné body.")
            return

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

    def plot_section_points_3d(
        self,
        df_points: pd.DataFrame,
        plane_id: int | None = None
    ):
        """
        Vykreslí body řezu ve 3D.
        """

        if df_points.empty:
            print("DataFrame je prázdný, není co vykreslit.")
            return

        if plane_id is not None:
            df = df_points[df_points["plane_id"] == plane_id]
        else:
            df = df_points

        if df.empty:
            print(f"Pro plane_id={plane_id} nejsou žádné body.")
            return

        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

        ax.scatter(
            df["x"],
            df["y"],
            df["z"],
            s=5
        )

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        if plane_id is None:
            ax.set_title("Všechny body řezů")
        else:
            ax.set_title(f"Body řezu - plane_id = {plane_id}")

        plt.show()

if __name__ == "__main__":
    planes = [
        {
            "origin": [0, 0, 50],
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
        export_csv_path="export/rez_body.csv",
        closed_contours=True,
        apply_transform=False
    )

    print(df_points)

    cut_process.plot_section_points_2d_xy(
        df_points=df_points,
        plane_id=0
    )

    cut_process.plot_section_points_3d(
        df_points=df_points,
        plane_id=0
    )