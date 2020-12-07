from PyQt5 import QtWidgets

import mainwindow
import profilewindow
import properties
from playerMenu import Ui_MainWindow as playerMenuMain

class playerMenuWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = playerMenuMain()
        self.ui.setupUi(self)
        self.setWindowTitle("Футболист")
        self.ui.exitButton.clicked.connect(self.exitButton_clicked)
        #self.ui.teamButton.clicked.connect(self.teamButton_clicked)
        #self.ui.ticketsButton.clicked.connect(self.ticketsButton_clicked)
        #self.ui.knowledgesButton.clicked.connect(self.knowledgesButton_clicked)
        #self.ui.calendarButton.clicked.connect(self.calendarButton_clicked)
        self.ui.profileButton.clicked.connect(self.profileButton_clicked)
    def profileButton_clicked(self):
        self.profile = profilewindow.profilewindow()
        self.profile.show()
        self.close()

    def exitButton_clicked(self):
        message = 'Вы уверены, что хотите выйти?'
        reply = QtWidgets.QMessageBox.question(self, 'Выход из базы данных', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            properties.prcurrent_role = 0
            properties.current_userID = 0
            self.main = mainwindow.mainwindow()
            self.main.show()
            self.close()