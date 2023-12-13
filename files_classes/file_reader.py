import constants.constants as constants

class FileReader:

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.check_file_exists()

    def check_file_exists(self):
        try:
            open(self.filename).close()
        except FileNotFoundError:
            raise FileNotFoundError

    def get_all_data_from_file(self) -> str:
        data = constants.EMPTY_STRING
        with open(self.filename) as file:
            data = file.read()
        return data

    def get_entry_word_from_file(self) -> str:
        with open(self.filename) as file:
            lines = file.readlines()
        search_line = lines.index(constants.SEARCH_LINE)
        return lines[search_line + constants.NEXT_INDEX][:constants.LAST_CHAR_INDEX]
