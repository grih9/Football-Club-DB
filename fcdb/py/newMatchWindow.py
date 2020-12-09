from PyQt5 import QtWidgets, QtCore

import managerManagingWindow
import sql
from newMatch import Ui_MainWindow as newMatchMain
import resultsWindow


class newMatchWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = newMatchMain()
        self.ui.setupUi(self)
        self.stadiums = list()
        self.setWindowTitle("Создание матча")
        self.ui.backButton.clicked.connect(self.backButton_clicked)
        self.ui.createButton.clicked.connect(self.createButton_clicked)
        self.ui.teamCombo.currentIndexChanged.connect(self.teamComboHandler)
        self.db = sql.Sql("football_club")
        self.ui.teamCombo.clear()
        self.ui.teamCombo.addItem("")
        self.ui.date.setDate(QtCore.QDate.currentDate())
        self.ui.date.setMinimumDate(QtCore.QDate.currentDate())
        self.stadiums = list()
        self.stadiums.append("")
        self.db.cursor.execute(
            "SELECT Команда, ID_стадиона FROM Команды where Команда != 'Манчестер Юнайтед' order by Команда ASC")
        row = self.db.cursor.fetchone()
        while (row is not None):
            self.ui.teamCombo.addItem(row[0].rstrip())
            self.stadiums.append(row[1])
            row = self.db.cursor.fetchone()
        self.ui.stadiumCombo.clear()
        for elem in self.stadiums:
            if elem == "":
                self.ui.stadiumCombo.addItem(elem)
                continue
            self.db.cursor.execute("SELECT Название from Стадионы where ID_стадиона =" + str(elem))
            row = self.db.cursor.fetchone()
            val = row[0]
            self.ui.stadiumCombo.addItem(val)

    def teamComboHandler(self, index):
        if index == 0:
            self.ui.stadiumCombo.clear()
            for elem in self.stadiums:
                if elem == "":
                    self.ui.stadiumCombo.addItem(elem)
                    continue
                self.db.cursor.execute("SELECT Название from Стадионы where ID_стадиона =" + str(elem))
                row = self.db.cursor.fetchone()
                val = row[0]
                self.ui.stadiumCombo.addItem(val)
        else:
            self.ui.stadiumCombo.clear()
            self.ui.stadiumCombo.addItem("")
            if (index != 0 and index != -1):
                val = self.stadiums[index]
                self.db.cursor.execute("SELECT Название from Стадионы where ID_стадиона=" + str(val))
                row = self.db.cursor.fetchone()
                val = row[0]
                self.ui.stadiumCombo.addItem(val)
            self.ui.stadiumCombo.addItem("Олд Траффорд")

    def backButton_clicked(self):
        self.manager = resultsWindow.resultsWindow()
        self.manager.show()
        self.close()

    def createButton_clicked(self):
        t = self.ui.teamCombo.currentText()
        d = self.ui.date.text()
        s = self.ui.stadiumCombo.currentText()
        c = self.ui.typeCombo.currentText()
        i = self.ui.infoText.toPlainText()
        if i.strip() == "":
            i = "-"
        if t == "" or s == "" or c == "":
            message = "Необходимо выбрать стадион, соперника и тип матча."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Пустое поле")
            error_message.showMessage(message)
        else:
            self.db.cursor.execute("select COUNT(*) from Календарь where DATEDIFF(DAY, Дата,'"+ d +"')=0")
            row =self.db.cursor.fetchone()
            counter = row[0]
            if (counter >= 1):
                message = "В этот день уже назначен матч. Выберите другой день"
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setModal(True)
                error_message.setWindowTitle("Пустое поле")
                error_message.showMessage(message)
            else:
                self.db.cursor.execute("SELECT ID_команды from Команды where Команда = '" + t.rstrip() + "'")
                row = self.db.cursor.fetchone()
                tid = row[0]
                self.db.cursor.execute("SELECT ID_стадиона from Стадионы where Название = '" + s.rstrip() + "'")
                row = self.db.cursor.fetchone()
                sid = row[0]

                self.db.cursor.execute("INSERT INTO Календарь(ID_соперника, Тип, Дата, ID_стадиона, Доп_информация) "
                                       "VALUES(" + str(tid) + ",'" + c + "', '" +str(d)+ "', " + str(sid) + ", '" +i +"')")
                self.db.cnxn.commit()
                self.wind = resultsWindow.resultsWindow()
                self.wind.show()
                self.close()







