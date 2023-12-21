import sys
from itertools import islice, repeat
from typing import Iterator

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QHeaderView, QTableWidgetItem, QFileDialog
from PySide6.QtGui import QPixmap, QColor, QPainter, QPen, QPolygon, QFont, QGuiApplication
from PySide6.QtCore import Qt, QPoint, QRect

import turing.thread_config as config
import constants.constants as constants
from constants.enums import Indexes
from ui_form import Ui_MainWindow
from files_classes.file_reader import FileReader
from exceptions.exceptions import IncorrectFormatException
from gui.window_size import WindowSize
from constants.constants import (HEAD_LOC_COEFFICIENT, HEAD_X_BOTTOM_POINT_LOC_ABOVE_TAPE, HEAD_Y_BOTTOM_POINT_LOC_ABOVE_TAPE,
                                 HEAD_X_TOP_LEFT_POINT_LOC_ABOVE_TAPE, HEAD_X_TOP_RIGHT_POINT_LOC_ABOVE_TAPE, HEAD_Y_TOP_POINT_LOC_ABOVE_TAPE)
from turing.turing_machine import TuringMachine


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.filename: str = constants.EMPTY_STRING
        self.window_size: WindowSize = WindowSize(self.width(), self.height())
        self.center_window()
        self.turing_machine = None
        self.add_pixmap_for_turing_machine_label()
        self.draw_turing_machine()
        self.add_commands_for_buttons()

    def center_window(self) -> None:
        frameGeometry: QRect = self.frameGeometry()
        screen_center = QGuiApplication.primaryScreen().availableGeometry().center()
        frameGeometry.moveCenter(screen_center)
        self.move(frameGeometry.topLeft())

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.set_size_column_table()

    def closeEvent(self, event) -> None:
        if self.turing_machine and self.turing_machine.isRunning():
            button = self.show_warning_dialog(constants.MESSAGE_TITLE_END_PROGRAM, constants.MESSAGE_END_PROGRAM)
            if button == QMessageBox.StandardButton.Ok:
                self.stop_thread()
                event.accept()
            else:
                event.ignore()

    def set_size_column_table(self) -> None:
        header: QHeaderView = self.tape_state_table.horizontalHeader()
        for index in islice(Indexes, Indexes.FIVE.value):
            header.setSectionResizeMode(index.value, QHeaderView.Stretch)

    def set_contents_for_widgets(self) -> None:
        self.file_reader: FileReader = FileReader(self.filename)
        self.add_text_to_file_text_browser()
        self.set_entry_word_label()
        self.set_result_word_label(constants.EMPTY_STRING)
        self.turing_machine: TuringMachine = TuringMachine(self.file_reader)
        self.draw_turing_machine()
        self.fill_tape_state_table()

    def show_warning_dialog(self, title: str, message: str) -> None:
        QApplication.beep()
        button = QMessageBox.warning(self, title, message, QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Cancel)
        return button

    def show_error_dialog(self, title: str, message: str) -> None:
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

    def draw_turing_machine(self) -> None:
        canvas: QPixmap = self.turing_machine_label.pixmap()
        canvas.fill(QColor(constants.PIXMAP_BACKGROUND_COLOR))
        pen: QPen = QPen()
        self.draw_turing_machine_tape(canvas, pen)
        self.draw_turing_machine_cells(canvas, pen)
        self.draw_turing_machine_head(canvas, pen)
        self.draw_contents_of_tape_cells(canvas, pen)

    def draw_turing_machine_tape(self, canvas: QPixmap, pen: QPen) -> None:
        painter: QPainter = QPainter(canvas)
        pen.setColor(QColor(constants.BROWN))
        painter.setPen(pen)
        painter.setBrush(QColor(constants.BROWN))
        painter.drawRect(constants.BEG_POINT_X_RECT, self.window_size.height * constants.BEG_POINT_Y_RECT_COEFFICIENT,
                         self.window_size.width, constants.END_POINT_Y_RECT)
        painter.end()
        self.turing_machine_label.setPixmap(canvas)

    def draw_turing_machine_cells(self, canvas: QPixmap, pen: QPen) -> None:
        painter: QPainter = QPainter(canvas)
        pen.setColor(QColor(constants.PERU))
        pen.setWidth(constants.CELL_WIDTH_PEN)
        painter.setPen(pen)
        x_loc_cell = constants.X_LOC_FIRST_CELL
        y_loc_cell = self.window_size.height * constants.CELLS_LOCATION_HEIGHT_COEFFICIENT + constants.Y_LOC_CELL_INCREASED
        while x_loc_cell <= self.window_size.width:
            painter.drawPoint(x_loc_cell, y_loc_cell)
            x_loc_cell += constants.X_DIST_NEXT_CELL
        painter.end()
        self.turing_machine_label.setPixmap(canvas)

    def draw_turing_machine_head(self, canvas: QPixmap, pen: QPen) -> None:
        painter: QPainter = QPainter(canvas)
        polygon: QPolygon = self.create_head()
        pen.setWidth(constants.HEAD_WIDTH_PEN)
        painter.setBrush(Qt.black)
        pen.setColor(Qt.black)
        painter.setPen(pen)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawPolygon(polygon)
        painter.end()
        self.turing_machine_label.setPixmap(canvas)

    def create_head(self) -> QPolygon:
        polygon: QPolygon = QPolygon()
        head_position: int = self.turing_machine.get_actual_head_position() if self.turing_machine else constants.INITIAL_HEAD_POSITION
        (polygon << QPoint(self.window_size.width / HEAD_LOC_COEFFICIENT + HEAD_X_BOTTOM_POINT_LOC_ABOVE_TAPE[head_position],
                           self.window_size.height / HEAD_LOC_COEFFICIENT - HEAD_Y_BOTTOM_POINT_LOC_ABOVE_TAPE)
                 << QPoint(self.window_size.width / HEAD_LOC_COEFFICIENT + HEAD_X_TOP_LEFT_POINT_LOC_ABOVE_TAPE[head_position],
                           self.window_size.height / HEAD_LOC_COEFFICIENT - HEAD_Y_TOP_POINT_LOC_ABOVE_TAPE)
                 << QPoint(self.window_size.width / HEAD_LOC_COEFFICIENT + HEAD_X_TOP_RIGHT_POINT_LOC_ABOVE_TAPE[head_position],
                           self.window_size.height / HEAD_LOC_COEFFICIENT - HEAD_Y_TOP_POINT_LOC_ABOVE_TAPE))
        return polygon

    def draw_contents_of_tape_cells(self, canvas: QPixmap, pen: QPen) -> None:
        painter: QPainter = QPainter(canvas)
        text_font: QFont = QFont(constants.FAMILY_FONT, constants.POINT_SIZE)
        painter.setFont(text_font)
        first_letter_pos = constants.FIRST_LETTER_POS
        if self.turing_machine:
            fragment_tape: list[str] = self.turing_machine.get_fragment_of_tape()
        else:
            fragment_tape: Iterator[str] = repeat(constants.EMPTY_CHAR, constants.INITIAL_TAPE_SIZE)
        for elem in fragment_tape:
            painter.drawText(first_letter_pos, self.window_size.height * constants.LETTER_HEIGHT_COEFFICIENT, elem)
            first_letter_pos += constants.NEXT_LETTER_POS
        painter.end()
        self.turing_machine_label.setPixmap(canvas)

    def fill_tape_state_table(self) -> None:
        transition_function = self.turing_machine.get_actual_transition_function()
        if transition_function:
            self.tape_state_table.setItem(Indexes.ZERO.value, Indexes.ZERO.value,
                                          self.create_item_for_table(transition_function[Indexes.ZERO.value][Indexes.ZERO.value]))
            self.tape_state_table.setItem(Indexes.ZERO.value, Indexes.ONE.value,
                                          self.create_item_for_table(transition_function[Indexes.ZERO.value][Indexes.ONE.value]))
            self.tape_state_table.setItem(Indexes.ZERO.value, Indexes.TWO.value,
                                          self.create_item_for_table(transition_function[Indexes.ONE.value][Indexes.ZERO.value]))
            self.tape_state_table.setItem(Indexes.ZERO.value, Indexes.THREE.value,
                                          self.create_item_for_table(transition_function[Indexes.ONE.value][Indexes.ONE.value]))
            self.tape_state_table.setItem(Indexes.ZERO.value, Indexes.FOUR.value,
                                          self.create_item_for_table(transition_function[Indexes.ONE.value][Indexes.TWO.value]))
        else:
            for index in islice(Indexes, Indexes.FIVE.value):
                self.tape_state_table.setItem(Indexes.ZERO.value, index.value, self.create_item_for_table(constants.FILL_TABLE_NO_TRANSITION))

    def redraw_turing_machine(self) -> None:
        self.draw_turing_machine()
        self.fill_tape_state_table()

    def create_item_for_table(self, data: str) -> QTableWidgetItem:
        item: QTableWidgetItem = QTableWidgetItem(data)
        item.setTextAlignment(Qt.AlignHCenter)
        return item

    def set_entry_word_label(self) -> None:
        self.entry_word_label.clear()
        self.entry_word_label.setText(self.file_reader.get_entry_word_from_file())

    def set_result_word_label(self, result_text: str) -> None:
        self.result_word_label.clear()
        self.result_word_label.setText(result_text)

    def load_file(self) -> None:
        temp_filename: str = self.filename
        self.get_name_of_file()
        try:
            self.set_contents_for_widgets()
        except FileNotFoundError:
            self.filename: str = temp_filename
        except (IncorrectFormatException, IndexError):
            self.show_error_dialog(constants.MESSAGE_TITLE_FORMAT, constants.MESSAGE_FORMAT)
            self.filename: str = temp_filename
        else:
            self.switch_enabled_buttons()

    def get_name_of_file(self) -> None:
        self.filename: str = constants.EMPTY_STRING
        if not self.filename:
            self.filename: tuple[str, str] = QFileDialog.getOpenFileName(self, constants.FILE_OPEN_TITLE, constants.CURRENT_DIR,
                                                                         constants.TXT_FILTER)
        self.filename: str = self.filename[constants.FILENAME_INDEX]

    def add_commands_for_buttons(self) -> None:
        self.load_file_button.clicked.connect(self.load_file)
        self.refresh_button.clicked.connect(self.set_contents_for_widgets)
        self.start_button.clicked.connect(self.set_start_button_command)
        self.stop_button.clicked.connect(self.set_stop_button_command)
        self.step_forward_button.clicked.connect(self.set_step_forward_command)

    def stop_thread(self) -> None:
        config.finish_thread = True
        self.turing_machine.wait()
        config.finish_thread = False

    def switch_enabled_buttons(self) -> None:
        self.load_file_button.setEnabled(True)
        self.refresh_button.setEnabled(True)
        self.start_button.setEnabled(True)
        self.stop_button.setDisabled(True)
        self.step_backward_button.setEnabled(True)
        self.step_forward_button.setEnabled(True)
        self.reset_button.setEnabled(True)

    def set_start_button_command(self) -> None:
        self.load_file_button.setDisabled(True)
        self.refresh_button.setDisabled(True)
        self.start_button.setDisabled(True)
        self.stop_button.setEnabled(True)
        self.step_backward_button.setDisabled(True)
        self.step_forward_button.setDisabled(True)
        self.reset_button.setDisabled(True)
        self.turing_machine.thread_signals.draw.connect(self.redraw_turing_machine)
        self.turing_machine.thread_signals.end.connect(self.switch_enabled_buttons)
        self.turing_machine.thread_signals.end.connect(self.turing_machine.quit)
        self.turing_machine.start()

    def set_stop_button_command(self) -> None:
        self.switch_enabled_buttons()
        self.stop_thread()

    def set_step_forward_command(self) -> None:
        self.turing_machine.step_forward()
        self.redraw_turing_machine()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setWindowTitle(constants.WINDOW_TITLE)
    widget.show()
    sys.exit(app.exec())
