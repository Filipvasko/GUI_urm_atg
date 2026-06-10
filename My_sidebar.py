from design_gui_v2 import Ui_QMainWindow
from PySide6.QtWidgets import QMainWindow
from pages.home_page import HomePage
from pages.load_model_page import LoadModel
from pathlib import Path

class MySideBars(QMainWindow, Ui_QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ATG Navi GUI")
        self.root_folder = Path(__file__).resolve().parent

        self.home_page = HomePage(self)
        self.load_model = LoadModel(self,self.root_folder)
        self.Menu_btn.clicked.connect(self.switch_to_menu_page)
        self.load_model_btn.clicked.connect(self.switch_to_load_model_page)
        self.cut_process_btn.clicked.connect(self.switch_to_cut_process_page)
        self.trajektorie_btn.clicked.connect(self.switch_to_trajektorie_page)
        self.simulation_btn.clicked.connect(self.switch_to_simulation_page)
        self.database_btn.clicked.connect(self.switch_to_database_page)
        

    def switch_to_menu_page(self):
        self.stackedWidget.setCurrentWidget(self.menu_page)

    def switch_to_load_model_page(self):
        self.stackedWidget.setCurrentWidget(self.load_model_page)
    
    def switch_to_cut_process_page(self):
        self.stackedWidget.setCurrentWidget(self.cut_process)

    def switch_to_trajektorie_page(self):
        self.stackedWidget.setCurrentWidget(self.trajektorie_page)

    def switch_to_simulation_page(self):
        self.stackedWidget.setCurrentWidget(self.simulation_page)

    def switch_to_database_page(self):
        self.stackedWidget.setCurrentWidget(self.database_page)