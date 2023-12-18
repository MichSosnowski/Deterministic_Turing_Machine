from typing import TextIO

import constants.constants as constants
from constants.enums import Indexes
from exceptions.exceptions import IncorrectFormatException


class FileParser:

    def __init__(self, filename) -> None:
        self.filename: str = filename
        self.file: TextIO = open(filename)

    def parse_file(self) -> None:
        tape_alphabet: str = self.analyze_tape_alphabet()
        self.analyze_entry_alphabet_and_word(tape_alphabet)
        states = self.analyze_states()
        self.analyze_transition_function(tape_alphabet, states)
        self.file.close()

    def analyze_tape_alphabet(self) -> str:
        self.is_correct_line(constants.TAPE_ALPHABET)
        tape_alphabet: str = self.check_tape_alphabet()
        return tape_alphabet

    def analyze_entry_alphabet_and_word(self, tape_alphabet: str) -> None:
        self.is_correct_line(constants.ENTRY_ALPHABET)
        entry_alphabet: str = self.check_entry_alphabet(tape_alphabet)
        self.is_correct_line(constants.ENTRY_WORD)
        self.check_entry_word(entry_alphabet)

    def analyze_states(self) -> list[str]:
        self.is_correct_line(constants.STATES)
        states = self.get_all_states()
        self.is_correct_line(constants.INITIAL_STATE)
        self.check_initial_state(states)
        self.is_correct_line(constants.ACCEPTING_STATES)
        self.check_accepting_states(states)
        return states

    def analyze_transition_function(self, tape_alphabet: str, states: list[str]) -> None:
        self.is_correct_line(constants.TRANSITION_FUNCTION)
        self.check_transition_function(tape_alphabet, states)

    def is_correct_line(self, correct_line: str) -> None:
        read_line: str = self.file.readline()
        if read_line != correct_line:
            raise IncorrectFormatException

    def check_tape_alphabet(self) -> str:
        read_line: str = self.file.readline()[:constants.LAST_CHAR_INDEX]
        if len(read_line) < constants.REQUIRED_COUNT_TAPE_ALPHABET or read_line.find(constants.EMPTY_CHAR) == constants.CHAR_NOT_FOUND:
            raise IncorrectFormatException
        return read_line

    def check_entry_alphabet(self, tape_alphabet: str) -> str:
        read_line: str = self.file.readline()[:constants.LAST_CHAR_INDEX]
        is_all_chars_in_tape_alphabet = list(map(lambda elem: elem in tape_alphabet, read_line))
        if len(read_line) < constants.REQUIRED_COUNT or False in is_all_chars_in_tape_alphabet:
            raise IncorrectFormatException
        return read_line

    def check_entry_word(self, entry_alphabet: str) -> None:
        read_line: str = self.file.readline()[:constants.LAST_CHAR_INDEX]
        is_all_chars_in_entry_alphabet = list(map(lambda elem: elem in entry_alphabet, read_line))
        if len(read_line) < constants.REQUIRED_COUNT or len(read_line) > constants.MAX_LENGTH_ENTRY_WORD or False in is_all_chars_in_entry_alphabet:
            raise IncorrectFormatException

    def get_all_states(self) -> list[str]:
        read_line: str = self.file.readline()[:constants.LAST_CHAR_INDEX]
        if len(read_line) < constants.REQUIRED_COUNT:
            raise IncorrectFormatException
        states: list[str] = read_line.split(constants.SPACE)
        return states

    def check_initial_state(self, states: list[str]) -> None:
        read_line: str = self.file.readline()[:constants.LAST_CHAR_INDEX]
        if len(read_line) != constants.REQUIRED_COUNT or read_line not in states:
            raise IncorrectFormatException

    def check_accepting_states(self, states: list[str]) -> None:
        read_line: str = self.file.readline()[:constants.LAST_CHAR_INDEX]
        accepting_states: list[str] = read_line.split(constants.SPACE)
        is_accepting_states_in_states = list(map(lambda elem: elem in states, accepting_states))
        if len(read_line) < constants.REQUIRED_COUNT or False in is_accepting_states_in_states:
            raise IncorrectFormatException

    def check_transition_function(self, tape_alphabet: str, states: list[str]) -> None:
        self.check_eof()
        for line in self.file:
            line_elements: list[str] = self.get_elems_of_line_from_file(line)
            self.analyze_line_elements(line_elements, tape_alphabet, states)


    def get_elems_of_line_from_file(self, line: str) -> list[str]:
        if line.find(constants.NEWLINE) != constants.CHAR_NOT_FOUND:
            line_elements: list[str] = line[:constants.LAST_CHAR_INDEX].split(constants.SPACE)
        else:
            line_elements: list[str] = line.split(constants.SPACE)
        return line_elements

    def analyze_line_elements(self, line_elements: list[str], tape_alphabet: str, states: list[str]) -> None:
        moves: tuple(str, str) = (constants.LEFT, constants.RIGHT)
        if (line_elements[Indexes.ZERO.value] not in states or
            line_elements[Indexes.ONE.value] not in tape_alphabet or
            line_elements[Indexes.TWO.value] not in states or
            line_elements[Indexes.THREE.value] not in tape_alphabet or
            line_elements[Indexes.FOUR.value] not in moves):
                raise IncorrectFormatException

    def check_eof(self) -> None:
        position_now: int = self.file.tell()
        line: str = self.file.readline()
        if not line:
            raise IncorrectFormatException
        self.file.seek(position_now)
