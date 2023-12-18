from PySide6.QtCore import QObject, Signal


class ThreadSignals(QObject):
    draw = Signal()
    error = Signal()
    end = Signal()
