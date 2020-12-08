from results import Ui_MainWindow as resultsMain

from PyQt5 import QtWidgets, QtCore
import menuFanWindow
import playerMenuWindow
import coachMenuWindow
import managerMenuWindow
import properties
import sql

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

        self.ui.backButton.clicked.connect(self.backButton_clicked)

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
