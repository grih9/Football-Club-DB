from PyQt5 import QtWidgets

import loginwindow
import regFanWindow
from startMenu import Ui_MainWindow as startmain


class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = startmain()
        self.ui.setupUi(self)
        self.setWindowTitle("Добро пожаловать!")
        self.ui.enterButton.clicked.connect(self.enterButton_clicked)
        self.ui.noAccountButton.clicked.connect(self.noAccount_clicked)
    def enterButton_clicked(self):
        self.login = loginwindow.loginindow()
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
            self.reg = regFanWindow.regFanWindow()
            self.reg.show()
            self.close()