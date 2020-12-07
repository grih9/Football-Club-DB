from PyQt5 import QtWidgets, QtCore

import menuFanWindow
import properties
import sql
from tickets import Ui_MainWindow as ticketsMain


class ticketsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ticketsMain()
        self.ui.setupUi(self)
        header = self.ui.ticketsTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        header = self.ui.historyTabel.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.noTicketsLabel.hide()
        self.ui.buyBox.hide()
        self.setWindowTitle("Билеты")
        self.ui.tickets.setCurrentIndex(0)
        self.maxVal = 100000
        self.costs = list()
        self.tickets = list()
        self.matches = list()
        self.ui.buyButton2.setEnabled(False)
        self.ui.backButton.clicked.connect(self.backButton_clicked)
        self.ui.tickets.currentChanged.connect(self.tabChangedHandler)
        self.ui.buyButton1.clicked.connect(self.buyButton1_clicked)
        self.ui.buyButton2.clicked.connect(self.buyButton2_clicked)
        self.ui.checkBox.stateChanged.connect(self.checkBoxHandler)


        self.ui.matchesCombo.currentIndexChanged.connect(self.matchesComboHandler)
        self.ui.costSpin.valueChanged.connect(self.costSpinHandler)
        self.ui.sectorCheck.currentIndexChanged.connect(self.sectorComboHandler)
        self.ui.placeCombo.currentIndexChanged.connect(self.placeComboHandler)

        self.ui.summaryLabel.setText("")
        self.db = sql.Sql("football_club")
        self.db.cursor.execute("SELECT ФИО FROM Болельщики where ID_пользователя =" + str(properties.current_userID))
        row = self.db.cursor.fetchone()
        self.ui.fioLabel.setText(row[0].rstrip())
        self.ui.ticketsTable.setRowCount(0)
        self.db.cursor.execute(
            "SELECT c.Дата, s.Название, t.Команда, c.Тип, b.Сектор, b.Ряд, b.Место, b.Стоимость FROM Билеты b "
            "join Стадионы s on s.ID_стадиона = b.ID_cтадиона "
            "join Календарь c on c.ID_матча = b.id_матча "
            "join Команды t on t.ID_команды = c.ID_соперника "
            "where ID_болельщика=(select ID_болельщика from Болельщики where ID_пользователя=" + str(properties.current_userID) + ") and Дата>CURRENT_TIMESTAMP")

        row = self.db.cursor.fetchone()
        if (row is not None):
            i = 0
            while (row is not None):
                self.ui.ticketsTable.setRowCount(self.ui.ticketsTable.rowCount() + 1)
                item = QtWidgets.QTableWidgetItem()
                self.ui.ticketsTable.setVerticalHeaderItem(i, item)
                for j in range(8):
                    self.ui.ticketsTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                    self.ui.ticketsTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                row = self.db.cursor.fetchone()
                i += 1
        else:
            self.ui.ticketsTable.setColumnCount(0)
            self.ui.noTicketsLabel.show()

    def backButton_clicked(self):
        self.menu = menuFanWindow.menuFanWindow()
        self.menu.show()
        self.close()

    def buyButton1_clicked(self):
        self.ui.buyBox.show()
        self.ui.summaryLabel.hide()
        self.ui.fioLabel.hide()
        self.index = 0
        self.ui.matchesCombo.clear()
        self.matches = list()
        self.ui.placeCombo.clear()
        self.costs = list()
        self.tickets = list()
        self.ui.sectorCheck.clear()
        self.ui.matchesCombo.addItem("")
        self.ui.placeCombo.addItem("")
        self.ui.sectorCheck.addItem("")
        self.ui.buyButton2.setEnabled(False)
        self.db.cursor.execute(
            "SELECT Distinct c.Дата, s.Название, t.Команда, c.Тип, b.ID_матча FROM Билеты b "
            "join Стадионы s on s.ID_стадиона = b.ID_cтадиона "
            "join Календарь c on c.ID_матча = b.id_матча "
            "join Команды t on t.ID_команды = c.ID_соперника "
            "where ID_болельщика=0 and Дата>CURRENT_TIMESTAMP "
            "group by b.ID_матча, c.Дата, s.Название, t.Команда, c.Тип")

        self.matches = list()
        row = self.db.cursor.fetchone()
        i = 0
        while (row is not None):
            p = "Д"
            if (row[1].rstrip() != "Олд Траффорд"):
                p = "Г"
            m = (str(row[0]).rstrip()[0:-3] + ". " + row[2].lstrip()).rstrip() + " - " + row[3].rstrip()[0:4] + ". (" + p + ")"
            self.ui.matchesCombo.addItem(m)
            self.matches.append(row[4])
            row = self.db.cursor.fetchone()
            i += 1

        self.ui.sectorCheck.hide()
        self.ui.sectorLabel.hide()
        self.ui.placeLabel.hide()
        self.ui.placeCombo.hide()
        self.ui.buyButton1.hide()

    def tabChangedHandler(self, index):
        if (index == 0):
            self.ui.ticketsTable.setRowCount(0)
            self.ui.buyBox.hide()
            self.ui.buyButton1.show()
            self.index = 0
            self.ui.buyButton2.setEnabled(False)
            self.ui.noTicketsLabel.hide()
            self.db.cursor.execute(
                "SELECT c.Дата, s.Название, t.Команда, c.Тип, b.Сектор, b.Ряд, b.Место, b.Стоимость FROM Билеты b "
                "join Стадионы s on s.ID_стадиона = b.ID_cтадиона "
                "join Календарь c on c.ID_матча = b.id_матча "
                "join Команды t on t.ID_команды = c.ID_соперника "
                "where ID_болельщика=(select ID_болельщика from Болельщики where ID_пользователя=" + str(
                    str(properties.current_userID)) + ") and Дата>CURRENT_TIMESTAMP")
            row = self.db.cursor.fetchone()
            if (row is not None):
                i = 0
                while (row is not None):
                    self.ui.ticketsTable.setRowCount(self.ui.ticketsTable.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.ticketsTable.setVerticalHeaderItem(i, item)
                    for j in range(8):
                        self.ui.ticketsTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                        self.ui.ticketsTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.ticketsTable.setColumnCount(0)
                self.ui.noTicketsLabel.show()
        elif (index == 1):
            self.ui.historyTabel.setRowCount(0)
            self.ui.buyButton2.setEnabled(False)
            self.ui.noTicketsLabel2.hide()
            self.db.cursor.execute(
                "SELECT c.Дата, s.Название, t.Команда, c.Тип, b.Сектор, b.Ряд, b.Место, b.Стоимость FROM Билеты b "
                "join Стадионы s on s.ID_стадиона = b.ID_cтадиона "
                "join Календарь c on c.ID_матча = b.id_матча "
                "join Команды t on t.ID_команды = c.ID_соперника "
                "where ID_болельщика=(select ID_болельщика from Болельщики where ID_пользователя=" + str(
                    str(properties.current_userID)) + ") and Дата<=CURRENT_TIMESTAMP")

            row = self.db.cursor.fetchone()
            if (row is not None):
                i = 0
                while (row is not None):
                    self.ui.historyTabel.setRowCount(self.ui.ticketsTable.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.historyTabel.setVerticalHeaderItem(i, item)
                    for j in range(8):
                        self.ui.historyTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j])))
                        self.ui.historyTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.historyTabel.setColumnCount(0)
                self.ui.noTicketsLabel2.show()

    def checkBoxHandler(self):
        if self.ui.checkBox.isChecked():
            self.ui.costSpin.setEnabled(True)
            self.maxVal = self.ui.costSpin.value()
        else:
            self.ui.costSpin.setEnabled(False)
            self.maxVal = 100000
        if (self.index != 0):
            self.ui.placeCombo.clear()
            self.costs = list()
            self.tickets = list()
            self.ui.sectorCheck.clear()
            self.ui.sectorCheck.addItem("")
            self.ui.placeCombo.addItem("")
            self.db.cursor.execute(
                "SELECT Distinct b.Сектор FROM Билеты b "
                "join Календарь c on c.ID_матча = b.id_матча "
                "join Команды t on t.ID_команды = c.ID_соперника "
                "where ID_болельщика=0 and b.Стоимость <" + str(self.maxVal) + " and b.ID_матча=" + str(
                    self.matches[self.index - 1]) + " "
            "group by b.Сектор "
            "order by b.Сектор ASC")

            row = self.db.cursor.fetchone()
            i = 0
            while (row is not None):
                self.ui.sectorCheck.addItem(row[0].rstrip())
                row = self.db.cursor.fetchone()
                i += 1

    def matchesComboHandler(self, index):
        if (index == 0 or index == -1):
            self.ui.sectorCheck.hide()
            self.ui.placeCombo.hide()
            self.ui.placeLabel.hide()
            self.ui.buyButton2.setEnabled(False)
            self.ui.sectorLabel.hide()
            self.ui.placeCombo.clear()
            self.costs = list()
            self.tickets = list()
            self.index = 0
            self.ui.sectorCheck.clear()
            self.ui.sectorCheck.addItem("")
            self.ui.placeCombo.addItem("")
        else:
            self.ui.placeCombo.clear()
            self.costs = list()
            self.tickets = list()
            self.ui.sectorCheck.clear()
            self.ui.sectorCheck.addItem("")
            self.ui.placeCombo.addItem("")
            self.index = index
            self.db.cursor.execute(
                "SELECT Distinct b.Сектор FROM Билеты b "
            "join Календарь c on c.ID_матча = b.id_матча "
            "join Команды t on t.ID_команды = c.ID_соперника "
            "where ID_болельщика=0 and b.Стоимость <"+ str(self.maxVal) + " and b.ID_матча="+ str(self.matches[index - 1]) + " "
            "group by b.Сектор "
            "order by b.Сектор ASC")

            row = self.db.cursor.fetchone()
            i = 0
            while (row is not None):
                self.ui.sectorCheck.addItem(row[0].rstrip())
                row = self.db.cursor.fetchone()
                i += 1

            self.ui.sectorCheck.show()
            self.ui.sectorLabel.show()

    def costSpinHandler(self):
        if self.ui.checkBox.isChecked():
            self.maxVal = self.ui.costSpin.value()
            if (self.index != 0):
                self.ui.placeCombo.clear()
                self.ui.sectorCheck.clear()
                self.costs = list()
                self.tickets = list()
                self.ui.sectorCheck.addItem("")
                self.ui.placeCombo.addItem("")
                self.db.cursor.execute(
                    "SELECT Distinct b.Сектор FROM Билеты b "
                    "join Календарь c on c.ID_матча = b.id_матча "
                    "join Команды t on t.ID_команды = c.ID_соперника "
                    "where ID_болельщика=0 and b.Стоимость <" + str(self.maxVal) + " and b.ID_матча=" + str(
                        self.matches[self.index - 1]) + " "
                    "group by b.Сектор "
                    "order by b.Сектор ASC")

                row = self.db.cursor.fetchone()
                i = 0
                while (row is not None):
                    self.ui.sectorCheck.addItem(row[0].rstrip())
                    row = self.db.cursor.fetchone()
                    i += 1

    def sectorComboHandler(self, index):
        if (index == 0 or index == -1):
            self.ui.placeCombo.hide()
            self.ui.placeLabel.hide()
            self.ui.buyButton2.setEnabled(False)
            self.costs = list()
            self.tickets = list()
            self.ui.placeCombo.clear()
            self.ui.placeCombo.addItem("")
        else:
            self.ui.placeCombo.clear()
            self.ui.placeCombo.addItem("")
            sector = self.ui.sectorCheck.currentText().rstrip()
            self.db.cursor.execute(
                "SELECT b.Ряд, b.Место, b.Стоимость, b.ID_билета FROM Билеты b "
            "where ID_болельщика=0 and b.Стоимость <"+ str(self.maxVal) + " and b.Сектор='" + sector + "' "
             "and b.ID_матча="+ str(self.matches[self.index - 1]))

            row = self.db.cursor.fetchone()
            i = 0
            while (row is not None):
                if (row[0] != 0):
                    self.ui.placeCombo.addItem((str(row[0]) + " р. " + str(row[1])) + " м.")
                else:
                    self.ui.placeCombo.addItem(str(row[1]) + " м.")
                self.costs.append(row[2])
                self.tickets.append(row[3])
                row = self.db.cursor.fetchone()
                i += 1

            self.ui.placeCombo.show()
            self.ui.placeLabel.show()

    def placeComboHandler(self, index):
        if (index == 0 or index == -1):
            self.ui.buyButton2.setEnabled(False)
            self.ui.fioLabel.hide()
            self.ui.summaryLabel.hide()
        else:
            self.ui.summaryLabel.setText("К оплате: " + str(self.costs[index - 1]) + "€")
            self.ui.summaryLabel.show()
            self.ui.buyButton2.setEnabled(True)
            self.ui.fioLabel.show()

    def buyButton2_clicked(self):
        message = 'Оплатить?'
        reply = QtWidgets.QMessageBox.question(self, 'Покупка билета', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            index = self.ui.placeCombo.currentIndex()
            id = self.tickets[index - 1]
            self.db.cursor.execute("UPDATE Билеты SET ID_болельщика = "
                                   "(SELECT ID_болельщика FROM Болельщики where ID_пользователя =" + str(properties.current_userID) + ") "
                                    "where ID_билета=" + str(id))
            self.db.cnxn.commit()
            message = 'Успешно'
            QtWidgets.QMessageBox.question(self, 'Покупка билета', message,
                                                   QtWidgets.QMessageBox.Ok)
            self.wind = ticketsWindow()
            self.wind.show()
            self.close()

