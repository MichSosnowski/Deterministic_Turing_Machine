from os import mkdir
from os.path import isdir
from pathlib import Path
from typing import Deque

import constants.constants as constants


class FileWriter:

    def __init__(self, filename: str, shift_states: int) -> None:
        self.create_directory_for_results()
        self.filename: str = self.create_name_for_result_file(filename)
        self.shift_states = shift_states
        self.clear_file()

    def create_directory_for_results(self) -> None:
        if not isdir(constants.RESULT_DIRECTORY):
            mkdir(constants.RESULT_DIRECTORY)

    def create_name_for_result_file(self, filename: str) -> str:
        filename_path: Path = Path(filename)
        new_filename: str = constants.INDIRECT_PATH_TO_RESULT_DIRECTORY + filename_path.stem + constants.FILENAME_COMPLEMENT + filename_path.suffix
        return new_filename

    def clear_file(self) -> None:
        open(self.filename, constants.WRITE_MODE).close()

    def write_entry_word(self, entry_word: str) -> None:
        entry_word_text: str = f'{constants.ENTRY_WORD_FILE}{entry_word}\n\n'
        with open(self.filename, constants.APPEND_MODE) as file:
            file.write(entry_word_text)

    def write_head_position(self, head_position: int) -> None:
        head_position_shift: int = head_position + self.shift_states + constants.SHIFT_DUE_TO_STATE
        head_position_text: str = f'{constants.HEAD_CHAR:>{head_position_shift}}\n'
        with open(self.filename, constants.APPEND_MODE) as file:
            file.write(head_position_text)

    def write_state(self, state: str) -> None:
        additional_space_count: int = self.shift_states - len(state)
        state_text: str = f'{state}: ' + constants.SPACE * additional_space_count
        with open(self.filename, constants.APPEND_MODE) as file:
            file.write(state_text)

    def write_tape(self, tape: Deque[str]) -> None:
        with open(self.filename, constants.APPEND_MODE) as file:
            for cell in tape:
                file.write(cell)
            file.write(constants.NEWLINE)
            file.write(constants.NEWLINE)

    def write_info_text(self, info: str) -> None:
        with open(self.filename, constants.APPEND_MODE) as file:
            file.write(info)

    def write_success_end(self, info: str, result_word: str, calculation_length: str) -> None:
        result_word_text: str = f'{constants.RESULT_WORD_FILE}{result_word}\n'
        calculation_length_text: str = f'{constants.CALCULATION_LENGTH_FILE}{calculation_length}\n'
        with open(self.filename, constants.APPEND_MODE) as file:
            file.write(info)
            file.write(result_word_text)
            file.write(calculation_length_text)
