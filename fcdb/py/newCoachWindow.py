from newCoach import Ui_MainWindow as newCoachMain

from PyQt5 import QtWidgets, QtCore

import managerManagingWindow
import sql
import contractWindow

class newCoachWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = newCoachMain()
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
            self.ui.teamCombo.clear()
            self.ui.teamCombo.addItem("Манчестер Юнайтед")
            self.ui.workLabel.show()
            self.ui.workLine.show()
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
            self.ui.workLabel.hide()
            self.ui.workLine.hide()
            self.ui.passwordConfirmLine.hide()
            self.ui.passwordLine.hide()
            self.ui.loginLine.hide()
            self.ui.workLine.clear()
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
        pos = self.ui.positionBox.currentText()
        number = self.ui.numberBox.currentText()
        nat = self.ui.nationLine.text()
        w = self.ui.weightLine.text()
        h = self.ui.height.text()
        d = self.ui.birthdayLine.text()
        l = self.ui.loginLine.text()
        p = self.ui.passwordLine.text()
        pp = self.ui.passwordConfirmLine.text()
        check = self.ui.dontCreateCheckBox
        status = False
        uid = 3
        if (n.strip() == '') \
                or (s.strip() == '') \
                or (pos.strip() == '') \
                or (number.strip() == '') \
                or (nat.strip() == ''):
            message = "Необходимо заполнить каждое поле"
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Пустое поле")
            error_message.showMessage(message)
            if len(nat) != 0 and (nat.strip() == ''):
                self.ui.nationLine.clear()
            if len(n) != 0 and (n.strip() == ''):
                self.ui.nameLine.clear()
            if len(s) != 0 and (s.strip() == ''):
                self.ui.surnameLine.clear()
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
            if(check.isChecked() is False):
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
                    status, uid = self.db.addUser(l, p, 3)

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
                status, fid = self.db.addPlayer(uid, n, s, nat, d, pos, number, h, w)
                if (status is True):
                    self.contract = contractWindow.contractWindow()
                    self.contract.fid = fid
                    self.db.cursor.execute("SELECT * from Контракты where ID_футболиста=" + str(fid))
                    row = self.db.cursor.fetchone()
                    exdate = row[2]
                    sal = row[1]
                    self.contract.ui.expireDate.setMinimumDate(
                        QtCore.QDate(int(exdate[0:4]), int(exdate[5:7]), int(exdate[8:10])))
                    self.contract.ui.salary.setValue(sal)
                    self.contract.ui.backButton.hide()
                    self.contract.show()
                    self.close()
                else:
                    message = "Неопределенная ошибка. Повторите ввод."
                    error_message = QtWidgets.QErrorMessage(self)
                    error_message.setModal(True)
                    error_message.setWindowTitle("Ошибка БД")
                    error_message.showMessage(message)




