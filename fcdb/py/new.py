# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/new.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import eye

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
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 150, 861, 551))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox#groupBox {\n"
"    color: rgb(220, 220, 220);\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.enterButton = QtWidgets.QCommandLinkButton(self.groupBox)
        self.enterButton.setGeometry(QtCore.QRect(250, 480, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(23)
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
        self.nameLine = QtWidgets.QLineEdit(self.groupBox)
        self.nameLine.setGeometry(QtCore.QRect(20, 100, 275, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.nameLine.setFont(font)
        self.nameLine.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLine.setObjectName("nameLine")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 50, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(220, 220, 220);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 370, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(220, 220, 220);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.loginLine = QtWidgets.QLineEdit(self.groupBox)
        self.loginLine.setGeometry(QtCore.QRect(20, 420, 255, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.loginLine.setFont(font)
        self.loginLine.setMaxLength(20)
        self.loginLine.setAlignment(QtCore.Qt.AlignCenter)
        self.loginLine.setObjectName("loginLine")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(330, 370, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(220, 220, 220);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.passwordLine = QtWidgets.QLineEdit(self.groupBox)
        self.passwordLine.setGeometry(QtCore.QRect(300, 420, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.passwordLine.setFont(font)
        self.passwordLine.setMaxLength(20)
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordLine.setObjectName("passwordLine")
        self.passwordConfirmLine = QtWidgets.QLineEdit(self.groupBox)
        self.passwordConfirmLine.setGeometry(QtCore.QRect(595, 420, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.passwordConfirmLine.setFont(font)
        self.passwordConfirmLine.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.passwordConfirmLine.setMaxLength(20)
        self.passwordConfirmLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordConfirmLine.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordConfirmLine.setObjectName("passwordConfirmLine")
        self.birthdayLine = QtWidgets.QDateEdit(self.groupBox)
        self.birthdayLine.setGeometry(QtCore.QRect(20, 250, 275, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.birthdayLine.setFont(font)
        self.birthdayLine.setAlignment(QtCore.Qt.AlignCenter)
        self.birthdayLine.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2006, 12, 11), QtCore.QTime(23, 59, 59)))
        self.birthdayLine.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1970, 1, 1), QtCore.QTime(0, 0, 0)))
        self.birthdayLine.setMaximumDate(QtCore.QDate(2006, 12, 11))
        self.birthdayLine.setMinimumDate(QtCore.QDate(1970, 1, 1))
        self.birthdayLine.setCalendarPopup(True)
        self.birthdayLine.setObjectName("birthdayLine")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(11, 200, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(220, 220, 220);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(580, 370, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(220, 220, 220);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.surnameLine = QtWidgets.QLineEdit(self.groupBox)
        self.surnameLine.setGeometry(QtCore.QRect(320, 100, 275, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.surnameLine.setFont(font)
        self.surnameLine.setAlignment(QtCore.Qt.AlignCenter)
        self.surnameLine.setObjectName("surnameLine")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(360, 50, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(220, 220, 220);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.positionBox = QtWidgets.QComboBox(self.groupBox)
        self.positionBox.setGeometry(QtCore.QRect(640, 100, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.positionBox.setFont(font)
        self.positionBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.positionBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.positionBox.setObjectName("positionBox")
        self.positionBox.addItem("")
        self.positionBox.setItemText(0, "")
        self.positionBox.addItem("")
        self.positionBox.addItem("")
        self.positionBox.addItem("")
        self.positionBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(640, 50, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(220, 220, 220);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.height = QtWidgets.QSpinBox(self.groupBox)
        self.height.setGeometry(QtCore.QRect(660, 200, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.height.setFont(font)
        self.height.setAlignment(QtCore.Qt.AlignCenter)
        self.height.setMinimum(150)
        self.height.setMaximum(220)
        self.height.setProperty("value", 180)
        self.height.setObjectName("height")
        self.weightLine = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.weightLine.setGeometry(QtCore.QRect(660, 300, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.weightLine.setFont(font)
        self.weightLine.setAlignment(QtCore.Qt.AlignCenter)
        self.weightLine.setMinimum(50.0)
        self.weightLine.setMaximum(120.0)
        self.weightLine.setSingleStep(0.1)
        self.weightLine.setProperty("value", 80.0)
        self.weightLine.setObjectName("weightLine")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(641, 160, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(220, 220, 220);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(629, 260, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(220, 220, 220);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.nationLine = QtWidgets.QLineEdit(self.groupBox)
        self.nationLine.setGeometry(QtCore.QRect(320, 300, 275, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.nationLine.setFont(font)
        self.nationLine.setText("")
        self.nationLine.setAlignment(QtCore.Qt.AlignCenter)
        self.nationLine.setObjectName("nationLine")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(360, 255, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(220, 220, 220);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(558, 390, 31, 31))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/eye/eyepng.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.showPasswordCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.showPasswordCheckBox.setGeometry(QtCore.QRect(565, 420, 21, 40))
        self.showPasswordCheckBox.setText("")
        self.showPasswordCheckBox.setObjectName("showPasswordCheckBox")
        self.numberBox = QtWidgets.QComboBox(self.groupBox)
        self.numberBox.setGeometry(QtCore.QRect(410, 200, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.numberBox.setFont(font)
        self.numberBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.numberBox.setObjectName("numberBox")
        self.numberBox.addItem("")
        self.numberBox.setItemText(0, "")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(370, 160, 170, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(17)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(220, 220, 220);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.dontCreateCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.dontCreateCheckBox.setGeometry(QtCore.QRect(30, 320, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.dontCreateCheckBox.setFont(font)
        self.dontCreateCheckBox.setStyleSheet("color: rgb(220, 220, 220)")
        self.dontCreateCheckBox.setObjectName("dontCreateCheckBox")
        self.backButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(900, 580, 111, 51))
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
        self.groupBox.setTitle(_translate("MainWindow", "НОВЫЙ ИГРОК"))
        self.enterButton.setText(_translate("MainWindow", "ДОБАВИТЬ ИГРОКА"))
        self.label.setText(_translate("MainWindow", "ИМЯ"))
        self.label_2.setText(_translate("MainWindow", "ЛОГИН"))
        self.label_3.setText(_translate("MainWindow", "ПАРОЛЬ"))
        self.label_4.setText(_translate("MainWindow", "ДАТА РОЖДЕНИЯ"))
        self.label_5.setText(_translate("MainWindow", "ПОДТВЕРЖДЕНИЕ"))
        self.label_6.setText(_translate("MainWindow", "ФАМИЛИЯ"))
        self.positionBox.setPlaceholderText(_translate("MainWindow", "Позиция"))
        self.positionBox.setItemText(1, _translate("MainWindow", "Вратарь"))
        self.positionBox.setItemText(2, _translate("MainWindow", "Защитник"))
        self.positionBox.setItemText(3, _translate("MainWindow", "Полузащитник"))
        self.positionBox.setItemText(4, _translate("MainWindow", "Нападающий"))
        self.label_7.setText(_translate("MainWindow", "ПОЗИЦИЯ"))
        self.label_8.setText(_translate("MainWindow", "РОСТ"))
        self.label_9.setText(_translate("MainWindow", "ВЕС"))
        self.label_10.setText(_translate("MainWindow", "СТРАНА"))
        self.label_12.setText(_translate("MainWindow", "НОМЕР"))
        self.dontCreateCheckBox.setText(_translate("MainWindow", "Не создавать аккаунт"))
        self.backButton.setText(_translate("MainWindow", "НАЗАД"))
