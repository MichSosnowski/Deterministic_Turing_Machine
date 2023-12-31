from sys import argv, exit
from itertools import islice, repeat, count
from typing import Iterator, Deque

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QHeaderView, QTableWidgetItem, QFileDialog
from PySide6.QtGui import QPixmap, QColor, QPainter, QPen, QPolygon, QFont, QGuiApplication
from PySide6.QtCore import Qt, QPoint, QRect, QWaitCondition

import turing.config as config
import constants.constants as constants
from constants.enums import Indexes
from ui_form import Ui_MainWindow
from files_classes.file_reader import FileReader
from exceptions.exceptions import IncorrectFormatException
from gui.window_size import WindowSize
from constants.constants import HEAD_LOC_COEFFICIENT, HEAD_Y_BOTTOM_POINT_LOC_ABOVE_TAPE, HEAD_Y_TOP_POINT_LOC_ABOVE_TAPE
from turing.turing_machine import TuringMachine
from turing.turing_memento import TuringMachineMemento


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.filename: str = constants.EMPTY_STRING
        self.window_size: WindowSize = WindowSize(self.width(), self.height())
        self.wait_condition: QWaitCondition = QWaitCondition()
        self.previous_head_position: int = constants.INITIAL_HEAD_POSITION
        self.history_turing_machine: list[TuringMachine] = list()
        self.center_window()
        self.turing_machine = None
        self.add_pixmap_for_turing_machine_label()
        self.draw_turing_machine()
        self.add_commands_for_buttons()

    def save_state_turing_machine(self) -> None:
        self.history_turing_machine.append(self.turing_machine.save_state())
        self.wait_condition.wakeAll()

    def restore_state_turing_machine(self, index: int = constants.LAST_INDEX_HISTORY) -> None:
        if len(self.history_turing_machine):
            self.turing_machine.restore_state(self.history_turing_machine.pop(index))

    def remove_memento_from_history_error_end(self) -> None:
        last_item: TuringMachineMemento = self.history_turing_machine.pop()
        if self.turing_machine != last_item:
            self.history_turing_machine.append(last_item)

    def center_window(self) -> None:
        frameGeometry: QRect = self.frameGeometry()
        screen_center: QPoint = QGuiApplication.primaryScreen().availableGeometry().center()
        frameGeometry.moveCenter(screen_center)
        self.move(frameGeometry.topLeft())

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.set_size_column_table()

    def closeEvent(self, event) -> None:
        if self.turing_machine and self.turing_machine.isRunning():
            button = self.show_warning_dialog(constants.MESSAGE_TITLE_END_PROGRAM, constants.MESSAGE_END_PROGRAM)
            match button:
                case QMessageBox.StandardButton.Ok:
                    self.stop_thread()
                    event.accept()
                case _:
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
        self.set_calculation_length_label(constants.EMPTY_STRING)
        self.turing_machine: TuringMachine = TuringMachine(self.file_reader, self.wait_condition)
        self.previous_head_position: int = self.turing_machine.get_actual_head_position()
        self.history_turing_machine.clear()
        self.add_pixmap_for_turing_machine_label()
        self.draw_turing_machine()
        self.fill_tape_state_table()

    def show_info_dialog(self, title: str, message: str) -> None:
        QApplication.beep()
        QMessageBox.information(self, title, message)

    def show_warning_dialog(self, title: str, message: str) -> QMessageBox.StandardButton:
        QApplication.beep()
        warning_message_box = QMessageBox()
        warning_message_box.setIcon(QMessageBox.Warning)
        warning_message_box.setWindowTitle(title)
        warning_message_box.setText(message)
        warning_message_box.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        cancel_button = warning_message_box.button(QMessageBox.StandardButton.Cancel)
        cancel_button.setText(constants.CANCEL)
        return warning_message_box.exec()

    def show_error_dialog(self, title: str, message: str) -> None:
        QApplication.beep()
        QMessageBox.critical(self, title, message)

    def add_text_to_file_text_browser(self) -> None:
        self.file_text_browser.clear()
        self.file_text_browser.setText(self.file_reader.get_all_data_from_file())

    def get_new_pixmap_width(self) -> float:
        if not self.turing_machine:
            return self.window_size.width * constants.WIDTH_COEFFICIENT
        else:
            return len(self.turing_machine.get_tape()) * constants.ONE_CELL_WIDTH

    def add_pixmap_for_turing_machine_label(self) -> None:
        pixmap_width: float = self.get_new_pixmap_width()
        pixmap_height: float = self.window_size.height * constants.HEIGHT_COEFFICIENT
        canvas: QPixmap = QPixmap(pixmap_width, pixmap_height)
        canvas.fill(QColor(constants.PIXMAP_BACKGROUND_COLOR))
        self.turing_machine_label.setPixmap(canvas)

    def draw_turing_machine(self) -> None:
        canvas: QPixmap = self.turing_machine_label.pixmap()
        canvas.fill(QColor(constants.PIXMAP_BACKGROUND_COLOR))
        pen: QPen = QPen()
        self.draw_turing_machine_tape(canvas, pen)
        self.draw_turing_machine_cells(canvas, pen)
        self.draw_contents_of_tape_cells(canvas, pen)
        self.draw_turing_machine_head(canvas, pen)

    def paint_tape(self, painter: QPainter) -> None:
        rect_width: float = len(self.turing_machine.get_tape()) * constants.ONE_CELL_WIDTH if self.turing_machine else self.window_size.width
        painter.drawRect(constants.BEG_POINT_X_RECT, self.window_size.height * constants.BEG_POINT_Y_RECT_COEFFICIENT,
                         rect_width, constants.END_POINT_Y_RECT)

    def draw_turing_machine_tape(self, canvas: QPixmap, pen: QPen) -> None:
        painter: QPainter = QPainter(canvas)
        pen.setColor(QColor(constants.BROWN))
        painter.setPen(pen)
        painter.setBrush(QColor(constants.BROWN))
        self.paint_tape(painter)
        painter.end()
        self.turing_machine_label.setPixmap(canvas)

    def draw_cells(self, painter: QPainter) -> None:
        x_loc_cell = constants.X_LOC_FIRST_CELL
        y_loc_cell = self.window_size.height * constants.CELLS_LOCATION_HEIGHT_COEFFICIENT + constants.Y_LOC_CELL_INCREASED
        max_width: float = len(self.turing_machine.get_tape()) * constants.ONE_CELL_WIDTH if self.turing_machine else self.window_size.width
        while x_loc_cell <= max_width:
            painter.drawPoint(x_loc_cell, y_loc_cell)
            x_loc_cell += constants.X_DIST_NEXT_CELL

    def draw_turing_machine_cells(self, canvas: QPixmap, pen: QPen) -> None:
        painter: QPainter = QPainter(canvas)
        pen.setColor(QColor(constants.PERU))
        pen.setWidth(constants.CELL_WIDTH_PEN)
        painter.setPen(pen)
        self.draw_cells(painter)
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

    def set_first_position_of_head(self, head_position: int) -> None:
        _iter = count(constants.HEAD_X_BOTTOM_FIRST, constants.NEXT_VALUE)
        self.head_x_bottom_point_loc_above_tape: int = next(islice(_iter, head_position, None))
        _iter = count(constants.HEAD_X_TOP_LEFT_FIRST, constants.NEXT_VALUE)
        self.head_x_top_left_point_loc_above_tape: int = next(islice(_iter, head_position, None))
        _iter = count(constants.HEAD_X_TOP_RIGHT_FIRST, constants.NEXT_VALUE)
        self.head_x_top_right_point_loc_aboce_tape: int = next(islice(_iter, head_position, None))

    def set_positions_of_head(self) -> None:
        head_position: int = self.turing_machine.get_actual_head_position() if self.turing_machine else constants.INITIAL_HEAD_POSITION
        if self.previous_head_position < head_position:
            self.head_x_bottom_point_loc_above_tape += constants.NEXT_VALUE
            self.head_x_top_left_point_loc_above_tape += constants.NEXT_VALUE
            self.head_x_top_right_point_loc_aboce_tape += constants.NEXT_VALUE
        elif head_position < self.previous_head_position:
            self.head_x_bottom_point_loc_above_tape -= constants.NEXT_VALUE
            self.head_x_top_left_point_loc_above_tape -= constants.NEXT_VALUE
            self.head_x_top_right_point_loc_aboce_tape -= constants.NEXT_VALUE
        else:
            self.set_first_position_of_head(head_position)
        self.previous_head_position: int = head_position

    def create_head(self) -> QPolygon:
        polygon: QPolygon = QPolygon()
        self.set_positions_of_head()
        (polygon << QPoint(self.window_size.width / HEAD_LOC_COEFFICIENT + self.head_x_bottom_point_loc_above_tape,
                           self.window_size.height / HEAD_LOC_COEFFICIENT - HEAD_Y_BOTTOM_POINT_LOC_ABOVE_TAPE)
                 << QPoint(self.window_size.width / HEAD_LOC_COEFFICIENT + self.head_x_top_left_point_loc_above_tape,
                           self.window_size.height / HEAD_LOC_COEFFICIENT - HEAD_Y_TOP_POINT_LOC_ABOVE_TAPE)
                 << QPoint(self.window_size.width / HEAD_LOC_COEFFICIENT + self.head_x_top_right_point_loc_aboce_tape,
                           self.window_size.height / HEAD_LOC_COEFFICIENT - HEAD_Y_TOP_POINT_LOC_ABOVE_TAPE))
        return polygon

    def get_tape_from_turing_machine(self) -> Deque[str]:
        if self.turing_machine:
            tape: Deque[str] = self.turing_machine.get_tape()
        else:
            tape: Iterator[str] = repeat(constants.EMPTY_CHAR, constants.INITIAL_TAPE_SIZE)
        return tape

    def draw_contents_of_tape_cells(self, canvas: QPixmap, pen: QPen) -> None:
        painter: QPainter = QPainter(canvas)
        text_font: QFont = QFont(constants.FAMILY_FONT, constants.POINT_SIZE)
        painter.setFont(text_font)
        first_letter_pos = constants.FIRST_LETTER_POS
        tape = self.get_tape_from_turing_machine()
        for elem in tape:
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

    def set_calculation_length_label(self, calculation_length_text: str) -> None:
        self.calculation_length_label.clear()
        self.calculation_length_label.setText(calculation_length_text)

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

    def execute_extend_tape(self, message: str) -> None:
        self.add_pixmap_for_turing_machine_label()
        self.redraw_turing_machine()
        self.show_info_dialog(constants.EXTEND_TAPE_INFO_TITLE, message)
        self.wait_condition.wakeAll()

    def inform_about_extend_tape(self) -> None:
        if config.extend_tape_left:
            self.show_info_dialog(constants.EXTEND_TAPE_INFO_TITLE, constants.EXTEND_TAPE_LEFT_INFO)
            config.extend_tape_left: bool = False
        elif config.extend_tape_right:
            self.show_info_dialog(constants.EXTEND_TAPE_INFO_TITLE, constants.EXTEND_TAPE_RIGHT_INFO)
            config.extend_tape_right: bool = False

    def add_commands_for_buttons(self) -> None:
        self.load_file_button.clicked.connect(self.load_file)
        self.refresh_button.clicked.connect(self.set_contents_for_widgets)
        self.start_button.clicked.connect(self.set_start_button_command)
        self.slow_head_button.clicked.connect(self.slow_thread_down)
        self.fast_head_button.clicked.connect(self.speed_thread_up)
        self.stop_button.clicked.connect(self.set_stop_button_command)
        self.step_forward_button.clicked.connect(self.set_step_forward_command)
        self.step_backward_button.clicked.connect(self.set_step_backward_command)
        self.reset_button.clicked.connect(self.set_reset_button_command)

    def slow_thread_down(self) -> None:
        config.slow_head: bool = True

    def speed_thread_up(self) -> None:
        config.speed_head: bool = True

    def stop_thread(self) -> None:
        config.finish_thread = True
        self.turing_machine.wait()
        config.finish_thread = False

    def switch_enabled_buttons(self) -> None:
        self.load_file_button.setEnabled(True)
        self.refresh_button.setEnabled(True)
        self.start_button.setEnabled(True)
        self.slow_head_button.setDisabled(True)
        self.fast_head_button.setDisabled(True)
        self.stop_button.setDisabled(True)
        self.step_backward_button.setEnabled(True)
        self.step_forward_button.setEnabled(True)
        self.reset_button.setEnabled(True)

    def connect_signals(self) -> None:
        self.turing_machine.thread_signals.draw.connect(self.redraw_turing_machine)
        self.turing_machine.thread_signals.save.connect(self.save_state_turing_machine)
        self.turing_machine.thread_signals.extend_tape.connect(self.execute_extend_tape)
        self.turing_machine.thread_signals.stop.connect(self.switch_enabled_buttons)
        self.turing_machine.thread_signals.stop.connect(self.turing_machine.quit)
        self.turing_machine.thread_signals.error.connect(self.switch_enabled_buttons)
        self.turing_machine.thread_signals.error.connect(self.execute_error_thread)
        self.turing_machine.thread_signals.error.connect(self.turing_machine.quit)
        self.turing_machine.thread_signals.end.connect(self.switch_enabled_buttons)
        self.turing_machine.thread_signals.end.connect(self.execute_success_end_thread)
        self.turing_machine.thread_signals.end.connect(self.turing_machine.quit)

    def disconnect_signals(self) -> None:
        self.turing_machine.thread_signals.draw.disconnect(self.redraw_turing_machine)
        self.turing_machine.thread_signals.save.disconnect(self.save_state_turing_machine)
        self.turing_machine.thread_signals.extend_tape.disconnect(self.execute_extend_tape)
        self.turing_machine.thread_signals.stop.disconnect(self.switch_enabled_buttons)
        self.turing_machine.thread_signals.error.disconnect(self.switch_enabled_buttons)
        self.turing_machine.thread_signals.error.disconnect(self.execute_error_thread)
        self.turing_machine.thread_signals.end.disconnect(self.switch_enabled_buttons)
        self.turing_machine.thread_signals.end.disconnect(self.execute_success_end_thread)

    def execute_success_end_step(self) -> None:
        self.set_result_word_label(self.turing_machine.get_result_word())
        self.set_calculation_length_label(str(self.turing_machine.get_calculation_length()))
        self.remove_memento_from_history_error_end()
        self.show_info_dialog(constants.SUCCESS_END_OR_ERROR_INFO_TITLE, constants.SUCCESS_END_INFO_MESSAGE)
        config.finish_step_work: bool = False

    def execute_success_end_thread(self) -> None:
        self.execute_success_end_step()
        self.disconnect_signals()

    def execute_error_step(self) -> None:
        self.remove_memento_from_history_error_end()
        self.show_info_dialog(constants.SUCCESS_END_OR_ERROR_INFO_TITLE, constants.ERROR_INFO_MESSAGE)
        config.error: bool = False

    def execute_error_thread(self) -> None:
        self.execute_error_step()
        self.disconnect_signals()

    def set_start_button_command(self) -> None:
        self.load_file_button.setDisabled(True)
        self.refresh_button.setDisabled(True)
        self.start_button.setDisabled(True)
        self.slow_head_button.setEnabled(True)
        self.fast_head_button.setEnabled(True)
        self.stop_button.setEnabled(True)
        self.step_backward_button.setDisabled(True)
        self.step_forward_button.setDisabled(True)
        self.reset_button.setDisabled(True)
        self.connect_signals()
        self.turing_machine.start()

    def set_stop_button_command(self) -> None:
        self.switch_enabled_buttons()
        self.stop_thread()
        self.disconnect_signals()

    def set_step_forward_command(self) -> None:
        self.save_state_turing_machine()
        self.turing_machine.step_forward()
        if config.error:
            self.execute_error_step()
            return
        self.add_pixmap_for_turing_machine_label()
        self.redraw_turing_machine()
        self.inform_about_extend_tape()
        if config.finish_step_work:
            self.execute_success_end_step()

    def set_step_backward_command(self) -> None:
        self.result_word_label.clear()
        self.calculation_length_label.clear()
        self.restore_state_turing_machine()
        self.add_pixmap_for_turing_machine_label()
        self.redraw_turing_machine()

    def set_reset_button_command(self) -> None:
        self.result_word_label.clear()
        self.calculation_length_label.clear()
        self.restore_state_turing_machine(Indexes.ZERO.value)
        self.previous_head_position: int = self.turing_machine.get_actual_head_position()
        self.turing_machine.reset_state_of_written_file()
        self.add_pixmap_for_turing_machine_label()
        self.redraw_turing_machine()
        self.history_turing_machine.clear()


if __name__ == "__main__":
    app = QApplication(argv)
    widget = MainWindow()
    widget.setWindowTitle(constants.WINDOW_TITLE)
    widget.show()
    exit(app.exec())
