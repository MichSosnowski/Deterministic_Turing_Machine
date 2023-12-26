from itertools import count


# constants used in file_reader.py, mainwindow.py and turing_machine.py
EMPTY_STRING: str = ''


# constants used in file_parser.py, mainwindow.py and turing_machine.py
EMPTY_CHAR: str = '#'


# constants used in file_reader.py and file_parser.py
ENTRY_WORD: str = 'slowo wejsciowe:\n'
INITIAL_STATE: str = 'stan poczatkowy:\n'
ACCEPTING_STATES: str = 'stany akceptujace:\n'
TRANSITION_FUNCTION: str = 'relacja przejscia:\n'


# constants used in file_reader.py, file_parser.py and turing_machine.py
LAST_CHAR_INDEX: int = -1
SPACE: str = ' '


# constants used in mainwindow.py and turing_machine.py
INITIAL_TAPE_SIZE: int = 32
INITIAL_HEAD_POSITION: int = 15


# constants used in file_parser.py and turing_machine.py
LEFT: str = 'L'
RIGHT: str = 'P'


# constants used in file_parser.py and file_writer.py
NEWLINE: str = '\n'


# constants used in turing_machine.py
DRAWN_TAPE_SIZE: int = 19
FIRST_TAPE_INDEX: int = 0
LAST_TAPE_FRAGMENT_INDEX: int = 31
EXTEND_TAPE_SIZE: int = 16
EMPTY_CHAR_ENTRY_WORD_POSITION: int = 15
INITIAL_FRAGMENT_POSITION_BACK: int = 9
END_FRAGMENT_POSITION_FORWARD: int = 10
INITIAL_CALCULATION_LENGTH: int = 0
PREVIOUS_CELL: int = -1
NEXT_CELL: int = 1
CALCULATION_LENGTH_INCREASE: int = 1
INITIAL_SPEED_THREAD: float = 0.25
COEFFICIENT_SPEED_THREAD: int = 2
FASTEST_SPEED_THREAD: float = 0.03125
SLOWEST_SPEED_THREAD: float = 0.5
EXTEND_TAPE_LEFT_INFO: str = 'Nastąpiło rozszerzenie taśmy z jej lewej strony.'
EXTEND_TAPE_RIGHT_INFO: str = 'Nastąpiło rozszerzenie taśmy z jej prawej strony.'
EXTEND_TAPE_LEFT_INFO_FILE: str = 'ROZSZERZENIE TAŚMY Z LEWEJ STRONY\n\n'
EXTEND_TAPE_RIGHT_INFO_FILE: str = 'ROZSZERZENIE TAŚMY Z PRAWEJ STRONY\n\n'
ERROR_INFO_FILE: str = 'MASZYNA TURINGA ZAKOŃCZYŁA SWOJE DZIAŁANIE BŁĘDEM\n'
SUCCESS_END_INFO_FILE: str = 'MASZYNA TURINGA ZAKOŃCZYŁA SWOJE DZIAŁANIE POMYŚLNIE\n'


# constants used in file_reader.py
NEXT_INDEX: int = 1


# constants used in file_parser.py
TAPE_ALPHABET: str = 'alfabet tasmowy:\n'
ENTRY_ALPHABET: str = 'alfabet wejsciowy:\n'
STATES: str = 'stany:\n'
CHAR_NOT_FOUND: int = -1
REQUIRED_COUNT: int = 1
REQUIRED_COUNT_TAPE_ALPHABET: int = 2
MAX_LENGTH_ENTRY_WORD: int = 30


# constants used in file_writer.py
RESULT_DIRECTORY: str = 'wyniki'
INDIRECT_PATH_TO_RESULT_DIRECTORY: str = '.\\wyniki\\'
FILENAME_COMPLEMENT: str = '_wynik'
WRITE_MODE: str = 'w'
APPEND_MODE: str = 'a'
HEAD_CHAR: str = 'v'
SHIFT_DUE_TO_STATE: int = 4
ENTRY_WORD_FILE: str = 'SŁOWO WEJŚCIOWE: '
RESULT_WORD_FILE: str = 'SŁOWO OBLICZONE: '
CALCULATION_LENGTH_FILE: str = 'DŁUGOŚĆ OBLICZENIA: '


# constants used in mainwindow.py
WINDOW_TITLE: str = 'Maszyna Turinga'
MESSAGE_TITLE_FORMAT: str = 'Niepoprawny format!'
MESSAGE_FORMAT: str = 'Niepoprawny format pliku wejściowego.\nSprawdź format pliku i spróbuj ponownie.'
MESSAGE_TITLE_END_PROGRAM: str = 'Zamknąć program?'
MESSAGE_END_PROGRAM: str = 'Maszyna Turinga wciąż działa.\nCzy na pewno chcesz wyjść?'
CANCEL: str = 'Anuluj'
FILE_OPEN_TITLE: str = 'Wybierz plik z opisem maszyny Turinga...'
SUCCESS_END_OR_ERROR_INFO_TITLE: str = 'Koniec obliczeń!'
SUCCESS_END_INFO_MESSAGE: str = 'Maszyna Turinga zakończyła swoje działanie pomyślnie.'
ERROR_INFO_MESSAGE: str = 'Maszyna Turinga zakończyła swoje działanie błędem.'
CURRENT_DIR: str = '.'
TXT_FILTER: str = 'Pliki tekstowe (*.txt)'
EXTEND_TAPE_INFO_TITLE: str = 'Rozszerzenie taśmy'
FILENAME_INDEX: int = 0
PIXMAP_BACKGROUND_COLOR: str = '#f0f0f0'
BROWN: str = 'brown'
PERU: str = 'peru'
WIDTH_COEFFICIENT: float = 0.802
HEIGHT_COEFFICIENT: float = 0.6
BEG_POINT_X_RECT: int = 0
BEG_POINT_Y_RECT_COEFFICIENT: float = 0.3
END_POINT_Y_RECT: int = 45
CELLS_LOCATION_HEIGHT_COEFFICIENT: float = BEG_POINT_Y_RECT_COEFFICIENT
CELL_WIDTH_PEN: int = 32
X_LOC_FIRST_CELL: int = 18
Y_LOC_CELL_INCREASED: int = 23
X_DIST_NEXT_CELL: int = 35
HEAD_LOC_COEFFICIENT: int = 3
_iter = count(-450, 35)
HEAD_X_BOTTOM_POINT_LOC_ABOVE_TAPE: int = [next(_iter) for _ in range(32)]
HEAD_Y_BOTTOM_POINT_LOC_ABOVE_TAPE: int = 70
_iter = count(-433, 35)
HEAD_X_TOP_LEFT_POINT_LOC_ABOVE_TAPE: int = [next(_iter) for _ in range(32)]
_iter = count(-467, 35)
HEAD_X_TOP_RIGHT_POINT_LOC_ABOVE_TAPE: int = [next(_iter) for _ in range(32)]
HEAD_Y_TOP_POINT_LOC_ABOVE_TAPE: int = 100
HEAD_WIDTH_PEN: int = 1
FAMILY_FONT: str = 'Times'
POINT_SIZE: int = 25
FIRST_LETTER_POS: int = 5
NEXT_LETTER_POS: int = 35
LETTER_HEIGHT_COEFFICIENT: float = 0.347
FILL_TABLE_NO_TRANSITION: str = ' '
LAST_INDEX_HISTORY: int = -1
