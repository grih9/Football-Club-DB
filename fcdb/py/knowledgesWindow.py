from knowledges import Ui_MainWindow as knowledgesMain
from PyQt5 import QtWidgets, QtCore
import menuFanWindow
import playerMenuWindow
import coachMenuWindow
import managerMenuWindow
import properties
import sql

class knowledgesWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = knowledgesMain()
        self.ui.setupUi(self)
        header = self.ui.teamsTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header = self.ui.coachesTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header = self.ui.ownersTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header = self.ui.stadiumsTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.setWindowTitle("База знаний")
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.backButton.clicked.connect(self.backButton_clicked)
        self.ui.tabWidget.currentChanged.connect(self.tabChangedHandler)
        self.db = sql.Sql("football_club")
        self.db.cursor.execute(
            "SELECT k.Команда, k.Страна, k.Город, s.Название, t.ФИО, v.ФИО, k.Контакты FROM Команды k "
            "join Стадионы s on s.ID_стадиона = k.ID_стадиона "
            "left join Тренеры_и_персонал t on t.ID_cпециалиста= k.ID_главного_тренера "
            "left join Руководство v on v.ID_владельца = k.ID_владельца")

        row = self.db.cursor.fetchone()
        i = 0
        while (row is not None):
            self.ui.teamsTable.setRowCount(self.ui.teamsTable.rowCount() + 1)
            item = QtWidgets.QTableWidgetItem()
            self.ui.teamsTable.setVerticalHeaderItem(i, item)
            for j in range(7):
                if (row[j] is None):
                    self.ui.teamsTable.setItem(i, j, QtWidgets.QTableWidgetItem("-"))
                elif (((j == 5) or (j == 4)) and row[j].rstrip() == "Другой"):
                    self.ui.teamsTable.setItem(i, j, QtWidgets.QTableWidgetItem("-"))
                else:
                    self.ui.teamsTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                self.ui.teamsTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
            row = self.db.cursor.fetchone()
            i += 1

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
            self.ui.teamsTable.setRowCount(0)
            self.db.cursor.execute(
                "SELECT k.Команда, k.Страна, k.Город, s.Название, t.ФИО, v.ФИО, k.Контакты FROM Команды k "
                "join Стадионы s on s.ID_стадиона = k.ID_стадиона "
                "left join Тренеры_и_персонал t on t.ID_cпециалиста= k.ID_главного_тренера "
                "left join Руководство v on v.ID_владельца = k.ID_владельца")

            row = self.db.cursor.fetchone()
            i = 0
            while (row is not None):
                self.ui.teamsTable.setRowCount(self.ui.teamsTable.rowCount() + 1)
                item = QtWidgets.QTableWidgetItem()
                self.ui.teamsTable.setVerticalHeaderItem(i, item)
                for j in range(7):
                    if (row[j] is None):
                        self.ui.teamsTable.setItem(i, j, QtWidgets.QTableWidgetItem("-"))
                    elif (((j == 5) or (j == 4)) and row[j].rstrip() == "Другой"):
                        self.ui.teamsTable.setItem(i, j, QtWidgets.QTableWidgetItem("-"))
                    else:
                        self.ui.teamsTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                    self.ui.teamsTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                row = self.db.cursor.fetchone()
                i += 1

        elif (index == 1):
            self.ui.coachesTable.setRowCount(0)
            self.db.cursor.execute(
                "SELECT t.ФИО, t.Национальность, t.Дата_рождения, k.Команда FROM Тренеры_и_персонал t "
                "left join Команды k on t.ID_cпециалиста=k.ID_главного_тренера where t.Должность = 'Главный тренер'")
            row = self.db.cursor.fetchone()
            i = 0
            while (row is not None):
                self.ui.coachesTable.setRowCount(self.ui.coachesTable.rowCount() + 1)
                item = QtWidgets.QTableWidgetItem()
                self.ui.coachesTable.setVerticalHeaderItem(i, item)
                for j in range(4):
                    if row[j] is None:
                        self.ui.coachesTable.setItem(i, j, QtWidgets.QTableWidgetItem("-"))
                    elif (j == 0 and row[j].rstrip() == "Другой"):
                        self.ui.coachesTable.setRowCount(self.ui.coachesTable.rowCount() - 1)
                        i -= 1
                        break
                    else:
                        self.ui.coachesTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                    self.ui.coachesTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                row = self.db.cursor.fetchone()
                i += 1
        elif (index == 2):
            self.ui.ownersTable.setRowCount(0)
            self.db.cursor.execute(
                "SELECT ФИО, Дата_рождения,Национальность FROM Руководство ")
            row = self.db.cursor.fetchone()
            i = 0
            while (row is not None):
                self.ui.ownersTable.setRowCount(self.ui.ownersTable.rowCount() + 1)
                item = QtWidgets.QTableWidgetItem()
                self.ui.ownersTable.setVerticalHeaderItem(i, item)
                for j in range(3):
                    if row[j] is None:
                        self.ui.ownersTable.setItem(i, j, QtWidgets.QTableWidgetItem("-"))
                    elif (j == 0 and row[j].rstrip() == "Другой"):
                        self.ui.ownersTable.setRowCount(self.ui.ownersTable.rowCount() - 1)
                        i -= 1
                        break
                    else:
                        self.ui.ownersTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                    self.ui.ownersTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                row = self.db.cursor.fetchone()
                i += 1
        elif (index == 3):
            self.ui.stadiumsTable.setRowCount(0)
            self.db.cursor.execute(
                "SELECT s.Название, s.Страна, s.Город, s.Вместимость, k.Команда, s.Тип  FROM Стадионы s "
                "LEFT JOIN Команды k on s.ID_Домашней_команды=k.ID_команды")
            row = self.db.cursor.fetchone()
            i = 0
            while (row is not None):
                self.ui.stadiumsTable.setRowCount(self.ui.stadiumsTable.rowCount() + 1)
                item = QtWidgets.QTableWidgetItem()
                self.ui.stadiumsTable.setVerticalHeaderItem(i, item)
                for j in range(6):
                    if row[j] is None:
                        self.ui.stadiumsTable.setItem(i, j, QtWidgets.QTableWidgetItem("-"))
                    else:
                        self.ui.stadiumsTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                    self.ui.stadiumsTable.item(i,j).setFlags(QtCore.Qt.NoItemFlags)
                row = self.db.cursor.fetchone()
                i += 1

