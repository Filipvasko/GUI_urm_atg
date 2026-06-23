from src.python.config.dataclass import GUIData
from PySide6.QtWidgets import QMessageBox
import numpy as np
import pandas as pd

class Cutprocess():
    def __init__(self,ui,data: GUIData):
        self.ui = ui
        self.data = data
        
