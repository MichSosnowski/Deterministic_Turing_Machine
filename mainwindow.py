import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap, QColor, QPainter, QPen
from ui_form import Ui_MainWindow
from files_classes.file_reader import FileReader
import constants.constants as constants


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.set_contents_for_widgets()
        self.add_pixmap_for_turing_machine_label()
        self.draw_turing_machine()
        self.add_commands_for_buttons()

    def set_contents_for_widgets(self) -> None:
        self.create_file_connection()
        self.add_text_to_file_text_browser()
        self.set_entry_word_label()
        self.set_result_word_label(constants.EMPTY_STRING)

    def create_file_connection(self) -> None:
        try:
            self.file_reader: FileReader = FileReader(constants.FILENAME)
        except FileNotFoundError:
            self.show_file_error_dialog(constants.MESSAGE_TITLE, constants.MESSAGE)
            exit(constants.EXIT_FAILURE)

    def show_file_error_dialog(self, title: str, message: str) -> None:
        QApplication.beep()
        QMessageBox.critical(self, title, message)

    def add_text_to_file_text_browser(self) -> None:
        self.file_text_browser.clear()
        self.file_text_browser.setText(self.file_reader.get_all_data_from_file())

    def add_pixmap_for_turing_machine_label(self) -> None:
        pixmap_width: int = self.width() * constants.WIDTH_COEFFICIENT
        pixmap_height: int = self.height() * constants.HEIGHT_COEFFICIENT
        canvas: QPixmap = QPixmap(pixmap_width, pixmap_height)
        canvas.fill(QColor(constants.PIXMAP_BACKGROUND_COLOR))
        self.turing_machine_label.setPixmap(canvas)
        self.turing_machine_label.setScaledContents(True)

    def draw_turing_machine(self) -> None:
        canvas: QPixmap = self.turing_machine_label.pixmap()
        pen: QPen = QPen()
        self.draw_turing_machine_tape(canvas, pen)
        self.draw_turing_machine_cells(canvas, pen)

    def draw_turing_machine_tape(self, canvas: QPixmap, pen: QPen) -> None:
        painter: QPainter = QPainter(canvas)
        pen.setColor(QColor(constants.BROWN))
        painter.setPen(pen)
        painter.setBrush(QColor(constants.BROWN))
        painter.drawRect(constants.BEG_POINT_X_RECT, self.height() * constants.BEG_POINT_Y_RECT_COEFFICIENT,
                         self.width(), constants.END_POINT_Y_RECT)
        painter.end()
        self.turing_machine_label.setPixmap(canvas)

    def draw_turing_machine_cells(self, canvas: QPixmap, pen: QPen) -> None:
        painter: QPainter = QPainter(canvas)
        pen.setColor(QColor(constants.PERU))
        pen.setWidth(constants.CELL_WIDTH_PEN)
        painter.setPen(pen)
        x_loc_cell = constants.X_LOC_FIRST_CELL
        y_loc_cell = self.height() * constants.CELLS_LOCATION_HEIGHT_COEFFICIENT + constants.Y_LOC_CELL_INCREASED
        while x_loc_cell <= self.width():
            painter.drawPoint(x_loc_cell, y_loc_cell)
            x_loc_cell += constants.X_DIST_NEXT_CELL
        painter.end()
        self.turing_machine_label.setPixmap(canvas)

    def set_entry_word_label(self) -> None:
        self.entry_word_label.clear()
        self.entry_word_label.setText(self.file_reader.get_entry_word_from_file())

    def set_result_word_label(self, result_text: str) -> None:
        self.result_word_label.clear()
        self.result_word_label.setText(result_text)

    def add_commands_for_buttons(self) -> None:
        self.refresh_button.clicked.connect(self.set_contents_for_widgets)
        self.start_button.clicked.connect(self.set_start_button_command)
        self.stop_button.clicked.connect(self.set_stop_button_command)

    def set_start_button_command(self):
        self.refresh_button.setDisabled(True)
        self.start_button.setDisabled(True)
        self.stop_button.setEnabled(True)
        self.step_backward_button.setDisabled(True)
        self.step_forward_button.setDisabled(True)
        self.reset_button.setDisabled(True)

    def set_stop_button_command(self):
        self.refresh_button.setEnabled(True)
        self.start_button.setEnabled(True)
        self.stop_button.setDisabled(True)
        self.step_backward_button.setEnabled(True)
        self.step_forward_button.setEnabled(True)
        self.reset_button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setWindowTitle(constants.WINDOW_TITLE)
    widget.show()
    sys.exit(app.exec())
