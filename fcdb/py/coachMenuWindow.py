from PyQt5 import QtWidgets

import mainwindow
import profilewindow
import properties
from coachMenu import Ui_MainWindow as coachMenuMain
import teamWindow
import resultsWindow
import knowledgesWindow
import trainingWindow

class coachMenuWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = coachMenuMain()
        self.ui.setupUi(self)
        self.setWindowTitle("Тренерский штаб")
        self.ui.exitButton.clicked.connect(self.exitButton_clicked)
        self.ui.teamButton.clicked.connect(self.teamButton_clicked)
        self.ui.trainingButton.clicked.connect(self.trainingButton_clicked)
        self.ui.knowledgesButton.clicked.connect(self.knowledgesButton_clicked)
        self.ui.calendarButton.clicked.connect(self.resultsButton_clicked)
        self.ui.profileButton.clicked.connect(self.profileButton_clicked)
    def profileButton_clicked(self):
        self.profile = profilewindow.profilewindow()
        self.profile.show()
        self.close()

    def teamButton_clicked(self):
        self.team = teamWindow.teamWindow()
        self.team.show()
        self.close()

    def resultsButton_clicked(self):
        self.results = resultsWindow.resultsWindow()
        self.results.show()
        self.close()

    def knowledgesButton_clicked(self):
        self.knowledges = knowledgesWindow.knowledgesWindow()
        self.knowledges.show()
        self.close()

    def trainingButton_clicked(self):
        self.train = trainingWindow.trainingWindow()
        self.train.show()
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