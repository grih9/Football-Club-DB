from PyQt5 import QtWidgets, QtCore, Qt

import teamWindow
import properties
import sql
from injury import Ui_MainWindow as injuryMain


class injuryWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = injuryMain()
        self.ui.setupUi(self)
        header = self.ui.currentTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header = self.ui.historyTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.addBox.hide()
        self.ui.noInjuriesLabel.hide()
        self.setWindowTitle("Журнал травм")
        self.ui.injuries.setCurrentIndex(0)
        self.ui.backButton.clicked.connect(self.backButton_clicked)
        self.ui.addButton1.clicked.connect(self.addButton1_clicked)
        self.ui.addButton2.clicked.connect(self.addButton2_clicked)
        self.ui.date1.dateChanged.connect(self.date1Handler)
        self.ui.date2.dateChanged.connect(self.date2Handler)
        self.ui.injuries.currentChanged.connect(self.tabChangedHandler)
        self.ui.fromDate.dateChanged.connect(self.fromDateHandler)
        self.ui.toDate.dateChanged.connect(self.toDateHandler)
        self.ui.searchButton.clicked.connect(self.searchButton_clicked)
        self.ui.resetButton.clicked.connect(self.resetButton_clicked)
        self.ui.fromDate.setDate(QtCore.QDate.currentDate())
        self.ui.toDate.setDate(QtCore.QDate.currentDate().addDays(1))
        self.ui.date1.setDate(QtCore.QDate.currentDate())
        self.ui.date2.setDate(QtCore.QDate.currentDate().addDays(1))

        if properties.current_role == 1:
            self.ui.addButton1.hide()
            self.ui.addBox.hide()
        elif properties.current_role == 2:
            self.ui.addButton1.show()

        self.db = sql.Sql("football_club")

        self.ui.currentTable.setRowCount(0)
        self.db.cursor.execute(
            "SELECT p.Номер_футболиста, p.ФИО, t.Травма, t.Дата, t.Срок_восстановления, t.Доп_информация FROM Журнал_травм t "
            "join Футболисты p on p.ID_футболиста = t.ID_футболиста "
            "where t.Срок_восстановления >= CURRENT_TIMESTAMP order by Срок_восстановления asc")
        row = self.db.cursor.fetchone()
        if (row is not None):
            i = 0
            while (row is not None):
                self.ui.currentTable.setRowCount(self.ui.currentTable.rowCount() + 1)
                item = QtWidgets.QTableWidgetItem()
                self.ui.currentTable.setVerticalHeaderItem(i, item)
                for j in range(6):
                    self.ui.currentTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                    self.ui.currentTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                row = self.db.cursor.fetchone()
                i += 1
        else:
            self.ui.currentTable.setColumnCount(0)
            self.ui.noInjuriesLabel.show()

    def backButton_clicked(self):
        self.menu = teamWindow.teamWindow()
        self.menu.ui.tabWidget.setCurrentIndex(1)
        self.menu.show()
        self.close()

    def addButton1_clicked(self):
        self.ui.addBox.show()
        #self.db.cursor.execute(
        #    "SELECT ФИО from Футболисты WHERE not EXISTS (SELECT p.ФИО FROM Журнал_травм t "
        #    "join Футболисты p on p.ID_футболиста = t.ID_футболиста )")
        self.db.cursor.execute(
            "SELECT ФИО, Номер_футболиста from Футболисты order by Номер_футболиста")

        row = self.db.cursor.fetchone()
        while (row is not None):
            m = str(row[1]) + ". " + row[0].rstrip()
            self.ui.playerCombo.addItem(m)
            row = self.db.cursor.fetchone()

        self.ui.addButton1.hide()

    def tabChangedHandler(self, index):
        if (index == 0):
            self.ui.date1.setDate(QtCore.QDate.currentDate())
            self.ui.date2.setDate(QtCore.QDate.currentDate().addDays(1))
            self.ui.addBox.hide()
            self.ui.noInjuriesLabel.hide()
            self.ui.addButton1.show()
            self.ui.currentTable.setRowCount(0)
            self.db.cursor.execute(
                "SELECT p.Номер_футболиста, p.ФИО, t.Травма, t.Дата, t.Срок_восстановления, t.Доп_информация FROM Журнал_травм t "
                "join Футболисты p on p.ID_футболиста = t.ID_футболиста "
                "where t.Срок_восстановления >= CURRENT_TIMESTAMP order by Срок_восстановления asc")
            row = self.db.cursor.fetchone()
            if properties.current_role == 1:
                self.ui.addButton1.hide()
                self.ui.addBox.hide()
            elif properties.current_role == 2:
                self.ui.addButton1.show()
            if (row is not None):
                i = 0
                while (row is not None):
                    self.ui.currentTable.setRowCount(self.ui.currentTable.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.currentTable.setVerticalHeaderItem(i, item)
                    for j in range(6):
                        self.ui.currentTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                        self.ui.currentTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.currentTable.setColumnCount(0)
                self.ui.noInjuriesLabel.show()
        elif (index == 1):
            self.ui.fromDate.setDate(QtCore.QDate.currentDate())
            self.ui.toDate.setDate(QtCore.QDate.currentDate().addDays(1))
            self.ui.historyTable.show()
            self.ui.historyTable.setRowCount(0)
            self.ui.noInjLabel.hide()
            self.db.cursor.execute(
                "SELECT p.Номер_футболиста, p.ФИО, t.Травма, t.Дата, t.Срок_восстановления, t.Доп_информация FROM Журнал_травм t "
                "join Футболисты p on p.ID_футболиста = t.ID_футболиста "
                "where t.Срок_восстановления < CURRENT_TIMESTAMP order by Срок_восстановления asc")
            row = self.db.cursor.fetchone()
            if (row is not None):
                i = 0
                while (row is not None):
                    self.ui.historyTable.setRowCount(self.ui.historyTable.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.historyTable.setVerticalHeaderItem(i, item)
                    for j in range(6):
                        self.ui.historyTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                        self.ui.historyTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1
            else:
                self.ui.historyTable.hide()
                self.ui.noInjLabel.show()


    def addButton2_clicked(self):
        f = self.ui.playerCombo.currentText()
        t = self.ui.enjLine.text()
        d1 = self.ui.date1.text()
        d2 = self.ui.date2.text()
        i = self.ui.infoText.toPlainText()
        if (i.strip() == "" or i is None):
            i = "-"
        if (f.strip() == "" or t.strip() == ""):
            message = "Необходимо заполнить каждое поле"
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Пустое поле")
            error_message.showMessage(message)
        else:
            if (f[2] == "."):
                f = f[0:2]
            else:
                f = f[0]

            self.db.cursor.execute("SELECT ID_футболиста from Футболисты where Номер_футболиста=" + str(f))
            row = self.db.cursor.fetchone()
            id = row[0]
            self.db.cursor.execute("INSERT INTO Журнал_травм(ID_футболиста, Травма, Дата, Срок_восстановления, Доп_информация) "
                               "VALUES('" + str(id)  + "', '" + t + "', '" + str(d1)  +"', '"+ str(d2) +"', '" + i +"')")
            self.db.cnxn.commit()
            self.wind = injuryWindow()
            self.wind.show()
            self.close()

    def searchButton_clicked(self):
        self.ui.historyTable.show()
        self.ui.historyTable.setRowCount(0)
        self.ui.noInjLabel.hide()
        self.db.cursor.execute(
            "SELECT p.Номер_футболиста, p.ФИО, t.Травма, t.Дата, t.Срок_восстановления, t.Доп_информация FROM Журнал_травм t "
            "join Футболисты p on p.ID_футболиста = t.ID_футболиста "
            "where t.Дата <= '" + str(self.ui.toDate.text()) + "' and t.Дата >= '" + str(
                self.ui.fromDate.text()) + "' order by Срок_восстановления asc")
        row = self.db.cursor.fetchone()
        if (row is not None):
            i = 0
            while (row is not None):
                self.ui.historyTable.setRowCount(self.ui.historyTable.rowCount() + 1)
                item = QtWidgets.QTableWidgetItem()
                self.ui.historyTable.setVerticalHeaderItem(i, item)
                for j in range(6):
                    self.ui.historyTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                    self.ui.historyTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                row = self.db.cursor.fetchone()
                i += 1
        else:
            self.ui.historyTable.hide()
            self.ui.noInjLabel.show()
    def resetButton_clicked(self):
        self.ui.fromDate.setDate(QtCore.QDate.currentDate())
        self.ui.toDate.setDate(QtCore.QDate.currentDate().addDays(1))
        self.ui.historyTable.show()
        self.ui.historyTable.setRowCount(0)
        self.ui.noInjLabel.hide()
        self.db.cursor.execute(
            "SELECT p.Номер_футболиста, p.ФИО, t.Травма, t.Дата, t.Срок_восстановления, t.Доп_информация FROM Журнал_травм t "
            "join Футболисты p on p.ID_футболиста = t.ID_футболиста "
            "where t.Срок_восстановления < CURRENT_TIMESTAMP order by Срок_восстановления asc")
        row = self.db.cursor.fetchone()
        if (row is not None):
            i = 0
            while (row is not None):
                self.ui.historyTable.setRowCount(self.ui.historyTable.rowCount() + 1)
                item = QtWidgets.QTableWidgetItem()
                self.ui.historyTable.setVerticalHeaderItem(i, item)
                for j in range(6):
                    self.ui.historyTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                    self.ui.historyTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                row = self.db.cursor.fetchone()
                i += 1
        else:
            self.ui.historyTable.hide()
            self.ui.noInjLabel.show()

    def date1Handler(self, date):
        self.ui.date2.setMinimumDate(date.addDays(1))

    def date2Handler(self, date):
        self.ui.date1.setMaximumDate(date.addDays(-1))

    def fromDateHandler(self, date):
        self.ui.toDate.setMinimumDate(date.addDays(1))

    def toDateHandler(self, date):
        self.ui.fromDate.setMaximumDate(date.addDays(-1))

