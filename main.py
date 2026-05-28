import sys
import os
from PySide6.QtWidgets import QApplication
from My_sidebar import MySideBar


# print(f"Cesty k DLL: {os.environ.get('PATH')}")
app = QApplication(sys.argv)
window = MySideBar()
window.show()
sys.exit(app.exec())
