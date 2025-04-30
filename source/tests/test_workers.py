import pytest
from ..workers.base_worker import BaseWorker

def test_worker_signals(qtbot, tmp_path):
    # Create dummy CSVs
    r1 = tmp_path / "r1.csv"; r1.write_text("ticket,time_open,time_close,profit\n")
    r2 = tmp_path / "r2.csv"; r2.write_text("ticket,time_open,time_close,profit\n")
    settings = {'file1': str(r1), 'file2': str(r2)}

    worker = BaseWorker(settings)
    # Collect signals
    logs = []
    worker.signals.log.connect(logs.append)
    finishes = []
    worker.signals.finished.connect(lambda: finishes.append(True))

    # Run synchronously
    worker.run()
    assert finishes
