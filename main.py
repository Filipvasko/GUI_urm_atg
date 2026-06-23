import sys
import os
from PySide6.QtWidgets import QApplication, QStyleFactory
from My_sidebar import MySideBars


# print(f"Cesty k DLL: {os.environ.get('PATH')}")
app = QApplication(sys.argv)

print("Python:", sys.executable)
print("Dostupné styly:", QStyleFactory.keys())
print("Aktivní styl:", app.style().objectName())

app.setStyle("windowsvista")
window = MySideBars()
window.show()
sys.exit(app.exec())
