# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mbedOven.ui'
#
# Created: Mon Mar 23 10:31:00 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Rb Oven Control"))
        MainWindow.resize(230, 122)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.AlimOn = QtGui.QPushButton(self.centralwidget)
        self.AlimOn.setGeometry(QtCore.QRect(10, 0, 96, 31))
        self.AlimOn.setObjectName(_fromUtf8("AlimOn"))
        self.AlimOff = QtGui.QPushButton(self.centralwidget)
        self.AlimOff.setGeometry(QtCore.QRect(120, 0, 96, 31))
        self.AlimOff.setObjectName(_fromUtf8("AlimOff"))
        self.CurrentValueTxt = QtGui.QLabel(self.centralwidget)
        self.CurrentValueTxt.setGeometry(QtCore.QRect(10, 40, 101, 21))
        self.CurrentValueTxt.setObjectName(_fromUtf8("CurrentValueTxt"))
        self.CurrentValueValue = QtGui.QLabel(self.centralwidget)
        self.CurrentValueValue.setGeometry(QtCore.QRect(130, 40, 65, 21))
        self.CurrentValueValue.setObjectName(_fromUtf8("CurrentValueValue"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 230, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Rb Oven Control", None))
        self.AlimOn.setText(_translate("MainWindow", "On", None))
        self.AlimOff.setText(_translate("MainWindow", "Off", None))
        self.CurrentValueTxt.setText(_translate("MainWindow", "Current value :", None))
        self.CurrentValueValue.setText(_translate("MainWindow", "0.0", None))

