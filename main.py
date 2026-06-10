import sys
import os
from PySide6.QtWidgets import QApplication
from My_sidebar import MySideBars


# print(f"Cesty k DLL: {os.environ.get('PATH')}")
app = QApplication(sys.argv)
window = MySideBars()
window.show()
sys.exit(app.exec())
