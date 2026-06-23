from dataclasses import dataclass, field
from pathlib import Path
import numpy as np
import pyvista as pv


@dataclass
class GUIData:
    # -------------------------
    # Load model page
    # -------------------------
    model_path: Path = field(default_factory=lambda: Path())

    # [x, y, z, W, P, R]
    position_model: np.ndarray = field(default_factory=lambda: np.zeros(6))

    # aktuální mesh po transformaci
    active_mesh: pv.PolyData | None = None

    # transformační matice modelu
    transform_matrix: np.ndarray = field(default_factory=lambda: np.eye(4))
    # -------------------------
    # Řez modelem a generátor bodů
    # -------------------------

    # strategie skenování
    sken_kolmo_k_povrchu: bool = False
    sken_rovina_uhel: bool = False
    sken_mimo_rovina: bool = False

    # vnější / vnitřní sken
    out_sken_zleva_doprava: bool = False
    out_sken_zprava_doleva: bool = False
    in_sken_shora_dolu: bool = False
    in_sken_dolu_nahoru: bool = False

    # skenovací krok
    sken_step: float = 0.5

    # vygenerované body / trajektorie
    scan_points: np.ndarray | None = None
    half_points: np.ndarray | None = None
    global_start: np.ndarray | None = None
    global_goal: np.ndarray | None = None
    global_trajectory: np.ndarray | None = None

    # -------------------------
    # Databáze / robotické rámce
    # -------------------------

    # [x, y, z, W, P, R]
    toolframe: np.ndarray = field(default_factory=lambda: np.array([0, 0, 336, 0, 0, 0], dtype=float))
    userframe: np.ndarray = field(default_factory=lambda: np.array([0, 0, -1095, 0, 0, 0], dtype=float))
    homeposition: np.ndarray = field(default_factory=lambda: np.zeros(6))

    # -------------------------
    # Simulace
    # -------------------------

    config_robot: str = "NUT"
    typ_sondy: str = "Sonda1"

    joint_trajectory: np.ndarray | None = None