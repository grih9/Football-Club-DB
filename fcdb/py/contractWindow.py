from PyQt5 import QtWidgets

import managerManagingWindow
import teamWindow
import sql
from contract import Ui_MainWindow as contractMain


class contractWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = contractMain()
        self.ui.setupUi(self)
        self.fid = 0
        self.setWindowTitle("Контракт")
        self.ui.backButton.clicked.connect(self.backButton_clicked)
        self.ui.createAccountButton.clicked.connect(self.create_clicked)
        self.db = sql.Sql("football_club")

    def backButton_clicked(self):
        self.menu = managerManagingWindow.managerManagingWindow()
        self.menu.show()
        self.close()

    def create_clicked(self):
        s = self.ui.salary.value()
        d = self.ui.expireDate.text()

        message = 'Вы уверены?'
        reply = QtWidgets.QMessageBox.question(self, 'Подписание контракта', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.db.updateContract(self.fid, s, d)
            message = 'Контракт успешно подписан'
            reply = QtWidgets.QMessageBox.question(self, 'Успех', message,
                                               QtWidgets.QMessageBox.Ok)

            self.team = teamWindow.teamWindow()
            self.team.ui.tabWidget.setCurrentIndex(1)
            self.team.show()
            self.db.cnxn.close()
            self.close()
