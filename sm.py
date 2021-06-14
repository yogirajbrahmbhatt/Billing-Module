# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from sr import Ui_billy
from src import Ui_src

class Ui_StockManagement(object):
    def file12(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_billy()
        self.ui.setupUi (self.window2)
        self.window2.show()

    def file21(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_src()
        self.ui.setupUi (self.window2)
        self.window2.show()

    def setupUi(self, StockManagement):
        StockManagement.setObjectName("StockManagement")
        StockManagement.setEnabled(True)
        StockManagement.setFixedSize(769, 633)
        StockManagement.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StockManagement.setWindowIcon(icon)
        StockManagement.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.centralwidget = QtWidgets.QWidget(StockManagement)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 10, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 0, 0);\n"
"")
        self.label.setObjectName("label")
        self.billing = QtWidgets.QLabel(self.centralwidget)
        self.billing.setGeometry(QtCore.QRect(80, 180, 201, 171))
        self.billing.setAutoFillBackground(False)
        self.billing.setText("")
        self.billing.setPixmap(QtGui.QPixmap("icons/icon-registration-registry-registration-151047317-removebg-preview (1).png"))
        self.billing.setScaledContents(True)
        self.billing.setOpenExternalLinks(True)
        self.billing.setObjectName("billing")
        self.Stock = QtWidgets.QLabel(self.centralwidget)
        self.Stock.setGeometry(QtCore.QRect(510, 180, 201, 171))
        self.Stock.setText("")
        self.Stock.setPixmap(QtGui.QPixmap("icons/inventory-checking-1084771-removebg-preview.png"))
        self.Stock.setScaledContents(True)
        self.Stock.setOpenExternalLinks(True)
        self.Stock.setObjectName("Stock")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 80, 501, 21))
        font = QtGui.QFont()
        font.setFamily("Rod")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.srpush = QtWidgets.QPushButton(self.centralwidget)
        self.srpush.setGeometry(QtCore.QRect(80, 360, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(14)
        font.setUnderline(True)
        self.srpush.setFont(font)
        self.srpush.setFlat(True)
        self.srpush.setObjectName("srpush")
        self.srpush.clicked.connect(self.file12)  
        self.scpush = QtWidgets.QPushButton(self.centralwidget)
        self.scpush.setGeometry(QtCore.QRect(510, 360, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(14)
        font.setUnderline(True)
        self.scpush.setFont(font)
        self.scpush.setFlat(True)
        self.scpush.setObjectName("scpush")
        self.scpush.clicked.connect(self.file21) 
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 550, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Rod")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 100, 771, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 530, 771, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        StockManagement.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StockManagement)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 21))
        self.menubar.setObjectName("menubar")
        StockManagement.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StockManagement)
        self.statusbar.setObjectName("statusbar")
        StockManagement.setStatusBar(self.statusbar)

        self.retranslateUi(StockManagement)
        QtCore.QMetaObject.connectSlotsByName(StockManagement)

    def retranslateUi(self, StockManagement):
        _translate = QtCore.QCoreApplication.translate
        StockManagement.setWindowTitle(_translate("StockManagement", "SToRE +"))
        self.label.setText(_translate("StockManagement", "SToRE +"))
        self.label_2.setText(_translate("StockManagement", "Stock Management"))
        self.srpush.setText(_translate("StockManagement", "STOCK REGISTRY"))
        self.scpush.setText(_translate("StockManagement", "STOCK CHECKING"))
        self.label_3.setText(_translate("StockManagement", "made with ❤ by Yogiraj Brahmbhatt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StockManagement = QtWidgets.QMainWindow()
    ui = Ui_StockManagement()
    ui.setupUi(StockManagement)
    StockManagement.show()
    sys.exit(app.exec_())
