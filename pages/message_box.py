from PySide6.QtWidgets import QMessageBox


class MessageBox:
    @staticmethod
    def show(parent=None, title="Message", text="", icon=QMessageBox.Question):
        msg_box = QMessageBox(parent)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setIcon(icon)
        if icon==QMessageBox.Question:
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
        elif icon == QMessageBox.critical or QMessageBox.information:
            msg_box.setStandardButtons(QMessageBox.Ok)

        msg_box.setStyleSheet("""
        QMessageBox {
            background-color: white;
        }

        QMessageBox QLabel {
            color: black;
            background-color: transparent;
            font-size: 14px;
        }

        QMessageBox QPushButton {
            background-color: #f0f0f0;
            color: black;
            border: 1px solid #b0b0b0;
            border-radius: 4px;
            padding: 6px 16px;
            min-width: 80px;
        }

        QMessageBox QPushButton:hover {
            background-color: #e0e0e0;
        }

        QMessageBox QPushButton:pressed {
            background-color: #d0d0d0;
        }
        """)

        return msg_box.exec()