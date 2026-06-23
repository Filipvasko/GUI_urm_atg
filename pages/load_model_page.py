from PySide6.QtWidgets import QFileDialog, QMessageBox
from pages.message_box import MessageBox
import os
import pyvista as pv
import numpy as np
from scipy.spatial.transform import Rotation as R
from src.python.config.dataclass import GUIData

class LoadModel():
    def __init__(self,ui,project_root,data: GUIData):
        self.ui = ui
        self.project_root = project_root
        self.load_model_btn = self.ui.load_model_btn
        self.ui.open_model_btn.clicked.connect(self.show_part)
        self.ui.btn_save_param.clicked.connect(self.fill_model_params)
        self.ui.btn_update_plot.clicked.connect(self.transform_model)
        self.valid_model_position = None
        self.file_path = None
        self.matrix_rotation_4 = np.eye(4)
        self.transform_vector = [0,0,0]
        self.open_dialog = True
        self.data = data


    def load_model(self):
            '''
            V této funkci nečteme z adresáře stl model a vykreslíme ho
            '''
            if self.open_dialog:
                try:
                    self.file_path, _ = QFileDialog.getOpenFileName(None,  "Vyberte STL model skenovaného dílu", str(self.project_root/ "STL_modely") , "STL soubory (*.stl)")
                    self.data.model_path = self.file_path
                except Exception as e:
                    print(f"Nebyla nalazená požadovaná složka: {e}")
                self.file_path = self.file_path
            return self.file_path
    def add_world_axes(self,plotter, length):
        x_axis = pv.Arrow(
            start=(0, 0, 0),
            direction=(1, 0, 0),
            scale=length
        )

        y_axis = pv.Arrow(
            start=(0, 0, 0),
            direction=(0, 1, 0),
            scale=length
        )

        z_axis = pv.Arrow(
            start=(0, 0, 0),
            direction=(0, 0, 1),
            scale=length
        )

        plotter.add_mesh(x_axis, color="red")
        plotter.add_mesh(y_axis, color="green")
        plotter.add_mesh(z_axis, color="blue")

        plotter.add_point_labels(
            [(length, 0, 0), (0, length, 0), (0, 0, length)],
            ["X", "Y", "Z"],
            font_size=18,
            text_color="black"
        )
    def show_part(self):
        self.load_model()
        try:
            reader = pv.STLReader(str(self.file_path))
            mesh = reader.read()
            mesh.transform(self.matrix_rotation_4,inplace=True)
            stl_show = pv.Plotter()
            self.add_world_axes(stl_show, length=100)
            stl_show.add_mesh(mesh, color="lightgray", show_edges=False)
            stl_show.show_grid()
            stl_show.reset_camera()
            stl_show.show()
            self.data.active_mesh = mesh
        except Exception as e:
            print(f"Chyba při načítání STL souboru: {e}")
            return
        
    def fill_model_params(self,message=True):
        numbers = [("X",self.ui.model_x_text.text()),("Y",self.ui.model_y_text.text()),("Z",self.ui.model_z_text.text()),("W",self.ui.model_yaw_text.text()),("P",self.ui.model_pitch_text.text()),("R",self.ui.model_roll_text.text())]
        invalid_numbers = []
        self.valid_model_position = []
        for index,value in numbers:
            try:
                float(value)
                self.valid_model_position.append(float(value))
                
            except ValueError:
                invalid_numbers.append(index)
                error_message = f"Chyba,v polích {','.join(invalid_numbers)} není platné číslo"
        
        if invalid_numbers:
            MessageBox.show(
                parent=self.ui.centralwidget,
                title="Nesprávný vstup",
                text=error_message,
                icon=QMessageBox.Critical
            )
        else:
            MessageBox.show(
                parent=self.ui.centralwidget,
                title="Úspěch",
                text="Všechny hodnoty jsou v pořádku",
                icon=QMessageBox.Information
            )
            
        return numbers
    
    def transform_model(self):
        try:
            if not hasattr(self, "valid_model_position"):
                raise ValueError("Nejdříve zadej a potvrď polohu modelu.")

            if self.valid_model_position is None:
                raise ValueError("Nejdříve zadej a potvrď polohu modelu.")

            if len(self.valid_model_position) != 6:
                raise ValueError("Poloha modelu musí obsahovat přesně 6 hodnot: X, Y, Z, W, P, R.")

            x_model, y_model, z_model, yaw_model, pitch_model, roll_model = self.valid_model_position
            self.data.position_model = self.valid_model_position
            self.transform_vector = [x_model, y_model, z_model]
            self.matrix_rotation_3 = R.from_euler('xyz',[yaw_model, pitch_model, roll_model],degrees=True).as_matrix()
            self.matrix_rotation_4 = np.eye(4)
            self.matrix_rotation_4[:3, :3] = self.matrix_rotation_3
            self.matrix_rotation_4[:3, 3] = self.transform_vector
            self.data.transform_matrix = self.matrix_rotation_4
            self.open_dialog = False
            self.show_part()
            return self.matrix_rotation_4

        except (ValueError, AttributeError, IndexError, TypeError) as e:
            MessageBox.show(
                parent=self.ui.centralwidget,
                title="Chyba",
                text=f"{e}",
                icon=QMessageBox.Warning
            )
            return None      



        