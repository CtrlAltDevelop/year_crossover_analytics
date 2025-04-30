from PySide6.QtCore import QObject, QRunnable, Signal, Slot
from ..core.analyzer import Analyzer


class WorkerSignals(QObject):
    log            = Signal(str)
    phase_progress = Signal(int)
    inner_progress = Signal(int)
    finished       = Signal()


class BaseWorker(QRunnable):
    def __init__(self, settings: dict):
        super().__init__()
        self.signals = WorkerSignals()
        self.settings = settings

    @Slot()
    def run(self):
        try:
            mac = self.settings['mac']
            pass_number = self.settings['pass_number']
            report = self.settings['report']
            connect = self.settings['connect']

            self.signals.log.emit("🚀 Starting analysis...")
            self.signals.log.emit(f"🖥️ MAC: {mac}")
            self.signals.log.emit(f"📑 Using report: {report}")
            if connect:
                self.signals.log.emit(f"📃 Using connect: {connect}")

            for phase, inner, msg in Analyzer(pass_number, report).process():
                if phase:
                    self.signals.phase_progress.emit(phase)
                if inner:
                    self.signals.inner_progress.emit(inner)
                if msg:
                    self.signals.log.emit(msg)

            self.signals.log.emit("✅ Analysis completed.")
        except Exception as e:
            self.signals.log.emit(f"❌ Error: {str(e)}")
        finally:
            self.signals.finished.emit()
