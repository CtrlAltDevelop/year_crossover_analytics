from contextlib import contextmanager
from pathlib import Path
from typing import Tuple, List, Dict, Any, Optional

import pandas as pd
from PySide6.QtCore import SignalInstance


class ReportClass:
    # @contextmanager
    # def _tkinter_root(self):
    #     """Context manager to handle the Tkinter root window lifecycle."""
    #     root = Tk()
    #     try:
    #         root.withdraw()
    #         yield root
    #     finally:
    #         root.destroy()

    # def _get_file_via_dialog(self, title: str, filetypes: List[Tuple[str, str]], base_path: Path = Path.cwd()
    #                          ) -> Tuple[str, Tuple[pd.DataFrame, Dict[str, Any]]]:
    #     """
    #     Opens a file dialog for the user to select a CSV file and processes it.
    #
    #     :param title: Title of the file dialog.
    #     :param filetypes: List of tuples specifying the file types.
    #     :param base_path: The initial directory for the file dialog. Defaults to the current working directory.
    #     :return: A tuple containing the selected file path as a string and the processed pandas DataFrame.
    #     :raises FileNotFoundError: If no file is selected.
    #     """
    #     with self._tkinter_root():
    #         file_path = filedialog.askopenfilename(title=title, filetypes=filetypes, initialdir=str(base_path))
    #     if not file_path:
    #         raise FileNotFoundError(f"{title} not selected.")
    #     return file_path, self._analyzed_data(Path(file_path))

    def get_file_via_path(self, path: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """
        Processes a CSV file from a given path.

        :param path: Path to the CSV file.
        :return: A processed pandas DataFrame.
        """
        return self._analyzed_data(path)

    def get_file_via_path_with_gui(self, path: Path, connect: Optional[Path], progress: SignalInstance) -> Tuple[
        pd.DataFrame, Dict[str, Any]]:
        """
        Processes a CSV file from a given path.

        :param path: Path to the CSV file.
        :param connect: Path to the Connect CSV file.
        :param progress: Qt Progress bar instance.
        :return: A processed pandas DataFrame.
        """
        return self._analyzed_data_with_gui(path, connect, progress)

    def _analyzed_data(self, file: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """
        Reads, processes, and merges open and close trades from the CSV.

        :param file: Path to the CSV file.
        :return: A merged pandas DataFrame containing open and close trades.
        """
        pass

    def _analyzed_data_with_gui(self, file: Path, connect: Optional[Path], progress: SignalInstance) -> Tuple[
        pd.DataFrame, Dict[str, Any]]:
        """
        Reads, processes, and merges open and close trades from the CSV.

        :param path: Path to the CSV file.
        :return: A merged pandas DataFrame containing open and close trades.
        """
        pass
