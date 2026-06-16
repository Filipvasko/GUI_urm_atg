from PySide6.QtWidgets import QMessageBox


class MessageBox:
    @staticmethod
    def show(parent=None, title="Message", text="", icon=QMessageBox.Question):
        msg_box = QMessageBox(parent)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setIcon(icon)

        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)

        msg_box.setStyleSheet("""
        QMessageBox {
            background-color: #252525;
        }

        QMessageBox QLabel {
            color: white;
            font-size: 14px;
        }

        QMessageBox QPushButton {
            background-color: #3a7afe;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 6px 12px;
            min-width: 80px;
        }

        QMessageBox QPushButton:hover {
            background-color: #245fd1;
        }
        """)

        return msg_box.exec()