from enum import Enum, verify, UNIQUE, CONTINUOUS


@verify(UNIQUE)
@verify(CONTINUOUS)
class Indexes(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
