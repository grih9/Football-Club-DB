from PyQt5 import QtWidgets

import properties
from login import Ui_MainWindow as loginmain
import mainwindow
import managerMenuWindow
import menuFanWindow
import sql

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
            error_message.setModal(True)
            error_message.setWindowTitle("Ошибка входа")
            error_message.showMessage(message)
            if len(l) != 0:
                self.ui.loginLine.clear()
            self.ui.passwordLine.clear()
        elif (p.strip() == ''):
            message = "Поле пароля пустое! Введите пароль!"
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Ошибка входа")
            error_message.showMessage(message)
            if len(p) != 0:
                self.ui.passwordLine.clear()
        elif (l.find(' ') != -1):
            message = "Недопустимый символ в поле логина. Проверьте правильность данных и повторите вход."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Ошибка входа")
            error_message.showMessage(message)
            self.ui.loginLine.clear()
            self.ui.passwordLine.clear()
        elif (p.find(' ') != -1):
            message = "Данного пользователя не существует или введен неверный пароль! Проверьте правильность данных и повторите вход."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Ошибка входа")
            error_message.showMessage(message)
            self.ui.passwordLine.clear()
        else:
            self.db = sql.Sql("football_club")
            status, role, id = self.db.checkPassword(l, p)
            self.db.cnxn.close()
            if (status == False):
                message = "Данного пользователя не существует или введен неверный пароль! Проверьте правильность данных и повторите вход."
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setModal(True)
                error_message.setWindowTitle("Ошибка входа")
                error_message.showMessage(message)
                self.ui.passwordLine.clear()
            else:
                properties.current_role = role
                properties.current_userID = id
                if properties.current_role == 1:
                    self.menu = managerMenuWindow.managerMenuWindow()
                #elif properties.current_role == 2:
                #    self.menu = coachMenuWindow()
                #elif properties.current_role == 3:
                #    self.menu = playerMenuWindow()
                elif properties.current_role == 4:
                    self.menu = menuFanWindow.menuFanWindow()
                self.menu.show()
                self.close()

    def backButton_clicked(self):
        self.main = mainwindow.mainwindow()
        self.main.show()
        self.close()