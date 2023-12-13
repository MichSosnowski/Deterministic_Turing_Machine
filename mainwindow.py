import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from ui_form import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        canvas = QPixmap(self.turing_machine_tape.width(), self.turing_machine_tape.height())
        canvas.fill(Qt.white)
        self.turing_machine_tape.setPixmap(canvas)
        self.turing_machine_tape.setScaledContents(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setWindowTitle('Maszyna Turinga')
    widget.show()
    sys.exit(app.exec())
