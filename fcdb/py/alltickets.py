# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/allTickets.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import ball
import eye
import home
import logo

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1016, 755)
        MainWindow.setMinimumSize(QtCore.QSize(1016, 755))
        MainWindow.setMaximumSize(QtCore.QSize(1016, 755))
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QWidget#centralwidget {\n"
"    background-image: url(C:/git/fcdb/Football-Club-DB/fcdb/resources/back.jpg);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(890, 670, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 50, 541, 121))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(220, 220, 220);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(840, 75, 101, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/ball/ball.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.tickets = QtWidgets.QTabWidget(self.centralwidget)
        self.tickets.setGeometry(QtCore.QRect(10, 150, 991, 511))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.tickets.setFont(font)
        self.tickets.setStyleSheet("background-color: rgb(255, 237, 237);\n"
"color: rgb(0, 0, 0)")
        self.tickets.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tickets.setTabBarAutoHide(True)
        self.tickets.setObjectName("tickets")
        self.upcoming = QtWidgets.QWidget()
        self.upcoming.setObjectName("upcoming")
        self.noTicketsLabel = QtWidgets.QLabel(self.upcoming)
        self.noTicketsLabel.setGeometry(QtCore.QRect(220, 190, 551, 81))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(25)
        self.noTicketsLabel.setFont(font)
        self.noTicketsLabel.setStyleSheet("color: rgb(255, 129, 129);")
        self.noTicketsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noTicketsLabel.setObjectName("noTicketsLabel")
        self.ticketsTable = QtWidgets.QTableWidget(self.upcoming)
        self.ticketsTable.setGeometry(QtCore.QRect(10, 20, 971, 451))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.ticketsTable.setFont(font)
        self.ticketsTable.setGridStyle(QtCore.Qt.SolidLine)
        self.ticketsTable.setObjectName("ticketsTable")
        self.ticketsTable.setColumnCount(9)
        self.ticketsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ticketsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ticketsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ticketsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ticketsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ticketsTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ticketsTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ticketsTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ticketsTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ticketsTable.setHorizontalHeaderItem(8, item)
        self.ticketsTable.horizontalHeader().setDefaultSectionSize(135)
        self.ticketsTable.horizontalHeader().setHighlightSections(False)
        self.ticketsTable.horizontalHeader().setMinimumSectionSize(50)
        self.ticketsTable.horizontalHeader().setSortIndicatorShown(False)
        self.ticketsTable.verticalHeader().setDefaultSectionSize(35)
        self.ticketsTable.verticalHeader().setHighlightSections(False)
        self.ticketsTable.raise_()
        self.noTicketsLabel.raise_()
        self.tickets.addTab(self.upcoming, "")
        self.history = QtWidgets.QWidget()
        self.history.setObjectName("history")
        self.noTicketsLabel2 = QtWidgets.QLabel(self.history)
        self.noTicketsLabel2.setGeometry(QtCore.QRect(150, 210, 671, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(25)
        self.noTicketsLabel2.setFont(font)
        self.noTicketsLabel2.setStyleSheet("color: rgb(255, 129, 129);")
        self.noTicketsLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.noTicketsLabel2.setObjectName("noTicketsLabel2")
        self.historyTable = QtWidgets.QTableWidget(self.history)
        self.historyTable.setGeometry(QtCore.QRect(10, 20, 971, 451))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.historyTable.setFont(font)
        self.historyTable.setGridStyle(QtCore.Qt.SolidLine)
        self.historyTable.setObjectName("historyTable")
        self.historyTable.setColumnCount(9)
        self.historyTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.historyTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.historyTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.historyTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.historyTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.historyTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.historyTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.historyTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.historyTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.historyTable.setHorizontalHeaderItem(8, item)
        self.historyTable.horizontalHeader().setDefaultSectionSize(135)
        self.historyTable.horizontalHeader().setHighlightSections(False)
        self.historyTable.horizontalHeader().setMinimumSectionSize(50)
        self.historyTable.horizontalHeader().setSortIndicatorShown(False)
        self.historyTable.verticalHeader().setDefaultSectionSize(35)
        self.historyTable.verticalHeader().setHighlightSections(False)
        self.historyTable.raise_()
        self.noTicketsLabel2.raise_()
        self.tickets.addTab(self.history, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tickets.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backButton.setText(_translate("MainWindow", "НАЗАД"))
        self.label.setText(_translate("MainWindow", "БИЛЕТЫ"))
        self.noTicketsLabel.setText(_translate("MainWindow", "Проданных билетов нет!"))
        item = self.ticketsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Владелец"))
        item = self.ticketsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.ticketsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Стадион"))
        item = self.ticketsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Соперник"))
        item = self.ticketsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Турнир"))
        item = self.ticketsTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Сектор"))
        item = self.ticketsTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Ряд"))
        item = self.ticketsTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Место"))
        item = self.ticketsTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Цена"))
        self.tickets.setTabText(self.tickets.indexOf(self.upcoming), _translate("MainWindow", "Билеты"))
        self.noTicketsLabel2.setText(_translate("MainWindow", "Проданных билетов нет!"))
        item = self.historyTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Владелец"))
        item = self.historyTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.historyTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Стадион"))
        item = self.historyTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Соперник"))
        item = self.historyTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Турнир"))
        item = self.historyTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Сектор"))
        item = self.historyTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Ряд"))
        item = self.historyTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Место"))
        item = self.historyTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Цена"))
        self.tickets.setTabText(self.tickets.indexOf(self.history), _translate("MainWindow", "История"))

