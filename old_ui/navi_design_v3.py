# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design_v3.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_QMainWindow(object):
    def setupUi(self, QMainWindow):
        if not QMainWindow.objectName():
            QMainWindow.setObjectName(u"QMainWindow")
        QMainWindow.resize(1221, 825)
        QMainWindow.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u"../atg_logo.jpg", QSize(), QIcon.Normal, QIcon.On)
        QMainWindow.setWindowIcon(icon)
        QMainWindow.setAutoFillBackground(False)
        QMainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.528, y1:0.34, x2:1, y2:1, stop:0 rgba(63, 159, 219, 255), stop:0.579545 rgba(253, 255, 255, 255));")
        QMainWindow.setAnimated(True)
        self.centralwidget = QWidget(QMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.side_bar = QWidget(self.centralwidget)
        self.side_bar.setObjectName(u"side_bar")
        self.side_bar.setGeometry(QRect(0, 90, 261, 951))
        self.side_bar.setStyleSheet(u"background-color: rgb(0, 84, 252);")
        self.verticalLayoutWidget_2 = QWidget(self.side_bar)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(30, 0, 191, 621))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.Menu_btn = QPushButton(self.verticalLayoutWidget_2)
        self.Menu_btn.setObjectName(u"Menu_btn")
        self.Menu_btn.setMinimumSize(QSize(150, 40))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(14)
        font.setBold(True)
        self.Menu_btn.setFont(font)
        self.Menu_btn.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        icon1 = QIcon()
        icon1.addFile(u"icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu_btn.setIcon(icon1)
        self.Menu_btn.setIconSize(QSize(25, 25))
        self.Menu_btn.setCheckable(True)
        self.Menu_btn.setChecked(False)
        self.Menu_btn.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.Menu_btn)

        self.load_model_btn = QPushButton(self.verticalLayoutWidget_2)
        self.load_model_btn.setObjectName(u"load_model_btn")
        self.load_model_btn.setMinimumSize(QSize(150, 50))
        self.load_model_btn.setFont(font)
        self.load_model_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 255);\n"
"border-radius: 10px;")
        icon2 = QIcon(QIcon.fromTheme(u"QIcon::ThemeIcon::FolderOpen"))
        self.load_model_btn.setIcon(icon2)
        self.load_model_btn.setIconSize(QSize(25, 25))
        self.load_model_btn.setCheckable(True)

        self.verticalLayout_3.addWidget(self.load_model_btn)

        self.cut_process_btn = QPushButton(self.verticalLayoutWidget_2)
        self.cut_process_btn.setObjectName(u"cut_process_btn")
        self.cut_process_btn.setMinimumSize(QSize(150, 50))
        self.cut_process_btn.setFont(font)
        self.cut_process_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 255);\n"
"border-radius: 15px;")
        icon3 = QIcon()
        icon3.addFile(u"../scissor_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cut_process_btn.setIcon(icon3)
        self.cut_process_btn.setIconSize(QSize(25, 25))
        self.cut_process_btn.setCheckable(True)

        self.verticalLayout_3.addWidget(self.cut_process_btn)

        self.database_btn = QPushButton(self.verticalLayoutWidget_2)
        self.database_btn.setObjectName(u"database_btn")
        self.database_btn.setMinimumSize(QSize(150, 50))
        self.database_btn.setFont(font)
        self.database_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 255);\n"
"border-radius: 15px;")
        icon4 = QIcon()
        icon4.addFile(u"../database_log.png", QSize(), QIcon.Normal, QIcon.Off)
        self.database_btn.setIcon(icon4)
        self.database_btn.setIconSize(QSize(25, 25))
        self.database_btn.setCheckable(True)

        self.verticalLayout_3.addWidget(self.database_btn)

        self.trajektorie_btn = QPushButton(self.verticalLayoutWidget_2)
        self.trajektorie_btn.setObjectName(u"trajektorie_btn")
        self.trajektorie_btn.setMinimumSize(QSize(150, 50))
        self.trajektorie_btn.setFont(font)
        self.trajektorie_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 255);\n"
"border-radius: 15px;")
        icon5 = QIcon()
        icon5.addFile(u"icons/line_traj.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.trajektorie_btn.setIcon(icon5)
        self.trajektorie_btn.setIconSize(QSize(25, 25))
        self.trajektorie_btn.setCheckable(True)

        self.verticalLayout_3.addWidget(self.trajektorie_btn)

        self.simulation_btn = QPushButton(self.verticalLayoutWidget_2)
        self.simulation_btn.setObjectName(u"simulation_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simulation_btn.sizePolicy().hasHeightForWidth())
        self.simulation_btn.setSizePolicy(sizePolicy)
        self.simulation_btn.setMinimumSize(QSize(150, 50))
        self.simulation_btn.setFont(font)
        self.simulation_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 255);\n"
"border-radius: 15px;")
        icon6 = QIcon()
        icon6.addFile(u"icons/play_button.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.simulation_btn.setIcon(icon6)
        self.simulation_btn.setIconSize(QSize(25, 25))
        self.simulation_btn.setCheckable(True)

        self.verticalLayout_3.addWidget(self.simulation_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.end_btn = QPushButton(self.verticalLayoutWidget_2)
        self.end_btn.setObjectName(u"end_btn")
        self.end_btn.setMinimumSize(QSize(150, 50))
        self.end_btn.setFont(font)
        self.end_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 255);\n"
"border-radius: 15px;")
        icon7 = QIcon(QIcon.fromTheme(u"QIcon::ThemeIcon::SystemShutdown"))
        self.end_btn.setIcon(icon7)
        self.end_btn.setIconSize(QSize(25, 25))
        self.end_btn.setCheckable(True)
        self.end_btn.setChecked(False)

        self.verticalLayout_3.addWidget(self.end_btn)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, -3, 1231, 91))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.518, x2:0.284227, y2:0.529, stop:0.136364 rgba(54, 208, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.atg_logo_image = QLabel(self.frame)
        self.atg_logo_image.setObjectName(u"atg_logo_image")
        self.atg_logo_image.setGeometry(QRect(10, 10, 291, 81))
        self.atg_logo_image.setAutoFillBackground(False)
        self.atg_logo_image.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.atg_logo_image.setFrameShape(QFrame.Shape.Panel)
        self.atg_logo_image.setFrameShadow(QFrame.Shadow.Sunken)
        self.atg_logo_image.setPixmap(QPixmap(u"../atg_logo.jpg"))
        self.atg_logo_image.setScaledContents(True)
        self.atg_logo_image.setMargin(0)
        self.atg_logo_image.setOpenExternalLinks(False)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 20, 501, 41))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 255);")
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(320, 10, 20, 91))
        self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(350, 60, 501, 21))
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(260, 90, 961, 951))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(224, 251, 255);")
        self.load_model_page = QWidget()
        self.load_model_page.setObjectName(u"load_model_page")
        self.verticalLayoutWidget_9 = QWidget(self.load_model_page)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(110, 0, 720, 702))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_10.setSpacing(15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(70)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 1, 10, 1)
        self.load_model_btn_2 = QPushButton(self.verticalLayoutWidget_9)
        self.load_model_btn_2.setObjectName(u"load_model_btn_2")
        self.load_model_btn_2.setMinimumSize(QSize(150, 30))
        self.load_model_btn_2.setMaximumSize(QSize(200, 30))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.load_model_btn_2.setFont(font2)
        self.load_model_btn_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 255);\n"
"border-radius: 15px;\n"
"border: 2px solid #00AEEF;\n"
"border-color: rgb(0, 85, 255);")
        self.load_model_btn_2.setIcon(icon1)
        self.load_model_btn_2.setIconSize(QSize(25, 25))
        self.load_model_btn_2.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.load_model_btn_2)

        self.model_path = QLabel(self.verticalLayoutWidget_9)
        self.model_path.setObjectName(u"model_path")
        self.model_path.setMinimumSize(QSize(120, 30))
        self.model_path.setMaximumSize(QSize(200, 30))
        self.model_path.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_6.addWidget(self.model_path)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(30)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.parametry_modelu = QFrame(self.verticalLayoutWidget_9)
        self.parametry_modelu.setObjectName(u"parametry_modelu")
        self.parametry_modelu.setMinimumSize(QSize(300, 250))
        self.parametry_modelu.setMaximumSize(QSize(300, 400))
        self.parametry_modelu.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.parametry_modelu_layout = QVBoxLayout(self.parametry_modelu)
        self.parametry_modelu_layout.setSpacing(9)
        self.parametry_modelu_layout.setObjectName(u"parametry_modelu_layout")
        self.parametry_modelu_layout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.layout_parametry_modelu = QVBoxLayout()
        self.layout_parametry_modelu.setSpacing(15)
        self.layout_parametry_modelu.setObjectName(u"layout_parametry_modelu")
        self.layout_parametry_modelu.setContentsMargins(10, 10, 10, 10)
        self.label_18 = QLabel(self.parametry_modelu)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_parametry_modelu.addWidget(self.label_18)

        self.label_6 = QLabel(self.parametry_modelu)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setItalic(True)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_parametry_modelu.addWidget(self.label_6)

        self.label_5 = QLabel(self.parametry_modelu)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_parametry_modelu.addWidget(self.label_5)

        self.label_7 = QLabel(self.parametry_modelu)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_parametry_modelu.addWidget(self.label_7)

        self.label_8 = QLabel(self.parametry_modelu)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_parametry_modelu.addWidget(self.label_8)

        self.label_9 = QLabel(self.parametry_modelu)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_parametry_modelu.addWidget(self.label_9)

        self.label_10 = QLabel(self.parametry_modelu)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_parametry_modelu.addWidget(self.label_10)


        self.parametry_modelu_layout.addLayout(self.layout_parametry_modelu)


        self.horizontalLayout_7.addWidget(self.parametry_modelu)

        self.hodnoty_modelu = QWidget(self.verticalLayoutWidget_9)
        self.hodnoty_modelu.setObjectName(u"hodnoty_modelu")
        self.hodnoty_modelu.setMinimumSize(QSize(350, 250))
        self.hodnoty_modelu.setMaximumSize(QSize(350, 400))
        self.hodnoty_modelu.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(self.hodnoty_modelu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_19 = QLabel(self.hodnoty_modelu)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_19)

        self.set_x_model = QLabel(self.hodnoty_modelu)
        self.set_x_model.setObjectName(u"set_x_model")
        self.set_x_model.setStyleSheet(u"border: 2px solid #00AEEF;\n"
"border-color: rgb(0, 85, 255);")
        self.set_x_model.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextEditable)

        self.verticalLayout_4.addWidget(self.set_x_model)

        self.set_y_model = QLabel(self.hodnoty_modelu)
        self.set_y_model.setObjectName(u"set_y_model")
        self.set_y_model.setStyleSheet(u"border: 2px solid #00AEEF;\n"
"border-color: rgb(0, 85, 255);")
        self.set_y_model.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextEditable)

        self.verticalLayout_4.addWidget(self.set_y_model)

        self.set_z_model = QLabel(self.hodnoty_modelu)
        self.set_z_model.setObjectName(u"set_z_model")
        self.set_z_model.setStyleSheet(u"border: 2px solid #00AEEF;\n"
"border-color: rgb(0, 85, 255);")
        self.set_z_model.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextEditable)

        self.verticalLayout_4.addWidget(self.set_z_model)

        self.set_yaw_model = QLabel(self.hodnoty_modelu)
        self.set_yaw_model.setObjectName(u"set_yaw_model")
        self.set_yaw_model.setStyleSheet(u"border: 2px solid #00AEEF;\n"
"border-color: rgb(0, 85, 255);")
        self.set_yaw_model.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextEditable)

        self.verticalLayout_4.addWidget(self.set_yaw_model)

        self.set_pitch_model = QLabel(self.hodnoty_modelu)
        self.set_pitch_model.setObjectName(u"set_pitch_model")
        self.set_pitch_model.setStyleSheet(u"border: 2px solid #00AEEF;\n"
"border-color: rgb(0, 85, 255);")
        self.set_pitch_model.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextEditable)

        self.verticalLayout_4.addWidget(self.set_pitch_model)

        self.set_roll_model = QLabel(self.hodnoty_modelu)
        self.set_roll_model.setObjectName(u"set_roll_model")
        self.set_roll_model.setStyleSheet(u"border: 2px solid #00AEEF;\n"
"border-color: rgb(0, 85, 255);")
        self.set_roll_model.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextEditable)

        self.verticalLayout_4.addWidget(self.set_roll_model)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)


        self.horizontalLayout_7.addWidget(self.hodnoty_modelu)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.openGLWidget = QOpenGLWidget(self.verticalLayoutWidget_9)
        self.openGLWidget.setObjectName(u"openGLWidget")
        self.openGLWidget.setMinimumSize(QSize(0, 350))
        self.openGLWidget.setMaximumSize(QSize(700, 500))

        self.verticalLayout_10.addWidget(self.openGLWidget)

        self.stackedWidget.addWidget(self.load_model_page)
        self.cut_process = QWidget()
        self.cut_process.setObjectName(u"cut_process")
        self.verticalLayoutWidget_5 = QWidget(self.cut_process)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(100, 0, 7661, 711))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 5, 20, 5)
        self.wid_sken_strategy = QWidget(self.verticalLayoutWidget_5)
        self.wid_sken_strategy.setObjectName(u"wid_sken_strategy")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wid_sken_strategy.sizePolicy().hasHeightForWidth())
        self.wid_sken_strategy.setSizePolicy(sizePolicy1)
        self.wid_sken_strategy.setMinimumSize(QSize(500, 130))
        self.wid_sken_strategy.setMaximumSize(QSize(700, 250))
        self.wid_sken_strategy.setAutoFillBackground(False)
        self.wid_sken_strategy.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"")
        self.title_sken_strategy = QLabel(self.wid_sken_strategy)
        self.title_sken_strategy.setObjectName(u"title_sken_strategy")
        self.title_sken_strategy.setGeometry(QRect(20, 20, 211, 31))
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.title_sken_strategy.setFont(font4)
        self.title_sken_strategy.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.title_sken_strategy.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_vnejsi_sken = QLabel(self.wid_sken_strategy)
        self.lbl_vnejsi_sken.setObjectName(u"lbl_vnejsi_sken")
        self.lbl_vnejsi_sken.setGeometry(QRect(330, 60, 101, 16))
        font5 = QFont()
        font5.setFamilies([u"Verdana"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.lbl_vnejsi_sken.setFont(font5)
        self.lbl_vnitrni_sken = QLabel(self.wid_sken_strategy)
        self.lbl_vnitrni_sken.setObjectName(u"lbl_vnitrni_sken")
        self.lbl_vnitrni_sken.setGeometry(QRect(540, 60, 101, 16))
        self.lbl_vnitrni_sken.setFont(font5)
        self.layoutWidget = QWidget(self.wid_sken_strategy)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(300, 90, 169, 91))
        self.layout_vnejsi_sken = QVBoxLayout(self.layoutWidget)
        self.layout_vnejsi_sken.setObjectName(u"layout_vnejsi_sken")
        self.layout_vnejsi_sken.setContentsMargins(0, 0, 0, 0)
        self.sken_zleva_pravo = QRadioButton(self.layoutWidget)
        self.sken_zleva_pravo.setObjectName(u"sken_zleva_pravo")

        self.layout_vnejsi_sken.addWidget(self.sken_zleva_pravo)

        self.sken_zprava_doleva = QRadioButton(self.layoutWidget)
        self.sken_zprava_doleva.setObjectName(u"sken_zprava_doleva")

        self.layout_vnejsi_sken.addWidget(self.sken_zprava_doleva)

        self.layoutWidget1 = QWidget(self.wid_sken_strategy)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(510, 90, 179, 91))
        self.layout_vnitrni_sken = QVBoxLayout(self.layoutWidget1)
        self.layout_vnitrni_sken.setObjectName(u"layout_vnitrni_sken")
        self.layout_vnitrni_sken.setContentsMargins(0, 0, 0, 0)
        self.sken_nahoru_dolu = QRadioButton(self.layoutWidget1)
        self.sken_nahoru_dolu.setObjectName(u"sken_nahoru_dolu")

        self.layout_vnitrni_sken.addWidget(self.sken_nahoru_dolu)

        self.sken_dolu_nahoru = QRadioButton(self.layoutWidget1)
        self.sken_dolu_nahoru.setObjectName(u"sken_dolu_nahoru")

        self.layout_vnitrni_sken.addWidget(self.sken_dolu_nahoru)

        self.label_4 = QLabel(self.wid_sken_strategy)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 60, 101, 16))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        self.label_4.setFont(font6)
        self.verticalLayoutWidget = QWidget(self.wid_sken_strategy)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 90, 241, 91))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout.addWidget(self.radioButton_3)


        self.verticalLayout_5.addWidget(self.wid_sken_strategy)

        self.wid_skenovaci_krok = QWidget(self.verticalLayoutWidget_5)
        self.wid_skenovaci_krok.setObjectName(u"wid_skenovaci_krok")
        sizePolicy1.setHeightForWidth(self.wid_skenovaci_krok.sizePolicy().hasHeightForWidth())
        self.wid_skenovaci_krok.setSizePolicy(sizePolicy1)
        self.wid_skenovaci_krok.setMinimumSize(QSize(500, 80))
        self.wid_skenovaci_krok.setMaximumSize(QSize(700, 80))
        self.wid_skenovaci_krok.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 12px;")
        self.title_sken_krok = QLabel(self.wid_skenovaci_krok)
        self.title_sken_krok.setObjectName(u"title_sken_krok")
        self.title_sken_krok.setGeometry(QRect(20, 10, 211, 31))
        self.title_sken_krok.setFont(font4)
        self.title_sken_krok.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.title_sken_krok.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutWidget2 = QWidget(self.wid_skenovaci_krok)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(50, 50, 531, 21))
        self.krok_skenu = QHBoxLayout(self.layoutWidget2)
        self.krok_skenu.setObjectName(u"krok_skenu")
        self.krok_skenu.setContentsMargins(0, 0, 0, 0)
        self.lbl_krok = QLabel(self.layoutWidget2)
        self.lbl_krok.setObjectName(u"lbl_krok")
        font7 = QFont()
        font7.setFamilies([u"Verdana"])
        font7.setBold(True)
        self.lbl_krok.setFont(font7)

        self.krok_skenu.addWidget(self.lbl_krok)

        self.set_krok = QLabel(self.layoutWidget2)
        self.set_krok.setObjectName(u"set_krok")
        font8 = QFont()
        font8.setFamilies([u"Verdana"])
        font8.setPointSize(12)
        self.set_krok.setFont(font8)
        self.set_krok.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.set_krok.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextEditable)

        self.krok_skenu.addWidget(self.set_krok)


        self.verticalLayout_5.addWidget(self.wid_skenovaci_krok)

        self.wid_sken_trajektorie = QWidget(self.verticalLayoutWidget_5)
        self.wid_sken_trajektorie.setObjectName(u"wid_sken_trajektorie")
        sizePolicy1.setHeightForWidth(self.wid_sken_trajektorie.sizePolicy().hasHeightForWidth())
        self.wid_sken_trajektorie.setSizePolicy(sizePolicy1)
        self.wid_sken_trajektorie.setMinimumSize(QSize(500, 80))
        self.wid_sken_trajektorie.setMaximumSize(QSize(700, 130))
        self.wid_sken_trajektorie.setAutoFillBackground(False)
        self.wid_sken_trajektorie.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"")
        self.title_sken_trajektorie = QLabel(self.wid_sken_trajektorie)
        self.title_sken_trajektorie.setObjectName(u"title_sken_trajektorie")
        self.title_sken_trajektorie.setGeometry(QRect(20, 10, 231, 31))
        self.title_sken_trajektorie.setFont(font4)
        self.title_sken_trajektorie.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.title_sken_trajektorie.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.create_traj = QPushButton(self.wid_sken_trajektorie)
        self.create_traj.setObjectName(u"create_traj")
        self.create_traj.setGeometry(QRect(250, 50, 181, 31))
        font9 = QFont()
        font9.setFamilies([u"Verdana"])
        font9.setPointSize(9)
        font9.setBold(False)
        font9.setItalic(False)
        self.create_traj.setFont(font9)
        self.create_traj.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.layoutWidget3 = QWidget(self.wid_sken_trajektorie)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(40, 60, 141, 23))
        self.layout_start = QHBoxLayout(self.layoutWidget3)
        self.layout_start.setObjectName(u"layout_start")
        self.layout_start.setContentsMargins(0, 0, 0, 0)
        self.lbl_start = QLabel(self.layoutWidget3)
        self.lbl_start.setObjectName(u"lbl_start")
        self.lbl_start.setFont(font5)

        self.layout_start.addWidget(self.lbl_start)

        self.set_start = QLabel(self.layoutWidget3)
        self.set_start.setObjectName(u"set_start")
        self.set_start.setFont(font8)
        self.set_start.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextEditable)

        self.layout_start.addWidget(self.set_start)

        self.layoutWidget4 = QWidget(self.wid_sken_trajektorie)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(40, 100, 141, 24))
        self.layout_cil = QHBoxLayout(self.layoutWidget4)
        self.layout_cil.setObjectName(u"layout_cil")
        self.layout_cil.setContentsMargins(0, 0, 0, 0)
        self.lbl_cil = QLabel(self.layoutWidget4)
        self.lbl_cil.setObjectName(u"lbl_cil")
        self.lbl_cil.setFont(font5)

        self.layout_cil.addWidget(self.lbl_cil)

        self.set_cil = QLabel(self.layoutWidget4)
        self.set_cil.setObjectName(u"set_cil")
        font10 = QFont()
        font10.setFamilies([u"Verdana"])
        font10.setPointSize(13)
        self.set_cil.setFont(font10)
        self.set_cil.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextEditable)

        self.layout_cil.addWidget(self.set_cil)

        self.save_traj = QPushButton(self.wid_sken_trajektorie)
        self.save_traj.setObjectName(u"save_traj")
        self.save_traj.setGeometry(QRect(250, 90, 181, 31))
        font11 = QFont()
        font11.setFamilies([u"Verdana"])
        self.save_traj.setFont(font11)
        self.save_traj.setStyleSheet(u"background-color: rgb(170, 255, 255);")

        self.verticalLayout_5.addWidget(self.wid_sken_trajektorie)

        self.openGLWidget_2 = QOpenGLWidget(self.verticalLayoutWidget_5)
        self.openGLWidget_2.setObjectName(u"openGLWidget_2")
        self.openGLWidget_2.setMinimumSize(QSize(500, 300))
        self.openGLWidget_2.setMaximumSize(QSize(700, 350))

        self.verticalLayout_5.addWidget(self.openGLWidget_2)

        self.stackedWidget.addWidget(self.cut_process)
        self.Simulation_page = QWidget()
        self.Simulation_page.setObjectName(u"Simulation_page")
        self.verticalLayoutWidget_6 = QWidget(self.Simulation_page)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(30, 10, 871, 671))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(30, 1, 5, 10)
        self.wid_sken_strategy_2 = QWidget(self.verticalLayoutWidget_6)
        self.wid_sken_strategy_2.setObjectName(u"wid_sken_strategy_2")
        self.wid_sken_strategy_2.setMinimumSize(QSize(700, 250))
        self.wid_sken_strategy_2.setMaximumSize(QSize(800, 300))
        self.wid_sken_strategy_2.setAutoFillBackground(False)
        self.wid_sken_strategy_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"")
        self.title_sken_strategy_2 = QLabel(self.wid_sken_strategy_2)
        self.title_sken_strategy_2.setObjectName(u"title_sken_strategy_2")
        self.title_sken_strategy_2.setGeometry(QRect(20, 10, 331, 31))
        self.title_sken_strategy_2.setFont(font4)
        self.title_sken_strategy_2.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.title_sken_strategy_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayoutWidget_2 = QWidget(self.wid_sken_strategy_2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 50, 761, 241))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 1, 10, 10)
        self.create_traj_2 = QPushButton(self.horizontalLayoutWidget_2)
        self.create_traj_2.setObjectName(u"create_traj_2")
        self.create_traj_2.setMinimumSize(QSize(150, 40))
        self.create_traj_2.setMaximumSize(QSize(220, 40))
        self.create_traj_2.setFont(font9)
        self.create_traj_2.setStyleSheet(u"border: 2px solid #00AEEF;\n"
"border-color: rgb(0, 85, 255);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_7.addWidget(self.create_traj_2)

        self.create_traj_3 = QPushButton(self.horizontalLayoutWidget_2)
        self.create_traj_3.setObjectName(u"create_traj_3")
        self.create_traj_3.setMinimumSize(QSize(220, 40))
        self.create_traj_3.setMaximumSize(QSize(220, 40))
        self.create_traj_3.setFont(font9)
        self.create_traj_3.setStyleSheet(u"border: 2px solid #00AEEF;\n"
"border-color: rgb(0, 85, 255);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_7.addWidget(self.create_traj_3)

        self.create_traj_4 = QPushButton(self.horizontalLayoutWidget_2)
        self.create_traj_4.setObjectName(u"create_traj_4")
        self.create_traj_4.setMinimumSize(QSize(150, 40))
        self.create_traj_4.setMaximumSize(QSize(220, 40))
        self.create_traj_4.setFont(font9)
        self.create_traj_4.setStyleSheet(u"border: 2px solid #00AEEF;\n"
"background-color: rgb(179, 255, 250);\n"
"border-color: rgb(0, 85, 255);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_7.addWidget(self.create_traj_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.scrollArea = QScrollArea(self.horizontalLayoutWidget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(400, 200))
        self.scrollArea.setMaximumSize(QSize(500, 200))
        self.scrollArea.setStyleSheet(u"background-color: rgb(226, 226, 226);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 500, 200))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_6.addWidget(self.wid_sken_strategy_2)

        self.wid_sken_strategy_3 = QWidget(self.verticalLayoutWidget_6)
        self.wid_sken_strategy_3.setObjectName(u"wid_sken_strategy_3")
        self.wid_sken_strategy_3.setMinimumSize(QSize(700, 300))
        self.wid_sken_strategy_3.setMaximumSize(QSize(800, 350))
        self.wid_sken_strategy_3.setAutoFillBackground(False)
        self.wid_sken_strategy_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"")
        self.title_sken_strategy_3 = QLabel(self.wid_sken_strategy_3)
        self.title_sken_strategy_3.setObjectName(u"title_sken_strategy_3")
        self.title_sken_strategy_3.setGeometry(QRect(20, 10, 391, 31))
        self.title_sken_strategy_3.setFont(font4)
        self.title_sken_strategy_3.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.title_sken_strategy_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayoutWidget_3 = QWidget(self.wid_sken_strategy_3)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(20, 50, 761, 281))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.create_traj_5 = QPushButton(self.horizontalLayoutWidget_3)
        self.create_traj_5.setObjectName(u"create_traj_5")
        self.create_traj_5.setMinimumSize(QSize(250, 50))
        self.create_traj_5.setMaximumSize(QSize(250, 50))
        self.create_traj_5.setFont(font9)
        self.create_traj_5.setStyleSheet(u"border: 2px solid #00AEEF;\n"
"border-color: rgb(0, 85, 255);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_8.addWidget(self.create_traj_5)

        self.create_traj_6 = QPushButton(self.horizontalLayoutWidget_3)
        self.create_traj_6.setObjectName(u"create_traj_6")
        self.create_traj_6.setMinimumSize(QSize(220, 50))
        self.create_traj_6.setMaximumSize(QSize(250, 50))
        self.create_traj_6.setFont(font9)
        self.create_traj_6.setStyleSheet(u"border: 2px solid #00AEEF;\n"
"border-color: rgb(0, 85, 255);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_8.addWidget(self.create_traj_6)

        self.create_traj_7 = QPushButton(self.horizontalLayoutWidget_3)
        self.create_traj_7.setObjectName(u"create_traj_7")
        self.create_traj_7.setMinimumSize(QSize(200, 50))
        self.create_traj_7.setMaximumSize(QSize(250, 50))
        self.create_traj_7.setFont(font9)
        self.create_traj_7.setStyleSheet(u"border: 2px solid #00AEEF;\n"
"background-color: rgb(179, 255, 250);\n"
"border-color: rgb(0, 85, 255);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_8.addWidget(self.create_traj_7)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.scrollArea_2 = QScrollArea(self.horizontalLayoutWidget_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(400, 250))
        self.scrollArea_2.setMaximumSize(QSize(500, 250))
        self.scrollArea_2.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 461, 250))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_4.addWidget(self.scrollArea_2)


        self.verticalLayout_6.addWidget(self.wid_sken_strategy_3)

        self.stackedWidget.addWidget(self.Simulation_page)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayoutWidget_4 = QWidget(self.page)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(60, 0, 872, 651))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.label_13 = QLabel(self.verticalLayoutWidget_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(360, 25))
        self.label_13.setMaximumSize(QSize(370, 35))
        font12 = QFont()
        font12.setFamilies([u"Verdana"])
        font12.setPointSize(10)
        self.label_13.setFont(font12)
        self.label_13.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")

        self.verticalLayout_9.addWidget(self.label_13)

        self.widget = QWidget(self.verticalLayoutWidget_4)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(600, 80))
        self.widget.setMaximumSize(QSize(850, 90))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayoutWidget_4 = QWidget(self.widget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(0, 10, 751, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.label_11 = QLabel(self.horizontalLayoutWidget_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(130, 25))
        self.label_11.setMaximumSize(QSize(140, 35))
        self.label_11.setFont(font12)
        self.label_11.setStyleSheet(u"border: 2px solid #00AEEF;\n"
"border-color: rgb(0, 85, 255);")

        self.horizontalLayout.addWidget(self.label_11)

        self.comboBox = QComboBox(self.horizontalLayoutWidget_4)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(90, 25))
        self.comboBox.setMaximumSize(QSize(100, 35))
        self.comboBox.setSizeIncrement(QSize(60, 35))

        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_12 = QLabel(self.horizontalLayoutWidget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(80, 25))
        self.label_12.setMaximumSize(QSize(100, 35))
        self.label_12.setSizeIncrement(QSize(100, 30))
        self.label_12.setFont(font12)
        self.label_12.setStyleSheet(u"border: 2px solid #00AEEF;\n"
"border-color: rgb(0, 85, 255);")

        self.horizontalLayout.addWidget(self.label_12)

        self.comboBox_2 = QComboBox(self.horizontalLayoutWidget_4)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(130, 25))
        self.comboBox_2.setMaximumSize(QSize(150, 35))

        self.horizontalLayout.addWidget(self.comboBox_2)


        self.verticalLayout_9.addWidget(self.widget)


        self.verticalLayout_11.addLayout(self.verticalLayout_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.verticalLayoutWidget_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(800, 80))
        self.widget_2.setMaximumSize(QSize(900, 150))
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayoutWidget_6 = QWidget(self.widget_2)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 40, 741, 45))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.label_15 = QLabel(self.horizontalLayoutWidget_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(50, 25))
        self.label_15.setMaximumSize(QSize(80, 35))
        self.label_15.setFont(font7)
        self.label_15.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.label_15)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(120, 25))
        self.lineEdit.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_9.addWidget(self.lineEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.label_16 = QLabel(self.horizontalLayoutWidget_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(50, 25))
        self.label_16.setMaximumSize(QSize(80, 35))
        self.label_16.setFont(font7)
        self.label_16.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.label_16)

        self.lineEdit_2 = QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(120, 25))
        self.lineEdit_2.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_9.addWidget(self.lineEdit_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.label_17 = QLabel(self.horizontalLayoutWidget_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(50, 25))
        self.label_17.setMaximumSize(QSize(80, 35))
        self.label_17.setFont(font7)
        self.label_17.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.label_17)

        self.lineEdit_3 = QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(120, 25))
        self.lineEdit_3.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_9.addWidget(self.lineEdit_3)

        self.label_14 = QLabel(self.widget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 0, 180, 31))
        self.label_14.setMinimumSize(QSize(150, 25))
        self.label_14.setMaximumSize(QSize(180, 35))
        self.label_14.setFont(font12)
        self.label_14.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.horizontalLayoutWidget_7 = QWidget(self.widget_2)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(10, 80, 741, 45))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.label_20 = QLabel(self.horizontalLayoutWidget_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(50, 25))
        self.label_20.setMaximumSize(QSize(80, 35))
        self.label_20.setFont(font7)
        self.label_20.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.label_20)

        self.lineEdit_4 = QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(120, 25))
        self.lineEdit_4.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_10.addWidget(self.lineEdit_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.label_21 = QLabel(self.horizontalLayoutWidget_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(50, 25))
        self.label_21.setMaximumSize(QSize(80, 35))
        self.label_21.setFont(font7)
        self.label_21.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.label_21)

        self.lineEdit_5 = QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(120, 25))
        self.lineEdit_5.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_10.addWidget(self.lineEdit_5)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.label_22 = QLabel(self.horizontalLayoutWidget_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(50, 25))
        self.label_22.setMaximumSize(QSize(80, 35))
        self.label_22.setFont(font7)
        self.label_22.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.label_22)

        self.lineEdit_6 = QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(120, 25))
        self.lineEdit_6.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_10.addWidget(self.lineEdit_6)


        self.horizontalLayout_5.addWidget(self.widget_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.verticalLayoutWidget_4)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(850, 100))
        self.widget_3.setMaximumSize(QSize(900, 150))
        self.widget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayoutWidget_9 = QWidget(self.widget_3)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 50, 741, 45))
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.label_23 = QLabel(self.horizontalLayoutWidget_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(50, 25))
        self.label_23.setMaximumSize(QSize(80, 35))
        self.label_23.setFont(font7)
        self.label_23.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.label_23)

        self.lineEdit_7 = QLineEdit(self.horizontalLayoutWidget_9)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(120, 25))
        self.lineEdit_7.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_12.addWidget(self.lineEdit_7)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)

        self.label_24 = QLabel(self.horizontalLayoutWidget_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(50, 25))
        self.label_24.setMaximumSize(QSize(80, 35))
        self.label_24.setFont(font7)
        self.label_24.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.label_24)

        self.lineEdit_8 = QLineEdit(self.horizontalLayoutWidget_9)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(120, 25))
        self.lineEdit_8.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_12.addWidget(self.lineEdit_8)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)

        self.label_25 = QLabel(self.horizontalLayoutWidget_9)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(50, 25))
        self.label_25.setMaximumSize(QSize(80, 35))
        self.label_25.setFont(font7)
        self.label_25.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.label_25)

        self.lineEdit_9 = QLineEdit(self.horizontalLayoutWidget_9)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(120, 25))
        self.lineEdit_9.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_12.addWidget(self.lineEdit_9)

        self.label_26 = QLabel(self.widget_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 10, 180, 31))
        self.label_26.setMinimumSize(QSize(150, 25))
        self.label_26.setMaximumSize(QSize(180, 35))
        self.label_26.setFont(font12)
        self.label_26.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.horizontalLayoutWidget_10 = QWidget(self.widget_3)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(10, 90, 741, 45))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(10, 10, 10, 10)
        self.label_27 = QLabel(self.horizontalLayoutWidget_10)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(50, 25))
        self.label_27.setMaximumSize(QSize(80, 35))
        self.label_27.setFont(font7)
        self.label_27.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.label_27)

        self.lineEdit_10 = QLineEdit(self.horizontalLayoutWidget_10)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(120, 25))
        self.lineEdit_10.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_13.addWidget(self.lineEdit_10)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)

        self.label_28 = QLabel(self.horizontalLayoutWidget_10)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(50, 25))
        self.label_28.setMaximumSize(QSize(80, 35))
        self.label_28.setFont(font7)
        self.label_28.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.label_28)

        self.lineEdit_11 = QLineEdit(self.horizontalLayoutWidget_10)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(120, 25))
        self.lineEdit_11.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_13.addWidget(self.lineEdit_11)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)

        self.label_29 = QLabel(self.horizontalLayoutWidget_10)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(50, 25))
        self.label_29.setMaximumSize(QSize(80, 35))
        self.label_29.setFont(font7)
        self.label_29.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.label_29)

        self.lineEdit_12 = QLineEdit(self.horizontalLayoutWidget_10)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(120, 25))
        self.lineEdit_12.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_13.addWidget(self.lineEdit_12)


        self.horizontalLayout_11.addWidget(self.widget_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.verticalLayoutWidget_4)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(850, 100))
        self.widget_4.setMaximumSize(QSize(900, 150))
        self.widget_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayoutWidget_12 = QWidget(self.widget_4)
        self.horizontalLayoutWidget_12.setObjectName(u"horizontalLayoutWidget_12")
        self.horizontalLayoutWidget_12.setGeometry(QRect(10, 50, 741, 45))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.label_30 = QLabel(self.horizontalLayoutWidget_12)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(50, 25))
        self.label_30.setMaximumSize(QSize(80, 35))
        self.label_30.setFont(font7)
        self.label_30.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.label_30)

        self.lineEdit_13 = QLineEdit(self.horizontalLayoutWidget_12)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMinimumSize(QSize(120, 25))
        self.lineEdit_13.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_15.addWidget(self.lineEdit_13)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_10)

        self.label_31 = QLabel(self.horizontalLayoutWidget_12)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(50, 25))
        self.label_31.setMaximumSize(QSize(80, 35))
        self.label_31.setFont(font7)
        self.label_31.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.label_31)

        self.lineEdit_14 = QLineEdit(self.horizontalLayoutWidget_12)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(120, 25))
        self.lineEdit_14.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_15.addWidget(self.lineEdit_14)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_11)

        self.label_32 = QLabel(self.horizontalLayoutWidget_12)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(50, 25))
        self.label_32.setMaximumSize(QSize(80, 35))
        self.label_32.setFont(font7)
        self.label_32.setStyleSheet(u"")

        self.horizontalLayout_15.addWidget(self.label_32)

        self.lineEdit_15 = QLineEdit(self.horizontalLayoutWidget_12)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMinimumSize(QSize(120, 25))
        self.lineEdit_15.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_15.addWidget(self.lineEdit_15)

        self.label_33 = QLabel(self.widget_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(10, 10, 180, 31))
        self.label_33.setMinimumSize(QSize(150, 25))
        self.label_33.setMaximumSize(QSize(180, 35))
        self.label_33.setFont(font12)
        self.label_33.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.horizontalLayoutWidget_13 = QWidget(self.widget_4)
        self.horizontalLayoutWidget_13.setObjectName(u"horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(10, 90, 741, 45))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(10, 10, 10, 10)
        self.label_34 = QLabel(self.horizontalLayoutWidget_13)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(50, 25))
        self.label_34.setMaximumSize(QSize(80, 35))
        self.label_34.setFont(font7)
        self.label_34.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.label_34)

        self.lineEdit_16 = QLineEdit(self.horizontalLayoutWidget_13)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(120, 25))
        self.lineEdit_16.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_16.addWidget(self.lineEdit_16)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_12)

        self.label_35 = QLabel(self.horizontalLayoutWidget_13)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(50, 25))
        self.label_35.setMaximumSize(QSize(80, 35))
        self.label_35.setFont(font7)
        self.label_35.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.label_35)

        self.lineEdit_17 = QLineEdit(self.horizontalLayoutWidget_13)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMinimumSize(QSize(120, 25))
        self.lineEdit_17.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_16.addWidget(self.lineEdit_17)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_13)

        self.label_36 = QLabel(self.horizontalLayoutWidget_13)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(50, 25))
        self.label_36.setMaximumSize(QSize(80, 35))
        self.label_36.setFont(font7)
        self.label_36.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.label_36)

        self.lineEdit_18 = QLineEdit(self.horizontalLayoutWidget_13)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMinimumSize(QSize(120, 25))
        self.lineEdit_18.setMaximumSize(QSize(150, 35))

        self.horizontalLayout_16.addWidget(self.lineEdit_18)


        self.horizontalLayout_14.addWidget(self.widget_4)


        self.verticalLayout_11.addLayout(self.horizontalLayout_14)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(720, 650, 150, 51))
        self.pushButton.setMinimumSize(QSize(150, 50))
        self.pushButton.setMaximumSize(QSize(200, 60))
        self.pushButton.setFont(font5)
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 255, 162);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;\n"
"border: 2px solid #00AEEF;\n"
"border-color: rgb(0, 85, 255);")
        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(479, 650, 191, 51))
        self.pushButton_2.setMinimumSize(QSize(150, 50))
        self.pushButton_2.setMaximumSize(QSize(200, 60))
        self.pushButton_2.setFont(font5)
        self.pushButton_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 127);\n"
"border-radius: 15px;\n"
"border: 2px solid #00AEEF;\n"
"border-color: rgb(0, 85, 255);")
        self.stackedWidget.addWidget(self.page)
        self.menu_page = QWidget()
        self.menu_page.setObjectName(u"menu_page")
        self.label = QLabel(self.menu_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 310, 591, 351))
        self.label.setPixmap(QPixmap(u"../vana_scanmaster.jpg"))
        self.label.setScaledContents(True)
        self.horizontalLayoutWidget = QWidget(self.menu_page)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(190, 50, 581, 211))
        self.new_old_generator = QHBoxLayout(self.horizontalLayoutWidget)
        self.new_old_generator.setSpacing(15)
        self.new_old_generator.setObjectName(u"new_old_generator")
        self.new_old_generator.setContentsMargins(10, 10, 10, 10)
        self.exist_project_btn = QPushButton(self.horizontalLayoutWidget)
        self.exist_project_btn.setObjectName(u"exist_project_btn")
        sizePolicy.setHeightForWidth(self.exist_project_btn.sizePolicy().hasHeightForWidth())
        self.exist_project_btn.setSizePolicy(sizePolicy)
        self.exist_project_btn.setMinimumSize(QSize(200, 100))
        font13 = QFont()
        font13.setFamilies([u"Verdana"])
        font13.setPointSize(16)
        self.exist_project_btn.setFont(font13)
        self.exist_project_btn.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border: 2px solid #00AEEF;\n"
"border-color: rgb(0, 85, 255);")
        self.exist_project_btn.setIcon(icon2)
        self.exist_project_btn.setIconSize(QSize(30, 30))

        self.new_old_generator.addWidget(self.exist_project_btn)

        self.new_project_btn = QPushButton(self.horizontalLayoutWidget)
        self.new_project_btn.setObjectName(u"new_project_btn")
        sizePolicy.setHeightForWidth(self.new_project_btn.sizePolicy().hasHeightForWidth())
        self.new_project_btn.setSizePolicy(sizePolicy)
        self.new_project_btn.setMinimumSize(QSize(200, 100))
        font14 = QFont()
        font14.setFamilies([u"Verdana"])
        font14.setPointSize(15)
        font14.setBold(False)
        self.new_project_btn.setFont(font14)
        self.new_project_btn.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid #00AEEF;\n"
"border-color: rgb(0, 85, 255);")
        icon8 = QIcon(QIcon.fromTheme(u"QIcon::ThemeIcon::DocumentNew"))
        self.new_project_btn.setIcon(icon8)
        self.new_project_btn.setIconSize(QSize(30, 30))

        self.new_old_generator.addWidget(self.new_project_btn)

        self.stackedWidget.addWidget(self.menu_page)
        self.layoutWidget5 = QWidget(self.centralwidget)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        QMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(QMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        QMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(QMainWindow)
        self.end_btn.clicked.connect(QMainWindow.close)
        self.cut_process_btn.toggled.connect(self.stackedWidget.show)
        self.load_model_btn.clicked.connect(self.stackedWidget.show)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(QMainWindow)
    # setupUi

    def retranslateUi(self, QMainWindow):
        QMainWindow.setWindowTitle(QCoreApplication.translate("QMainWindow", u"ATG NAVI - generator", None))
        self.Menu_btn.setText(QCoreApplication.translate("QMainWindow", u"Menu", None))
        self.load_model_btn.setText(QCoreApplication.translate("QMainWindow", u"Load model", None))
        self.cut_process_btn.setText(QCoreApplication.translate("QMainWindow", u"Cut process", None))
        self.database_btn.setText(QCoreApplication.translate("QMainWindow", u"Database", None))
        self.trajektorie_btn.setText(QCoreApplication.translate("QMainWindow", u"Trajektorie", None))
        self.simulation_btn.setText(QCoreApplication.translate("QMainWindow", u"Simulation", None))
        self.end_btn.setText(QCoreApplication.translate("QMainWindow", u"End", None))
        self.atg_logo_image.setText("")
        self.label_2.setText(QCoreApplication.translate("QMainWindow", u"NAVI - GENER\u00c1TOR TRAJEKTORI\u00cd ", None))
        self.label_3.setText(QCoreApplication.translate("QMainWindow", u"N\u00e1stroj pro generov\u00e1n\u00ed trajektorie a simulaci", None))
        self.load_model_btn_2.setText(QCoreApplication.translate("QMainWindow", u"OTEV\u0158\u00cdT MODEL", None))
        self.model_path.setText(QCoreApplication.translate("QMainWindow", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("QMainWindow", u"PARAMETRY MODELU", None))
        self.label_6.setText(QCoreApplication.translate("QMainWindow", u"Poloha modelu v ose Y [mm]", None))
        self.label_5.setText(QCoreApplication.translate("QMainWindow", u"Poloha modelu v ose X [mm]", None))
        self.label_7.setText(QCoreApplication.translate("QMainWindow", u"Poloha modelu v ose Z [mm]", None))
        self.label_8.setText(QCoreApplication.translate("QMainWindow", u"Orientace modelu YAW [\u00b0]", None))
        self.label_9.setText(QCoreApplication.translate("QMainWindow", u"Orientace modelu PITCH [\u00b0]", None))
        self.label_10.setText(QCoreApplication.translate("QMainWindow", u"Orientace modelu ROLL [\u00b0]", None))
        self.label_19.setText(QCoreApplication.translate("QMainWindow", u"HODNOTY ", None))
        self.set_x_model.setText("")
        self.set_y_model.setText("")
        self.set_z_model.setText("")
        self.set_yaw_model.setText("")
        self.set_pitch_model.setText("")
        self.set_roll_model.setText("")
        self.title_sken_strategy.setText(QCoreApplication.translate("QMainWindow", u"Skenovac\u00ed strategie", None))
        self.lbl_vnejsi_sken.setText(QCoreApplication.translate("QMainWindow", u"Vn\u011bj\u0161\u00ed sken", None))
        self.lbl_vnitrni_sken.setText(QCoreApplication.translate("QMainWindow", u"Vnit\u0159n\u00ed sken", None))
        self.sken_zleva_pravo.setText(QCoreApplication.translate("QMainWindow", u"Skenov\u00e1n\u00ed zleva do prava", None))
        self.sken_zprava_doleva.setText(QCoreApplication.translate("QMainWindow", u"Skenov\u00e1n\u00ed z prava do leva", None))
        self.sken_nahoru_dolu.setText(QCoreApplication.translate("QMainWindow", u"Skenov\u00e1n\u00ed ze shora dol\u016f", None))
        self.sken_dolu_nahoru.setText(QCoreApplication.translate("QMainWindow", u"Skenov\u00e1n\u00ed ze spodu nahoru", None))
        self.label_4.setText(QCoreApplication.translate("QMainWindow", u"Orientace sondy", None))
        self.radioButton.setText(QCoreApplication.translate("QMainWindow", u"Sonda je kolmo k povrchu", None))
        self.radioButton_2.setText(QCoreApplication.translate("QMainWindow", u"Sonda je v rovin\u011b skenu nato\u010den\u00e1", None))
        self.radioButton_3.setText(QCoreApplication.translate("QMainWindow", u"Sonda nen\u00ed v rovin\u011b skenu", None))
        self.title_sken_krok.setText(QCoreApplication.translate("QMainWindow", u"Skenovac\u00ed krok", None))
        self.lbl_krok.setText(QCoreApplication.translate("QMainWindow", u"Krok mezi dv\u011bma po sob\u011b skenovac\u00edmi body [mm]", None))
        self.set_krok.setText(QCoreApplication.translate("QMainWindow", u"0.5", None))
        self.title_sken_trajektorie.setText(QCoreApplication.translate("QMainWindow", u"Skenovac\u00ed trajektorie", None))
        self.create_traj.setText(QCoreApplication.translate("QMainWindow", u"VYTVO\u0158IT TRAJEKTORII", None))
        self.lbl_start.setText(QCoreApplication.translate("QMainWindow", u"START", None))
        self.set_start.setText(QCoreApplication.translate("QMainWindow", u"100", None))
        self.lbl_cil.setText(QCoreApplication.translate("QMainWindow", u"C\u00cdL", None))
        self.set_cil.setText(QCoreApplication.translate("QMainWindow", u"200", None))
        self.save_traj.setText(QCoreApplication.translate("QMainWindow", u"ULO\u017dIT TRAJEKTORII", None))
        self.title_sken_strategy_2.setText(QCoreApplication.translate("QMainWindow", u"V\u00fdb\u011br skenovac\u00edch trajektori\u00ed", None))
        self.create_traj_2.setText(QCoreApplication.translate("QMainWindow", u"OTEV\u0158\u00cdT SEZNAM TRAJEKTORI\u00cd", None))
        self.create_traj_3.setText(QCoreApplication.translate("QMainWindow", u"SMAZAT VYBRANOU TRAJEKTORII", None))
        self.create_traj_4.setText(QCoreApplication.translate("QMainWindow", u"ULO\u017dIT V\u00ddB\u011aR", None))
        self.title_sken_strategy_3.setText(QCoreApplication.translate("QMainWindow", u"\u00daprava p\u0159\u00edjezdov\u00e9 a odjezdov\u00e9 trajektorie", None))
        self.create_traj_5.setText(QCoreApplication.translate("QMainWindow", u"P\u0158IDAT P\u0158\u00cdJEZDOVOU TRAJEKTORII", None))
        self.create_traj_6.setText(QCoreApplication.translate("QMainWindow", u"P\u0158IDAT ODJEZDOVOU TRAJEKTORII", None))
        self.create_traj_7.setText(QCoreApplication.translate("QMainWindow", u"POTVRDIT VOLBU", None))
        self.label_13.setText(QCoreApplication.translate("QMainWindow", u"Nastaven\u00ed konfigurace robota a vybr\u00e1n\u00ed typu sondy ", None))
        self.label_11.setText(QCoreApplication.translate("QMainWindow", u"Konfigurace robota", None))
        self.label_12.setText(QCoreApplication.translate("QMainWindow", u"Typ sondy", None))
        self.label_15.setText(QCoreApplication.translate("QMainWindow", u"x [mm]", None))
        self.label_16.setText(QCoreApplication.translate("QMainWindow", u"y [mm]", None))
        self.label_17.setText(QCoreApplication.translate("QMainWindow", u"z [mm]", None))
        self.label_14.setText(QCoreApplication.translate("QMainWindow", u"Home poloha robota", None))
        self.label_20.setText(QCoreApplication.translate("QMainWindow", u"W [\u00b0]", None))
        self.label_21.setText(QCoreApplication.translate("QMainWindow", u"P [\u00b0]", None))
        self.label_22.setText(QCoreApplication.translate("QMainWindow", u"R [\u00b0]", None))
        self.label_23.setText(QCoreApplication.translate("QMainWindow", u"x [mm]", None))
        self.label_24.setText(QCoreApplication.translate("QMainWindow", u"y [mm]", None))
        self.label_25.setText(QCoreApplication.translate("QMainWindow", u"z [mm]", None))
        self.label_26.setText(QCoreApplication.translate("QMainWindow", u"Toolframe robota", None))
        self.label_27.setText(QCoreApplication.translate("QMainWindow", u"W [\u00b0]", None))
        self.label_28.setText(QCoreApplication.translate("QMainWindow", u"P [\u00b0]", None))
        self.label_29.setText(QCoreApplication.translate("QMainWindow", u"R [\u00b0]", None))
        self.label_30.setText(QCoreApplication.translate("QMainWindow", u"x [mm]", None))
        self.label_31.setText(QCoreApplication.translate("QMainWindow", u"y [mm]", None))
        self.label_32.setText(QCoreApplication.translate("QMainWindow", u"z [mm]", None))
        self.label_33.setText(QCoreApplication.translate("QMainWindow", u"Userframe robota", None))
        self.label_34.setText(QCoreApplication.translate("QMainWindow", u"W [\u00b0]", None))
        self.label_35.setText(QCoreApplication.translate("QMainWindow", u"P [\u00b0]", None))
        self.label_36.setText(QCoreApplication.translate("QMainWindow", u"R [\u00b0]", None))
        self.pushButton.setText(QCoreApplication.translate("QMainWindow", u"SPUSTIT SIMULACI", None))
        self.pushButton_2.setText(QCoreApplication.translate("QMainWindow", u"RESTARTOVAT SIMULACI", None))
        self.label.setText("")
#if QT_CONFIG(tooltip)
        self.exist_project_btn.setToolTip(QCoreApplication.translate("QMainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">Otestuje se ji\u017e vytvo\u0159en\u00e1 trajektorie</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.exist_project_btn.setText(QCoreApplication.translate("QMainWindow", u"OPEN GENERATOR", None))
#if QT_CONFIG(tooltip)
        self.new_project_btn.setToolTip(QCoreApplication.translate("QMainWindow", u"<html><head/><body><p>Vytvo\u0159\u00ed se nov\u00e1 trajektorie pro konkr\u00e9tn\u00ed d\u00edl</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.new_project_btn.setText(QCoreApplication.translate("QMainWindow", u"NEW GENERATOR", None))
    # retranslateUi

