import sys
import pathlib
import warnings

from PySide6.QtWidgets import QApplication

from source.ui.controllers.main_window import MainWindow
from source.config import parse_args


def main(root: pathlib.Path):
    warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

    args = parse_args()

    app = QApplication(sys.argv)
    app.setApplicationName("Year Crossover Analytics")

    if args.debug:
        print("🛠 Debug mode enabled")
        print(f"🧵 Max threads: {args.max_threads}")

    window = MainWindow(root)
    window.show()
    sys.exit(app.exec())
