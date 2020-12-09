from results import Ui_MainWindow as resultsMain

from PyQt5 import QtWidgets, QtCore
import menuFanWindow
import playerMenuWindow
import coachMenuWindow
import managerMenuWindow
import properties
import sql
import allTicketsWindow
import newMatchWindow

class resultsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = resultsMain()
        self.ui.setupUi(self)
        header = self.ui.historyTabel.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.setWindowTitle("Расписание и результаты")

        self.ui.line.hide()
        self.ui.ticketsButton.hide()
        self.ui.createResult.hide()
        self.ui.createMatch.hide()
        self.ui.awaySpin.hide()
        self.ui.homeSpin.hide()
        self.ui.resultCombo.hide()
        self.ui.label_3.hide()
        self.ui.resultCombo.hide()
        self.ui.createTickets.hide()
        self.ui.ticketsCombo.hide()

        self.ui.createTickets.setEnabled(False)
        self.ui.ticketsCombo.setEnabled(False)
        self.ui.ticketsSpin.setEnabled(False)

        self.ui.ticketsSpin.hide()
        self.ui.percent.hide()

        if (properties.current_role == 1):
            self.ui.line.show()
            self.ui.ticketsButton.show()
            self.ui.createResult.show()
            self.ui.createMatch.show()
            self.ui.awaySpin.show()
            self.ui.homeSpin.show()
            self.ui.resultCombo.show()
            self.ui.label_3.show()
            self.ui.resultCombo.show()
            self.ui.createTickets.show()
            self.ui.ticketsCombo.show()
            self.ui.ticketsSpin.show()
            self.ui.percent.show()



        self.ui.backButton.clicked.connect(self.backButton_clicked)
        self.ui.ticketsButton.clicked.connect(self.ticketsButton_clicked)
        self.ui.createMatch.clicked.connect(self.createMatch_clicked)
        self.ui.createResult.clicked.connect(self.createResult_clicked)

        self.db = sql.Sql("football_club")
        self.db.cursor.execute(
            "SELECT Дата, Команда as Соперник, Результат, Календарь.Тип, Стадионы.Название as Стадион, Результаты.Доп_информация "
            "from Календарь "
            "JOIN Стадионы on Календарь.ID_стадиона=Стадионы.ID_стадиона "
            "JOIN Команды on Календарь.ID_соперника=Команды.ID_команды and DATEDIFF(DAY, Календарь.Дата, CURRENT_TIMESTAMP)<=366 "
            "and DATEDIFF(DAY, Календарь.Дата, CURRENT_TIMESTAMP)>=-366 "
            "left join Результаты on Результаты.ID_матча=Календарь.ID_матча order by Дата asc")

        row = self.db.cursor.fetchone()
        i = 0
        while (row is not None):
            self.ui.historyTabel.setRowCount(self.ui.historyTabel.rowCount() + 1)
            item = QtWidgets.QTableWidgetItem()
            self.ui.historyTabel.setVerticalHeaderItem(i, item)
            for j in range(6):
                if (j == 0):
                    self.ui.historyTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()[0:-3]))
                elif (row[j] is None):
                    self.ui.historyTabel.setItem(i, j, QtWidgets.QTableWidgetItem("-"))
                else:
                    self.ui.historyTabel.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))

                self.ui.historyTabel.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
            i += 1
            row = self.db.cursor.fetchone()

        self.ui.resultCombo.clear()
        self.ui.resultCombo.addItem("")
        self.db.cursor.execute(
            "SELECT Дата, Команда from Календарь "
            "JOIN Команды on Календарь.ID_соперника=Команды.ID_команды and Дата < CURRENT_TIMESTAMP "
            "EXCEPT (SELECT Дата, Команда from Результаты JOIN Календарь on Календарь.ID_Матча=Результаты.ID_матча "
            "JOIN Команды on Календарь.ID_соперника=Команды.ID_команды)")
        row = self.db.cursor.fetchone()
        while (row is not None):
            self.ui.resultCombo.addItem(str(row[0])[0:-3] + ". " + row[1].rstrip())
            row = self.db.cursor.fetchone()


    def ticketsButton_clicked(self):
        self.tick = allTicketsWindow.allTicketsWindow()
        self.tick.show()
        self.close()

    def createMatch_clicked(self):
        self.match = newMatchWindow.newMatchWindow()
        self.match.show()
        self.close()

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

    def createResult_clicked(self):
        t = self.ui.resultCombo.currentText()
        h = self.ui.homeSpin.value()
        a = self.ui.awaySpin.value()
        if (t == ""):
            message = "Выберите матч"
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Пустое поле")
            error_message.showMessage(message)
        else:
            d = str(t)[0:16] + ":00"
            d = d[0:10] + "T" + d[11:]
            self.db.cursor.execute("SELECT ID_матча from Календарь where Дата = '" + str(d) + "'")
            row = self.db.cursor.fetchone()
            tid = row[0]

            self.db.cursor.execute("INSERT INTO Результаты(ID_матча, Результат, Доп_информация) "
                                   "VALUES(" + str(tid) + ",'" + str(h)+"-"+str(a) + "', '-')")
            self.db.cnxn.commit()
            self.wind = resultsWindow()
            self.wind.show()
            self.close()
