from PyQt5 import QtWidgets

from choose import Ui_MainWindow as managerChooseMain
import managerMenuWindow

class managerManagingWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = managerChooseMain()
        self.ui.setupUi(self)
        self.ui.coachButton.hide()
        self.ui.playerButton.hide()
        self.button = None
        self.ui.fanButton.hide()
        self.ui.stadiumButton.hide()
        self.ui.teamButton.hide()
        self.ui.managerButton.hide()
        self.setWindowTitle("Руководство")
        self.ui.backButton.clicked.connect(self.backButton_clicked)
        self.ui.addButton.clicked.connect(self.addButton_clicked)
        self.ui.updateButton.clicked.connect(self.updateButton_clicked)
        self.ui.deleteButton.clicked.connect(self.deleteButton_clicked)

    def backButton_clicked(self):
        if self.button == None:
            self.menu = managerMenuWindow.managerMenuWindow()
            self.menu.show()
            self.close()
        else:
            self.ui.coachButton.hide()
            self.ui.playerButton.hide()
            self.button = None
            self.ui.fanButton.hide()
            self.ui.stadiumButton.hide()
            self.ui.teamButton.hide()
            self.ui.managerButton.hide()
            self.ui.addButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")
            self.ui.deleteButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")
            self.ui.updateButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")

    def addButton_clicked(self):
        self.ui.addButton.setStyleSheet(
            "background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.363184 rgba(222, 0, 0, 255), stop:1 rgba(255, 136, 136, 255));\n"
            "color: rgb(220, 220, 220)")
        self.ui.deleteButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")
        self.ui.updateButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")
        self.ui.coachButton.show()
        self.ui.playerButton.show()
        self.button = "Add"
        self.ui.fanButton.show()
        self.ui.stadiumButton.show()
        self.ui.teamButton.show()
        self.ui.managerButton.show()

    def updateButton_clicked(self):
        self.ui.updateButton.setStyleSheet(
            "background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.363184 rgba(222, 0, 0, 255), stop:1 rgba(255, 136, 136, 255));\n"
            "color: rgb(220, 220, 220)")
        self.ui.deleteButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")
        self.ui.addButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")
        self.ui.coachButton.show()
        self.ui.playerButton.show()
        self.button = "Update"
        self.ui.fanButton.show()
        self.ui.stadiumButton.show()
        self.ui.teamButton.show()
        self.ui.managerButton.show()

    def deleteButton_clicked(self):
        self.ui.deleteButton.setStyleSheet(
            "background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.363184 rgba(222, 0, 0, 255), stop:1 rgba(255, 136, 136, 255));\n"
            "color: rgb(220, 220, 220)")
        self.ui.updateButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")
        self.ui.addButton.setStyleSheet("background-color: rgb(255, 129, 129);\n"
                                            "color: rgb(220, 220, 220)")
        self.ui.coachButton.show()
        self.ui.playerButton.show()
        self.button = "Delete"
        self.ui.fanButton.show()
        self.ui.stadiumButton.show()
        self.ui.teamButton.show()
        self.ui.managerButton.show()