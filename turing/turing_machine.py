from collections import deque
from typing import Deque
from itertools import repeat
from PySide6.QtCore import QThread
import constants.constants as constants
from files_classes.file_reader import FileReader
from constants.enums import Indexes


class TuringMachine(QThread):

    def __init__(self, file_reader: FileReader):
        super().__init__()
        self.entry_word: str = file_reader.get_entry_word_from_file()
        self.actual_state: str = file_reader.get_initial_state_from_file()
        self.accepting_states: list[str] = file_reader.get_accepting_states_from_file()
        self.transition_function: dict[tuple[str, str], tuple[str, str, str]] = self.transform_transition_function(file_reader)
        self.tape: Deque[str] = self.create_tape()
        self.position_head: int = self.get_initial_position_head()
        self.result_word = constants.EMPTY_STRING
        self.result_length = constants.INITIAL_CALCULATION_LENGTH

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

    def get_initial_position_head(self) -> int:
        return self.tape.index(self.entry_word[Indexes.ZERO.value])

    def get_fragment_of_tape(self) -> list[str]:
        fragment_start_position: int = self.position_head - constants.INITIAL_FRAGMENT_POSITION_BACK
        fragment_end_position: int = self.position_head + constants.END_FRAGMENT_POSITION_FORWARD
        fragment_tape: list[str] = list()
        if fragment_start_position < constants.FIRST_TAPE_INDEX:
            fragment_tape.extend(repeat(constants.EMPTY_STRING, constants.FIRST_TAPE_INDEX - fragment_start_position))
            fragment_start_position = constants.FIRST_TAPE_INDEX
        for index in range(fragment_start_position, fragment_end_position):
            if index < len(self.tape):
                fragment_tape.append(self.tape[index])
        fragment_tape.extend(repeat(constants.EMPTY_STRING, fragment_end_position - len(self.tape)))
        return fragment_tape

    def get_actual_transition_function(self) -> tuple[tuple[str, str], tuple[str, str, str]]:
        read_character: str = self.tape[self.position_head]
        key: tuple[str, str] = (self.actual_state, read_character)
        return (key, self.transition_function.get(key))

    def set_new_position_head(self, direction: str) -> None:
        if direction == constants.LEFT:
            self.position_head += constants.PREVIOUS_CELL
        elif direction == constants.RIGHT:
            self.position_head += constants.NEXT_CELL

    def step_forward(self) -> None:
        read_character: str = self.tape[self.position_head]
        transition: tuple[str, str, str] = self.transition_function.get((self.actual_state, read_character))
        self.actual_state: str = transition[Indexes.ZERO.value]
        self.tape[self.position_head]: str = transition[Indexes.ONE.value]
        self.set_new_position_head(transition[Indexes.TWO.value])

    def run(self):
        pass
