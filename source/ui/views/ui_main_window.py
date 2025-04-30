# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowIEGyib.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(700, 450)
        MainWindow.setMinimumSize(QSize(700, 450))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"/* Main Window */\n"
"QMainWindow {\n"
"	background-color: #f0f0f0;\n"
"}\n"
"\n"
"\n"
"/* Label */\n"
"QLabel {\n"
"	font-size: 13px;\n"
"    font-weight: 600;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    color: #2d3436;\n"
"}\n"
"\n"
"\n"
"/* Group Box */\n"
"QGroupBox {\n"
"    font-size: 14px;\n"
"    font-weight: 800;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    color: #2d3436;\n"
"    border: 1px solid #b0b5b8;\n"
"    border-radius: 6px;\n"
"    background-color: #ffffff;\n"
"    margin-top: 18px;\n"
"    padding: 6px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 5px 8px;\n"
"    color: #2d3436;\n"
"    left: 10px;\n"
"    top: 4px;\n"
"}\n"
"\n"
"\n"
"/* Push Button */\n"
"QPushButton {\n"
"    background-color: #4CAF50;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    border-radius: 5px;\n"
"    padding: 8px 16p"
                        "x;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #429746;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 1px solid #54be59;\n"
"}\n"
"\n"
"\n"
"/* Line Edit */\n"
"QLineEdit {\n"
"	padding: 6px;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    border: 1px solid #b0b5b8;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"    color: #2d3436;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #54be59;\n"
"    background-color: #f8fbff;\n"
"}\n"
"\n"
"\n"
"/* Combo Box */\n"
"QComboBox {\n"
"    border: 1px solid #b0b5b8;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    color: #2d3436;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #f1f3f5;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #54be59;\n"
"}\n"
"\n"
"QComboBox::drop"
                        "-down {\n"
"    width: 24px;\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    /* Optional: Add custom arrow icon in resource file */\n"
"    /* image: url(:/icons/down_arrow.png); */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #b0b5b8;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"    selection-background-color: #45a049;\n"
"    selection-color: #ffffff;\n"
"    color: #2d3436;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 10px;\n"
"    min-height: 28px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #f1f3f5;\n"
"    color: #2d3436;\n"
"}\n"
"\n"
"\n"
"/* Progress Bar */\n"
"QProgressBar {\n"
"	border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    font-size: 14px;\n"
"    margin-top: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: #4CAF50;\n"
"    width: 10px;\n"
""
                        "}\n"
"\n"
"\n"
"/* Text Edit */\n"
"QTextEdit {\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    border: 1px solid #b0b5b8;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"    color: #2d3436;\n"
"    padding: 6px;\n"
"    line-height: 1.5;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"    background-color: #f1f3f5;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 1px solid #0984e3;\n"
"    background-color: #f8fbff;\n"
"}\n"
"\n"
"\n"
"/* Check Box */\n"
"QCheckBox {\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    color: #2d3436;\n"
"    spacing: 8px;\n"
"padding-left: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border: 1px solid #b0b5b8;\n"
"    border-radius: 4px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background-color: #f1f3f5;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #0984e3;\n"
"   "
                        " border: 1px solid #0984e3;\n"
"    image: url(:/icons/checkmark.png); /* Optional: Add custom checkmark icon */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background-color: #0871c4;\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: none;\n"
"    outline: none;\n"
"}")
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 10, 10)
        self.groupBox_2 = QGroupBox(self.page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"")
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)

        self.gridLayout_2.addWidget(self.checkBox, 1, 4, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 3, 1, 1)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 3)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.lineEdit_6.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)

        self.gridLayout_2.addWidget(self.lineEdit_6, 0, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.lineEdit, 1, 3, 1, 3)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lineEdit_4.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_4, 5, 3, 1, 3)

        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.pushButton_4, 3, 6, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_3, 3, 3, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lineEdit_2.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_2, 2, 3, 1, 1)

        self.pushButton_7 = QPushButton(self.groupBox)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.pushButton_7, 5, 6, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.pushButton_3, 2, 6, 1, 1)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 4, 2, 1, 5)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(90, 0))
        self.pushButton_2.setMaximumSize(QSize(90, 16777215))
        self.pushButton_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.pushButton_2, 1, 6, 1, 1)

        self.pushButton_9 = QPushButton(self.groupBox)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    background-color: #ff7070;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c40808;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #9f0606;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 1px solid #ff7474;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_9, 3, 4, 1, 1)

        self.pushButton_8 = QPushButton(self.groupBox)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"    background-color: #ff7070;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c40808;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #9f0606;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 1px solid #ff7474;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_8, 2, 4, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #0984e3;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    border-radius: 6px;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0871c4;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #065a9f;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 1px solid #74b9ff;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalLayout_2.setStretch(0, 8)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(3, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.textEdit = QTextEdit(self.page_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFrameShadow(QFrame.Shadow.Sunken)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.textEdit.setTabChangesFocus(False)
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setAcceptRichText(False)

        self.verticalLayout_2.addWidget(self.textEdit)

        self.progressBar_2 = QProgressBar(self.page_2)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setValue(4)
        self.progressBar_2.setInvertedAppearance(False)

        self.verticalLayout_2.addWidget(self.progressBar_2)

        self.progressBar = QProgressBar(self.page_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar::chunk {\n"
"	background-color: #55aaff;\n"
"}\n"
"")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(20)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.BottomToTop)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	background-color: #2196F3;\n"
"	font: 700;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #1976D2;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(2, 1)
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout.setStretch(0, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_8.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_9.clicked.connect(self.lineEdit_3.clear)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MQL5 Trade Analyzer", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Analyze Settings", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Create Build Features file", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Risk Amount", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Calculation based on Commission Database", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Read from the ReportTester file", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Commission Method", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Optimization Pass", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Reports file", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Meta Report", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select an Report file to analyze", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Result Path (Optional)", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select a Path to Store Results", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select an Margin Data file", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select an Deal Connect file", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Deal Connect (Optional)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Margin Data (Optional)", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.textEdit.setMarkdown("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI','Arial','sans-serif'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.progressBar_2.setFormat(QCoreApplication.translate("MainWindow", u"Read M5 Trades %p%", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"Main Progress %p%", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Open Results", None))
    # retranslateUi

