import constants.constants as constants
from .file_parser import FileParser


class FileReader:

    def __init__(self, filename: str) -> None:
        self.filename: str = filename
        self.check_file_exists()
        file_parser: FileParser = FileParser(filename)
        file_parser.parse_file()

    def check_file_exists(self) -> None:
        open(self.filename).close()

    def get_all_data_from_file(self) -> str:
        data: str = constants.EMPTY_STRING
        with open(self.filename) as file:
            data: str = file.read()
        return data

    def get_all_lines_from_file(self) -> list[str]:
        with open(self.filename) as file:
            lines: list[str] = file.readlines()
        return lines

    def get_entry_word_from_file(self) -> str:
        lines: list[str] = self.get_all_lines_from_file()
        entry_word_index: int = lines.index(constants.ENTRY_WORD) + constants.NEXT_INDEX
        return lines[entry_word_index].rstrip(constants.NEWLINE)

    def get_states_from_file(self) -> list[str]:
        lines: list[str] = self.get_all_lines_from_file()
        states_index: int = lines.index(constants.STATES) + constants.NEXT_INDEX
        states: list[str] = lines[states_index].rstrip(constants.NEWLINE).split(constants.SPACE)
        return states

    def get_initial_state_from_file(self) -> str:
        lines: list[str] = self.get_all_lines_from_file()
        initial_state_index: int = lines.index(constants.INITIAL_STATE) + constants.NEXT_INDEX
        return lines[initial_state_index].rstrip(constants.NEWLINE)

    def get_accepting_states_from_file(self) -> list[str]:
        lines: list[str] = self.get_all_lines_from_file()
        accepting_states_index: int = lines.index(constants.ACCEPTING_STATES) + constants.NEXT_INDEX
        accepting_states: list[str] = lines[accepting_states_index].rstrip(constants.NEWLINE).split(constants.SPACE)
        return accepting_states

    def get_transition_function_from_file(self) -> list[str]:
        lines: list[str] = self.get_all_lines_from_file()
        transition_function_index: int = lines.index(constants.TRANSITION_FUNCTION) + constants.NEXT_INDEX
        transition_function: list[str] = lines[transition_function_index:]
        return transition_function
