from team import Ui_MainWindow as teamMain
from PyQt5 import QtWidgets, QtCore
import menuFanWindow
import playerMenuWindow
import coachMenuWindow
import managerMenuWindow
import properties
import sql
import injuryWindow

class teamWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = teamMain()
        self.ui.setupUi(self)
        header = self.ui.playersTabel.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header = self.ui.coachesTabel.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header = self.ui.contractsTabel.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header = self.ui.fansTabel.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.setWindowTitle("Команда")

        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.backButton.clicked.connect(self.backButton_clicked)
        self.ui.tabWidget.currentChanged.connect(self.tabChangedHandler)
        self.ui.injJournalButton.clicked.connect(self.injButtonHandler)
        self.ui.maleRadio.clicked.connect(self.maleRadioHandler)
        self.ui.femaleRadio.clicked.connect(self.femaleRadioHandler)
        self.ui.youngRadio.clicked.connect(self.youngRadioHandler)
        self.ui.resetButton.clicked.connect(self.resetButton_clicked)
        self.ui.allPlayersRadio.clicked.connect(self.allPlayersRadioHandler)
        self.ui.defRadio.clicked.connect(self.defRadioHandler)
        self.ui.midRadio.clicked.connect(self.midRadioHandler)
        self.ui.forwardRadio.clicked.connect(self.forwardRadioHandler)
        self.ui.goalkeepersRadio.clicked.connect(self.goalkeepersRadioHandler)
        self.ui.injCheckBox.stateChanged.connect(self.injCheckBoxHandler)

        self.db = sql.Sql("football_club")
        self.db.cursor.execute(
            "SELECT Команды.Страна, Команды.Город, Стадионы.Название, Стадионы.Вместимость, Стадионы.Город, Тренеры_и_персонал.ФИО,"
            "Тренеры_и_персонал.Национальность, Руководство.ФИО, Руководство.Национальность"
            " FROM Команды "
            "join Стадионы on Стадионы.ID_стадиона = Команды.ID_стадиона "
            "join Тренеры_и_персонал on Тренеры_и_персонал.ID_cпециалиста=ID_главного_тренера "
            "join Руководство on Руководство.ID_владельца = Команды.ID_владельца "
            "where  Команды.Команда ='" + str("Манчестер Юнайтед") + "'")
        row = self.db.cursor.fetchone()
        country = row[0]
        city = row[1]
        stadium = row[2]
        capacity = row[3]
        stadiumCity = row[4]
        coachFIO = row[5]
        coachCountry = row[6]
        ownerFIO = row[7]
        ownerCountry = row[8]
        self.ui.countryLabel.setText(country.rstrip())
        self.ui.cityLabel.setText(city.rstrip())
        self.ui.stadiumLabel.setText((stadium.rstrip() + " (" + stadiumCity.lstrip()).rstrip() + ")")
        self.ui.capacityLabel.setText(str(capacity))
        self.ui.coachLabel.setText((coachFIO.rstrip() + " (" + coachCountry.lstrip()).rstrip() + ")")
        self.ui.ownerLabel.setText((ownerFIO.rstrip() + " (" + ownerCountry.lstrip()).rstrip() + ")")
        self.ui.allPlayersRadio.setChecked(True)
        self.ui.allRadio.setChecked(True)
        self.ui.youngRadio.setChecked(False)
        self.ui.defB.setChecked(True)
        self.ui.defB.hide()
        self.ui.maleRadio.setChecked(False)
        self.ui.noContractrsLabel.hide()
        self.ui.noPlayersLabel.hide()
        self.ui.noFansLabel_3.hide()
        if properties.current_role == 1:
            self.ui.team.show()
            self.ui.players.show()
            self.ui.coaches.show()
            self.ui.contracts.show()
            self.ui.fans.show()
        elif properties.current_role == 2:
            self.ui.team.show()
            self.ui.players.show()
            self.ui.coaches.show()
            self.ui.tabWidget.removeTab(4)
            self.ui.tabWidget.removeTab(3)
        elif properties.current_role == 3:
            self.ui.team.show()
            self.ui.players.show()
            self.ui.coaches.show()
            self.ui.injJournalButton.hide()
            self.ui.tabWidget.removeTab(4)
            self.ui.tabWidget.removeTab(3)
        elif properties.current_role == 4:
            self.ui.team.show()
            self.ui.players.show()
            self.ui.coaches.show()
            self.ui.injJournalButton.hide()
            self.ui.injCheckBox.hide()
            self.ui.tabWidget.removeTab(4)
            self.ui.tabWidget.removeTab(3)
    def backButton_clicked(self):
        if properties.current_role == 1:
            self.menu = managerMenuWindow.managerMenuWindow()
        elif properties.current_role == 2:
            self.menu = coachMenuWindow.coachMenuWindow()
        elif properties.current_role == 3:
            self.menu = playerMenuWindow.playerMenuWindow()
        elif properties.current_role == 4:
            self.menu = menuFanWindow.menuFanWindow()
        self.menu.show()
        self.close()

    def tabChangedHandler(self, index):
        if (index == 0):
            self.ui.injCheckBox.setChecked(False)
            self.ui.defB.setChecked(True)
            self.ui.allPlayersRadio.setChecked(True)
            self.ui.allRadio.setChecked(True)
            self.ui.youngRadio.setChecked(False)
            self.ui.maleRadio.setChecked(False)
            self.ui.femaleRadio.setChecked(False)
            self.db.cursor.execute(
                "SELECT Команды.Страна, Команды.Город, Стадионы.Название, Стадионы.Вместимость, Стадионы.Город, Тренеры_и_персонал.ФИО,"
                "Тренеры_и_персонал.Национальность, Руководство.ФИО, Руководство.Национальность"
                " FROM Команды "
                "join Стадионы on Стадионы.ID_стадиона = Команды.ID_стадиона "
                "join Тренеры_и_персонал on Тренеры_и_персонал.ID_cпециалиста=ID_главного_тренера "
                "join Руководство on Руководство.ID_владельца = Команды.ID_владельца "
                "where  Команды.Команда ='" + str("Манчестер Юнайтед") + "'")
            row = self.db.cursor.fetchone()
            country = row[0]
            city = row[1]
            stadium = row[2]
            capacity = row[3]
            stadiumCity = row[4]
            coachFIO = row[5]
            coachCountry = row[6]
            ownerFIO = row[7]
            ownerCountry = row[8]
            self.ui.countryLabel.setText(country.rstrip())
            self.ui.cityLabel.setText(city.rstrip())
            self.ui.stadiumLabel.setText((stadium.rstrip() + " (" + stadiumCity.lstrip()).rstrip() + ")")
            self.ui.capacityLabel.setText(str(capacity))
            self.ui.coachLabel.setText((coachFIO.rstrip() + " (" + coachCountry.lstrip()).rstrip() + ")")
            self.ui.ownerLabel.setText((ownerFIO.rstrip() + " (" + ownerCountry.lstrip()).rstrip() + ")")
        elif (index == 1):
            self.ui.injCheckBox.setChecked(False)
            self.ui.defB.setChecked(True)
            self.ui.noContractrsLabel.hide()
            self.ui.noPlayersLabel.hide()
            self.ui.noFansLabel_3.hide()
            self.ui.noPlayersLabel.hide()
            self.ui.playersTabel.show()
            self.ui.allPlayersRadio.setChecked(True)
            self.ui.allRadio.setChecked(True)
            self.ui.youngRadio.setChecked(False)
            self.ui.maleRadio.setChecked(False)
            self.ui.femaleRadio.setChecked(False)
            self.ui.playersTabel.setRowCount(0)
            self.db.cursor.execute(
                "SELECT Номер_футболиста, ФИО, Позиция, Национальность, Дата_рождения, Рост, Вес FROM Футболисты order by Номер_футболиста")
            row = self.db.cursor.fetchone()
            if (row is not None):
                i = 0
                while (row is not None):
                    self.ui.playersTabel.setRowCount(self.ui.playersTabel.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.playersTabel.setVerticalHeaderItem(i, item)
                    for j in range(7):
                        self.ui.playersTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                        self.ui.playersTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.noPlayersLabel.show()
                self.ui.playersTabel.hide()
        elif (index == 2):
            self.ui.injCheckBox.setChecked(False)
            self.ui.defB.setChecked(True)
            self.ui.noContractrsLabel.hide()
            self.ui.noPlayersLabel.hide()
            self.ui.noFansLabel_3.hide()
            self.ui.allPlayersRadio.setChecked(True)
            self.ui.allRadio.setChecked(True)
            self.ui.youngRadio.setChecked(False)
            self.ui.maleRadio.setChecked(False)
            self.ui.femaleRadio.setChecked(False)
            self.ui.coachesTabel.setRowCount(0)
            self.db.cursor.execute(
                "SELECT ФИО, Национальность, Дата_рождения, Должность FROM Тренеры_и_персонал "
                "join Команды on Команды.ID_команды=Тренеры_и_персонал.ID_команды where Команда ='" + str("Манчестер Юнайтед") + "'")
            row = self.db.cursor.fetchone()
            i = 0
            while (row is not None):
                self.ui.coachesTabel.setRowCount(self.ui.coachesTabel.rowCount() + 1)
                item = QtWidgets.QTableWidgetItem()
                self.ui.coachesTabel.setVerticalHeaderItem(i, item)
                for j in range(4):
                    self.ui.coachesTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                    self.ui.coachesTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                row = self.db.cursor.fetchone()
                i += 1
        elif (index == 3):
            self.ui.injCheckBox.setChecked(False)
            self.ui.defB.setChecked(True)
            self.ui.noContractrsLabel.hide()
            self.ui.noPlayersLabel.hide()
            self.ui.noFansLabel_3.hide()
            self.ui.noFansLabel_3.hide()
            self.ui.fansTabel.show()
            self.ui.allPlayersRadio.setChecked(True)
            self.ui.allRadio.setChecked(True)
            self.ui.youngRadio.setChecked(False)
            self.ui.maleRadio.setChecked(False)
            self.ui.femaleRadio.setChecked(False)
            self.ui.contractsTabel.setRowCount(0)
            self.db.cursor.execute(
                "SELECT Номер_футболиста, ФИО, Зарплата, Дата_окончания  FROM Контракты"
                " join Футболисты on Футболисты.ID_футболиста=Контракты.ID_футболиста order by Номер_футболиста")
            row = self.db.cursor.fetchone()
            if (row is not None):
                i = 0
                while (row is not None):
                    self.ui.contractsTabel.setRowCount(self.ui.contractsTabel.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.contractsTabel.setVerticalHeaderItem(i, item)
                    for j in range(4):
                        if (j == 2):
                            self.ui.contractsTabel.setItem(i, j, QtWidgets.QTableWidgetItem(
                                str(round(row[j], 2)) + "м €/год"))
                        else:
                            self.ui.contractsTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                        self.ui.contractsTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.noFansLabel_3.show()
                self.ui.fansTabel.hide()
        elif (index == 4):
            self.ui.injCheckBox.setChecked(False)
            self.ui.defB.setChecked(True)
            self.ui.noContractrsLabel.hide()
            self.ui.noPlayersLabel.hide()
            self.ui.noFansLabel_3.hide()
            self.ui.allPlayersRadio.setChecked(True)
            self.ui.allRadio.setChecked(True)
            self.ui.youngRadio.setChecked(False)
            self.ui.maleRadio.setChecked(False)
            self.ui.femaleRadio.setChecked(False)
            self.ui.fansTabel.setRowCount(0)
            self.ui.fansTabel.show()
            self.db.cursor.execute(
                "SELECT ФИО, Дата_рождения, Пол FROM Болельщики where ID_болельщика != 0")
            row = self.db.cursor.fetchone()
            i = 0
            if (row is not None):
                i = 0
                while (row is not None):
                    self.ui.fansTabel.setRowCount(self.ui.fansTabel.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.fansTabel.setVerticalHeaderItem(i, item)
                    for j in range(3):
                        self.ui.fansTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                        self.ui.fansTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.noFansLabel_3.show()
                self.ui.fansTabel.hide()


    def injButtonHandler(self):
        self.inj = injuryWindow.injuryWindow()
        self.inj.show()
        self.close()

    def maleRadioHandler(self):
        self.ui.noFansLabel_3.hide()
        self.ui.fansTabel.show()
        self.ui.fansTabel.setRowCount(0)
        self.db.cursor.execute(
            "SELECT ФИО, Дата_рождения, Пол FROM Болельщики where ID_болельщика != 0 and Пол='М'")
        row = self.db.cursor.fetchone()
        if row is not None:
            i = 0
            while (row is not None):
                self.ui.fansTabel.setRowCount(self.ui.fansTabel.rowCount() + 1)
                item = QtWidgets.QTableWidgetItem()
                self.ui.fansTabel.setVerticalHeaderItem(i, item)
                for j in range(3):
                    self.ui.fansTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                    self.ui.fansTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                row = self.db.cursor.fetchone()
                i += 1
        else:
            self.ui.noFansLabel_3.show()
            self.ui.fansTabel.hide()

    def femaleRadioHandler(self):
        self.ui.noFansLabel_3.hide()
        self.ui.fansTabel.show()
        self.ui.fansTabel.setRowCount(0)
        self.db.cursor.execute(
            "SELECT ФИО, Дата_рождения, Пол FROM Болельщики where ID_болельщика != 0 and Пол='Ж'")
        row = self.db.cursor.fetchone()
        if row is not None:
            i = 0
            while (row is not None):
                self.ui.fansTabel.setRowCount(self.ui.fansTabel.rowCount() + 1)
                item = QtWidgets.QTableWidgetItem()
                self.ui.fansTabel.setVerticalHeaderItem(i, item)
                for j in range(3):
                    self.ui.fansTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                    self.ui.fansTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                row = self.db.cursor.fetchone()
                i += 1
        else:
            self.ui.noFansLabel_3.show()
            self.ui.fansTabel.hide()

    def youngRadioHandler(self):
        self.ui.noFansLabel_3.hide()
        self.ui.fansTabel.show()
        self.ui.fansTabel.setRowCount(0)
        self.db.cursor.execute(
            "SELECT ФИО, Дата_рождения, Пол FROM Болельщики where ID_болельщика != 0 "
            "and DATEDIFF(DAY, Болельщики.Дата_рождения, CURRENT_TIMESTAMP) <= 5120 order by Дата_рождения asc")
        row = self.db.cursor.fetchone()
        if row is not None:
            i = 0
            while (row is not None):
                self.ui.fansTabel.setRowCount(self.ui.fansTabel.rowCount() + 1)
                item = QtWidgets.QTableWidgetItem()
                self.ui.fansTabel.setVerticalHeaderItem(i, item)
                for j in range(3):
                    self.ui.fansTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                    self.ui.fansTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                row = self.db.cursor.fetchone()
                i += 1
        else:
            self.ui.noFansLabel_3.show()
            self.ui.fansTabel.hide()

    def resetButton_clicked(self):
        self.ui.noFansLabel_3.hide()
        self.ui.fansTabel.show()
        self.ui.allPlayersRadio.setChecked(True)
        self.ui.allRadio.setChecked(True)
        self.ui.youngRadio.setChecked(False)
        self.ui.maleRadio.setChecked(False)
        self.ui.femaleRadio.setChecked(False)
        self.ui.defB.setChecked(True)
        self.ui.fansTabel.setRowCount(0)
        self.db.cursor.execute(
            "SELECT ФИО, Дата_рождения, Пол FROM Болельщики where ID_болельщика != 0")
        row = self.db.cursor.fetchone()
        if row is not None:
            i = 0
            while (row is not None):
                self.ui.fansTabel.setRowCount(self.ui.fansTabel.rowCount() + 1)
                item = QtWidgets.QTableWidgetItem()
                self.ui.fansTabel.setVerticalHeaderItem(i, item)
                for j in range(3):
                    self.ui.fansTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                    self.ui.fansTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                row = self.db.cursor.fetchone()
                i += 1
        else:
            self.ui.noFansLabel_3.show()
            self.ui.fansTabel.hide()


    def allPlayersRadioHandler(self):
        if not self.ui.injCheckBox.isChecked():
            self.ui.noPlayersLabel.hide()
            self.ui.playersTabel.show()
            self.ui.allRadio.setChecked(True)
            self.ui.youngRadio.setChecked(False)
            self.ui.maleRadio.setChecked(False)
            self.ui.femaleRadio.setChecked(False)
            self.ui.playersTabel.setRowCount(0)
            self.db.cursor.execute(
                "SELECT Номер_футболиста, ФИО, Позиция, Национальность, Дата_рождения, Рост, Вес FROM Футболисты order by Номер_футболиста")
            row = self.db.cursor.fetchone()
            if row is not None:
                i = 0
                while (row is not None):
                    self.ui.playersTabel.setRowCount(self.ui.playersTabel.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.playersTabel.setVerticalHeaderItem(i, item)
                    for j in range(7):
                        self.ui.playersTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                        self.ui.playersTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.noPlayersLabel.show()
                self.ui.playersTabel.hide()
        else:
            self.ui.noPlayersLabel.hide()
            self.ui.playersTabel.show()
            self.ui.allRadio.setChecked(True)
            self.ui.youngRadio.setChecked(False)
            self.ui.maleRadio.setChecked(False)
            self.ui.femaleRadio.setChecked(False)
            self.ui.playersTabel.setRowCount(0)
            self.db.cursor.execute(
                "SELECT Номер_футболиста, ФИО, Позиция, Национальность, Дата_рождения, Рост, Вес FROM Футболисты "
                "EXCEPT (SELECT Номер_футболиста, ФИО, Позиция, Национальность, Дата_рождения, Рост, Вес FROM Футболисты p JOIN Журнал_травм t on t.ID_футболиста = p.ID_футболиста "
                "where t.Срок_восстановления >= CURRENT_TIMESTAMP) order by Номер_футболиста")
            row = self.db.cursor.fetchone()
            if row is not None:
                i = 0
                while (row is not None):
                    self.ui.playersTabel.setRowCount(self.ui.playersTabel.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.playersTabel.setVerticalHeaderItem(i, item)
                    for j in range(7):
                        self.ui.playersTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                        self.ui.playersTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.noPlayersLabel.show()
                self.ui.playersTabel.hide()

    def defRadioHandler(self):
        if not self.ui.injCheckBox.isChecked():
            self.ui.noPlayersLabel.hide()
            self.ui.playersTabel.show()
            self.ui.playersTabel.setRowCount(0)
            self.db.cursor.execute(
                "SELECT * from Защитники")
            row = self.db.cursor.fetchone()
            if row is not None:
                i = 0
                while (row is not None):
                    self.ui.playersTabel.setRowCount(self.ui.playersTabel.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.playersTabel.setVerticalHeaderItem(i, item)
                    for j in range(7):
                        self.ui.playersTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                        self.ui.playersTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.noPlayersLabel.show()
                self.ui.playersTabel.hide()
        else:
            self.ui.noPlayersLabel.hide()
            self.ui.playersTabel.show()
            self.ui.playersTabel.setRowCount(0)
            self.db.cursor.execute(
                "SELECT Номер_футболиста, ФИО, Позиция, Национальность, Дата_рождения, Рост, Вес from Защитники "
                "EXCEPT (SELECT Номер_футболиста, ФИО, Позиция, Национальность, Дата_рождения, Рост, Вес FROM Футболисты p JOIN Журнал_травм t on t.ID_футболиста = p.ID_футболиста "
                "where t.Срок_восстановления >= CURRENT_TIMESTAMP)")
            row = self.db.cursor.fetchone()
            if row is not None:
                i = 0
                while (row is not None):
                    self.ui.playersTabel.setRowCount(self.ui.playersTabel.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.playersTabel.setVerticalHeaderItem(i, item)
                    for j in range(7):
                        self.ui.playersTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                        self.ui.playersTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.noPlayersLabel.show()
                self.ui.playersTabel.hide()



    def midRadioHandler(self):
        if not self.ui.injCheckBox.isChecked():
            self.ui.noPlayersLabel.hide()
            self.ui.playersTabel.show()
            self.ui.playersTabel.setRowCount(0)
            self.db.cursor.execute(
                "SELECT * from Полузащитники")
            row = self.db.cursor.fetchone()
            if row is not None:
                i = 0
                while (row is not None):
                    self.ui.playersTabel.setRowCount(self.ui.playersTabel.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.playersTabel.setVerticalHeaderItem(i, item)
                    for j in range(7):
                        self.ui.playersTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                        self.ui.playersTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.noPlayersLabel.show()
                self.ui.playersTabel.hide()
        else:
            self.ui.noPlayersLabel.hide()
            self.ui.playersTabel.show()
            self.ui.playersTabel.setRowCount(0)
            self.db.cursor.execute(
                "SELECT Номер_футболиста, ФИО, Позиция, Национальность, Дата_рождения, Рост, Вес from Полузащитники "
                "EXCEPT (SELECT Номер_футболиста, ФИО, Позиция, Национальность, Дата_рождения, Рост, Вес FROM Футболисты p JOIN Журнал_травм t on t.ID_футболиста = p.ID_футболиста "
                "where t.Срок_восстановления >= CURRENT_TIMESTAMP)")
            row = self.db.cursor.fetchone()
            if row is not None:
                i = 0
                while (row is not None):
                    self.ui.playersTabel.setRowCount(self.ui.playersTabel.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.playersTabel.setVerticalHeaderItem(i, item)
                    for j in range(7):
                        self.ui.playersTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                        self.ui.playersTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.noPlayersLabel.show()
                self.ui.playersTabel.hide()

    def forwardRadioHandler(self):
        if not self.ui.injCheckBox.isChecked():
            self.ui.noPlayersLabel.hide()
            self.ui.playersTabel.show()
            self.ui.playersTabel.setRowCount(0)
            self.db.cursor.execute(
                "SELECT * from Нападающие")
            row = self.db.cursor.fetchone()
            if row is not None:
                i = 0
                while (row is not None):
                    self.ui.playersTabel.setRowCount(self.ui.playersTabel.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.playersTabel.setVerticalHeaderItem(i, item)
                    for j in range(7):
                        self.ui.playersTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                        self.ui.playersTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.noPlayersLabel.show()
                self.ui.playersTabel.hide()
        else:
            self.ui.noPlayersLabel.hide()
            self.ui.playersTabel.show()
            self.ui.playersTabel.setRowCount(0)
            self.db.cursor.execute(
                "SELECT Номер_футболиста, ФИО, Позиция, Национальность, Дата_рождения, Рост, Вес from Нападающие "
                "EXCEPT (SELECT Номер_футболиста, ФИО, Позиция, Национальность, Дата_рождения, Рост, Вес FROM Футболисты p JOIN Журнал_травм t on t.ID_футболиста = p.ID_футболиста "
                "where t.Срок_восстановления >= CURRENT_TIMESTAMP)")
            row = self.db.cursor.fetchone()
            if row is not None:
                i = 0
                while (row is not None):
                    self.ui.playersTabel.setRowCount(self.ui.playersTabel.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.playersTabel.setVerticalHeaderItem(i, item)
                    for j in range(7):
                        self.ui.playersTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                        self.ui.playersTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.noPlayersLabel.show()
                self.ui.playersTabel.hide()

    def goalkeepersRadioHandler(self):
        if not self.ui.injCheckBox.isChecked():
            self.ui.noPlayersLabel.hide()
            self.ui.playersTabel.show()
            self.ui.playersTabel.setRowCount(0)
            self.db.cursor.execute(
                "SELECT * from Вратари")
            row = self.db.cursor.fetchone()
            if row is not None:
                i = 0
                while (row is not None):
                    self.ui.playersTabel.setRowCount(self.ui.playersTabel.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.playersTabel.setVerticalHeaderItem(i, item)
                    for j in range(7):
                        self.ui.playersTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                        self.ui.playersTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.noPlayersLabel.show()
                self.ui.playersTabel.hide()
        else:
            self.ui.noPlayersLabel.hide()
            self.ui.playersTabel.show()
            self.ui.playersTabel.setRowCount(0)
            self.db.cursor.execute(
                "SELECT Номер_футболиста, ФИО, Позиция, Национальность, Дата_рождения, Рост, Вес from Вратари "
                "EXCEPT (SELECT Номер_футболиста, ФИО, Позиция, Национальность, Дата_рождения, Рост, Вес FROM Футболисты p JOIN Журнал_травм t on t.ID_футболиста = p.ID_футболиста "
                "where t.Срок_восстановления >= CURRENT_TIMESTAMP)")
            row = self.db.cursor.fetchone()
            if row is not None:
                i = 0
                while (row is not None):
                    self.ui.playersTabel.setRowCount(self.ui.playersTabel.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.playersTabel.setVerticalHeaderItem(i, item)
                    for j in range(7):
                        self.ui.playersTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                        self.ui.playersTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.noPlayersLabel.show()
                self.ui.playersTabel.hide()


    def injCheckBoxHandler(self):
        if self.ui.injCheckBox.isChecked():
            if self.ui.allPlayersRadio.isChecked():
                self.allPlayersRadioHandler()
            elif self.ui.goalkeepersRadio.isChecked():
                self.goalkeepersRadioHandler()
            elif self.ui.defRadio.isChecked():
                self.defRadioHandler()
            elif self.ui.midRadio.isChecked():
                self.midRadioHandler()
            elif self.ui.forwardRadio.isChecked():
                self.forwardRadioHandler()
        else:
            if self.ui.allPlayersRadio.isChecked():
                self.allPlayersRadioHandler()
            elif self.ui.goalkeepersRadio.isChecked():
                self.goalkeepersRadioHandler()
            elif self.ui.defRadio.isChecked():
                self.defRadioHandler()
            elif self.ui.midRadio.isChecked():
                self.midRadioHandler()
            elif self.ui.forwardRadio.isChecked():
                self.forwardRadioHandler()
