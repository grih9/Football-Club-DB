# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1016, 755)
        MainWindow.setMinimumSize(QtCore.QSize(1016, 755))
        MainWindow.setMaximumSize(QtCore.QSize(1016, 755))
        MainWindow.setStyleSheet("QWidget#centralwidget {\n"
"    background-image: url(C:/git/fcdb/Football-Club-DB/fcdb/resources/back.jpg);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(850, 630, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
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
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(320, 220, 381, 431))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.loginLine = QtWidgets.QLineEdit(self.groupBox)
        self.loginLine.setGeometry(QtCore.QRect(50, 70, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.loginLine.setFont(font)
        self.loginLine.setAlignment(QtCore.Qt.AlignCenter)
        self.loginLine.setObjectName("loginLine")
        self.passwordLine = QtWidgets.QLineEdit(self.groupBox)
        self.passwordLine.setGeometry(QtCore.QRect(50, 200, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.passwordLine.setFont(font)
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordLine.setObjectName("passwordLine")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(90, 15, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(220, 220, 220);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(90, 145, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(220, 220, 220);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.enterButton = QtWidgets.QCommandLinkButton(self.groupBox)
        self.enterButton.setGeometry(QtCore.QRect(55, 310, 291, 91))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.enterButton.setFont(font)
        self.enterButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enterButton.setStyleSheet(" color: rgb(255, 129, 129)")
        icon = QtGui.QIcon.fromTheme("NO")
        self.enterButton.setIcon(icon)
        self.enterButton.setIconSize(QtCore.QSize(300, 300))
        self.enterButton.setObjectName("enterButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backButton.setText(_translate("MainWindow", "НАЗАД"))
        self.label.setText(_translate("MainWindow", "ЛОГИН"))
        self.label_2.setText(_translate("MainWindow", "ПАРОЛЬ"))
        self.enterButton.setText(_translate("MainWindow", "ВОЙТИ"))
