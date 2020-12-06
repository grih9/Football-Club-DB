from PyQt5 import QtWidgets
from registerFan import Ui_MainWindow as regFanmain
import mainwindow
import sql

class regFanWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = regFanmain()
        self.ui.setupUi(self)
        self.setWindowTitle("Регистрация болельщика")
        self.ui.backButton.clicked.connect(self.backButton_clicked)
        self.ui.passwodCheckbox. stateChanged.connect(self.checkboxHandler)
        self.ui.createAccountButton.clicked.connect(self.createButton_clicked)

    def backButton_clicked(self):
        self.main = mainwindow.mainwindow()
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
            error_message.setModal(True)
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
            error_message.setModal(True)
            error_message.showMessage(message)
            self.ui.loginLine.clear()
            self.ui.passwordLine.clear()
            self.ui.passwordConfirmLine.clear()
        elif " " in p:
            message = "Недопустимый символ в поле пароля - пробел. Проверьте правильность введенных данных."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Ошибка ввода")
            error_message.showMessage(message)
            self.ui.passwordLine.clear()
            self.ui.passwordConfirmLine.clear()
        elif any(map(str.isdigit, n)):
            message = "Недопустимый символ в поле имени - цифра. Проверьте правильность введенных данных."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Ошибка ввода")
            error_message.showMessage(message)
            self.ui.nameLine.clear()
            self.ui.passwordLine.clear()
            self.ui.passwordConfirmLine.clear()
        elif any(map(str.isdigit, s)):
            message = "Недопустимый символ в поле фамилии - цифра. Проверьте правильность введенных данных."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Ошибка ввода")
            error_message.showMessage(message)
            self.ui.surnameLine.clear()
            self.ui.passwordLine.clear()
            self.ui.passwordConfirmLine.clear()
        elif (p != pp):
            message = "Введенные пароли не совпадают. Проверьте правильность введенных данных."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Ошибка ввода")
            error_message.showMessage(message)
            self.ui.passwordLine.clear()
            self.ui.passwordConfirmLine.clear()
        else:
            self.db = sql.Sql("football_club")
            status, id = self.db.addUser(l, p, 4)

            if (status is False):
                message = "Введенный логин занят. Повторите ввод."
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setModal(True)
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

                status = self.db.addFan(id, n, s, gender, d)
                if (status is True):
                    message = 'Аккаунт успешно создан!'
                    reply = QtWidgets.QMessageBox.question(self, 'Успех', message,
                                                           QtWidgets.QMessageBox.Ok)
                    if reply == QtWidgets.QMessageBox.Ok:
                        self.main = mainwindow.mainwindow()
                        self.main.show()
                        self.db.cnxn.close()
                        self.close()
                else:
                    message = "Неопределенная ошибка. Повторите ввод."
                    error_message = QtWidgets.QErrorMessage(self)
                    error_message.setModal(True)
                    error_message.setWindowTitle("Ошибка БД")
                    error_message.showMessage(message)
                    self.db.cursor.execute("DELETE FROM Пользователи where Логин='" + l + "'")
                    self.ui.passwordLine.clear()
                    self.ui.passwordConfirmLine.clear()
                    self.db.cnxn.close()