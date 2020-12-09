from alltickets import  Ui_MainWindow as tickMain

from PyQt5 import QtWidgets, QtCore, Qt

import menuFanWindow
import properties
import sql
import resultsWindow

class allTicketsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = tickMain()
        self.ui.setupUi(self)
        header = self.ui.ticketsTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        header = self.ui.historyTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.noTicketsLabel.hide()
        self.setWindowTitle("Билеты")
        self.ui.tickets.setCurrentIndex(0)

        self.ui.backButton.clicked.connect(self.backButton_clicked)
        self.ui.tickets.currentChanged.connect(self.tabChangedHandler)

        self.db = sql.Sql("football_club")
        self.db.cursor.execute("SELECT ФИО FROM Болельщики where ID_пользователя =" + str(properties.current_userID))
        row = self.db.cursor.fetchone()
        self.ui.ticketsTable.setRowCount(0)
        self.db.cursor.execute(
            "SELECT f.ФИО, c.Дата, s.Название, t.Команда, c.Тип, b.Сектор, b.Ряд, b.Место, b.Стоимость FROM Билеты b "
            "join Стадионы s on s.ID_стадиона = b.ID_cтадиона "
            "join Календарь c on c.ID_матча = b.id_матча "
            "join Команды t on t.ID_команды = c.ID_соперника "
            "join Болельщики f on f.ID_болельщика=b.ID_болельщика "
            "where b.ID_болельщика!= 0 and Дата>CURRENT_TIMESTAMP order by Дата")

        row = self.db.cursor.fetchone()
        if (row is not None):
            i = 0
            while (row is not None):
                self.ui.ticketsTable.setRowCount(self.ui.ticketsTable.rowCount() + 1)
                item = QtWidgets.QTableWidgetItem()
                self.ui.ticketsTable.setVerticalHeaderItem(i, item)
                for j in range(9):
                    self.ui.ticketsTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                    self.ui.ticketsTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                row = self.db.cursor.fetchone()
                i += 1
        else:
            self.ui.ticketsTable.setColumnCount(0)
            self.ui.noTicketsLabel.show()


    def backButton_clicked(self):
        self.menu = resultsWindow.resultsWindow()
        self.menu.show()
        self.close()


    def tabChangedHandler(self, index):
        if (index == 0):
            self.ui.noTicketsLabel.hide()
            self.ui.ticketsTable.setRowCount(0)
            self.db.cursor.execute(
            "SELECT f.ФИО, c.Дата, s.Название, t.Команда, c.Тип, b.Сектор, b.Ряд, b.Место, b.Стоимость FROM Билеты b "
            "join Стадионы s on s.ID_стадиона = b.ID_cтадиона "
            "join Календарь c on c.ID_матча = b.id_матча "
            "join Команды t on t.ID_команды = c.ID_соперника "
            "join Болельщики f on f.ID_болельщика=b.ID_болельщика "
            "where b.ID_болельщика!= 0 and Дата>CURRENT_TIMESTAMP order by Дата")
            row = self.db.cursor.fetchone()
            if (row is not None):
                i = 0
                while (row is not None):
                    self.ui.ticketsTable.setRowCount(self.ui.ticketsTable.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.ticketsTable.setVerticalHeaderItem(i, item)
                    for j in range(9):
                        self.ui.ticketsTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                        self.ui.ticketsTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.ticketsTable.setColumnCount(0)
                self.ui.noTicketsLabel.show()

        elif (index == 1):
            self.ui.historyTable.setRowCount(0)
            self.ui.noTicketsLabel2.hide()
            self.db.cursor.execute(
                "SELECT f.ФИО, c.Дата, s.Название, t.Команда, c.Тип, b.Сектор, b.Ряд, b.Место, b.Стоимость FROM Билеты b "
                "join Стадионы s on s.ID_стадиона = b.ID_cтадиона "
                "join Календарь c on c.ID_матча = b.id_матча "
                "join Команды t on t.ID_команды = c.ID_соперника "
                "join Болельщики f on f.ID_болельщика=b.ID_болельщика "
                "where b.ID_болельщика!= 0 and Дата<=CURRENT_TIMESTAMP order by Дата")

            row = self.db.cursor.fetchone()
            if (row is not None):
                i = 0
                while (row is not None):
                    self.ui.historyTable.setRowCount(self.ui.historyTable.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.historyTable.setVerticalHeaderItem(i, item)
                    for j in range(9):
                        self.ui.historyTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                        self.ui.historyTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.historyTable.setColumnCount(0)
                self.ui.noTicketsLabel2.show()

