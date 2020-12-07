# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/team.ui'
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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 150, 991, 521))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 237, 237);\n"
"color: rgb(0, 0, 0)")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.team = QtWidgets.QWidget()
        self.team.setObjectName("team")
        self.infoBox = QtWidgets.QGroupBox(self.team)
        self.infoBox.setGeometry(QtCore.QRect(10, 60, 971, 431))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.infoBox.setFont(font)
        self.infoBox.setStyleSheet("color: rgb(0, 0, 0)")
        self.infoBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.infoBox.setObjectName("infoBox")
        self.city = QtWidgets.QLabel(self.infoBox)
        self.city.setGeometry(QtCore.QRect(20, 110, 220, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.city.setFont(font)
        self.city.setObjectName("city")
        self.country = QtWidgets.QLabel(self.infoBox)
        self.country.setGeometry(QtCore.QRect(20, 50, 241, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.country.setFont(font)
        self.country.setObjectName("country")
        self.coach = QtWidgets.QLabel(self.infoBox)
        self.coach.setGeometry(QtCore.QRect(20, 170, 271, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.coach.setFont(font)
        self.coach.setObjectName("coach")
        self.coachLabel = QtWidgets.QLabel(self.infoBox)
        self.coachLabel.setGeometry(QtCore.QRect(250, 170, 581, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.coachLabel.setFont(font)
        self.coachLabel.setObjectName("coachLabel")
        self.stadium = QtWidgets.QLabel(self.infoBox)
        self.stadium.setGeometry(QtCore.QRect(20, 230, 131, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.stadium.setFont(font)
        self.stadium.setObjectName("stadium")
        self.cityLabel = QtWidgets.QLabel(self.infoBox)
        self.cityLabel.setGeometry(QtCore.QRect(120, 110, 391, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.cityLabel.setFont(font)
        self.cityLabel.setObjectName("cityLabel")
        self.stadiumLabel = QtWidgets.QLabel(self.infoBox)
        self.stadiumLabel.setGeometry(QtCore.QRect(150, 230, 661, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.stadiumLabel.setFont(font)
        self.stadiumLabel.setObjectName("stadiumLabel")
        self.countryLabel = QtWidgets.QLabel(self.infoBox)
        self.countryLabel.setGeometry(QtCore.QRect(140, 50, 411, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.countryLabel.setFont(font)
        self.countryLabel.setObjectName("countryLabel")
        self.owner = QtWidgets.QLabel(self.infoBox)
        self.owner.setGeometry(QtCore.QRect(20, 350, 151, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.owner.setFont(font)
        self.owner.setObjectName("owner")
        self.ownerLabel = QtWidgets.QLabel(self.infoBox)
        self.ownerLabel.setGeometry(QtCore.QRect(160, 350, 581, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.ownerLabel.setFont(font)
        self.ownerLabel.setText("")
        self.ownerLabel.setObjectName("ownerLabel")
        self.capacity = QtWidgets.QLabel(self.infoBox)
        self.capacity.setGeometry(QtCore.QRect(20, 290, 181, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.capacity.setFont(font)
        self.capacity.setObjectName("capacity")
        self.capacityLabel = QtWidgets.QLabel(self.infoBox)
        self.capacityLabel.setGeometry(QtCore.QRect(210, 290, 191, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.capacityLabel.setFont(font)
        self.capacityLabel.setObjectName("capacityLabel")
        self.label_3 = QtWidgets.QLabel(self.team)
        self.label_3.setGeometry(QtCore.QRect(730, 10, 241, 221))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/logo/logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.team, "")
        self.players = QtWidgets.QWidget()
        self.players.setObjectName("players")
        self.playersTabel = QtWidgets.QTableWidget(self.players)
        self.playersTabel.setGeometry(QtCore.QRect(10, 50, 971, 441))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.playersTabel.setFont(font)
        self.playersTabel.setGridStyle(QtCore.Qt.SolidLine)
        self.playersTabel.setObjectName("playersTabel")
        self.playersTabel.setColumnCount(7)
        self.playersTabel.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        item.setFont(font)
        self.playersTabel.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.playersTabel.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.playersTabel.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.playersTabel.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.playersTabel.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.playersTabel.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.playersTabel.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.playersTabel.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.playersTabel.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.playersTabel.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.playersTabel.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.playersTabel.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.playersTabel.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.playersTabel.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.playersTabel.setItem(0, 6, item)
        self.playersTabel.horizontalHeader().setDefaultSectionSize(135)
        self.playersTabel.horizontalHeader().setHighlightSections(False)
        self.playersTabel.horizontalHeader().setMinimumSectionSize(50)
        self.playersTabel.horizontalHeader().setSortIndicatorShown(False)
        self.playersTabel.verticalHeader().setDefaultSectionSize(35)
        self.playersTabel.verticalHeader().setHighlightSections(False)
        self.tabWidget.addTab(self.players, "")
        self.coaches = QtWidgets.QWidget()
        self.coaches.setObjectName("coaches")
        self.coachesTabel = QtWidgets.QTableWidget(self.coaches)
        self.coachesTabel.setGeometry(QtCore.QRect(10, 50, 971, 441))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.coachesTabel.setFont(font)
        self.coachesTabel.setGridStyle(QtCore.Qt.SolidLine)
        self.coachesTabel.setObjectName("coachesTabel")
        self.coachesTabel.setColumnCount(4)
        self.coachesTabel.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        item.setFont(font)
        self.coachesTabel.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.coachesTabel.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.coachesTabel.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.coachesTabel.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.coachesTabel.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.coachesTabel.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.coachesTabel.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.coachesTabel.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.coachesTabel.setItem(0, 3, item)
        self.coachesTabel.horizontalHeader().setDefaultSectionSize(135)
        self.coachesTabel.horizontalHeader().setMinimumSectionSize(50)
        self.coachesTabel.horizontalHeader().setSortIndicatorShown(False)
        self.coachesTabel.verticalHeader().setDefaultSectionSize(35)
        self.tabWidget.addTab(self.coaches, "")
        self.contracts = QtWidgets.QWidget()
        self.contracts.setObjectName("contracts")
        self.contractsTabel = QtWidgets.QTableWidget(self.contracts)
        self.contractsTabel.setGeometry(QtCore.QRect(10, 50, 971, 441))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.contractsTabel.setFont(font)
        self.contractsTabel.setGridStyle(QtCore.Qt.SolidLine)
        self.contractsTabel.setObjectName("contractsTabel")
        self.contractsTabel.setColumnCount(4)
        self.contractsTabel.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        item.setFont(font)
        self.contractsTabel.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.contractsTabel.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.contractsTabel.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.contractsTabel.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.contractsTabel.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.contractsTabel.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.contractsTabel.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.contractsTabel.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.contractsTabel.setItem(0, 3, item)
        self.contractsTabel.horizontalHeader().setDefaultSectionSize(135)
        self.contractsTabel.horizontalHeader().setMinimumSectionSize(50)
        self.contractsTabel.horizontalHeader().setSortIndicatorShown(False)
        self.contractsTabel.verticalHeader().setDefaultSectionSize(35)
        self.tabWidget.addTab(self.contracts, "")
        self.fans = QtWidgets.QWidget()
        self.fans.setObjectName("fans")
        self.fansTabel = QtWidgets.QTableWidget(self.fans)
        self.fansTabel.setGeometry(QtCore.QRect(10, 50, 970, 441))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.fansTabel.setFont(font)
        self.fansTabel.setGridStyle(QtCore.Qt.SolidLine)
        self.fansTabel.setObjectName("fansTabel")
        self.fansTabel.setColumnCount(3)
        self.fansTabel.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        item.setFont(font)
        self.fansTabel.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.fansTabel.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.fansTabel.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.fansTabel.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.fansTabel.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.fansTabel.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.fansTabel.setItem(0, 2, item)
        self.fansTabel.horizontalHeader().setDefaultSectionSize(135)
        self.fansTabel.horizontalHeader().setMinimumSectionSize(50)
        self.fansTabel.horizontalHeader().setSortIndicatorShown(False)
        self.fansTabel.verticalHeader().setDefaultSectionSize(35)
        self.tabWidget.addTab(self.fans, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backButton.setText(_translate("MainWindow", "НАЗАД"))
        self.label.setText(_translate("MainWindow", "МОЯ КОМАНДА"))
        self.infoBox.setTitle(_translate("MainWindow", "Манчестер Юнайтед"))
        self.city.setText(_translate("MainWindow", "Город:"))
        self.country.setText(_translate("MainWindow", "Страна:"))
        self.coach.setText(_translate("MainWindow", "Главный тренер:"))
        self.coachLabel.setText(_translate("MainWindow", "Уле Гуннар Сульшер (Босния и Герцеговина)"))
        self.stadium.setText(_translate("MainWindow", "Стадион:"))
        self.cityLabel.setText(_translate("MainWindow", "Манчестер"))
        self.stadiumLabel.setText(_translate("MainWindow", "Олд Траффорд (Манчестер)"))
        self.countryLabel.setText(_translate("MainWindow", "Босния и Герцеговина"))
        self.owner.setText(_translate("MainWindow", "Владелец:"))
        self.capacity.setText(_translate("MainWindow", "Вместимоcть:"))
        self.capacityLabel.setText(_translate("MainWindow", "80000"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.team), _translate("MainWindow", "Манчестер Юнайтед"))
        item = self.playersTabel.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер"))
        item = self.playersTabel.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.playersTabel.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Позиция"))
        item = self.playersTabel.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Страна"))
        item = self.playersTabel.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.playersTabel.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Рост"))
        item = self.playersTabel.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Вес"))
        __sortingEnabled = self.playersTabel.isSortingEnabled()
        self.playersTabel.setSortingEnabled(False)
        self.playersTabel.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.players), _translate("MainWindow", "Футболисты"))
        item = self.coachesTabel.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.coachesTabel.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Страна"))
        item = self.coachesTabel.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.coachesTabel.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Должность"))
        __sortingEnabled = self.coachesTabel.isSortingEnabled()
        self.coachesTabel.setSortingEnabled(False)
        self.coachesTabel.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.coaches), _translate("MainWindow", "Тренерский штаб"))
        item = self.contractsTabel.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер"))
        item = self.contractsTabel.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.contractsTabel.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Зарплата"))
        item = self.contractsTabel.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата окончания"))
        __sortingEnabled = self.contractsTabel.isSortingEnabled()
        self.contractsTabel.setSortingEnabled(False)
        self.contractsTabel.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.contracts), _translate("MainWindow", "Контракты"))
        item = self.fansTabel.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.fansTabel.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.fansTabel.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Пол"))
        __sortingEnabled = self.fansTabel.isSortingEnabled()
        self.fansTabel.setSortingEnabled(False)
        self.fansTabel.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fans), _translate("MainWindow", "Болельщики"))

