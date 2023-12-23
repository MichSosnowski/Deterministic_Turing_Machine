from PySide6.QtCore import QObject, Signal


class ThreadSignals(QObject):
    draw = Signal()
    extend_tape = Signal(str)
    error = Signal()
    stop = Signal()
    end = Signal()
