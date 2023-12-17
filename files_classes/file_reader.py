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

    def get_entry_word_from_file(self) -> str:
        with open(self.filename) as file:
            lines: list[str] = file.readlines()
        search_line: str = lines.index(constants.SEARCH_LINE)
        return lines[search_line + constants.NEXT_INDEX][:constants.LAST_CHAR_INDEX]
