from PyQt5 import QtWidgets, QtCore, Qt

import teamWindow
import properties
import sql
import coachMenuWindow
import playerMenuWindow
from training import Ui_MainWindow as trainingMain


class trainingWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = trainingMain()
        self.ui.setupUi(self)
        header = self.ui.currentTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header = self.ui.historyTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.addBox.hide()
        self.ui.noTrainingLabel.hide()
        self.setWindowTitle("Расписание тренировок")
        self.ui.trainings.setCurrentIndex(0)
        self.ui.backButton.clicked.connect(self.backButton_clicked)
        self.ui.addButton1.clicked.connect(self.addButton1_clicked)
        self.ui.addButton2.clicked.connect(self.addButton2_clicked)
        self.ui.commonTraining.stateChanged.connect(self.commonTrainingHandler)
        self.ui.trainings.currentChanged.connect(self.tabChangedHandler)
        self.ui.fromDate.dateChanged.connect(self.fromDateHandler)
        self.ui.toDate.dateChanged.connect(self.toDateHandler)
        self.ui.searchButton.clicked.connect(self.searchButton_clicked)
        self.ui.resetButton.clicked.connect(self.resetButton_clicked)
        self.ui.fromDate.setDate(QtCore.QDate.currentDate())
        self.ui.toDate.setDate(QtCore.QDate.currentDate().addDays(1))
        self.ui.dateTrain.setDate(QtCore.QDate.currentDate())

        self.db = sql.Sql("football_club")
        uid = 0
        if properties.current_role == 3:
            self.db.cursor.execute("SELECT Номер_футболиста from Футболисты where ID_пользователя=" + str(properties.current_userID))
            row = self.db.cursor.fetchone()
            uid = row[0]
            self.ui.addButton1.hide()
            self.ui.addBox.hide()
            header = self.ui.currentTable.setHorizontalHeaderLabels(["Футболист", "Дата", "Тренер", "Описание"])
            header = self.ui.historyTable.setHorizontalHeaderLabels(["Футболист", "Дата", "Тренер", "Описание"])
            self.ui.currentTable.setRowCount(0)
            sqlt = """
            if object_id(N'tempdb..#t12',N'U') is not null drop table #t12
            SET NOCOUNT ON
            create table #t12(p1 varchar(max),p2 smalldatetime,p3 varchar(max),p4 varchar(max))
            insert #t12 exec GetTrainingPlayer ?, ?
            select * from #t12
            """
            params = (str(uid), str(0))
            self.db.cursor.execute(sqlt, params)
            row = self.db.cursor.fetchone()
            if (row is not None):
                i = 0
                while (row is not None):
                    self.ui.currentTable.setRowCount(self.ui.currentTable.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.currentTable.setVerticalHeaderItem(i, item)
                    for j in range(4):
                        self.ui.currentTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                        self.ui.currentTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1

            else:
                self.ui.currentTable.hide()
                self.ui.noTrainingLabel.show()

        elif properties.current_role == 2:
            self.db.cursor.execute(
                "SELECT ID_специалиста, Должность, ID_команды from Тренеры_и_персонал where ID_пользователя=" + str(properties.current_userID))
            row = self.db.cursor.fetchone()
            uid = row[0]
            work = row[1]
            kom = row[2]
            self.ui.addButton1.show()
            if (work.rstrip() == "Главный тренер"):
                if (kom == 1):
                    self.ui.currentTable.setRowCount(0)
                    self.db.cursor.execute("SELECT t.ФИО, Дата, 'Все', Описание  FROM Тренеры_и_персонал t, Общие_тренировки where t.ID_пользователя= " +
                                           str(uid) +
                                           " UNION SELECT t.ФИО, Дата, p.ФИО, Описание FROM Индивидуальные_тренировки i, Тренеры_и_персонал t, Футболисты p "
                                           "where t.ID_специалиста = i.ID_тренера and p.ID_футболиста = i.ID_футболиста "
                                           "ORDER BY Дата")
                    row = self.db.cursor.fetchone()
                    if (row is not None):
                        i = 0
                        while (row is not None):
                            self.ui.currentTable.setRowCount(self.ui.currentTable.rowCount() + 1)
                            item = QtWidgets.QTableWidgetItem()
                            self.ui.currentTable.setVerticalHeaderItem(i, item)
                            for j in range(4):
                                self.ui.currentTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                                self.ui.currentTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                            row = self.db.cursor.fetchone()
                            i += 1

                    else:
                        self.ui.currentTable.hide()
                        self.ui.noTrainingLabel.show()

            else:
                self.ui.currentTable.setRowCount(0)
                sqlt = """
                            if object_id(N'tempdb..#t12',N'U') is not null drop table #t12
                            SET NOCOUNT ON
                            create table #t12(p1 varchar(max),p2 smalldatetime,p3 varchar(max),p4 varchar(max))
                            insert #t12 exec GetTrainingCoach ?, ?
                            select * from #t12
                            """
                params = (str(uid), str(0))
                self.db.cursor.execute(sqlt, params)
                row = self.db.cursor.fetchone()
                if (row is not None):
                    i = 0
                    while (row is not None):
                        self.ui.currentTable.setRowCount(self.ui.currentTable.rowCount() + 1)
                        item = QtWidgets.QTableWidgetItem()
                        self.ui.currentTable.setVerticalHeaderItem(i, item)
                        for j in range(4):
                            self.ui.currentTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                            self.ui.currentTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                        row = self.db.cursor.fetchone()
                        i += 1
                else:
                    self.ui.currentTable.hide()
                    self.ui.noTrainingLabel.show()

    def backButton_clicked(self):
        if (properties.current_role == 2):
            self.menu = coachMenuWindow.coachMenuWindow()
        elif (properties.current_role == 3):
            self.menu = playerMenuWindow.playerMenuWindow()

        self.menu.show()
        self.close()

    def addButton1_clicked(self):
        self.ui.addBox.show()
        self.db.cursor.execute(
            "SELECT ФИО, Номер_футболиста from Футболисты order by Номер_футболиста")

        row = self.db.cursor.fetchone()
        while (row is not None):
            m = str(row[1]) + ". " + row[0].rstrip()
            self.ui.playerCombo.addItem(m)
            row = self.db.cursor.fetchone()

        self.db.cursor.execute(
            "SELECT ID_специалиста, Должность, ID_команды from Тренеры_и_персонал where ID_пользователя=" + str(
                properties.current_userID))
        row = self.db.cursor.fetchone()
        uid = row[0]
        work = row[1]
        kom = row[2]
        self.ui.addButton1.show()
        if (work.rstrip() == "Главный тренер"):
            if (kom == 1):
                self.db.cursor.execute(
                    "SELECT ФИО from Тренеры_и_персонал where ID_команды=" + str(1))
                row = self.db.cursor.fetchone()
                while (row is not None):
                    self.ui.coachCombo.addItem(row[0])
                    row = self.db.cursor.fetchone()
        else:
            self.db.cursor.execute(
            "SELECT ФИО from Тренеры_и_персонал where ID_пользователя=" + str(properties.current_userID))
            row = self.db.cursor.fetchone()
            while (row is not None):
                self.ui.coachCombo.addItem(row[0])
                row = self.db.cursor.fetchone()

        self.ui.addButton1.hide()

    def tabChangedHandler(self, index):
        if (index == 0):
            uid = 0
            if properties.current_role == 3:
                self.db.cursor.execute(
                    "SELECT Номер_футболиста from Футболисты where ID_пользователя=" + str(properties.current_userID))
                row = self.db.cursor.fetchone()
                uid = row[0]
                self.ui.addButton1.hide()
                self.ui.addBox.hide()
                self.ui.currentTable.setRowCount(0)
                sqlt = """
                        if object_id(N'tempdb..#t12',N'U') is not null drop table #t12
                        SET NOCOUNT ON
                        create table #t12(p1 varchar(max),p2 smalldatetime,p3 varchar(max),p4 varchar(max))
                        insert #t12 exec GetTrainingPlayer ?, ?
                        select * from #t12
                        """
                params = (str(uid), str(0))
                self.db.cursor.execute(sqlt, params)
                row = self.db.cursor.fetchone()
                if (row is not None):
                    i = 0
                    while (row is not None):
                        self.ui.currentTable.setRowCount(self.ui.currentTable.rowCount() + 1)
                        item = QtWidgets.QTableWidgetItem()
                        self.ui.currentTable.setVerticalHeaderItem(i, item)
                        for j in range(4):
                            self.ui.currentTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                            self.ui.currentTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                        row = self.db.cursor.fetchone()
                        i += 1

                else:
                    self.ui.currentTable.hide()
                    self.ui.noTrainingLabel.show()

            elif properties.current_role == 2:
                self.db.cursor.execute(
                    "SELECT ID_специалиста, Должность, ID_команды from Тренеры_и_персонал where ID_пользователя=" + str(
                        properties.current_userID))
                row = self.db.cursor.fetchone()
                uid = row[0]
                work = row[1]
                kom = row[2]
                self.ui.addButton1.show()
                if (work.rstrip() == "Главный тренер"):
                    if (kom == 1):
                        self.ui.currentTable.setRowCount(0)
                        self.db.cursor.execute(
                            "SELECT t.ФИО, Дата, 'Все', Описание  FROM Тренеры_и_персонал t, Общие_тренировки where t.ID_пользователя= " +
                            str(uid) +
                            " UNION SELECT t.ФИО, Дата, p.ФИО, Описание FROM Индивидуальные_тренировки i, Тренеры_и_персонал t, Футболисты p "
                            "where t.ID_специалиста = i.ID_тренера and p.ID_футболиста = i.ID_футболиста "
                            "ORDER BY Дата")
                        row = self.db.cursor.fetchone()
                        if (row is not None):
                            i = 0
                            while (row is not None):
                                self.ui.currentTable.setRowCount(self.ui.currentTable.rowCount() + 1)
                                item = QtWidgets.QTableWidgetItem()
                                self.ui.currentTable.setVerticalHeaderItem(i, item)
                                for j in range(4):
                                    self.ui.currentTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                                    self.ui.currentTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                                row = self.db.cursor.fetchone()
                                i += 1

                        else:
                            self.ui.currentTable.hide()
                            self.ui.noTrainingLabel.show()

                else:
                    self.ui.currentTable.setRowCount(0)
                    sqlt = """
                                        if object_id(N'tempdb..#t12',N'U') is not null drop table #t12
                                        SET NOCOUNT ON
                                        create table #t12(p1 varchar(max),p2 smalldatetime,p3 varchar(max),p4 varchar(max))
                                        insert #t12 exec GetTrainingCoach ?, ?
                                        select * from #t12
                                        """
                    params = (str(uid), str(0))
                    self.db.cursor.execute(sqlt, params)
                    row = self.db.cursor.fetchone()
                    if (row is not None):
                        i = 0
                        while (row is not None):
                            self.ui.currentTable.setRowCount(self.ui.currentTable.rowCount() + 1)
                            item = QtWidgets.QTableWidgetItem()
                            self.ui.currentTable.setVerticalHeaderItem(i, item)
                            for j in range(4):
                                self.ui.currentTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                                self.ui.currentTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                            row = self.db.cursor.fetchone()
                            i += 1
                    else:
                        self.ui.currentTable.hide()
                        self.ui.noTrainingLabel.show()

        elif (index == 1):
            uid = 0
            self.ui.historyLabel.close()
            if properties.current_role == 3:
                self.db.cursor.execute(
                    "SELECT Номер_футболиста from Футболисты where ID_пользователя=" + str(properties.current_userID))
                row = self.db.cursor.fetchone()
                uid = row[0]
                self.ui.historyTable.setRowCount(0)
                sqlt = """
                        if object_id(N'tempdb..#t12',N'U') is not null drop table #t12
                        SET NOCOUNT ON
                        create table #t12(p1 varchar(max),p2 smalldatetime,p3 varchar(max),p4 varchar(max))
                        insert #t12 exec GetTrainingPlayer ?, ?
                        select * from #t12
                        """
                params = (str(uid), str(1))
                self.db.cursor.execute(sqlt, params)
                row = self.db.cursor.fetchone()
                if (row is not None):
                    i = 0
                    while (row is not None):
                        self.ui.historyTable.setRowCount(self.ui.historyTable.rowCount() + 1)
                        item = QtWidgets.QTableWidgetItem()
                        self.ui.historyTable.setVerticalHeaderItem(i, item)
                        for j in range(4):
                            self.ui.historyTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                            self.ui.historyTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                        row = self.db.cursor.fetchone()
                        i += 1

                else:
                    self.ui.historyTable.hide()
                    self.ui.noTrainingLabel.show()

            elif properties.current_role == 2:
                self.db.cursor.execute(
                    "SELECT ID_специалиста, Должность, ID_команды from Тренеры_и_персонал where ID_пользователя=" + str(
                        properties.current_userID))
                row = self.db.cursor.fetchone()
                uid = row[0]
                work = row[1]
                kom = row[2]
                self.ui.addButton1.show()
                if (work.rstrip() == "Главный тренер"):
                    if (kom == 1):
                        self.ui.historyTable.setRowCount(0)
                        self.db.cursor.execute(
                            "SELECT t.ФИО, Дата, 'Все', Описание  FROM Тренеры_и_персонал t, Общие_тренировки where t.ID_пользователя= " +
                            str(uid) +
                            " UNION SELECT t.ФИО, Дата, p.ФИО, Описание FROM Индивидуальные_тренировки i, Тренеры_и_персонал t, Футболисты p "
                            "where t.ID_специалиста = i.ID_тренера and p.ID_футболиста = i.ID_футболиста "
                            "ORDER BY Дата")
                        row = self.db.cursor.fetchone()
                        if (row is not None):
                            i = 0
                            while (row is not None):
                                self.ui.historyTable.setRowCount(self.ui.historyTable.rowCount() + 1)
                                item = QtWidgets.QTableWidgetItem()
                                self.ui.historyTable.setVerticalHeaderItem(i, item)
                                for j in range(4):
                                    self.ui.historyTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                                    self.ui.historyTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                                row = self.db.cursor.fetchone()
                                i += 1

                        else:
                            self.ui.historyTable.hide()
                            self.ui.noTrainingLabel.show()

                else:
                    self.ui.historyTable.setRowCount(0)
                    sqlt = """
                                        if object_id(N'tempdb..#t12',N'U') is not null drop table #t12
                                        SET NOCOUNT ON
                                        create table #t12(p1 varchar(max),p2 smalldatetime,p3 varchar(max),p4 varchar(max))
                                        insert #t12 exec GetTrainingCoach ?, ?
                                        select * from #t12
                                        """
                    params = (str(uid), str(1))
                    self.db.cursor.execute(sqlt, params)
                    row = self.db.cursor.fetchone()
                    if (row is not None):
                        i = 0
                        while (row is not None):
                            self.ui.historyTable.setRowCount(self.ui.historyTable.rowCount() + 1)
                            item = QtWidgets.QTableWidgetItem()
                            self.ui.historyTable.setVerticalHeaderItem(i, item)
                            for j in range(4):
                                self.ui.historyTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                                self.ui.historyTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                            row = self.db.cursor.fetchone()
                            i += 1
                    else:
                        self.ui.historyTable.hide()
                        self.ui.historyLabel.show()


    def addButton2_clicked(self):
        f = self.ui.playerCombo.currentText()
        t = self.ui.coachCombo.currentText()
        d1 = self.ui.dateTrain.text()
        i = self.ui.infoText.toPlainText()
        if (i.strip() == "" or i is None):
            i = "-"
        if ((f.strip() == "" or t.strip() == "") and self.ui.commonTraining.isChecked() is False):
            message = "Необходимо заполнить каждое поле"
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Пустое поле")
            error_message.showMessage(message)
        else:
            if (self.ui.commonTraining.isChecked()):
                self.db.cursor.execute("select COUNT(*) from Общие_тренировки where DATEDIFF(DAY, Дата,'"+d1+"')=0")
                row = self.db.cursor.fetchone()
                if (row[0] >= 3):
                    message = "Превышено число общих тренировок в день"
                    error_message = QtWidgets.QErrorMessage(self)
                    error_message.setModal(True)
                    error_message.setWindowTitle("Максимальное число тренировок")
                    error_message.showMessage(message)
                else:
                    self.db.cursor.execute(
                    "INSERT INTO Общие_тренировки(Дата, Описание) "
                    "VALUES('" + d1 + "', '" + i + "')")
                    self.db.cnxn.commit()
                    self.wind = trainingWindow()
                    self.wind.show()
                    self.close()
            else:
                if (f[2] == "."):
                    f = f[0:2]
                else:
                    f = f[0]

                self.db.cursor.execute("SELECT ID_футболиста from Футболисты where Номер_футболиста=" + str(f))
                row = self.db.cursor.fetchone()
                pid = row[0]
                self.db.cursor.execute("select COUNT(*) from Индивидуальные_тренировки where ID_футболиста="+str(pid)+" and DATEDIFF(DAY, Дата,'" + d1 + "')=0")
                row = self.db.cursor.fetchone()
                if (row[0] >= 3):
                    message = "Превышено число индивидуальных тренировок в день"
                    error_message = QtWidgets.QErrorMessage(self)
                    error_message.setModal(True)
                    error_message.setWindowTitle("Максимальное число тренировок")
                    error_message.showMessage(message)
                else:
                    self.db.cursor.execute("SELECT ID_специалиста from Тренеры_и_персонал where ФИО='" + t.rstrip()+"'")
                    row = self.db.cursor.fetchone()
                    tid = row[0]
                    self.db.cursor.execute(
                    "INSERT INTO Индивидуальные_тренировки(ID_футболиста, Дата, ID_тренера, Описание) "
                    "VALUES(" + str(pid)+ ", '" + d1 + "'," + str(tid) + ", '"+ i +"')")
                    self.db.cnxn.commit()
                    self.wind = trainingWindow()
                    self.wind.show()
                    self.close()

    def searchButton_clicked(self):
        self.ui.historyTable.show()
        self.ui.historyTable.setRowCount(0)
        self.ui.historyLabel.hide()
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
            self.ui.historyLabel.show()

    def resetButton_clicked(self):
        self.ui.fromDate.setDate(QtCore.QDate.currentDate())
        self.ui.toDate.setDate(QtCore.QDate.currentDate().addDays(1))
        self.ui.historyTable.show()
        self.ui.historyTable.setRowCount(0)
        uid = 0
        self.ui.historyLabel.close()
        if properties.current_role == 3:
            self.db.cursor.execute(
                "SELECT Номер_футболиста from Футболисты where ID_пользователя=" + str(properties.current_userID))
            row = self.db.cursor.fetchone()
            uid = row[0]
            self.ui.historyTable.setRowCount(0)
            sqlt = """
                                if object_id(N'tempdb..#t12',N'U') is not null drop table #t12
                                SET NOCOUNT ON
                                create table #t12(p1 varchar(max),p2 smalldatetime,p3 varchar(max),p4 varchar(max))
                                insert #t12 exec GetTrainingPlayer ?, ?
                                select * from #t12
                                """
            params = (str(uid), str(1))
            self.db.cursor.execute(sqlt, params)
            row = self.db.cursor.fetchone()
            if (row is not None):
                i = 0
                while (row is not None):
                    self.ui.historyTable.setRowCount(self.ui.historyTable.rowCount() + 1)
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.historyTable.setVerticalHeaderItem(i, item)
                    for j in range(4):
                        self.ui.historyTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                        self.ui.historyTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                    row = self.db.cursor.fetchone()
                    i += 1

            else:
                self.ui.historyTable.hide()
                self.ui.noTrainingLabel.show()

        elif properties.current_role == 2:
            self.db.cursor.execute(
                "SELECT ID_специалиста, Должность, ID_команды from Тренеры_и_персонал where ID_пользователя=" + str(
                    properties.current_userID))
            row = self.db.cursor.fetchone()
            uid = row[0]
            work = row[1]
            kom = row[2]
            self.ui.addButton1.show()
            if (work.rstrip() == "Главный тренер"):
                if (kom == 1):
                    self.ui.historyTable.setRowCount(0)
                    self.db.cursor.execute(
                        "SELECT t.ФИО, Дата, 'Все', Описание  FROM Тренеры_и_персонал t, Общие_тренировки where t.ID_пользователя= " +
                        str(uid) +
                        " UNION SELECT t.ФИО, Дата, p.ФИО, Описание FROM Индивидуальные_тренировки i, Тренеры_и_персонал t, Футболисты p "
                        "where t.ID_специалиста = i.ID_тренера and p.ID_футболиста = i.ID_футболиста "
                        "ORDER BY Дата")
                    row = self.db.cursor.fetchone()
                    if (row is not None):
                        i = 0
                        while (row is not None):
                            self.ui.historyTable.setRowCount(self.ui.historyTable.rowCount() + 1)
                            item = QtWidgets.QTableWidgetItem()
                            self.ui.historyTable.setVerticalHeaderItem(i, item)
                            for j in range(4):
                                self.ui.historyTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                                self.ui.historyTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                            row = self.db.cursor.fetchone()
                            i += 1

                    else:
                        self.ui.historyTable.hide()
                        self.ui.noTrainingLabel.show()

            else:
                self.ui.historyTable.setRowCount(0)
                sqlt = """
                                                if object_id(N'tempdb..#t12',N'U') is not null drop table #t12
                                                SET NOCOUNT ON
                                                create table #t12(p1 varchar(max),p2 smalldatetime,p3 varchar(max),p4 varchar(max))
                                                insert #t12 exec GetTrainingCoach ?, ?
                                                select * from #t12
                                                """
                params = (str(uid), str(1))
                self.db.cursor.execute(sqlt, params)
                row = self.db.cursor.fetchone()
                if (row is not None):
                    i = 0
                    while (row is not None):
                        self.ui.historyTable.setRowCount(self.ui.historyTable.rowCount() + 1)
                        item = QtWidgets.QTableWidgetItem()
                        self.ui.historyTable.setVerticalHeaderItem(i, item)
                        for j in range(4):
                            self.ui.historyTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(row[j]).rstrip()))
                            self.ui.historyTable.item(i, j).setFlags(QtCore.Qt.NoItemFlags)
                        row = self.db.cursor.fetchone()
                        i += 1
                else:
                    self.ui.historyTable.hide()
                    self.ui.historyLabel.show()

    def commonTrainingHandler(self):
        if (self.ui.commonTraining.isChecked()):
            self.ui.coachCombo.setEnabled(False)
            self.ui.playerCombo.setEnabled(False)
        else:
            self.ui.coachCombo.setEnabled(True)
            self.ui.playerCombo.setEnabled(True)


    def fromDateHandler(self, date):
        self.ui.toDate.setMinimumDate(date.addDays(1))

    def toDateHandler(self, date):
        self.ui.fromDate.setMaximumDate(date.addDays(-1))

