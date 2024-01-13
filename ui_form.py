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
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1400, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.file_text_browser = QTextBrowser(self.groupBox_2)
        self.file_text_browser.setObjectName(u"file_text_browser")
        self.file_text_browser.setContextMenuPolicy(Qt.NoContextMenu)
        self.file_text_browser.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.file_text_browser.setFrameShape(QFrame.NoFrame)

        self.gridLayout_3.addWidget(self.file_text_browser, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 2, 1)

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

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QSize(16777215, 45))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 341, 45))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.result_word_label = QLabel(self.scrollAreaWidgetContents)
        self.result_word_label.setObjectName(u"result_word_label")
        self.result_word_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.result_word_label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.calculation_length_label = QLabel(self.centralwidget)
        self.calculation_length_label.setObjectName(u"calculation_length_label")
        self.calculation_length_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.calculation_length_label)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 2, 0, 4, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.slow_head_button = QPushButton(self.groupBox)
        self.slow_head_button.setObjectName(u"slow_head_button")
        self.slow_head_button.setEnabled(False)

        self.gridLayout.addWidget(self.slow_head_button, 3, 1, 1, 1)

        self.step_forward_button = QPushButton(self.groupBox)
        self.step_forward_button.setObjectName(u"step_forward_button")
        self.step_forward_button.setEnabled(False)

        self.gridLayout.addWidget(self.step_forward_button, 2, 2, 1, 1)

        self.start_button = QPushButton(self.groupBox)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setEnabled(False)

        self.gridLayout.addWidget(self.start_button, 3, 0, 1, 1)

        self.step_backward_button = QPushButton(self.groupBox)
        self.step_backward_button.setObjectName(u"step_backward_button")
        self.step_backward_button.setEnabled(False)

        self.gridLayout.addWidget(self.step_backward_button, 2, 1, 1, 1)

        self.stop_button = QPushButton(self.groupBox)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setEnabled(False)

        self.gridLayout.addWidget(self.stop_button, 3, 3, 1, 1)

        self.fast_head_button = QPushButton(self.groupBox)
        self.fast_head_button.setObjectName(u"fast_head_button")
        self.fast_head_button.setEnabled(False)

        self.gridLayout.addWidget(self.fast_head_button, 3, 2, 1, 1)

        self.reset_button = QPushButton(self.groupBox)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setEnabled(False)

        self.gridLayout.addWidget(self.reset_button, 4, 1, 1, 2)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)

        self.horizontalLayout_2.addWidget(self.groupBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 6, 1, 2, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.refresh_button = QPushButton(self.centralwidget)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setEnabled(False)

        self.gridLayout_4.addWidget(self.refresh_button, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.load_file_button = QPushButton(self.centralwidget)
        self.load_file_button.setObjectName(u"load_file_button")

        self.gridLayout_4.addWidget(self.load_file_button, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 3, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.open_load_file_button = QPushButton(self.centralwidget)
        self.open_load_file_button.setObjectName(u"open_load_file_button")
        self.open_load_file_button.setEnabled(False)

        self.gridLayout_4.addWidget(self.open_load_file_button, 2, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 2, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_8, 2, 2, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 4)
        self.gridLayout_4.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout_4, 6, 0, 2, 1)

        self.scrollArea_2 = QScrollArea(self.centralwidget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1028, 349))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.turing_machine_label = QLabel(self.scrollAreaWidgetContents_2)
        self.turing_machine_label.setObjectName(u"turing_machine_label")

        self.verticalLayout_4.addWidget(self.turing_machine_label)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 1, 4, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.groupBox_3.setFlat(False)
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tape_state_table = QTableWidget(self.groupBox_3)
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
        self.tape_state_table.horizontalHeader().setDefaultSectionSize(137)
        self.tape_state_table.horizontalHeader().setHighlightSections(False)
        self.tape_state_table.horizontalHeader().setStretchLastSection(True)
        self.tape_state_table.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout.addWidget(self.tape_state_table)


        self.gridLayout_2.addWidget(self.groupBox_3, 5, 1, 1, 1)

        self.configuration_label = QLabel(self.centralwidget)
        self.configuration_label.setObjectName(u"configuration_label")
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setKerning(True)
        self.configuration_label.setFont(font1)
        self.configuration_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.configuration_label, 4, 1, 1, 1)

        self.gridLayout_2.setRowStretch(0, 5)
        self.gridLayout_2.setRowStretch(1, 2)
        self.gridLayout_2.setRowStretch(2, 2)
        self.gridLayout_2.setRowStretch(3, 1)
        self.gridLayout_2.setRowStretch(4, 1)
        self.gridLayout_2.setRowStretch(5, 2)
        self.gridLayout_2.setRowStretch(6, 2)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"WCZYTANA MASZYNA TURINGA", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"S\u0141OWO WEJ\u015aCIOWE", None))
        self.entry_word_label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"S\u0141OWO OBLICZONE", None))
        self.result_word_label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"D\u0141UGO\u015a\u0106 OBLICZENIA", None))
        self.calculation_length_label.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"STEROWANIE MASZYN\u0104 TURINGA", None))
#if QT_CONFIG(tooltip)
        self.slow_head_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Spowalnia prac\u0119 g\u0142owicy maszyny Turinga podczas symulacji.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.slow_head_button.setText(QCoreApplication.translate("MainWindow", u"SPOWOLNIJ G\u0141OWIC\u0118", None))
#if QT_CONFIG(tooltip)
        self.step_forward_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Wykonuje kolejn\u0105 operacj\u0119 przewidzian\u0105 przez program wczytanej maszyny Turinga.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.step_forward_button.setText(QCoreApplication.translate("MainWindow", u"KROK W PRZ\u00d3D", None))
#if QT_CONFIG(tooltip)
        self.start_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Rozpoczyna symulacj\u0119 dzia\u0142ania maszyny Turinga.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"START", None))
#if QT_CONFIG(tooltip)
        self.step_backward_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Przywraca poprzedni\u0105 operacj\u0119 wykonan\u0105 przez maszyn\u0119 Turinga.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.step_backward_button.setText(QCoreApplication.translate("MainWindow", u"KROK WSTECZ", None))
#if QT_CONFIG(tooltip)
        self.stop_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Zatrzymuje symulacj\u0119 dzia\u0142ania maszyny Turinga.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
#if QT_CONFIG(tooltip)
        self.fast_head_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Przyspiesza prac\u0119 g\u0142owicy maszyny Turinga podczas symulacji.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fast_head_button.setText(QCoreApplication.translate("MainWindow", u"PRZYSPIESZ G\u0141OWIC\u0118", None))
#if QT_CONFIG(tooltip)
        self.reset_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Ustawia pocz\u0105tkowy stan symulatora maszyny Turinga z wczytanego uprzednio pliku z opisem, lecz nie zaci\u0105ga jakichkolwiek zmian, kt\u00f3re w mi\u0119dzyczasie nast\u0105pi\u0142y w tym pliku.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
#if QT_CONFIG(tooltip)
        self.refresh_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Wczytuje ponownie uprzednio wczytany plik z opisem maszyny Turinga wraz ze wszelkimi wykonanymi przez u\u017cytkownika zmianami w tym pliku oraz odpowiednio ustawia symulator zgodnie z dokonanymi zmianami.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.refresh_button.setText(QCoreApplication.translate("MainWindow", u"OD\u015aWIE\u017b", None))
#if QT_CONFIG(tooltip)
        self.load_file_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Otwiera eksplorator plik\u00f3w celem umo\u017cliwenia u\u017cytkownikowi wyboru pliku z opisem maszyny Turinga do wczytania przez symulator.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.load_file_button.setText(QCoreApplication.translate("MainWindow", u"WCZYTAJ PLIK", None))
#if QT_CONFIG(tooltip)
        self.open_load_file_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Otwiera uprzednio wczytany przez u\u017cytkownika plik z opisem maszyny Turinga w standardowym edytorze tekstowym.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.open_load_file_button.setText(QCoreApplication.translate("MainWindow", u"OTW\u00d3RZ WCZYTANY PLIK", None))
        self.turing_machine_label.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"AKTUALNIE ROZPATRYWANA RELACJA PRZEJ\u015aCIA", None))
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
        self.configuration_label.setText(QCoreApplication.translate("MainWindow", u"AKTUALNA KONFIGURACJA MASZYNY\n"
"", None))
    # retranslateUi

