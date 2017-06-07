# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'touchUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import dbReaderWriter


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 690)
        MainWindow.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.zaisituButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.zaisituButton.sizePolicy().hasHeightForWidth())
        self.zaisituButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(45)
        self.zaisituButton.setFont(font)
        self.zaisituButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.zaisituButton.setStyleSheet("QPushButton{\n"
                                         "    background-color: rgb(33, 150, 243);\n"
                                         "    color: rgb(250, 250, 250);\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background-color: rgb(13, 71, 161);\n"
                                         "}")
        self.zaisituButton.setCheckable(False)
        self.zaisituButton.setChecked(False)
        self.zaisituButton.setAutoRepeatDelay(296)
        self.zaisituButton.setObjectName("zaisituButton")
        self.horizontalLayout_3.addWidget(self.zaisituButton)
        self.gakunai_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gakunai_Button.sizePolicy().hasHeightForWidth())
        self.gakunai_Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(45)
        self.gakunai_Button.setFont(font)
        self.gakunai_Button.setStyleSheet("QPushButton{\n"
                                          "    background-color: rgb(76, 175, 80);\n"
                                          "    color: rgb(250, 250, 250);\n"
                                          "}\n"
                                          "QPushButton:pressed{\n"
                                          "    \n"
                                          "    background-color: rgb(0, 77, 64);\n"
                                          "}")
        self.gakunai_Button.setObjectName("gakunai_Button")
        self.horizontalLayout_3.addWidget(self.gakunai_Button)
        self.kitaku_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.kitaku_Button.sizePolicy().hasHeightForWidth())
        self.kitaku_Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(45)
        self.kitaku_Button.setFont(font)
        self.kitaku_Button.setStyleSheet("QPushButton{\n"
                                         "    background-color: rgb(126, 87, 194);\n"
                                         "    color: rgb(250, 250, 250);\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    \n"
                                         "    background-color: rgb(49, 27, 146);\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.kitaku_Button.setAutoDefault(False)
        self.kitaku_Button.setDefault(False)
        self.kitaku_Button.setFlat(False)
        self.kitaku_Button.setObjectName("kitaku_Button")
        self.horizontalLayout_3.addWidget(self.kitaku_Button)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.soonBack_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.soonBack_Button.sizePolicy().hasHeightForWidth())
        self.soonBack_Button.setSizePolicy(sizePolicy)
        self.soonBack_Button.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(24)
        self.soonBack_Button.setFont(font)
        self.soonBack_Button.setStyleSheet("QPushButton{\n"
                                           "background-color: rgb(255, 87, 34);\n"
                                           "color: rgb(250, 250, 250);\n"
                                           "}\n"
                                           "QPushButton:pressed{\n"
                                           "    \n"
                                           "    background-color: rgb(191, 54, 12);\n"
                                           "}")
        self.soonBack_Button.setObjectName("soonBack_Button")
        self.verticalLayout.addWidget(self.soonBack_Button)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.soonBack_Button.clicked['bool'].connect(
            lambda: self.output_code(self.soonBack_Button, "3"))
        self.zaisituButton.clicked['bool'].connect(
            lambda: self.output_code(self.zaisituButton, "0"))
        self.gakunai_Button.clicked['bool'].connect(
            lambda: self.output_code(self.gakunai_Button, "1"))
        self.kitaku_Button.clicked['bool'].connect(
            lambda: self.output_code(self.kitaku_Button, "2"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.zaisituButton.setText(_translate("MainWindow", "在室"))
        self.gakunai_Button.setText(_translate("MainWindow", "学内"))
        self.kitaku_Button.setText(_translate("MainWindow", "帰宅"))
        self.soonBack_Button.setText(_translate("MainWindow", "すぐ戻る"))

    def output_code(self, Button, code):
        Button.repaint
        rw = dbReaderWriter.ReaderWriter()
        card_id = subprocess.check_output("./cardReader.sh")
        rw.ChangeCondition(card_id, code)
        rw.Close()
