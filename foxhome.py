# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'foxhome.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(210, 170, 87, 22))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(260, 70, 85, 27))
        self.pushButton.setObjectName("pushButton")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menuFox_home = QtWidgets.QMenu(self.menubar)
        self.menuFox_home.setObjectName("menuFox_home")

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.actionGogo = QtWidgets.QAction(MainWindow)
        self.actionGogo.setObjectName("actionGogo")
        self.menuFox_home.addSeparator()
        self.menuFox_home.addSeparator()
        self.menuFox_home.addAction(self.actionGogo)
        self.menubar.addAction(self.menuFox_home.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menuFox_home.setTitle(_translate("MainWindow", "fox home"))
        self.actionGogo.setText(_translate("MainWindow", "gogo"))


import sys
app=QtWidgets.QApplication(sys.argv)
widget=QtWidgets.QWidget()
ui=Ui_MainWindow()
ui.setupUi(widget)
widget.show()
sys.exit(app.exec_())