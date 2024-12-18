# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Программы\Программирование\Python\С телефона\Копии для редактирования на компе\Кубик\Интерфейс с кнопками\Кнопки 1.ui',
# licensing of 'E:\Программы\Программирование\Python\С телефона\Копии для редактирования на компе\Кубик\Интерфейс с кнопками\Кнопки 1.ui' applies.
#
# Created: Thu Sep 12 01:26:27 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.setEnabled(True)
        Window.resize(231, 246)
        Window.setStyleSheet("QWidget{\n"
"  background-color: black;\n"
"}\n"
"\n"
"QPushButton{\n"
"  background-color: silver;\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: silver;\n"
"}")
        self.gridLayoutWidget = QtWidgets.QWidget(Window)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 90, 151, 104))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.U = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.U.setMouseTracking(False)
        self.U.setStyleSheet("QPushButton{\n"
"  background-color: yellow;\n"
"  width: 45px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: yellow;\n"
"}")
        self.U.setObjectName("U")
        self.gridLayout_2.addWidget(self.U, 0, 0, 1, 1)
        self.B = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B.setStyleSheet("QPushButton{\n"
"  background-color: green;\n"
"  width: 45px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: green;\n"
"}")
        self.B.setObjectName("B")
        self.gridLayout_2.addWidget(self.B, 1, 1, 1, 1)
        self.D = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.D.setStyleSheet("QPushButton{\n"
"  background-color: white;\n"
"  width: 45px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: white;\n"
"}")
        self.D.setObjectName("D")
        self.gridLayout_2.addWidget(self.D, 1, 0, 1, 1)
        self.S = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.S.setStyleSheet("QPushButton{\n"
"  background-color: blue;\n"
"  width: 45px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: blue;\n"
"}")
        self.S.setObjectName("S")
        self.gridLayout_2.addWidget(self.S, 2, 1, 1, 1)
        self.F = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.F.setStyleSheet("QPushButton{\n"
"  background-color: blue;\n"
"  width: 45px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: blue;\n"
"}")
        self.F.setObjectName("F")
        self.gridLayout_2.addWidget(self.F, 0, 1, 1, 1)
        self.E = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.E.setStyleSheet("QPushButton{\n"
"  background-color: yellow;\n"
"  width: 45px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: yellow;\n"
"}")
        self.E.setObjectName("E")
        self.gridLayout_2.addWidget(self.E, 2, 0, 1, 1)
        self.R = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.R.setEnabled(True)
        self.R.setStyleSheet("QPushButton{\n"
"  background-color: red;\n"
"  width: 45px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: red;\n"
"}")
        self.R.setObjectName("R")
        self.gridLayout_2.addWidget(self.R, 0, 2, 1, 1)
        self.L = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.L.setStyleSheet("QPushButton{\n"
"  background-color: orange;\n"
"  width: 45px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: orange;\n"
"}")
        self.L.setObjectName("L")
        self.gridLayout_2.addWidget(self.L, 1, 2, 1, 1)
        self.M = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.M.setStyleSheet("QPushButton{\n"
"  background-color: red;\n"
"  width: 45px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: red;\n"
"}")
        self.M.setObjectName("M")
        self.gridLayout_2.addWidget(self.M, 2, 2, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(Window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 52, 104))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Backspace = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Backspace.setStyleSheet("QPushButton{\n"
"  background-color: gray;\n"
"  width: 50px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: silver;\n"
"}")
        self.Backspace.setCheckable(False)
        self.Backspace.setObjectName("Backspace")
        self.verticalLayout.addWidget(self.Backspace)
        self.Enter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Enter.setStyleSheet("QPushButton{\n"
"  background-color: gray;\n"
"  width: 50px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: silver;\n"
"}")
        self.Enter.setObjectName("Enter")
        self.verticalLayout.addWidget(self.Enter)
        self.Clear_all = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Clear_all.setStyleSheet("QPushButton{\n"
"  background-color: gray;\n"
"  width: 50px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: silver;\n"
"}")
        self.Clear_all.setObjectName("Clear_all")
        self.verticalLayout.addWidget(self.Clear_all)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Window)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 50, 161, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.x2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.x2.setStyleSheet("QPushButton{\n"
"  background-color: gray;\n"
"  width: 35px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: silver;\n"
"}")
        self.x2.setObjectName("x2")
        self.horizontalLayout.addWidget(self.x2)
        self.Apostrophe = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Apostrophe.setStyleSheet("QPushButton{\n"
"  background-color: gray;\n"
"  width: 35px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: silver;\n"
"}")
        self.Apostrophe.setObjectName("Apostrophe")
        self.horizontalLayout.addWidget(self.Apostrophe)
        self.bra = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.bra.setStyleSheet("QPushButton{\n"
"  background-color: gray;\n"
"  width: 35px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: silver;\n"
"}")
        self.bra.setObjectName("bra")
        self.horizontalLayout.addWidget(self.bra)
        self.ket = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ket.setStyleSheet("QPushButton{\n"
"  background-color: gray;\n"
"  width: 35px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: silver;\n"
"}")
        self.ket.setObjectName("ket")
        self.horizontalLayout.addWidget(self.ket)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Window)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 200, 174, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Cut = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Cut.setStyleSheet("QPushButton{\n"
"  background-color: gray;\n"
"  width: 55px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: silver;\n"
"}")
        self.Cut.setObjectName("Cut")
        self.horizontalLayout_2.addWidget(self.Cut)
        self.Copy = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Copy.setStyleSheet("QPushButton{\n"
"  background-color: gray;\n"
"  width: 55px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: silver;\n"
"}")
        self.Copy.setObjectName("Copy")
        self.horizontalLayout_2.addWidget(self.Copy)
        self.Paste = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Paste.setStyleSheet("QPushButton{\n"
"  background-color: gray;\n"
"  width: 50px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: silver;\n"
"}")
        self.Paste.setObjectName("Paste")
        self.horizontalLayout_2.addWidget(self.Paste)
        self.lineEdit = QtWidgets.QLineEdit(Window)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 211, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"  background-color: silver;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        Window.setWindowTitle(QtWidgets.QApplication.translate("Window", "Cube", None, -1))
        self.U.setText(QtWidgets.QApplication.translate("Window", "U", None, -1))
        self.B.setText(QtWidgets.QApplication.translate("Window", "B", None, -1))
        self.D.setText(QtWidgets.QApplication.translate("Window", "D", None, -1))
        self.S.setText(QtWidgets.QApplication.translate("Window", "S", None, -1))
        self.F.setText(QtWidgets.QApplication.translate("Window", "F", None, -1))
        self.E.setText(QtWidgets.QApplication.translate("Window", "E", None, -1))
        self.R.setText(QtWidgets.QApplication.translate("Window", "R", None, -1))
        self.L.setText(QtWidgets.QApplication.translate("Window", "L", None, -1))
        self.M.setText(QtWidgets.QApplication.translate("Window", "M", None, -1))
        self.Backspace.setText(QtWidgets.QApplication.translate("Window", "←", None, -1))
        self.Enter.setText(QtWidgets.QApplication.translate("Window", "Enter", None, -1))
        self.Clear_all.setText(QtWidgets.QApplication.translate("Window", "Clear", None, -1))
        self.x2.setText(QtWidgets.QApplication.translate("Window", "x2", None, -1))
        self.Apostrophe.setText(QtWidgets.QApplication.translate("Window", "\'", None, -1))
        self.bra.setText(QtWidgets.QApplication.translate("Window", "(", None, -1))
        self.ket.setText(QtWidgets.QApplication.translate("Window", ")", None, -1))
        self.Cut.setText(QtWidgets.QApplication.translate("Window", "Cut", None, -1))
        self.Copy.setText(QtWidgets.QApplication.translate("Window", "Copy", None, -1))
        self.Paste.setText(QtWidgets.QApplication.translate("Window", "Paste", None, -1))


