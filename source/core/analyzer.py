from pathlib import Path
from typing import Optional

from source.core.models.worker_signals import WorkerSignals


class Analyzer:
    def __init__(self, signals: WorkerSignals, base_path: Path, result_path: Path):
        self.signals = signals
        self.base_path = base_path
        self.result_path = result_path

    def process(self, pass_number: str, report: Path, connect: Optional[Path] = None):
        pass
