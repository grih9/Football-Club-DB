# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/contract.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import eye
import logo


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 674)
        MainWindow.setMinimumSize(QtCore.QSize(487, 674))
        MainWindow.setMaximumSize(QtCore.QSize(487, 674))
        MainWindow.setStyleSheet("QWidget#centralwidget {\n"
"    background-color: rgb(182, 0, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 150, 441, 451))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox#groupBox {\n"
"    color: rgb(220, 220, 220);\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.createAccountButton = QtWidgets.QCommandLinkButton(self.groupBox)
        self.createAccountButton.setGeometry(QtCore.QRect(50, 370, 381, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.createAccountButton.setFont(font)
        self.createAccountButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.createAccountButton.setStyleSheet(" color: rgb(255, 129, 129)")
        icon = QtGui.QIcon.fromTheme("NO")
        self.createAccountButton.setIcon(icon)
        self.createAccountButton.setIconSize(QtCore.QSize(300, 300))
        self.createAccountButton.setObjectName("createAccountButton")
        self.expireDate = QtWidgets.QDateEdit(self.groupBox)
        self.expireDate.setGeometry(QtCore.QRect(80, 260, 275, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.expireDate.setFont(font)
        self.expireDate.setAlignment(QtCore.Qt.AlignCenter)
        self.expireDate.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2040, 12, 31), QtCore.QTime(0, 0, 0)))
        self.expireDate.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 12, 31), QtCore.QTime(0, 0, 0)))
        self.expireDate.setMinimumDate(QtCore.QDate(2020, 12, 31))
        self.expireDate.setCalendarPopup(True)
        self.expireDate.setObjectName("expireDate")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(70, 210, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(220, 220, 220);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(90, 70, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(220, 220, 220);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.salary = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.salary.setGeometry(QtCore.QRect(140, 120, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.salary.setFont(font)
        self.salary.setAlignment(QtCore.Qt.AlignCenter)
        self.salary.setMinimum(0.01)
        self.salary.setMaximum(40.0)
        self.salary.setSingleStep(0.01)
        self.salary.setObjectName("salary")
        self.backButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(340, 100, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setStyleSheet(" color: rgb(255, 129, 129)")
        icon = QtGui.QIcon.fromTheme("NO")
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(300, 300))
        self.backButton.setObjectName("backButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 131, 131))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/logo/logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 487, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "КОНТРАКТ"))
        self.createAccountButton.setText(_translate("MainWindow", "ПОДПИСАТЬ КОНТРАКТ"))
        self.label_4.setText(_translate("MainWindow", "ДАТА ОКОНЧАНИЯ"))
        self.label_6.setText(_translate("MainWindow", "ЗАРПЛАТА (млн €/год"))
        self.backButton.setText(_translate("MainWindow", "НАЗАД"))
