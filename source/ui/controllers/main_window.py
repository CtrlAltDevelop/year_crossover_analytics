import os
import sys
import uuid
from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QThreadPool
from source.ui.views.ui_main_window import Ui_MainWindow
from source.core.features.mac_validator import VALID_MAC_LIST
from source.core.workers.base_worker import BaseWorker
from source.core.models.settings import Settings


class MainWindow(QMainWindow):
    def __init__(self, base_path: Path):
        super().__init__()
        self.base_path = base_path
        self.results = base_path / 'results'

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Year Crossover Analytics")
        self.pool = QThreadPool.globalInstance()
        self.pool.setMaxThreadCount(4)

        self.setWindowIcon(QIcon('icon.ico'))
        self._validate_mac()

        self._connect_ui()
        self._reset_ui()

    def _validate_mac(self):
        system_mac = self._get_mac_address()
        if system_mac not in VALID_MAC_LIST:
            QMessageBox.critical(self, "Unauthorized Device",
                                 f"MAC address not authorized: {system_mac}")
            sys.exit(1)

    @staticmethod
    def _get_mac_address():
        return ':'.join(("%012X" % uuid.getnode())[i:i + 2] for i in range(0, 12, 2))

    def select_file(self, target_lineedit):
        path, _ = QFileDialog.getOpenFileName(self, "Open Report File")
        if path:
            target_lineedit.setText(path)


    def _connect_ui(self):
        self.setWindowIcon(QIcon("icon.ico"))
        self.ui.progressBar_2.setVisible(False)
        self.ui.pushButton.clicked.connect(self.start_analysis)
        self.ui.pushButton_2.clicked.connect(self._load_file(self.ui.lineEdit, "Excel Files (*.xlsx *.xls)"))
        self.ui.pushButton_3.clicked.connect(self._load_file(self.ui.lineEdit_2, "CSV Files (*.csv)"))
        self.ui.pushButton_5.clicked.connect(lambda: os.startfile(self._get_result_path()))
        self.ui.pushButton_6.clicked.connect(self._reset_ui)
        self.ui.pushButton_7.clicked.connect(self._load_folder)
        self.ui.lineEdit_4.setText(str(self.results))
        self.ui.textEdit.textChanged.connect(self.scroll_to_bottom)

    def scroll_to_bottom(self):
        scrollbar = self.ui.textEdit.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def _load_file(self, line_edit, filter_string):
        def wrapper():
            file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "", filter_string)
            if file_name:
                line_edit.setText(file_name)

        return wrapper

    def _load_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.ui.lineEdit_4.setText(folder)

    def _get_result_path(self):
        folder_path = self.ui.lineEdit_4.text().strip()
        if not folder_path:
            folder_path = str(self.base_path / 'results')
        return folder_path

    def _reset_ui(self):
        self.ui.textEdit.clear()
        self.ui.progressBar.setValue(0)
        self.ui.progressBar_2.setValue(0)
        self.ui.progressBar_2.setVisible(False)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.frame.setVisible(False)

    def _set_value_to_progress(self, value: int):
        self.ui.progressBar_2.setVisible(0.1 < value < 99.9)
        self.ui.progressBar_2.setValue(value)

    def _analysis_done(self):
        self.ui.frame.setVisible(True)
        self.ui.progressBar_2.setVisible(False)

    def start_analysis(self):
        settings = Settings()
        settings.base_path = self.base_path
        settings.result_path = self._get_result_path()
        settings.mac = self._get_mac_address()

        settings.pass_number = self.ui.lineEdit_5.text().strip()
        settings.report_path = self.ui.lineEdit.text().strip()
        settings.connect_path = self.ui.lineEdit_2.text().strip()

        if not settings.pass_number.isdigit():
            QMessageBox.warning(self, "Input Error", "Optimization pass must be a number.")
            return

        if not settings.report_path:
            QMessageBox.warning(self, "Input Error", "Please select a report file.")
            return

        self.ui.textEdit.clear()
        self.ui.stackedWidget.setCurrentIndex(1)

        worker = BaseWorker(settings)
        worker.signals.log.connect(self.ui.textEdit.append)
        worker.signals.phase_progress.connect(self.ui.progressBar.setValue)
        worker.signals.inner_progress.connect(self._set_value_to_progress)
        worker.signals.finished.connect(self._analysis_done)
        self.pool.start(worker)
