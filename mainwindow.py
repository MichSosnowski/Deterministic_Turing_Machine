import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from ui_form import Ui_MainWindow
from files_classes.file_reader import FileReader
import constants.constants as constants


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.create_file_connection()
        self.add_pixmap_for_turing_machine_tape()
        self.add_text_to_file_text_browser()
        self.set_entry_word_label()
        self.set_result_word_label(constants.NO_WORD)

    def create_file_connection(self) -> None:
        try:
            self.file_reader: FileReader = FileReader(constants.FILENAME)
        except FileNotFoundError:
            QApplication.beep()
            self.show_file_error_dialog(constants.MESSAGE_TITLE, constants.MESSAGE)
            exit(constants.EXIT_FAILURE)

    def show_file_error_dialog(self, title: str, message: str) -> None:
        QMessageBox.critical(self, title, message)

    def add_pixmap_for_turing_machine_tape(self) -> None:
        canvas: QPixmap = QPixmap(self.turing_machine_tape.width(), self.turing_machine_tape.height())
        canvas.fill(Qt.white)
        self.turing_machine_tape.setPixmap(canvas)
        self.turing_machine_tape.setScaledContents(True)

    def add_text_to_file_text_browser(self) -> None:
        self.file_text_browser.clear()
        self.file_text_browser.setText(self.file_reader.get_all_data_from_file())

    def set_entry_word_label(self) -> None:
        self.entry_word_label.clear()
        self.entry_word_label.setText(constants.ENTRY_WORD + self.file_reader.get_entry_word_from_file())

    def set_result_word_label(self, result_text: str) -> None:
        self.result_word_label.clear()
        self.result_word_label.setText(constants.RESULT_WORD + result_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setWindowTitle(constants.WINDOW_TITLE)
    widget.show()
    sys.exit(app.exec())
