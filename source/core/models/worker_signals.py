from PySide6.QtCore import QObject, Signal


class WorkerSignals(QObject):
    log            = Signal(str)
    phase_progress = Signal(int)
    inner_progress = Signal(int)
    finished       = Signal()
