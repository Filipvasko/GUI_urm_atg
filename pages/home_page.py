from PySide6.QtWidgets import QMessageBox
from pages.message_box import MessageBox

class HomePage:
    def __init__(self, ui):
        self.ui = ui

        '''
        If the new_trajektorie_btn is clicked, the user will have to go through the process of loading model,
        generating each scanning trajectories and if the open_trajektorie_btn is clicked then user will jump straight to
        databse where he will select frames and then he will just check or edit whole trajectory
        '''
        self.ui.new_project_btn.clicked.connect(self.new_traj)
        self.ui.open_traj_btn.clicked.connect(self.open_traj)


    def new_traj(self):
        """
        It will jump to laod model and each filling forms will be deleted
        """
        msg_new_project = MessageBox.show(
            parent=self.ui.centralwidget,
            title="New trajectory",
            text="Are you sure you want to start new project? All data from current project will be lost",
        )
        if msg_new_project == msg_new_project.Yes:
            self.ui.stackedWidget.setCurrentWidget(self.ui.load_model_page)
            for field_name in (
                "hp_x_text",
                "hp_y_text",
                "hp_z_text",
                "hp_yaw_text",
                "hp_pitch_text",
                "hp_roll_text",
                "uf_x_text",
                "uf_y_text",
                "uf_z_text",
                "uf_yaw_text",
                "uf_pitch_text",
                "uf_roll_text",
            ):
                getattr(self.ui, field_name).clear()
    
    def open_traj(self):
        """
        It will jump to page databse and page load_model and create traj will be disabled
        """
        self.ui.stackedWidget.setCurrentWidget(self.ui.database_page)
        self.ui.load_model_btn.setEnabled(False)
        self.ui.new_project_btn.setEnabled(False)
