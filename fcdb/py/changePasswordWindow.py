from PyQt5 import QtWidgets

from changePassword import Ui_Dialog as change
import profilewindow


class changePasswordWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = change()
        self.ui.setupUi(self)
        self.setWindowTitle("Изменить пароль")
        self.ui.buttonBox.clicked.connect(self.on_buttonBox_clicked)

    def on_buttonBox_clicked(self, button):
        self.profile = profilewindow.profilewindow()
        self.profile.show()
        self.close()

