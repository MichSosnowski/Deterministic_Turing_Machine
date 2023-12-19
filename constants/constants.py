# constants used in file_reader.py, mainwindow.py and turing_machine.py
EMPTY_STRING = ''


# constants used in file_reader.py and file_parser.py
ENTRY_WORD = 'slowo wejsciowe:\n'
INITIAL_STATE = 'stan poczatkowy:\n'
ACCEPTING_STATES = 'stany akceptujace:\n'
TRANSITION_FUNCTION = 'relacja przejscia:\n'


# constants used in file_reader.py, file_parser.py and turing_machine.py
LAST_CHAR_INDEX = -1
SPACE = ' '


# constants used in file_parser.py and turing_machine.py
EMPTY_CHAR = '#'
LEFT = 'L'
RIGHT = 'P'


# constants used in turing_machine.py
INITIAL_TAPE_SIZE = 32
DRAWN_TAPE_SIZE = 19
FIRST_TAPE_INDEX = 0
EMPTY_CHAR_ENTRY_WORD_POSITION = 10
INITIAL_FRAGMENT_POSITION_BACK = 9
END_FRAGMENT_POSITION_FORWARD = 10
INITIAL_CALCULATION_LENGTH = 0
PREVIOUS_CELL = -1
NEXT_CELL = 1
CALCULATION_LENGTH_INCREASE = 1
THREAD_SLEEP_SECS = 0.25


# constants used in file_reader.py
NEXT_INDEX = 1


# constants used in file_parser.py
TAPE_ALPHABET = 'alfabet tasmowy:\n'
ENTRY_ALPHABET = 'alfabet wejsciowy:\n'
STATES = 'stany:\n'
NEWLINE = '\n'
CHAR_NOT_FOUND = -1
REQUIRED_COUNT = 1
REQUIRED_COUNT_TAPE_ALPHABET = 2
MAX_LENGTH_ENTRY_WORD = 30


# constants used in mainwindow.py
EXIT_SUCCESS = 0
EXIT_FAILURE = -1
WINDOW_TITLE = 'Maszyna Turinga'
MESSAGE_TITLE_FORMAT = 'Niepoprawny format!'
MESSAGE_FORMAT = 'Niepoprawny format pliku wejściowego.\nSprawdź format pliku i spróbuj ponownie.'
MESSAGE_TITLE_END_PROGRAM = 'Zamknąć program?'
MESSAGE_END_PROGRAM = 'Maszyna Turinga wciąż działa.\nCzy na pewno chcesz wyjść?'
FILE_OPEN_TITLE = 'Wybierz plik...'
CURRENT_DIR = '.'
TXT_FILTER = 'Pliki tekstowe (*.txt)'
FILENAME_INDEX = 0
PIXMAP_BACKGROUND_COLOR = '#f0f0f0'
BROWN = 'brown'
PERU = 'peru'
WIDTH_COEFFICIENT = 2/3
HEIGHT_COEFFICIENT = 0.6
BEG_POINT_X_RECT = 0
BEG_POINT_Y_RECT_COEFFICIENT = 0.3
END_POINT_Y_RECT = 45
CELLS_LOCATION_HEIGHT_COEFFICIENT = BEG_POINT_Y_RECT_COEFFICIENT
CELL_WIDTH_PEN = 32
X_LOC_FIRST_CELL = 18
Y_LOC_CELL_INCREASED = 23
X_DIST_NEXT_CELL = 35
HEAD_LOC_COEFFICIENT = 3
HEAD_Y_BOTTOM_POINT_LOC_ABOVE_TAPE = 70
HEAD_X_TOP_POINT_LOC_ABOVE_TAPE = 20
HEAD_Y_TOP_POINT_LOC_ABOVE_TAPE = 100
HEAD_WIDTH_PEN = 1
FAMILY_FONT = 'Times'
POINT_SIZE = 22
FIRST_LETTER_POS = 6
NEXT_LETTER_POS = 35
LETTER_HEIGHT_COEFFICIENT = 0.354
FILL_TABLE_NO_TRANSITION = ' '
