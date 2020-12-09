from newOwner import Ui_MainWindow as newOwnerMain

from PyQt5 import QtWidgets, QtCore

import managerManagingWindow
import sql
import teamWindow
import knowledgesWindow
import properties

class newOwnerWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = newOwnerMain()
        self.ui.setupUi(self)
        self.setWindowTitle("Добавление нового работника")
        self.ui.backButton.clicked.connect(self.backButton_clicked)
        self.ui.myTeamCheckBox.stateChanged.connect(self.myTeamCheckHandler)
        self.ui.showPasswordCheckBox.stateChanged.connect(self.checkboxHandler)
        self.ui.enterButton.clicked.connect(self.enterButton_clicked)
        self.ui.dontCreateCheckBox.stateChanged.connect(self.dontCreateHandler)
        self.db = sql.Sql("football_club")
        self.ui.teamCombo.clear()
        self.ui.teamCombo.addItem("Манчестер Юнайтед")

    def backButton_clicked(self):
        self.manager = managerManagingWindow.managerManagingWindow()
        self.manager.show()
        self.close()

    def checkboxHandler(self, state):
        if self.ui.showPasswordCheckBox.isChecked():
            self.ui.passwordConfirmLine.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.passwordLine.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ui.passwordConfirmLine.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)

    def myTeamCheckHandler(self, state):
        if self.ui.myTeamCheckBox.isChecked():
            self.ui.isOwner.setChecked(False)
            self.ui.isOwner.setEnabled(True)
            self.ui.teamCombo.clear()
            self.ui.teamCombo.addItem("Манчестер Юнайтед")
            self.ui.passwordConfirmLine.show()
            self.ui.dontCreateCheckBox.show()
            self.ui.dontCreateCheckBox.setChecked(False)
            self.ui.passwordLine.show()
            self.ui.loginLine.show()
            self.ui.loginLabel.show()
            self.ui.passwordConfirm.show()
            self.ui.passwordLabel.show()
            self.ui.showPasswordCheckBox.show()
            self.ui.eyeLabel.show()

        else:
            self.ui.isOwner.setChecked(True)
            self.ui.isOwner.setEnabled(False)
            self.ui.teamCombo.clear()
            self.ui.teamCombo.addItem("")
            self.db.cursor.execute(
                "SELECT Команда FROM Команды where Команда != 'Манчестер Юнайтед' order by Команда ASC")
            row = self.db.cursor.fetchone()
            while (row is not None):
                self.ui.teamCombo.addItem(row[0].rstrip())
                row = self.db.cursor.fetchone()

            self.ui.dontCreateCheckBox.setChecked(True)
            self.ui.dontCreateCheckBox.hide()
            self.ui.passwordConfirmLine.hide()
            self.ui.passwordLine.hide()
            self.ui.loginLine.hide()
            self.ui.loginLine.clear()
            self.ui.passwordLine.clear()
            self.ui.passwordConfirmLine.clear()
            self.ui.showPasswordCheckBox.setChecked(False)
            self.ui.loginLabel.hide()
            self.ui.passwordConfirm.hide()
            self.ui.passwordLabel.hide()
            self.ui.showPasswordCheckBox.hide()
            self.ui.eyeLabel.hide()

    def dontCreateHandler(self, state):
        if self.ui.dontCreateCheckBox.isChecked():
            self.ui.passwordLine.setEnabled(False)
            self.ui.passwordConfirmLine.setEnabled(False)
            self.ui.loginLine.setEnabled(False)
            self.ui.showPasswordCheckBox.setEnabled(False)
            self.ui.showPasswordCheckBox.setChecked(False)
        else:
            self.ui.passwordLine.setEnabled(True)
            self.ui.passwordConfirmLine.setEnabled(True)
            self.ui.loginLine.setEnabled(True)
            self.ui.showPasswordCheckBox.setEnabled(True)

    def enterButton_clicked(self):
        n = self.ui.nameLine.text()
        s = self.ui.surnameLine.text()
        nat = self.ui.nationLine.text()
        t = self.ui.teamCombo.currentText()
        d = self.ui.birthdayLine.text()
        l = self.ui.loginLine.text()
        p = self.ui.passwordLine.text()
        pp = self.ui.passwordConfirmLine.text()
        check = self.ui.dontCreateCheckBox
        status = False
        uid = 1
        if (self.ui.myTeamCheckBox.isChecked()):
            if ((n.strip() == '')or (nat.strip() == '')):
                message = "Необходимо заполнить поле 'Cтрана' и 'Имя'"
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setModal(True)
                error_message.setWindowTitle("Пустое поле")
                error_message.showMessage(message)
                if len(nat) != 0 and (nat.strip() == ''):
                    self.ui.nationLine.clear()
                if len(n) != 0 and (n.strip() == ''):
                    self.ui.nameLine.clear()
            elif any(map(str.isdigit, n)):
                message = "Недопустимый символ в поле имени - цифра. Проверьте правильность введенных данных."
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setModal(True)
                error_message.setWindowTitle("Ошибка ввода")
                error_message.showMessage(message)
                self.ui.nameLine.clear()
            elif any(map(str.isdigit, s)):
                message = "Недопустимый символ в поле фамилии - цифра. Проверьте правильность введенных данных."
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setModal(True)
                error_message.setWindowTitle("Ошибка ввода")
                error_message.showMessage(message)
                self.ui.surnameLine.clear()
            elif any(map(str.isdigit, nat)):
                message = "Недопустимый символ в поле страны - цифра. Проверьте правильность введенных данных."
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setModal(True)
                error_message.setWindowTitle("Ошибка ввода")
                error_message.showMessage(message)
                self.ui.nationLine.clear()
            else:
                if (check.isChecked() is False):
                    if (l.strip() == '') \
                            or (p.strip() == '') \
                            or (pp.strip() == ''):
                        message = "Необходимо заполнить поля логина и пароля"
                        error_message = QtWidgets.QErrorMessage(self)
                        error_message.setModal(True)
                        error_message.setWindowTitle("Пустые поля")
                        error_message.showMessage(message)
                        if len(l) != 0 and (l.strip() == ''):
                            self.ui.loginLine.clear()
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
                        status, uid = self.db.addUser(l, p, 1)
                        if (status is False):
                            message = "Введенный логин занят. Повторите ввод."
                            error_message = QtWidgets.QErrorMessage(self)
                            error_message.setModal(True)
                            error_message.setWindowTitle("Ошибка ввода")
                            error_message.showMessage(message)
                            self.ui.loginLine.clear()
                            self.ui.passwordLine.clear()
                            self.ui.passwordConfirmLine.clear()

                if (check.isChecked() is True) or status is True:
                    if (self.ui.isOwner.isChecked()):
                        self.db.cursor.execute("SELECT ID_владельца from Команды where Команда ='Манчестер Юнайтед'")
                        row = self.db.cursor.fetchone()
                        id = row[0]
                        self.db.cursor.execute("SELECT ID_пользователя from Руководство where ID_владельца=" + str(id))
                        row = self.db.cursor.fetchone()
                        id2 = row[0]
                        if (properties.current_userID != id2):
                            message = "Только владелец Манчестер Юнайтед может добавить нового владельца команды"
                            error_message = QtWidgets.QErrorMessage(self)
                            error_message.setModal(True)
                            error_message.setWindowTitle("Ошибка БД")
                            error_message.showMessage(message)
                            self.db.cursor.execute("DELETE FROM Пользователи where Логин='" + l + "'")
                        else:
                            message = 'Вы действительно хотите продать команду новому владельцу?'
                            reply = QtWidgets.QMessageBox.question(self, 'Успех', message,
                                                               QtWidgets.QMessageBox.Yes,
                                                               QtWidgets.QMessageBox.No)
                            if reply == QtWidgets.QMessageBox.Yes:
                                status, mid = self.db.addManager(uid, n, s, nat, d)
                                if (status is True):
                                    status = self.db.changeManager(mid, t)
                                    if (status is True):
                                        message = 'Владелец команды изменен'
                                        reply = QtWidgets.QMessageBox.question(self, 'Успех', message,
                                                                               QtWidgets.QMessageBox.Ok)

                                        self.team = teamWindow.teamWindow()
                                        self.team.ui.tabWidget.setCurrentIndex(0)
                                        self.team.show()
                                        self.db.cnxn.close()
                                        self.close()
                                    else:
                                        message = "Неопределенная ошибка. Повторите ввод."
                                        error_message = QtWidgets.QErrorMessage(self)
                                        error_message.setModal(True)
                                        error_message.setWindowTitle("Ошибка БД")
                                        error_message.showMessage(message)
                                        self.db.cursor.execute("DELETE FROM Пользователи where Логин='" + l + "'")
                            else:
                                message = "Неопределенная ошибка. Повторите ввод."
                                error_message = QtWidgets.QErrorMessage(self)
                                error_message.setModal(True)
                                error_message.setWindowTitle("Ошибка БД")
                                error_message.showMessage(message)
                                self.db.cursor.execute("DELETE FROM Пользователи where Логин='" + l + "'")
                    else:
                        status = self.db.addManager(uid, n, s, nat, d)
                        if (status is True):
                            message = 'Руководитель успешно добавлен'
                            reply = QtWidgets.QMessageBox.question(self, 'Успех', message,
                                                                   QtWidgets.QMessageBox.Ok)

                            self.team = teamWindow.teamWindow()
                            self.team.ui.tabWidget.setCurrentIndex(2)
                            self.team.show()
                            self.db.cnxn.close()
                            self.close()
                        else:
                            message = "Неопределенная ошибка. Повторите ввод."
                            error_message = QtWidgets.QErrorMessage(self)
                            error_message.setModal(True)
                            error_message.setWindowTitle("Ошибка БД")
                            error_message.showMessage(message)
                            self.db.cursor.execute("DELETE FROM Пользователи where Логин='" + l + "'")

        else:
            if self.ui.teamCombo.currentIndex() == 0:
                t = None
            if (n.strip() == '') or (nat.strip() == ''):
                message = "Необходимо заполнить поле 'Cтрана' и 'Имя'"
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setModal(True)
                error_message.setWindowTitle("Пустое поле")
                error_message.showMessage(message)
                if len(nat) != 0 and (nat.strip() == ''):
                    self.ui.nationLine.clear()
                if len(n) != 0 and (n.strip() == ''):
                    self.ui.nameLine.clear()
            elif any(map(str.isdigit, n)):
                message = "Недопустимый символ в поле имени - цифра. Проверьте правильность введенных данных."
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setModal(True)
                error_message.setWindowTitle("Ошибка ввода")
                error_message.showMessage(message)
                self.ui.nameLine.clear()
            elif any(map(str.isdigit, s)):
                message = "Недопустимый символ в поле фамилии - цифра. Проверьте правильность введенных данных."
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setModal(True)
                error_message.setWindowTitle("Ошибка ввода")
                error_message.showMessage(message)
                self.ui.surnameLine.clear()
            elif any(map(str.isdigit, nat)):
                message = "Недопустимый символ в поле страны - цифра. Проверьте правильность введенных данных."
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setModal(True)
                error_message.setWindowTitle("Ошибка ввода")
                error_message.showMessage(message)
                self.ui.nationLine.clear()
            else:
                if (self.ui.isOwner.isChecked() and t is not None):
                    message = 'Вы действительно хотите установить владельца для сторонней команды?'
                    reply = QtWidgets.QMessageBox.question(self, 'Успех', message,
                                                           QtWidgets.QMessageBox.Yes,
                                                           QtWidgets.QMessageBox.No)
                    if reply == QtWidgets.QMessageBox.Yes:
                        status, mid = self.db.addManager(uid, n, s, nat, d)
                        if (status is True):
                            status = self.db.changeManager(mid, t)
                            if (status is True):
                                message = 'Владелец команды изменен'
                                reply = QtWidgets.QMessageBox.question(self, 'Успех', message,
                                                                       QtWidgets.QMessageBox.Ok)

                                self.knowledges = knowledgesWindow.knowledgesWindow()
                                self.knowledges.ui.tabWidget.setCurrentIndex(2)
                                self.knowledges.show()
                                self.db.cnxn.close()
                                self.close()
                            else:
                                message = "Неопределенная ошибка. Повторите ввод."
                                error_message = QtWidgets.QErrorMessage(self)
                                error_message.setModal(True)
                                error_message.setWindowTitle("Ошибка БД")
                                error_message.showMessage(message)
                        else:
                            message = "Неопределенная ошибка. Повторите ввод."
                            error_message = QtWidgets.QErrorMessage(self)
                            error_message.setModal(True)
                            error_message.setWindowTitle("Ошибка БД")
                            error_message.showMessage(message)
                elif (self.ui.isOwner.isChecked() and t is None):
                    message = "Необходимо выбрать команду для добавления владельца."
                    error_message = QtWidgets.QErrorMessage(self)
                    error_message.setModal(True)
                    error_message.setWindowTitle("Ошибка ввода")
                    error_message.showMessage(message)
                    self.ui.nationLine.clear()
                else:
                    status = self.db.addManager(uid, n, s, nat, d)
                    if (status is True):
                        message = 'Руководитель успешно добавлен'
                        reply = QtWidgets.QMessageBox.question(self, 'Успех', message,
                                                               QtWidgets.QMessageBox.Ok)

                        self.knowledges = knowledgesWindow.knowledgesWindow()
                        self.knowledges.ui.tabWidget.setCurrentIndex(2)
                        self.knowledges.show()
                        self.db.cnxn.close()
                        self.close()
                    else:
                        message = "Неопределенная ошибка. Повторите ввод."
                        error_message = QtWidgets.QErrorMessage(self)
                        error_message.setModal(True)
                        error_message.setWindowTitle("Ошибка БД")
                        error_message.showMessage(message)

