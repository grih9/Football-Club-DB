from PyQt5 import QtWidgets
from startMenu import Ui_MainWindow as startmain
from login import Ui_MainWindow as loginmain
from registerFan import Ui_MainWindow as regFanmain
import sys
import pyodbc

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
        self.ui.enterButton_2.clicked.connect(self.backButton_clicked)
    def backButton_clicked(self):
        self.main = mainwindow()
        self.main.show()
        self.close()

class Sql:
    def __init__(self, database, server="DESKTOP-1IVLKJU\SQLSERVER"):
        self.cnxn = pyodbc.connect("Driver={SQL Server};"
                                   "Server="+server+";"
                                   "Database="+database+";"
                                   "Trusted_Connection=yes;")
        self.cursor = self.cnxn.cursor()

if __name__ == '__main__':
    db = Sql("football_club")
    db.cursor.execute("SELECT ФИО, Рост FROM Футболисты where Рост > 180")
    row = db.cursor.fetchall()
    print(row)
    app = QtWidgets.QApplication([])
    window = mainwindow()
    window.show()
    sys.exit(app.exec())
