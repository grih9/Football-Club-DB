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
        self.ui.fanButton.hide()
        self.ui.stadiumButton.hide()
        self.ui.teamButton.hide()
        self.ui.managerButton.hide()
        self.setWindowTitle("Руководство")
        self.ui.backButton.clicked.connect(self.backButton_clicked)
    def backButton_clicked(self):
        self.menu = managerMenuWindow()
        self.menu.show()
        self.close()

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
    print(encrypted_password)
    try:
        db.cursor.execute("INSERT INTO Пользователи(Логин, Пароль, Роль) "
                          "VALUES ('"+login+"','"+encrypted_password.decode("utf-8") +"',"+str(role)+")")
        db.cnxn.commit()
        print("ok")
    except pyodbc.Error as e:
        print("not ok")
        print(e)

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
