from PyQt5 import QtWidgets

from managerMenu import Ui_MainWindow as managerMenuMain
import mainwindow
import managerManagingWindow
import profilewindow
import properties
import teamWindow

class managerMenuWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = managerMenuMain()
        self.ui.setupUi(self)
        self.setWindowTitle("Руководство")
        self.ui.exitButton.clicked.connect(self.exitButton_clicked)
        self.ui.managingButton.clicked.connect(self.managingButton_clicked)
        self.ui.teamButton.clicked.connect(self.teamButton_clicked)
        self.ui.profileButton.clicked.connect(self.profileButton_clicked)

    def exitButton_clicked(self):
        message = 'Вы уверены, что хотите выйти?'
        reply = QtWidgets.QMessageBox.question(self, 'Выход из базы данных', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            properties.current_role = 0
            properties.current_userID = 0
            self.main = mainwindow.mainwindow()
            self.main.show()
            self.close()

    def teamButton_clicked(self):
        self.team = teamWindow.teamWindow()
        self.team.show()
        self.close()

    def managingButton_clicked(self):
        self.managingWindow = managerManagingWindow.managerManagingWindow()
        self.managingWindow.show()
        self.close()

    def profileButton_clicked(self):
        self.profile = profilewindow.profilewindow()
        self.profile.show()
        self.close()