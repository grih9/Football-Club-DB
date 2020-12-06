from PyQt5 import QtWidgets
from startMenu import Ui_MainWindow as startmain
from login import Ui_MainWindow as loginmain
from registerFan import Ui_MainWindow as regFanmain
from managerMenu import Ui_MainWindow as managerMenuMain
from choose import Ui_MainWindow as managerChooseMain
from cryptography.fernet import Fernet
import sys
import pyodbc

current_role = 0
current_userID = 0

class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = startmain()
        self.ui.setupUi(self)
        self.setWindowTitle("Добро пожаловать!")
        self.ui.enterButton.clicked.connect(self.enterButton_clicked)
        self.ui.noAccountButton.clicked.connect(self.noAccount_clicked)
    def enterButton_clicked(self):
        self.login = loginindow()
        self.login.show()
        self.close()
    def noAccount_clicked(self):
        message = 'Создание аккаунта доступно только для болельщиков. ' \
                  'Если Вы не являетесь болельщиком, обратитесь к руководству для создания аккаунта. ' \
                  'Хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Создание профиля болельщика', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.reg = regFanWindow()
            self.reg.show()
            self.close()



class regFanWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = regFanmain()
        self.ui.setupUi(self)
        self.setWindowTitle("Регистрация болельщика")
        self.ui.backButton.clicked.connect(self.backButton_clicked)
        self.ui.passwodCheckbox.stateChanged.connect(self.checkboxHandler)
        self.ui.createAccountButton.clicked.connect(self.createButton_clicked)

    def backButton_clicked(self):
        self.main = mainwindow()
        self.main.show()
        self.close()

    def checkboxHandler(self, state):
        if self.ui.passwodCheckbox.isChecked():
            self.ui.passwordConfirmLine.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.passwordLine.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ui.passwordConfirmLine.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)

    def createButton_clicked(self):
        n = self.ui.nameLine.text()
        s = self.ui.surnameLine.text()
        l = self.ui.loginLine.text()
        p = self.ui.passwordLine.text()
        pp = self.ui.passwordConfirmLine.text()
        m = self.ui.maleRadio.isChecked()
        f = self.ui.femaleRadio.isChecked()
        d = self.ui.birthdayLine.text()
        if (n.strip() == '') \
                or (s.strip() == '')\
                or (l.strip() == '')\
                or (p.strip() == '')\
                or (pp.strip() == '')\
                or (d.strip() == '')\
                or ((m is False) and (f is False)):
            message = "Необходимо заполнить каждое поле"
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Пустое поле")
            error_message.showMessage(message)
            if len(l) != 0 and (l.strip() == ''):
                self.ui.loginLine.clear()
            if len(n) != 0 and (n.strip() == ''):
                self.ui.nameLine.clear()
            if len(s) != 0 and (s.strip() == ''):
                self.ui.surnameLine.clear()
            self.ui.passwordLine.clear()
            self.ui.passwordConfirmLine.clear()
        elif " " in l:
            message = "Недопустимый символ в поле логина - пробел. Проверьте правильность введенных данных."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Ошибка ввода")
            error_message.showMessage(message)
            self.ui.loginLine.clear()
            self.ui.passwordLine.clear()
            self.ui.passwordConfirmLine.clear()
        elif " " in p:
            message = "Недопустимый символ в поле пароля - пробел. Проверьте правильность введенных данных."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Ошибка ввода")
            error_message.showMessage(message)
            self.ui.passwordLine.clear()
            self.ui.passwordConfirmLine.clear()
        elif any(map(str.isdigit, n)):
            message = "Недопустимый символ в поле имени - цифра. Проверьте правильность введенных данных."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Ошибка ввода")
            error_message.showMessage(message)
            self.ui.nameLine.clear()
            self.ui.passwordLine.clear()
            self.ui.passwordConfirmLine.clear()
        elif any(map(str.isdigit, s)):
            message = "Недопустимый символ в поле фамилии - цифра. Проверьте правильность введенных данных."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Ошибка ввода")
            error_message.showMessage(message)
            self.ui.surnameLine.clear()
            self.ui.passwordLine.clear()
            self.ui.passwordConfirmLine.clear()
        elif (p != pp):
            message = "Введенные пароли не совпадают. Проверьте правильность введенных данных."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Ошибка ввода")
            error_message.showMessage(message)
            self.ui.passwordLine.clear()
            self.ui.passwordConfirmLine.clear()
        else:
            self.db = Sql("football_club")
            status, id = addUser(self.db, l, p, 4)

            if (status is False):
                message = "Введенный логин занят. Повторите ввод."
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setWindowTitle("Ошибка ввода")
                error_message.showMessage(message)
                self.ui.loginLine.clear()
                self.ui.passwordLine.clear()
                self.ui.passwordConfirmLine.clear()
                self.db.cnxn.close()
            else:
                if (m is True):
                    gender = "М"
                elif (f is True):
                    gender = "Ж"
                else:
                    gender = "М"
                    print("Неопределенная ошибка ввода пола")

                status = addFan(self.db, id, n, s, gender, d)
                if (status is True):
                    message = 'Аккаунт успешно создан!'
                    reply = QtWidgets.QMessageBox.question(self, 'Успех', message,
                                                           QtWidgets.QMessageBox.Ok)
                    if reply == QtWidgets.QMessageBox.Ok:
                        self.main = mainwindow()
                        self.main.show()
                        self.db.cnxn.close()
                        self.close()
                else:
                    message = "Неопределенная ошибка. Повторите ввод."
                    error_message = QtWidgets.QErrorMessage(self)
                    error_message.setWindowTitle("Ошибка БД")
                    error_message.showMessage(message)
                    self.db.cursor.execute("DELETE FROM Пользователи where Логин='" + l + "'")
                    self.ui.passwordLine.clear()
                    self.ui.passwordConfirmLine.clear()
                    self.db.cnxn.close()



class loginindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loginmain()
        self.ui.setupUi(self)
        self.setWindowTitle("Вход")
        self.ui.enterButton.clicked.connect(self.enterButton_clicked)
        self.ui.backButton.clicked.connect(self.backButton_clicked)
    def enterButton_clicked(self):
        l = self.ui.loginLine.text()
        p = self.ui.passwordLine.text()
        if (l.strip() == ''):
            message = "Поле логина пустое! Введите логин!"
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Ошибка входа")
            error_message.showMessage(message)
            if len(l) != 0:
                self.ui.loginLine.clear()
        elif (p.strip() == ''):
            message = "Поле пароля пустое! Введите пароль!"
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Ошибка входа")
            error_message.showMessage(message)
            if len(p) != 0:
                self.ui.passwordLine.clear()
        elif (l.find(' ') != -1):
            message = "Недопустимый символ в поле логина. Проверьте правильность данных и повторите вход."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Ошибка входа")
            error_message.showMessage(message)
            self.ui.loginLine.clear()
        elif (p.find(' ') != -1):
            message = "Данного пользователя не существует или введен неверный пароль! Проверьте правильность данных и повторите вход."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Ошибка входа")
            error_message.showMessage(message)
            self.ui.passwordLine.clear()
        else:
            self.db =  Sql("football_club")
            status, role, id = checkPassword(self.db, l, p)
            self.db.cnxn.close()
            if (status == False):
                message = "Данного пользователя не существует или введен неверный пароль! Проверьте правильность данных и повторите вход."
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setWindowTitle("Ошибка входа")
                error_message.showMessage(message)
                self.ui.passwordLine.clear()
            else:
                global current_role
                global  current_userID
                current_role = role
                current_userID = id
                if current_role == 1:
                    self.menu = managerMenuWindow()
                    self.menu.show()
                    self.close()

    def backButton_clicked(self):
        self.main = mainwindow()
        self.main.show()
        self.close()


class managerMenuWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = managerMenuMain()
        self.ui.setupUi(self)
        self.setWindowTitle("Руководство")
        self.ui.exitButton.clicked.connect(self.exitButton_clicked)
        self.ui.managingButton.clicked.connect(self.managingButton_clicked)

    def exitButton_clicked(self):
        message = 'Вы уверены что хотите выйти?'
        reply = QtWidgets.QMessageBox.question(self, 'Выход из базы данных', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            global current_role
            global current_userID
            current_role = 0
            current_userID = 0
            self.main = mainwindow()
            self.main.show()
            self.close()

    def managingButton_clicked(self):
        self.managingWindow = managerManagingWindow()
        self.managingWindow.show()
        self.close()

class managerManagingWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = managerChooseMain()
        self.ui.setupUi(self)
        self.ui.coachButton.hide()
        self.ui.playerButton.hide()
        self.button = None
        self.ui.fanButton.hide()
        self.ui.stadiumButton.hide()
        self.ui.teamButton.hide()
        self.ui.managerButton.hide()
        self.setWindowTitle("Руководство")
        self.ui.backButton.clicked.connect(self.backButton_clicked)
        self.ui.addButton.clicked.connect(self.addButton_clicked)
        self.ui.updateButton.clicked.connect(self.updateButton_clicked)
        self.ui.deleteButton.clicked.connect(self.deleteButton_clicked)

    def backButton_clicked(self):
        if self.button == None:
            self.menu = managerMenuWindow()
            self.menu.show()
            self.close()
        else:
            self.ui.coachButton.hide()
            self.ui.playerButton.hide()
            self.button = None
            self.ui.fanButton.hide()
            self.ui.stadiumButton.hide()
            self.ui.teamButton.hide()
            self.ui.managerButton.hide()
            self.ui.addButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")
            self.ui.deleteButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")
            self.ui.updateButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")

    def addButton_clicked(self):
        self.ui.addButton.setStyleSheet(
            "background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.363184 rgba(222, 0, 0, 255), stop:1 rgba(255, 136, 136, 255));\n"
            "color: rgb(220, 220, 220)")
        self.ui.deleteButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")
        self.ui.updateButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")
        self.ui.coachButton.show()
        self.ui.playerButton.show()
        self.button = "Add"
        self.ui.fanButton.show()
        self.ui.stadiumButton.show()
        self.ui.teamButton.show()
        self.ui.managerButton.show()

    def updateButton_clicked(self):
        self.ui.updateButton.setStyleSheet(
            "background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.363184 rgba(222, 0, 0, 255), stop:1 rgba(255, 136, 136, 255));\n"
            "color: rgb(220, 220, 220)")
        self.ui.deleteButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")
        self.ui.addButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")
        self.ui.coachButton.show()
        self.ui.playerButton.show()
        self.button = "Update"
        self.ui.fanButton.show()
        self.ui.stadiumButton.show()
        self.ui.teamButton.show()
        self.ui.managerButton.show()

    def deleteButton_clicked(self):
        self.ui.deleteButton.setStyleSheet(
            "background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.363184 rgba(222, 0, 0, 255), stop:1 rgba(255, 136, 136, 255));\n"
            "color: rgb(220, 220, 220)")
        self.ui.updateButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")
        self.ui.addButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")
        self.ui.coachButton.show()
        self.ui.playerButton.show()
        self.button = "Delete"
        self.ui.fanButton.show()
        self.ui.stadiumButton.show()
        self.ui.teamButton.show()
        self.ui.managerButton.show()


class Sql:
    def __init__(self, database, server="DESKTOP-1IVLKJU\SQLSERVER"):
        self.cnxn = pyodbc.connect("Driver={SQL Server};"
                                   "Server="+server+";"
                                   "Database="+database+";"
                                   "Trusted_Connection=yes;")
        self.cursor = self.cnxn.cursor()
    def login(self, login, password):
        self.cursor = self.cnxn.cursor()
        self.cursor.execute("SELECT password")


def checkPassword(db, login, password):
    cipher_key = b'aIgO-OFHtCwB6LgfBcl1IQPYTVjQHzNsyzHK_PICN3s='
    cipher = Fernet(cipher_key)
    db.cursor.execute("SELECT ID_пользователя, Пароль, Роль FROM Пользователи where Логин='" + login + "'")
    row = db.cursor.fetchone()
    if row != None:
        passw = cipher.decrypt(str.encode(row[1])).decode('utf8')
        if passw == password:
            return True, row[2], row[0]
        else:
            return False, row[2], row[0]
    else:
        return False, 0, 0


def addUser(db, login, password, role):
    cipher_key = b'aIgO-OFHtCwB6LgfBcl1IQPYTVjQHzNsyzHK_PICN3s='
    cipher = Fernet(cipher_key)
    encrypted_password = password.encode('utf8')
    encrypted_password = cipher.encrypt(encrypted_password)
    try:
        db.cursor.execute("INSERT INTO Пользователи(Логин, Пароль, Роль) "
                          "VALUES ('"+login+"','"+encrypted_password.decode("utf-8") +"',"+str(role)+")")
        db.cnxn.commit()
        db.cursor.execute("SELECT ID_пользователя from Пользователи where Логин='"+login+"'")
        row = db.cursor.fetchone()
        return True, row[0]
    except pyodbc.Error as e:
        print(e)
        return False, 0

def addFan(db, id, name, surname, gender, birthday):
    cipher_key = b'aIgO-OFHtCwB6LgfBcl1IQPYTVjQHzNsyzHK_PICN3s='
    cipher = Fernet(cipher_key)
    name = name.rstrip()
    surname = surname.lstrip()
    fio = name + " " + surname
    try:
        db.cursor.execute("INSERT INTO Болельщики(ФИО, Пол, Дата_рождения, ID_пользователя) "
                          "VALUES ('" + fio + "','" + gender + "', '" + birthday + "',"+ str(id) +")")
        db.cnxn.commit()
        return True
    except pyodbc.Error as e:
        print(e)
        return False


def updatePassword(db, login, password):
    cipher_key = b'aIgO-OFHtCwB6LgfBcl1IQPYTVjQHzNsyzHK_PICN3s='
    cipher = Fernet(cipher_key)
    encrypted_password = password.encode('utf8')
    encrypted_password = cipher.encrypt(encrypted_password)
    db.cursor.execute("UPDATE Пользователи SET Пароль='"+encrypted_password.decode("utf-8")+"' where Логин='"+login+"'")
    db.cnxn.commit()


if __name__ == '__main__':
    db = Sql("football_club")

    #db.cursor.execute("SELECT ФИО, Рост FROM Футболисты where Рост > 180")
    #row = db.cursor.fetchall()
    #print(row)
    app = QtWidgets.QApplication([])
    window = mainwindow()
    window.show()
    db.cnxn.close()
    sys.exit(app.exec())
