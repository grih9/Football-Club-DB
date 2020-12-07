# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/playerMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import home

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
        self.profileButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.profileButton.setGeometry(QtCore.QRect(700, 95, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.profileButton.setFont(font)
        self.profileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profileButton.setStyleSheet(" color:rgb(255, 155, 130)")
        icon = QtGui.QIcon.fromTheme("NO")
        self.profileButton.setIcon(icon)
        self.profileButton.setIconSize(QtCore.QSize(300, 300))
        self.profileButton.setObjectName("profileButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 180, 801, 481))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255)")
        self.groupBox.setObjectName("groupBox")
        self.teamButton = QtWidgets.QCommandLinkButton(self.groupBox)
        self.teamButton.setGeometry(QtCore.QRect(200, 40, 421, 91))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.teamButton.setFont(font)
        self.teamButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.teamButton.setStyleSheet(" color: rgb(220, 220, 220);")
        icon = QtGui.QIcon.fromTheme("NO")
        self.teamButton.setIcon(icon)
        self.teamButton.setIconSize(QtCore.QSize(300, 300))
        self.teamButton.setObjectName("teamButton")
        self.trainingButton = QtWidgets.QCommandLinkButton(self.groupBox)
        self.trainingButton.setGeometry(QtCore.QRect(230, 150, 360, 91))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.trainingButton.setFont(font)
        self.trainingButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.trainingButton.setStyleSheet(" color: rgb(220, 220, 220);")
        icon = QtGui.QIcon.fromTheme("NO")
        self.trainingButton.setIcon(icon)
        self.trainingButton.setIconSize(QtCore.QSize(300, 300))
        self.trainingButton.setObjectName("trainingButton")
        self.calendarButton = QtWidgets.QCommandLinkButton(self.groupBox)
        self.calendarButton.setGeometry(QtCore.QRect(30, 260, 751, 91))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.calendarButton.setFont(font)
        self.calendarButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calendarButton.setStyleSheet(" color: rgb(220, 220, 220);")
        icon = QtGui.QIcon.fromTheme("NO")
        self.calendarButton.setIcon(icon)
        self.calendarButton.setIconSize(QtCore.QSize(300, 300))
        self.calendarButton.setObjectName("calendarButton")
        self.knowledgesButton = QtWidgets.QCommandLinkButton(self.groupBox)
        self.knowledgesButton.setGeometry(QtCore.QRect(230, 370, 381, 91))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.knowledgesButton.setFont(font)
        self.knowledgesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.knowledgesButton.setStyleSheet(" color: rgb(220, 220, 220);")
        icon = QtGui.QIcon.fromTheme("NO")
        self.knowledgesButton.setIcon(icon)
        self.knowledgesButton.setIconSize(QtCore.QSize(300, 300))
        self.knowledgesButton.setObjectName("knowledgesButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 100, 61, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/home/home.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.exitButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(890, 650, 101, 48))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet("color: rgb(255, 255, 255);")
        icon = QtGui.QIcon.fromTheme("NO")
        self.exitButton.setIcon(icon)
        self.exitButton.setObjectName("exitButton")
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
        self.profileButton.setText(_translate("MainWindow", "МОЙ ПРОФИЛЬ"))
        self.groupBox.setTitle(_translate("MainWindow", "МЕНЮ"))
        self.teamButton.setText(_translate("MainWindow", "МОЯ КОМАНДА"))
        self.trainingButton.setText(_translate("MainWindow", "ТРЕНИРОВКИ"))
        self.calendarButton.setText(_translate("MainWindow", "РАСПИСАНИЕ И РЕЗУЛЬТАТЫ"))
        self.knowledgesButton.setText(_translate("MainWindow", "БАЗА ЗНАНИЙ"))
        self.exitButton.setText(_translate("MainWindow", "ВЫХОД"))

