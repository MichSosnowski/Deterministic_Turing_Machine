# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.file_text_browser = QTextBrowser(self.groupBox_2)
        self.file_text_browser.setObjectName(u"file_text_browser")
        self.file_text_browser.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.file_text_browser.setFrameShape(QFrame.NoFrame)

        self.gridLayout_3.addWidget(self.file_text_browser, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 3, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stop_button = QPushButton(self.groupBox)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setEnabled(False)

        self.gridLayout.addWidget(self.stop_button, 1, 1, 1, 1)

        self.step_backward_button = QPushButton(self.groupBox)
        self.step_backward_button.setObjectName(u"step_backward_button")

        self.gridLayout.addWidget(self.step_backward_button, 2, 0, 1, 1)

        self.start_button = QPushButton(self.groupBox)
        self.start_button.setObjectName(u"start_button")

        self.gridLayout.addWidget(self.start_button, 1, 0, 1, 1)

        self.reset_button = QPushButton(self.groupBox)
        self.reset_button.setObjectName(u"reset_button")

        self.gridLayout.addWidget(self.reset_button, 3, 0, 1, 2)

        self.step_forward_button = QPushButton(self.groupBox)
        self.step_forward_button.setObjectName(u"step_forward_button")

        self.gridLayout.addWidget(self.step_forward_button, 2, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.horizontalLayout_2.addWidget(self.groupBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 6, 1, 2, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.refresh_button = QPushButton(self.centralwidget)
        self.refresh_button.setObjectName(u"refresh_button")

        self.horizontalLayout.addWidget(self.refresh_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 2, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.entry_word_label = QLabel(self.centralwidget)
        self.entry_word_label.setObjectName(u"entry_word_label")
        self.entry_word_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.entry_word_label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.result_word_label = QLabel(self.centralwidget)
        self.result_word_label.setObjectName(u"result_word_label")
        self.result_word_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.result_word_label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.calculation_length_label = QLabel(self.centralwidget)
        self.calculation_length_label.setObjectName(u"calculation_length_label")
        self.calculation_length_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.calculation_length_label)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 3, 0, 3, 1)

        self.turing_machine_tape = QLabel(self.centralwidget)
        self.turing_machine_tape.setObjectName(u"turing_machine_tape")

        self.gridLayout_2.addWidget(self.turing_machine_tape, 0, 1, 5, 1)

        self.tape_state_table = QTableWidget(self.centralwidget)
        if (self.tape_state_table.columnCount() < 5):
            self.tape_state_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tape_state_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tape_state_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tape_state_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tape_state_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tape_state_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tape_state_table.rowCount() < 1):
            self.tape_state_table.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tape_state_table.setVerticalHeaderItem(0, __qtablewidgetitem5)
        self.tape_state_table.setObjectName(u"tape_state_table")
        self.tape_state_table.setFocusPolicy(Qt.NoFocus)
        self.tape_state_table.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.tape_state_table.setFrameShape(QFrame.NoFrame)
        self.tape_state_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tape_state_table.setTabKeyNavigation(False)
        self.tape_state_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.tape_state_table.horizontalHeader().setCascadingSectionResizes(False)
        self.tape_state_table.horizontalHeader().setDefaultSectionSize(173)
        self.tape_state_table.horizontalHeader().setHighlightSections(False)
        self.tape_state_table.horizontalHeader().setStretchLastSection(True)
        self.tape_state_table.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_2.addWidget(self.tape_state_table, 5, 1, 1, 1)

        self.gridLayout_2.setRowStretch(0, 5)
        self.gridLayout_2.setRowStretch(1, 2)
        self.gridLayout_2.setRowStretch(2, 2)
        self.gridLayout_2.setRowStretch(3, 1)
        self.gridLayout_2.setRowStretch(4, 1)
        self.gridLayout_2.setRowStretch(5, 2)
        self.gridLayout_2.setRowStretch(6, 2)
        self.gridLayout_2.setRowStretch(7, 2)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"WCZYTANA MASZYNA TURINGA", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"STEROWANIE MASZYN\u0104 TURINGA", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.step_backward_button.setText(QCoreApplication.translate("MainWindow", u"KROK W TY\u0141", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.step_forward_button.setText(QCoreApplication.translate("MainWindow", u"KROK W PRZ\u00d3D", None))
        self.refresh_button.setText(QCoreApplication.translate("MainWindow", u"OD\u015aWIE\u017b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"S\u0141OWO WEJ\u015aCIOWE", None))
        self.entry_word_label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"S\u0141OWO WYJ\u015aCIOWE", None))
        self.result_word_label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"D\u0141UGO\u015a\u0106 OBLICZENIA", None))
        self.calculation_length_label.setText("")
        self.turing_machine_tape.setText("")
        ___qtablewidgetitem = self.tape_state_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"STAN BIE\u017b\u0104CY", None));
        ___qtablewidgetitem1 = self.tape_state_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ZNAK CZYTANY", None));
        ___qtablewidgetitem2 = self.tape_state_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"STAN DOCELOWY", None));
        ___qtablewidgetitem3 = self.tape_state_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ZNAK PISANY", None));
        ___qtablewidgetitem4 = self.tape_state_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"KIERUNEK", None));
    # retranslateUi

