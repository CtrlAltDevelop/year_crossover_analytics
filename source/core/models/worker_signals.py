from PySide6.QtCore import QObject, Signal


class WorkerSignals(QObject):
    log          = Signal(str)
    progress     = Signal(float)
    sub_progress = Signal(float)
    sub_format   = Signal(str)
    finished     = Signal()
