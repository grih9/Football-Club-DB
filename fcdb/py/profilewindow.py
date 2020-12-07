from PyQt5 import QtWidgets, QtCore

import properties
from cryptography.fernet import Fernet
import managerMenuWindow
import menuFanWindow
import playerMenuWindow
import coachMenuWindow
from profile import Ui_MainWindow as profileMain
import sql


class profilewindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.cipher = Fernet(properties.cipher_key)
        self.ui = profileMain()
        self.ui.setupUi(self)
        self.setWindowTitle("Профиль")
        self.ui.backButton.clicked.connect(self.backButton_clicked)
        self.ui.showPassword.pressed.connect(self.showPassword_pressed)
        self.ui.showPassword.released.connect(self.showPassword_released)
        self.db = sql.Sql("football_club")
        self.db.cursor.execute("SELECT Логин FROM Пользователи where ID_пользователя =" + str(properties.current_userID))
        row = self.db.cursor.fetchone()
        login = row[0]
        if (properties.current_role == 1):
            self.ui.roleLabel.setText("Руководство")
            self.db.cursor.execute("SELECT ФИО, Дата_рождения, Национальность FROM Руководство where ID_пользователя =" + str(properties.current_userID))
            row = self.db.cursor.fetchone()
            birthday = None
            fio = None
            nationality = None
            if (row is not None):
                fio = row[0]
                birthday = row[1]
                nationality = row[2]
            self.ui.loginLabel.setText(login)
            if (row is None) or (birthday is None):
                self.ui.birthdayLabel.setText("---")
            else:
                self.ui.birthdayLabel.setText(birthday)

            if (row is None) or (fio is None):
                self.ui.infoBox.setTitle("")
            else:
                self.ui.infoBox.setTitle(fio.rstrip())

            if (row is None) or (nationality is None):
                self.ui.nationalityLabel.setText("---")
            else:
                self.ui.nationalityLabel.setText(nationality)
            self.ui.passwordLabel.setText("******")
            self.ui.posOrGender.hide()
            self.ui.position_genderLabel.hide()
            self.ui.height.hide()
            self.ui.heightLabel.hide()
            self.ui.weightLabel.hide()
            self.ui.weight.hide()
            self.ui.number.hide()
            self.ui.salary.hide()
            self.ui.salaryLabel.hide()
            self.ui.expireDate.hide()
            self.ui.expireDateLabel.hide()
            self.ui.numberLabel.hide()
            self.ui.work.hide()
            self.ui.workLabel.hide()
        elif (properties.current_role == 2):
            self.ui.roleLabel.setText("Тренерский штаб")
            self.db.cursor.execute(
                "SELECT ФИО, Дата_рождения, Должность, Национальность FROM Тренеры_и_персонал where ID_пользователя =" + str(properties.current_userID))
            row = self.db.cursor.fetchone()
            fio = row[0]
            birthday = row[1]
            work = row[2]
            nationality = row[3]
            self.ui.loginLabel.setText(login)
            self.ui.birthdayLabel.setText(birthday)
            self.ui.infoBox.setTitle(fio.rstrip())
            self.ui.passwordLabel.setText("******")
            self.ui.height.hide()
            self.ui.heightLabel.hide()
            self.ui.nationalityLabel.setText(nationality)
            self.ui.weightLabel.hide()
            self.ui.weight.hide()
            self.ui.posOrGender.hide()
            self.ui.position_genderLabel.hide()
            self.ui.salary.hide()
            self.ui.salaryLabel.hide()
            self.ui.expireDate.hide()
            self.ui.expireDateLabel.hide()
            self.ui.number.hide()
            self.ui.numberLabel.hide()
            self.ui.workLabel.setText(work)
        elif (properties.current_role == 3):
            self.ui.roleLabel.setText("Футболист")
            self.db.cursor.execute(
                "SELECT ФИО, Номер_футболиста, Дата_рождения, Позиция, Национальность, Рост, Вес, ID_футболиста"
                " FROM Футболисты where ID_пользователя =" + str(properties.current_userID))
            row = self.db.cursor.fetchone()
            fio = row[0]
            number = row[1]
            birthday = row[2]
            position = row[3]
            nationality = row[4]
            height = row[5]
            weight = row[6]
            fid = row[7]
            self.db.cursor.execute(
                "SELECT Зарплата, Дата_окончания"
                " FROM Контракты where ID_футболиста =" + str(fid))
            row = self.db.cursor.fetchone()
            salary = row[0]
            expDate = row[1]
            salary = str(round(salary,2))
            self.ui.salaryLabel.setText(salary + "m €/год")
            self.ui.expireDateLabel.setText(expDate)
            self.ui.loginLabel.setText(login)
            self.ui.birthdayLabel.setText(birthday)
            self.ui.infoBox.setTitle(fio.rstrip())
            self.ui.posOrGender.setText("Позиция:")
            self.ui.position_genderLabel.setText(position)
            self.ui.passwordLabel.setText("******")
            self.ui.heightLabel.setText(str(height))
            self.ui.nationalityLabel.setText(nationality)
            self.ui.weightLabel.setText(str(weight))
            self.ui.numberLabel.setText(str(number))
            self.ui.work.hide()
            self.ui.workLabel.hide()
        elif (properties.current_role == 4):
            self.ui.roleLabel.setText("Болельщик")
            self.db.cursor.execute("SELECT ФИО, Пол, Дата_рождения FROM Болельщики where ID_пользователя =" + str(properties.current_userID))
            row = self.db.cursor.fetchone()
            fio = row[0]
            gender = row[1]
            birthday = row[2]
            self.ui.loginLabel.setText(login)
            self.ui.birthdayLabel.setText(birthday)
            self.ui.infoBox.setTitle(fio.rstrip())
            self.ui.birthday.setGeometry(QtCore.QRect(20, 50, 220, 50))
            self.ui.birthdayLabel.setGeometry(QtCore.QRect(250, 50, 171, 50))
            self.ui.posOrGender.setText("Пол:")
            self.ui.posOrGender.setGeometry(QtCore.QRect(165, 110, 80, 50))
            self.ui.position_genderLabel.setGeometry(QtCore.QRect(250, 110, 21, 50))
            self.ui.position_genderLabel.setText("М")
            self.ui.passwordLabel.setText("******")
            self.ui.height.hide()
            self.ui.heightLabel.hide()
            self.ui.salary.hide()
            self.ui.salaryLabel.hide()
            self.ui.expireDate.hide()
            self.ui.expireDateLabel.hide()
            self.ui.nationality.hide()
            self.ui.nationalityLabel.hide()
            self.ui.weightLabel.hide()
            self.ui.weight.hide()
            self.ui.work.hide()
            self.ui.workLabel.hide()
            self.ui.number.hide()
            self.ui.numberLabel.hide()
        self.db.cnxn.close()

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

    def showPassword_pressed(self):
        self.db = sql.Sql("football_club")
        self.db.cursor.execute("SELECT Пароль FROM Пользователи where ID_пользователя =" + str(properties.current_userID))
        row = self.db.cursor.fetchone()
        p = self.cipher.decrypt(str.encode(row[0])).decode('utf8')
        self.ui.passwordLabel.setText(p)
        self.db.cnxn.close()

    def showPassword_released(self):
        self.ui.passwordLabel.setText("******")