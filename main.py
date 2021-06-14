# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from bill import Ui_bill
from sm import Ui_StockManagement

class Ui_main(object):
    def file2(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_bill()
        self.ui.setupUi (self.window2)
        self.window2.show()
    def file3(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_StockManagement()
        self.ui.setupUi (self.window2)
        self.window2.show()
    
    def setupUi(self, main):
        main.setObjectName("main")
        main.setEnabled(True)
        main.setFixedSize(769, 633)
        main.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main.setWindowIcon(icon)
        main.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.centralwidget = QtWidgets.QWidget(main)
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
        self.billing.setGeometry(QtCore.QRect(70, 180, 201, 171))
        self.billing.setAutoFillBackground(False)
        self.billing.setText("")
        self.billing.setPixmap(QtGui.QPixmap("./icons/1120636-200.png"))
        self.billing.setScaledContents(True)
        self.billing.setOpenExternalLinks(True)
        self.billing.setObjectName("billing")
        
        self.Stock = QtWidgets.QLabel(self.centralwidget)
        self.Stock.setGeometry(QtCore.QRect(530, 180, 201, 171))
        self.Stock.setText("")
        self.Stock.setPixmap(QtGui.QPixmap("./icons/srtock.png"))
        self.Stock.setScaledContents(True)
        self.Stock.setOpenExternalLinks(True)
        self.Stock.setObjectName("Stock")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 80, 501, 21))
        font = QtGui.QFont()
        font.setFamily("Rod")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.billpush = QtWidgets.QPushButton(self.centralwidget)
        self.billpush.setGeometry(QtCore.QRect(110, 360, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(14)
        font.setUnderline(True)
        self.billpush.setFont(font)
        self.billpush.setFlat(True)
        self.billpush.setObjectName("billpush")
        self.billpush.clicked.connect(self.file2)  
        self.stockpush = QtWidgets.QPushButton(self.centralwidget)
        self.stockpush.setGeometry(QtCore.QRect(530, 360, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(14)
        font.setUnderline(True)
        self.stockpush.setFont(font)
        self.stockpush.setFlat(True)
        self.stockpush.setObjectName("stockpush")
        self.stockpush.clicked.connect(self.file3)  
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
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 21))
        self.menubar.setObjectName("menubar")
        main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "SToRE +"))
        self.label.setText(_translate("main", "SToRE +"))
        self.label_2.setText(_translate("main", "Billing and Stock Management Software"))
        self.billpush.setText(_translate("main", "BILLING"))
        self.stockpush.setText(_translate("main", "STOCK MANAGEMENT"))
        self.label_3.setText(_translate("main", "made with ❤ by Yogiraj Brahmbhatt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
