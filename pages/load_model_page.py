from PySide6.QtWidgets import QFileDialog
import os
import pyvista as pv

class LoadModel:
    def __init__(self,ui,project_root):
        self.ui = ui
        self.project_root = project_root
        self.load_model_btn = self.ui.load_model_btn
        self.ui.open_model_btn.clicked.connect(self.show_part)

    def load_model(self):
        '''
        V této funcki nečteme z adresáře stl model a vykreslíme ho
        '''
        file_path, _ = QFileDialog.getOpenFileName(None,  "Vyberte STL model skenovaného dílu", str(self.project_root/ "STL_modely") , "STL soubory (*.stl)")
        # file_path = os.path.normpath(file_path)
        self.file_path = file_path
        return file_path
    
    def show_part(self):
        self.load_model()
        try:
            mesh = pv.read(self.file_path)
        except Exception as e:
            print(f"Chyba při načítání STL souboru: {e}")
            return

        plotter = pv.Plotter()
        plotter.add_mesh(mesh, color="lightgray", show_edges=False)
        plotter.add_axes()
        plotter.show_grid()
        plotter.show()