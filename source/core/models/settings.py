from pathlib import Path
from typing import Optional


class Settings(object):
    mac: str
    base_path: Path
    result_path: Path
    report_path: Path
    connect_path: Optional[Path] = None
