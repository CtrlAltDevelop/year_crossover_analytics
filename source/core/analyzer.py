import time
from pathlib import Path
from typing import Optional

from source.core.models.worker_signals import WorkerSignals


class Analyzer:
    def __init__(self, signals: WorkerSignals, base_path: Path, result_path: Path):
        self.signals = signals
        self.base_path = base_path
        self.result_path = result_path

    def process(self, pass_number: str, report: Path, connect: Optional[Path] = None):
        self.signals.log.emit(f"🔍 Processing report: {report.name}")
        if connect:
            self.signals.log.emit(f"🔗 Using connection data: {connect.name}")

        for p in self._main_progression():
            self.signals.progress.emit(p)
            self.signals.log.emit(f"Phase progress: {p}%")

    def _main_progression(self):
        total_steps = 2
        for i in range(total_steps):
            self.signals.sub_format.emit(f"Read Data {i}: %p%")
            for sub in self._sub_progression():
                self.signals.sub_progress.emit(sub)
            yield (i + 1) / total_steps * 100

    @staticmethod
    def _sub_progression():
        total = 100
        for i in range(total):
            time.sleep(0.001)
            yield (i + 1) / total * 100
