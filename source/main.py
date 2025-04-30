
import sys
from pathlib import Path

from PySide6 import QtWidgets
from .ui.controllers.main_window import MainWindow


def main(root: Path):
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(root)
    window.show()
    sys.exit(app.exec())
