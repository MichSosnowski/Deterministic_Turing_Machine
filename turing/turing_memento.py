from typing import Deque


class TuringMachineMemento:

    def __init__(self, turing_machine) -> None:
        self.actual_state: str = turing_machine.actual_state
        self.tape: Deque[str] = turing_machine.tape.copy()
        self.head_position_tape: int = turing_machine.head_position_tape
        self.calculation_length: int = turing_machine.calculation_length
