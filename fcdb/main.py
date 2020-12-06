import sys

from PyQt5 import QtWidgets

from mainwindow import mainwindow
from sql import Sql

if __name__ == '__main__':
    db = Sql("football_club")

    #db.cursor.execute("SELECT ФИО, Рост FROM Футболисты where Рост > 180")
    #row = db.cursor.fetchall()
    #print(row)
    app = QtWidgets.QApplication([])
    window = mainwindow()
    window.show()
    db.cnxn.close()
    sys.exit(app.exec())
