# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/injury.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import med

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1016, 755)
        MainWindow.setMinimumSize(QtCore.QSize(1016, 755))
        MainWindow.setMaximumSize(QtCore.QSize(1016, 755))
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QWidget#centralwidget {\n"
"    background-image: url(C:/git/fcdb/Football-Club-DB/fcdb/resources/back.jpg);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(890, 670, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setStyleSheet(" color: rgb(255, 129, 129)")
        icon = QtGui.QIcon.fromTheme("NO")
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QtCore.QSize(300, 300))
        self.backButton.setObjectName("backButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 50, 541, 121))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(220, 220, 220);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(840, 75, 101, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/med/med.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.injuries = QtWidgets.QTabWidget(self.centralwidget)
        self.injuries.setGeometry(QtCore.QRect(10, 150, 991, 531))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.injuries.setFont(font)
        self.injuries.setStyleSheet("background-color: rgb(255, 237, 237);\n"
"color: rgb(0, 0, 0)")
        self.injuries.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.injuries.setTabBarAutoHide(True)
        self.injuries.setObjectName("injuries")
        self.current = QtWidgets.QWidget()
        self.current.setObjectName("current")
        self.currentTable = QtWidgets.QTableWidget(self.current)
        self.currentTable.setGeometry(QtCore.QRect(10, 20, 961, 231))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.currentTable.setFont(font)
        self.currentTable.setGridStyle(QtCore.Qt.SolidLine)
        self.currentTable.setObjectName("currentTable")
        self.currentTable.setColumnCount(6)
        self.currentTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.currentTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.currentTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.currentTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.currentTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.currentTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.currentTable.setHorizontalHeaderItem(5, item)
        self.currentTable.horizontalHeader().setDefaultSectionSize(135)
        self.currentTable.horizontalHeader().setHighlightSections(False)
        self.currentTable.horizontalHeader().setMinimumSectionSize(50)
        self.currentTable.horizontalHeader().setSortIndicatorShown(False)
        self.currentTable.verticalHeader().setDefaultSectionSize(35)
        self.currentTable.verticalHeader().setHighlightSections(False)
        self.addBox = QtWidgets.QGroupBox(self.current)
        self.addBox.setGeometry(QtCore.QRect(30, 260, 931, 241))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.addBox.setFont(font)
        self.addBox.setObjectName("addBox")
        self.addButton2 = QtWidgets.QPushButton(self.addBox)
        self.addButton2.setGeometry(QtCore.QRect(710, 180, 190, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.addButton2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.addButton2.setFont(font)
        self.addButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton2.setAutoFillBackground(False)
        self.addButton2.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.363184 rgba(222, 0, 0, 255), stop:1 rgba(255, 136, 136, 255));\n"
"color: rgb(220, 220, 220)")
        self.addButton2.setObjectName("addButton2")
        self.playerCombo = QtWidgets.QComboBox(self.addBox)
        self.playerCombo.setGeometry(QtCore.QRect(20, 70, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.playerCombo.setFont(font)
        self.playerCombo.setObjectName("playerCombo")
        self.playerCombo.addItem("")
        self.playerCombo.setItemText(0, "")
        self.label_6 = QtWidgets.QLabel(self.addBox)
        self.label_6.setGeometry(QtCore.QRect(30, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.sectorLabel = QtWidgets.QLabel(self.addBox)
        self.sectorLabel.setGeometry(QtCore.QRect(420, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.sectorLabel.setFont(font)
        self.sectorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sectorLabel.setObjectName("sectorLabel")
        self.placeLabel = QtWidgets.QLabel(self.addBox)
        self.placeLabel.setGeometry(QtCore.QRect(360, 120, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.placeLabel.setFont(font)
        self.placeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.placeLabel.setObjectName("placeLabel")
        self.date1 = QtWidgets.QDateEdit(self.addBox)
        self.date1.setGeometry(QtCore.QRect(370, 70, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.date1.setFont(font)
        self.date1.setAlignment(QtCore.Qt.AlignCenter)
        self.date1.setMaximumDate(QtCore.QDate(2040, 12, 31))
        self.date1.setMinimumDate(QtCore.QDate(2020, 10, 1))
        self.date1.setCalendarPopup(True)
        self.date1.setObjectName("date1")
        self.date2 = QtWidgets.QDateEdit(self.addBox)
        self.date2.setGeometry(QtCore.QRect(370, 160, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.date2.setFont(font)
        self.date2.setAlignment(QtCore.Qt.AlignCenter)
        self.date2.setMaximumDate(QtCore.QDate(2040, 12, 31))
        self.date2.setMinimumDate(QtCore.QDate(2020, 10, 2))
        self.date2.setCalendarPopup(True)
        self.date2.setObjectName("date2")
        self.enjLine = QtWidgets.QLineEdit(self.addBox)
        self.enjLine.setGeometry(QtCore.QRect(20, 160, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.enjLine.setFont(font)
        self.enjLine.setObjectName("enjLine")
        self.label_7 = QtWidgets.QLabel(self.addBox)
        self.label_7.setGeometry(QtCore.QRect(30, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.infoText = QtWidgets.QTextEdit(self.addBox)
        self.infoText.setGeometry(QtCore.QRect(640, 60, 281, 101))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.infoText.setFont(font)
        self.infoText.setObjectName("infoText")
        self.label_8 = QtWidgets.QLabel(self.addBox)
        self.label_8.setGeometry(QtCore.QRect(640, 20, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.addButton1 = QtWidgets.QPushButton(self.current)
        self.addButton1.setGeometry(QtCore.QRect(390, 260, 190, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.363184, QtGui.QColor(222, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(255, 136, 136))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 220, 220, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.addButton1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.addButton1.setFont(font)
        self.addButton1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton1.setAutoFillBackground(False)
        self.addButton1.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.363184 rgba(222, 0, 0, 255), stop:1 rgba(255, 136, 136, 255));\n"
"color: rgb(220, 220, 220)")
        self.addButton1.setObjectName("addButton1")
        self.noInjuriesLabel = QtWidgets.QLabel(self.current)
        self.noInjuriesLabel.setGeometry(QtCore.QRect(130, 110, 741, 81))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(25)
        self.noInjuriesLabel.setFont(font)
        self.noInjuriesLabel.setStyleSheet("color: rgb(255, 129, 129);")
        self.noInjuriesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noInjuriesLabel.setObjectName("noInjuriesLabel")
        self.addBox.raise_()
        self.currentTable.raise_()
        self.addButton1.raise_()
        self.noInjuriesLabel.raise_()
        self.injuries.addTab(self.current, "")
        self.history = QtWidgets.QWidget()
        self.history.setObjectName("history")
        self.historyTable = QtWidgets.QTableWidget(self.history)
        self.historyTable.setGeometry(QtCore.QRect(10, 70, 971, 421))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.historyTable.setFont(font)
        self.historyTable.setGridStyle(QtCore.Qt.SolidLine)
        self.historyTable.setObjectName("historyTable")
        self.historyTable.setColumnCount(6)
        self.historyTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.historyTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.historyTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.historyTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.historyTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.historyTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.historyTable.setHorizontalHeaderItem(5, item)
        self.historyTable.horizontalHeader().setDefaultSectionSize(135)
        self.historyTable.horizontalHeader().setHighlightSections(False)
        self.historyTable.horizontalHeader().setMinimumSectionSize(50)
        self.historyTable.horizontalHeader().setSortIndicatorShown(False)
        self.historyTable.verticalHeader().setDefaultSectionSize(35)
        self.historyTable.verticalHeader().setHighlightSections(False)
        self.fromDate = QtWidgets.QDateEdit(self.history)
        self.fromDate.setGeometry(QtCore.QRect(200, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.fromDate.setFont(font)
        self.fromDate.setAlignment(QtCore.Qt.AlignCenter)
        self.fromDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 9, 2), QtCore.QTime(0, 0, 0)))
        self.fromDate.setMaximumDate(QtCore.QDate(2040, 10, 2))
        self.fromDate.setMinimumDate(QtCore.QDate(2018, 9, 2))
        self.fromDate.setCalendarPopup(True)
        self.fromDate.setObjectName("fromDate")
        self.toDate = QtWidgets.QDateEdit(self.history)
        self.toDate.setGeometry(QtCore.QRect(490, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.toDate.setFont(font)
        self.toDate.setAlignment(QtCore.Qt.AlignCenter)
        self.toDate.setMaximumDate(QtCore.QDate(2040, 10, 2))
        self.toDate.setMinimumDate(QtCore.QDate(2018, 9, 2))
        self.toDate.setCalendarPopup(True)
        self.toDate.setObjectName("toDate")
        self.sectorLabel_2 = QtWidgets.QLabel(self.history)
        self.sectorLabel_2.setGeometry(QtCore.QRect(140, 15, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.sectorLabel_2.setFont(font)
        self.sectorLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.sectorLabel_2.setObjectName("sectorLabel_2")
        self.sectorLabel_3 = QtWidgets.QLabel(self.history)
        self.sectorLabel_3.setGeometry(QtCore.QRect(440, 15, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.sectorLabel_3.setFont(font)
        self.sectorLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.sectorLabel_3.setObjectName("sectorLabel_3")
        self.searchButton = QtWidgets.QPushButton(self.history)
        self.searchButton.setGeometry(QtCore.QRect(760, 15, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.resetButton = QtWidgets.QPushButton(self.history)
        self.resetButton.setGeometry(QtCore.QRect(870, 15, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
        self.noInjLabel = QtWidgets.QLabel(self.history)
        self.noInjLabel.setGeometry(QtCore.QRect(30, 260, 931, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(25)
        self.noInjLabel.setFont(font)
        self.noInjLabel.setStyleSheet("color: rgb(255, 129, 129);")
        self.noInjLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noInjLabel.setObjectName("noInjLabel")
        self.injuries.addTab(self.history, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.injuries.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backButton.setText(_translate("MainWindow", "НАЗАД"))
        self.label.setText(_translate("MainWindow", "ЖУРНАЛ ТРАВМ"))
        item = self.currentTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер"))
        item = self.currentTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Футболист"))
        item = self.currentTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Травма"))
        item = self.currentTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.currentTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Срок восстановления"))
        item = self.currentTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Доп. инфо."))
        self.addBox.setTitle(_translate("MainWindow", "Добавить информацию о травме"))
        self.addButton2.setText(_translate("MainWindow", "Добавить"))
        self.label_6.setText(_translate("MainWindow", "Игрок"))
        self.sectorLabel.setText(_translate("MainWindow", "Дата"))
        self.placeLabel.setText(_translate("MainWindow", "Дата восстановления"))
        self.label_7.setText(_translate("MainWindow", "Травма"))
        self.label_8.setText(_translate("MainWindow", "Дополнительная информация"))
        self.addButton1.setText(_translate("MainWindow", "Добавить"))
        self.noInjuriesLabel.setText(_translate("MainWindow", "Травмированных игроков нет!"))
        self.injuries.setTabText(self.injuries.indexOf(self.current), _translate("MainWindow", "Текущие травмы"))
        item = self.historyTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер"))
        item = self.historyTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Футболист"))
        item = self.historyTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Травма"))
        item = self.historyTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.historyTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Срок восстановления"))
        item = self.historyTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Доп. инфо."))
        self.sectorLabel_2.setText(_translate("MainWindow", "C"))
        self.sectorLabel_3.setText(_translate("MainWindow", "ПО"))
        self.searchButton.setText(_translate("MainWindow", "ПОИСК"))
        self.resetButton.setText(_translate("MainWindow", "СБРОС"))
        self.noInjLabel.setText(_translate("MainWindow", "Травмированных за данный период нет!"))
        self.injuries.setTabText(self.injuries.indexOf(self.history), _translate("MainWindow", "История"))


