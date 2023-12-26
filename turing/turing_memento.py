from typing import Deque


class TuringMachineMemento:

    def __init__(self, turing_machine) -> None:
        self.actual_state: str = turing_machine.actual_state
        self.tape: Deque[str] = turing_machine.tape.copy()
        self.head_position_tape: int = turing_machine.head_position_tape
        self.head_position_fragment_tape: int = turing_machine.head_position_fragment_tape
        self.first_index_fragment_tape: int = turing_machine.first_index_fragment_tape
        self.last_index_fragment_tape: int = turing_machine.last_index_fragment_tape
        self.calculation_length: int = turing_machine.calculation_length
