from PySide6.QtCore import QRunnable, Slot
from source.core.models.worker_signals import WorkerSignals
from source.core.features.analyzer import Analyzer
from source.core.models.settings import Settings


class BaseWorker(QRunnable):
    def __init__(self, settings: Settings):
        super().__init__()
        self.signals = WorkerSignals()
        self.settings = settings

    @Slot()
    def run(self):
        try:
            self.signals.log.emit("🚀 Starting analysis...")
            self.signals.log.emit(f"🖥️ MAC: {self.settings.mac}")

            analyzer = Analyzer(self.signals, self.settings.base_path, self.settings.result_path)
            analyzer.process(self.settings.report_path, self.settings.connect_path)

            self.signals.log.emit("✅ Analysis completed.")

        except Exception as e:
            self.signals.log.emit(f"❌ Error: {str(e)}")

        finally:
            self.signals.finished.emit()
