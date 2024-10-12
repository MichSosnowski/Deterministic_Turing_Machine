# constants used in file_reader.py, file_writer.py, file_parser.py and turing_machine.py
SPACE: str = ' '
NEWLINE: str = '\n'


# constants used in file_reader.py, file_writer.py, mainwindow.py and turing_machine.py
EMPTY_STRING: str = ''


# constants used in file_parser.py, mainwindow.py and turing_machine.py
EMPTY_CHAR: str = '#'


# constants used in file_reader.py and file_parser.py
ENTRY_WORD: str = 'slowo wejsciowe:\n'
STATES: str = 'stany:\n'
INITIAL_STATE: str = 'stan poczatkowy:\n'
ACCEPTING_STATES: str = 'stany akceptujace:\n'
TRANSITION_FUNCTION: str = 'relacja przejscia:\n'


# constants used in mainwindow.py and turing_machine.py
INITIAL_TAPE_SIZE: int = 32


# constants used in file_parser.py and turing_machine.py
LEFT: str = 'L'
RIGHT: str = 'P'


# constants used in turing_machine.py
FIRST_TAPE_INDEX: int = 0
EXTEND_TAPE_SIZE: int = 16
EMPTY_CHAR_ENTRY_WORD_POSITION: int = 15
INITIAL_CALCULATION_LENGTH: int = 0
INITIAL_DONT_WRITE: int = 0
PREVIOUS_CELL: int = -1
NEXT_CELL: int = 1
CALCULATION_LENGTH_INCREASE: int = 1
NEXT_DONT_WRITE_VALUE: int = 1
INITIAL_SPEED_THREAD: float = 0.25
COEFFICIENT_SPEED_THREAD: int = 2
FASTEST_SPEED_THREAD: float = 0.03125
SLOWEST_SPEED_THREAD: float = 0.5
STANDARD_MILISECONDS_WAIT_MUTEX: int = 0
SAVE_MILISECONDS_WAIT_MUTEX: int = 20
EQUAL_TWO_PARTS: int = 2
REMAINDER_ZERO: int = 0
EXTEND_TAPE_LEFT_INFO: str = 'Nastąpiło rozszerzenie taśmy z jej lewej strony.'
EXTEND_TAPE_RIGHT_INFO: str = 'Nastąpiło rozszerzenie taśmy z jej prawej strony.'
EXTEND_TAPE_LEFT_INFO_FILE: str = 'ROZSZERZENIE TAŚMY Z LEWEJ STRONY\n\n'
EXTEND_TAPE_RIGHT_INFO_FILE: str = 'ROZSZERZENIE TAŚMY Z PRAWEJ STRONY\n\n'
ERROR_INFO_FILE: str = 'MASZYNA TURINGA ZAKOŃCZYŁA SWOJE DZIAŁANIE BŁĘDEM\n'
SUCCESS_END_INFO_FILE: str = 'MASZYNA TURINGA ZAKOŃCZYŁA SWOJE DZIAŁANIE POMYŚLNIE\n'
LEFT_BRACKET: str = '('
RIGHT_BRACKET: str = ')'
COMMA: str = ', '


# constants used in file_parser.py
TAPE_ALPHABET: str = 'alfabet tasmowy:\n'
ENTRY_ALPHABET: str = 'alfabet wejsciowy:\n'
STATES: str = 'stany:\n'
CHAR_NOT_FOUND: int = -1
REQUIRED_COUNT: int = 1
MAX_LENGTH_ENTRY_WORD: int = 30
EXPECTED_LINE: str = 'Oczekiwana linia'
RECEIVED_LINE: str = 'Otrzymana linia'
TAPE_ALPHABET_ERROR: str = 'Alfabet taśmowy nie zawiera znaku pustego #.'
ENTRY_ALPHABET_ERROR: str = 'Nie wszystkie znaki alfabetu wejściowego zawarte są w alfabecie taśmowym.'
ENTRY_WORD_ERROR: str = 'Zbyt długie słowo wejściowe lub słowo wejściowe zawiera\nznaki spoza alfabetu wejściowego.'
STATES_ERROR: str = 'Zbyt mała liczba stanów.'
INITIAL_STATE_ERROR: str = 'Brak stanu wejściowego lub stan wejściowy nie jest stanem zdefiniowanym w stanach.'
ACCEPTING_STATES_ERROR: str = 'Brak stanów akceptujących lub któryś stan akceptujący nie jest stanem zdefiniowanym w stanach.'
NO_TRANSITION_FUNCTIONS_ERROR: str = 'Brak jakiejkolwiek relacji przejścia!'
INCORECT_TRANSITION_FUNCTION_ERROR: str = 'Niepoprawna relacja przejścia'


# constants used in file_reader.py
NEXT_INDEX: int = 1


# constants used in file_writer.py
RESULT_DIRECTORY: str = 'wyniki'
INDIRECT_PATH_TO_RESULT_DIRECTORY: str = '.\\wyniki\\'
FILENAME_COMPLEMENT: str = '_wynik'
WRITE_MODE: str = 'w'
APPEND_MODE: str = 'a'
HEAD_CHAR: str = 'v'
SHIFT_DUE_TO_STATE: int = 3
TWICE_STRING: int = 2
ENTRY_WORD_FILE: str = 'SŁOWO WEJŚCIOWE: '
RESULT_WORD_FILE: str = 'SŁOWO OBLICZONE: '
CALCULATION_LENGTH_FILE: str = 'DŁUGOŚĆ OBLICZENIA: '


# constants used in mainwindow.py
WINDOW_TITLE: str = 'Symulator deterministycznej maszyny Turinga'
MESSAGE_TITLE_FORMAT: str = 'Niepoprawny format!'
MESSAGE_FORMAT: str = 'Niepoprawny format pliku wejściowego.\n'
INDEX_ERROR: str = 'Niekompletna relacja przejścia!'
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
WORD_LENGTH_TEXT: str = 'Długość słowa: '
FILENAME_INDEX: int = 0
INITIAL_HEAD_POSITION: int = 15
PIXMAP_BACKGROUND_COLOR: str = '#f0f0f0'
BROWN: str = 'brown'
PERU: str = 'peru'
WIDTH_COEFFICIENT: float = 0.802
HEIGHT_COEFFICIENT: float = 0.47
BEG_POINT_X_RECT: int = 0
BEG_POINT_Y_RECT_COEFFICIENT: float = 0.25
END_POINT_Y_RECT: int = 45
CELLS_LOCATION_HEIGHT_COEFFICIENT: float = BEG_POINT_Y_RECT_COEFFICIENT
CELL_WIDTH_PEN: int = 32
X_LOC_FIRST_CELL: int = 18
Y_LOC_CELL_INCREASED: int = 23
X_DIST_NEXT_CELL: int = 35
HEAD_LOC_COEFFICIENT: int = 3
HEAD_Y_BOTTOM_POINT_LOC_ABOVE_TAPE: int = 100
HEAD_Y_TOP_POINT_LOC_ABOVE_TAPE: int = 130
HEAD_WIDTH_PEN: int = 1
FAMILY_FONT: str = 'TimesNewRoman'
POINT_SIZE: int = 25
FIRST_LETTER_POS: int = 5
NEXT_LETTER_POS: int = 35
LETTER_HEIGHT_COEFFICIENT: float = 0.298
FILL_TABLE_NO_TRANSITION: str = ' '
LAST_INDEX_HISTORY: int = -1
ONE_CELL_WIDTH: float = 35
HEAD_X_BOTTOM_FIRST: int = -450
HEAD_X_TOP_LEFT_FIRST: int = -433
HEAD_X_TOP_RIGHT_FIRST: int = -467
NEXT_VALUE: int = 35
