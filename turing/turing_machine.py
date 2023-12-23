import time
from collections import deque
from typing import Deque

from PySide6.QtCore import QThread

import constants.constants as constants
import turing.thread_config as config
from constants.enums import Indexes
from files_classes.file_reader import FileReader
from turing.thread_signals import ThreadSignals


class TuringMachine(QThread):

    def __init__(self, file_reader: FileReader):
        super().__init__()
        self.thread_signals = ThreadSignals()
        self.entry_word: str = file_reader.get_entry_word_from_file()
        self.actual_state: str = file_reader.get_initial_state_from_file()
        self.accepting_states: list[str] = file_reader.get_accepting_states_from_file()
        self.transition_function: dict[tuple[str, str], tuple[str, str, str]] = self.transform_transition_function(file_reader)
        self.tape: Deque[str] = self.create_tape()
        self.head_position: int = self.get_initial_head_position()
        self.result_word = constants.EMPTY_STRING
        self.calculation_length = constants.INITIAL_CALCULATION_LENGTH

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

    def get_actual_head_position(self) -> int:
        return self.head_position

    def get_fragment_of_tape(self) -> list[str]:
        return self.tape

    def get_actual_transition_function(self) -> tuple[tuple[str, str], tuple[str, str, str]]:
        read_character: str = self.tape[self.head_position]
        key: tuple[str, str] = (self.actual_state, read_character)
        value: tuple[str, str, str] = self.transition_function.get(key, constants.EMPTY_STRING)
        return (key, value) if value else constants.EMPTY_STRING

    def set_new_head_position(self, direction: str) -> None:
        if direction == constants.LEFT:
            self.head_position += constants.PREVIOUS_CELL
        elif direction == constants.RIGHT:
            self.head_position += constants.NEXT_CELL

    def step_forward(self) -> None:
        if self.actual_state not in self.accepting_states:
            read_character: str = self.tape[self.head_position]
            transition: tuple[str, str, str] = self.transition_function.get((self.actual_state, read_character))
            self.actual_state: str = transition[Indexes.ZERO.value]
            self.tape[self.head_position]: str = transition[Indexes.ONE.value]
            self.set_new_head_position(transition[Indexes.TWO.value])
            self.calculation_length += constants.CALCULATION_LENGTH_INCREASE

    def run(self) -> None:
        while self.actual_state not in self.accepting_states:
            self.step_forward()
            self.thread_signals.draw.emit()
            time.sleep(constants.THREAD_SLEEP_SECS)
            if config.finish_thread:
                self.thread_signals.end.emit()
                return
        self.thread_signals.end.emit()
