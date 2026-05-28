from design_gui_v2 import Ui_QMainWindow
from PySide6.QtWidgets import QWidget, QMessageBox

class HomePage(QWidget, Ui_QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        '''
        If the new_trajektorie_btn is clicked, the user will have to go through the process of loading model,
        generating each scanning trajectories and if the open_trajektorie_btn is clicked then user will jump straight to
        databse where he will select frames and then he will just check or edit whole trajectory
        '''
        self.new_project_btn.clicked.connect(self.new_traj)
        self.open_traj_btn.clicked.connect(self.open_traj)

    def new_traj(self):
        """
        It will jump to laod model and each filling forms will be deleted
        """
        msg_new_project = QMessageBox(self)
        msg_new_project.setText("Are you sure i want to start new project? All data from current project will be lost")
        msg_new_project.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_new_project.setDefaultButton(QMessageBox.No)
        if msg_new_project.exec() == QMessageBox.Yes:
            self.stackedWidget.setCurrentWidget(self.load_model_page)
            self.hp_x_text.clear()
            self.hp_y_text.clear()
            self.hp_z_text.clear()
            self.hp_yaw_text.clear()
            self.hp_pitch_text.clear()
            self.hp_roll_text.clear()
            self.uf_x_text.clear()
            self.uf_y_text.clear()
            self.uf_z_text.clear()
            self.uf_yaw_text.clear()
            self.uf_pitch_text.clear()
            self.uf_roll_text.clear()
        else:
            pass
    
    def open_traj(self):
        """
        It will jump to page databse and page load_model and create traj will be disabled
        """
        self.stackedWidget.setCurrentWidget(self.database_page)
        self.load_model_btn.setEnabled(False)
        self.new_project_btn.setEnabled(False)