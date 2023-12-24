import time
from collections import deque
from typing import Deque
from itertools import repeat, islice

from PySide6.QtCore import QThread, QMutex, QWaitCondition

import constants.constants as constants
import turing.config as config
from constants.enums import Indexes
from files_classes.file_reader import FileReader
from files_classes.file_writer import FileWriter
from turing.thread_signals import ThreadSignals


class TuringMachine(QThread):

    def __init__(self, file_reader: FileReader, wait_condition: QWaitCondition):
        super().__init__()
        self.thread_signals: ThreadSignals = ThreadSignals()
        self.mutex: QMutex = QMutex()
        self.wait_condition: QWaitCondition = wait_condition
        self.entry_word: str = file_reader.get_entry_word_from_file()
        self.actual_state: str = file_reader.get_initial_state_from_file()
        self.accepting_states: list[str] = file_reader.get_accepting_states_from_file()
        self.transition_function: dict[tuple[str, str], tuple[str, str, str]] = self.transform_transition_function(file_reader)
        self.tape: Deque[str] = self.create_tape()
        self.head_position_tape: int = self.get_initial_head_position()
        self.head_position_fragment_tape: int = self.get_initial_head_position()
        self.first_index_fragment_tape: int = constants.FIRST_TAPE_INDEX
        self.last_index_fragment_tape: int = constants.LAST_TAPE_FRAGMENT_INDEX
        self.calculation_length: int = constants.INITIAL_CALCULATION_LENGTH
        self.file_writer: FileWriter = FileWriter(file_reader.filename)
        self.file_writer.write_entry_word(self.entry_word)
        self.write_state_of_turing_machine_file()

    def transform_transition_function(self, file_reader: FileReader) -> dict[tuple[str, str], tuple[str, str, str]]:
        transition_function: dict[tuple(str, str), tuple(str, str, str)] = dict()
        transition_function_list: list[str] = file_reader.get_transition_function_from_file()
        for elem in transition_function_list:
            function: list[str] = elem[:constants.LAST_CHAR_INDEX].split(constants.SPACE)
            transition_function[(function[Indexes.ZERO.value], function[Indexes.ONE.value])] = (function[Indexes.TWO.value],
                                                                                                function[Indexes.THREE.value],
                                                                                                function[Indexes.FOUR.value])
        return transition_function

    def create_tape(self) -> Deque[str]:
        tape_deque: Deque[str] = deque()
        tape_deque.extend(self.entry_word)
        self.fill_tape_with_empty_char(tape_deque, constants.INITIAL_TAPE_SIZE)
        return tape_deque

    def extend_tape(self) -> None:
        if self.head_position_tape == constants.FIRST_TAPE_INDEX:
            self.tape.extendleft(repeat(constants.EMPTY_CHAR, constants.EXTEND_TAPE_SIZE))
            self.head_position_tape += constants.EXTEND_TAPE_SIZE
            self.first_index_fragment_tape += constants.EXTEND_TAPE_SIZE
            self.last_index_fragment_tape += constants.EXTEND_TAPE_SIZE
            self.file_writer.write_info_text(constants.EXTEND_TAPE_LEFT_INFO_FILE)
            config.extend_tape_left: bool = True
        elif self.head_position_tape == len(self.tape) + constants.PREVIOUS_CELL:
            self.tape.extend(repeat(constants.EMPTY_CHAR, constants.EXTEND_TAPE_SIZE))
            self.file_writer.write_info_text(constants.EXTEND_TAPE_RIGHT_INFO_FILE)
            config.extend_tape_right: bool = True

    def wait_for_wake(self) -> None:
        self.mutex.lock()
        self.wait_condition.wait(self.mutex)
        self.mutex.unlock()

    def fill_tape_with_empty_char(self, tape_deque: Deque[str], tape_size: int) -> None:
        filled_cells_count: int = len(tape_deque)
        while filled_cells_count < tape_size:
            tape_deque.appendleft(constants.EMPTY_CHAR)
            if len(tape_deque) < tape_size:
                tape_deque.append(constants.EMPTY_CHAR)
            filled_cells_count: int = len(tape_deque)

    def get_initial_head_position(self) -> int:
        if self.entry_word:
            return self.tape.index(self.entry_word[Indexes.ZERO.value])
        return constants.EMPTY_CHAR_ENTRY_WORD_POSITION

    def get_actual_head_position_fragment_tape(self) -> int:
        return self.head_position_fragment_tape

    def get_fragment_of_tape(self) -> list[str]:
        if self.head_position_fragment_tape == constants.FIRST_TAPE_INDEX:
            self.first_index_fragment_tape -= constants.EXTEND_TAPE_SIZE
            self.last_index_fragment_tape -= constants.EXTEND_TAPE_SIZE
            self.head_position_fragment_tape: int = constants.INITIAL_HEAD_POSITION + constants.NEXT_CELL
        elif self.head_position_fragment_tape == constants.LAST_TAPE_FRAGMENT_INDEX:
            self.first_index_fragment_tape += constants.EXTEND_TAPE_SIZE
            self.last_index_fragment_tape += constants.EXTEND_TAPE_SIZE
            self.head_position_fragment_tape: int = constants.INITIAL_HEAD_POSITION
        return islice(self.tape, self.first_index_fragment_tape, self.last_index_fragment_tape + constants.NEXT_CELL)

    def get_actual_transition_function(self) -> tuple[tuple[str, str], tuple[str, str, str]]:
        read_character: str = self.tape[self.head_position_tape]
        key: tuple[str, str] = (self.actual_state, read_character)
        value: tuple[str, str, str] = self.transition_function.get(key, constants.EMPTY_STRING)
        return (key, value) if value else constants.EMPTY_STRING

    def set_new_head_position(self, direction: str) -> None:
        if direction == constants.LEFT:
            self.head_position_tape += constants.PREVIOUS_CELL
            self.head_position_fragment_tape += constants.PREVIOUS_CELL
        elif direction == constants.RIGHT:
            self.head_position_tape += constants.NEXT_CELL
            self.head_position_fragment_tape += constants.NEXT_CELL

    def inform_about_extend_tape(self) -> None:
        if config.extend_tape_left:
            self.thread_signals.extend_tape.emit(constants.EXTEND_TAPE_LEFT_INFO)
            self.wait_for_wake()
            config.extend_tape_left: bool = False
        elif config.extend_tape_right:
            self.thread_signals.extend_tape.emit(constants.EXTEND_TAPE_RIGHT_INFO)
            self.wait_for_wake()
            config.extend_tape_right: bool = False

    def get_result_word(self) -> str:
        result_word_letters: list[str] = [elem for elem in self.tape if elem != constants.EMPTY_CHAR]
        result_word: str = constants.EMPTY_STRING.join(result_word_letters)
        return result_word

    def get_calculation_length(self) -> int:
        return self.calculation_length

    def write_state_of_turing_machine_file(self) -> None:
        self.file_writer.write_head_position(self.head_position_tape)
        self.file_writer.write_state(self.actual_state)
        self.file_writer.write_tape(self.tape)

    def step_forward(self) -> None:
        if self.actual_state not in self.accepting_states:
            read_character: str = self.tape[self.head_position_tape]
            transition: tuple[str, str, str] = self.transition_function.get((self.actual_state, read_character))
            if transition:
                self.actual_state: str = transition[Indexes.ZERO.value]
                self.tape[self.head_position_tape]: str = transition[Indexes.ONE.value]
                self.set_new_head_position(transition[Indexes.TWO.value])
                self.calculation_length += constants.CALCULATION_LENGTH_INCREASE
                self.extend_tape()
                self.write_state_of_turing_machine_file()
            else:
                self.file_writer.write_info_text(constants.ERROR_INFO_FILE)
                config.error = True
                return
        if self.actual_state in self.accepting_states:
            result_word: str = self.get_result_word()
            self.file_writer.write_success_end(constants.SUCCESS_END_INFO_FILE, result_word, self.calculation_length)
            config.finish_step_work = True

    def run(self) -> None:
        while self.actual_state not in self.accepting_states:
            self.step_forward()
            if config.error:
                self.thread_signals.error.emit()
                config.error = False
                break
            self.thread_signals.draw.emit()
            self.inform_about_extend_tape()
            time.sleep(constants.THREAD_SLEEP_SECS)
            if config.finish_thread:
                self.thread_signals.stop.emit()
                return
        else:
            self.thread_signals.end.emit()
