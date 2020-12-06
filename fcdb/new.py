# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
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
"    background-image: url(C:/git/fcdb/Football-Club-DB/fcdb/back.jpg);\n"
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
        self.enterButton.setGeometry(QtCore.QRect(250, 480, 451, 61))
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
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 100, 275, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
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
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 420, 255, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(330, 370, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(220, 220, 220);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 420, 255, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(590, 420, 255, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(20, 250, 275, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.dateEdit.setFont(font)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2006, 12, 11), QtCore.QTime(23, 59, 59)))
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1970, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMaximumDate(QtCore.QDate(2006, 12, 11))
        self.dateEdit.setMinimumDate(QtCore.QDate(1970, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
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
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(320, 100, 275, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(360, 50, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(220, 220, 220);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(640, 100, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(640, 50, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(220, 220, 220);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(660, 200, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.spinBox.setFont(font)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMinimum(150)
        self.spinBox.setMaximum(220)
        self.spinBox.setProperty("value", 180)
        self.spinBox.setObjectName("spinBox")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setGeometry(QtCore.QRect(660, 300, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox.setMinimum(50.0)
        self.doubleSpinBox.setMaximum(120.0)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setProperty("value", 80.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
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
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(320, 300, 275, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
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
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(565, 420, 41, 41))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(410, 200, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(370, 160, 170, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(17)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(220, 220, 220);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.enterButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.enterButton_2.setGeometry(QtCore.QRect(900, 580, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.enterButton_2.setFont(font)
        self.enterButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enterButton_2.setStyleSheet(" color: rgb(255, 129, 129)")
        icon = QtGui.QIcon.fromTheme("NO")
        self.enterButton_2.setIcon(icon)
        self.enterButton_2.setIconSize(QtCore.QSize(300, 300))
        self.enterButton_2.setObjectName("enterButton_2")
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
        self.enterButton.setText(_translate("MainWindow", "СОЗДАТЬ АККАУНТ"))
        self.label.setText(_translate("MainWindow", "ИМЯ"))
        self.label_2.setText(_translate("MainWindow", "ЛОГИН"))
        self.label_3.setText(_translate("MainWindow", "ПАРОЛЬ"))
        self.label_4.setText(_translate("MainWindow", "ДАТА РОЖДЕНИЯ"))
        self.label_5.setText(_translate("MainWindow", "ПОДТВЕРЖДЕНИЕ"))
        self.label_6.setText(_translate("MainWindow", "ФАМИЛИЯ"))
        self.comboBox.setPlaceholderText(_translate("MainWindow", "Позиция"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Вратарь"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Защитник"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Полузащитник"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Нападающий"))
        self.label_7.setText(_translate("MainWindow", "ПОЗИЦИЯ"))
        self.label_8.setText(_translate("MainWindow", "РОСТ"))
        self.label_9.setText(_translate("MainWindow", "ВЕС"))
        self.label_10.setText(_translate("MainWindow", "СТРАНА"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "99"))
        self.label_12.setText(_translate("MainWindow", "НОМЕР"))
        self.enterButton_2.setText(_translate("MainWindow", "НАЗАД"))
