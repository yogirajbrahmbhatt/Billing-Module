# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as s
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


db = s.connect("./database/store.db") 
cdb = db.cursor()
cdb.execute("SELECT DISTINCT product_subcat FROM raw_inventory")
dd = cdb.fetchall()
bad_chars = [';', ')', "(", ","]
cat = [] 
for i in range(len(dd)):
    nd = ''.join((filter(lambda i: i not in bad_chars, dd[i])))
    cat.append(nd)
cdb.execute("SELECT DISTINCT product_id FROM raw_inventory")
de = cdb.fetchall()
bad_chars = [';', ')', "(", ","]
ids = [] 
for ii in range(len(de)):
    de[ii] = str(de[ii])
    nde = ''.join((filter(lambda i: i not in bad_chars, de[ii])))
    ids.append(nde)
    
class Ui_src(object):
    def setupUi(self, src):
        src.setObjectName("src")
        src.setFixedSize(769, 633)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        src.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(src)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 441, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 30, 771, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.contact_3 = QtWidgets.QLabel(self.centralwidget)
        self.contact_3.setGeometry(QtCore.QRect(170, 40, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Rod")
        font.setPointSize(12)
        self.contact_3.setFont(font)
        self.contact_3.setObjectName("contact_3")
        self.resetall = QtWidgets.QPushButton(self.centralwidget)
        self.resetall.setGeometry(QtCore.QRect(470, 140, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Kozuka Mincho Pro B")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.resetall.setFont(font)
        self.resetall.setObjectName("resetall")

        self.add2db = QtWidgets.QPushButton(self.centralwidget)
        self.add2db.setGeometry(QtCore.QRect(130, 140, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Rod")
        font.setPointSize(16)
        self.add2db.setFont(font)
        self.add2db.setStyleSheet("color: rgb(170, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.add2db.setObjectName("add2db")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 120, 771, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.icat = QtWidgets.QComboBox(self.centralwidget)
        self.icat.setGeometry(QtCore.QRect(350, 50, 161, 31))
        self.icat.setObjectName("icat")
        self.icat.addItem(" ")
        for t in range(len(cat)):
            self.icat.addItem(cat[t])
        self.icat.activated.connect(self.pass_Net_Adap)
        
        self.contact_4 = QtWidgets.QLabel(self.centralwidget)
        self.contact_4.setGeometry(QtCore.QRect(170, 80, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Rod")
        font.setPointSize(12)
        self.contact_4.setFont(font)
        self.contact_4.setObjectName("contact_4")
        self.iname = QtWidgets.QComboBox(self.centralwidget)
        self.iname.setGeometry(QtCore.QRect(350, 90, 161, 31))
        self.iname.setObjectName("iname")
        self.iname.addItem(" ")
        self.contact_5 = QtWidgets.QLabel(self.centralwidget)
        self.contact_5.setGeometry(QtCore.QRect(10, 30, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Rod")
        font.setPointSize(12)
        self.contact_5.setFont(font)
        self.contact_5.setObjectName("contact_5")
        self.iid = QtWidgets.QComboBox(self.centralwidget)
        self.iid.setGeometry(QtCore.QRect(10, 80, 141, 31))
        self.iid.setObjectName("iid")
        self.iid.addItem(" ")
        for tt in range(len(ids)):
            self.iid.addItem(ids[tt])
            
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(150, 40, 20, 85))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 40, 101, 16))
        self.label_2.setObjectName("label_2")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(520, 40, 20, 85))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.contact_6 = QtWidgets.QLabel(self.centralwidget)
        self.contact_6.setGeometry(QtCore.QRect(540, 30, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Rod")
        font.setPointSize(12)
        self.contact_6.setFont(font)
        self.contact_6.setObjectName("contact_6")
        self.tsa = QtWidgets.QLineEdit(self.centralwidget)
        self.tsa.setGeometry(QtCore.QRect(580, 70, 131, 31))
        self.tsa.setObjectName("tsa")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 100, 181, 21))
        self.label_3.setObjectName("label_3")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 170, 771, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 190, 441, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.contact_7 = QtWidgets.QLabel(self.centralwidget)
        self.contact_7.setGeometry(QtCore.QRect(10, 200, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Rod")
        font.setPointSize(12)
        self.contact_7.setFont(font)
        self.contact_7.setObjectName("contact_7")
        self.iid_2 = QtWidgets.QComboBox(self.centralwidget)
        self.iid_2.setGeometry(QtCore.QRect(160, 210, 111, 31))
        self.iid_2.setObjectName("iid_2")
        self.iid_2.addItem(" ")
        for tt in range(len(ids)):
            self.iid_2.addItem(ids[tt])
        self.contact_8 = QtWidgets.QLabel(self.centralwidget)
        self.contact_8.setGeometry(QtCore.QRect(370, 200, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Rod")
        font.setPointSize(12)
        self.contact_8.setFont(font)
        self.contact_8.setObjectName("contact_8")
        self.icat_2 = QtWidgets.QComboBox(self.centralwidget)
        self.icat_2.setGeometry(QtCore.QRect(560, 200, 161, 31))
        self.icat_2.setObjectName("icat_2")
        self.icat_2.addItem(" ")
        for tt in range(len(cat)):
            self.icat_2.addItem(cat[tt])
        self.icat_2.activated.connect(self.pass_Net_Adap2)
        
        self.contact_9 = QtWidgets.QLabel(self.centralwidget)
        self.contact_9.setGeometry(QtCore.QRect(370, 240, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Rod")
        font.setPointSize(12)
        self.contact_9.setFont(font)
        self.contact_9.setObjectName("contact_9")
        self.iname_2 = QtWidgets.QComboBox(self.centralwidget)
        self.iname_2.setGeometry(QtCore.QRect(560, 250, 161, 31))
        self.iname_2.setObjectName("iname_2")
        self.iname_2.addItem(" ")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 220, 101, 16))
        self.label_5.setObjectName("label_5")
        self.add2db_2 = QtWidgets.QPushButton(self.centralwidget)
        self.add2db_2.setGeometry(QtCore.QRect(130, 300, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Rod")
        font.setPointSize(16)
        self.add2db_2.setFont(font)
        self.add2db_2.setStyleSheet("color: rgb(170, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.add2db_2.setObjectName("add2db_2")
        self.resetall_2 = QtWidgets.QPushButton(self.centralwidget)
        self.resetall_2.setGeometry(QtCore.QRect(470, 300, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Kozuka Mincho Pro B")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.resetall_2.setFont(font)
        self.resetall_2.setObjectName("resetall_2")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(0, 330, 771, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 350, 731, 231))
        self.tableWidget.setRowCount(9999)
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setObjectName("tableWidget")



        self.tableWidget.setHorizontalHeaderLabels(["Invoice No.", "Date", "Time", "Supplier Name", "Supplier Contact", "Item ID", "Item Category", "Item Name", "Stock available", "MRP", "Total Payed Amount", "Remarks", "Terms & Conditions", "Details Entered by", "Courier Service Reference", "Courier Service Name", "Courier Service Contact"])


        
        src.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(src)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 21))
        self.menubar.setObjectName("menubar")
        src.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(src)
        self.statusbar.setObjectName("statusbar")
        src.setStatusBar(self.statusbar)

        self.retranslateUi(src)
        QtCore.QMetaObject.connectSlotsByName(src)
        self.add2db.clicked.connect(self.stockcheck)
        self.add2db_2.clicked.connect(self.infocheck)
        self.resetall.clicked.connect(self.tsa.clear)
        self.resetall_2.clicked.connect(self.tableWidget.clear) 

    def retranslateUi(self, src):
        _translate = QtCore.QCoreApplication.translate
        src.setWindowTitle(_translate("src", "STOCK CHECKING MODULE"))
        self.label.setText(_translate("src", "STOCK CHECKING  MODULE"))
        self.contact_3.setText(_translate("src", "Select  CATEGORY"))
        self.resetall.setText(_translate("src", "CLEAR OUTPUT"))
        self.add2db.setText(_translate("src", "CHECK NOW"))
        self.contact_4.setText(_translate("src", "Select  ITEM NAME"))
        self.contact_5.setText(_translate("src", "Select ITEM Id"))
        self.label_2.setText(_translate("src", "OR you can..."))
        self.contact_6.setText(_translate("src", "Total stock available is"))
        self.label_3.setText(_translate("src", "{ items/articles/units }"))
        self.label_4.setText(_translate("src", "INFO.  MODULE"))
        self.contact_7.setText(_translate("src", "Select ITEM Id"))
        self.contact_8.setText(_translate("src", "Select  CATEGORY"))
        self.contact_9.setText(_translate("src", "Select  ITEM NAME"))
        self.label_5.setText(_translate("src", "OR you can..."))
        self.add2db_2.setText(_translate("src", "CHECK NOW"))
        self.resetall_2.setText(_translate("src", "CLEAR OUTPUT"))

    def pass_Net_Adap(self):
        self.iname.clear()
        itemname = str(self.icat.currentText())
        query = str('SELECT product_name FROM raw_inventory WHERE product_subcat = "'+itemname+'";')
        cdb.execute(query)
        ed = cdb.fetchall()
        bad_chars = [';', ')', "(", ","]
        inam = []
        for u in range(len(ed)):
            nd = ''.join((filter(lambda i: i not in bad_chars, ed[u])))
            inam.append(nd)
        self.iname.setObjectName("iname")
        for y in range(len(inam)):
            self.iname.addItem(inam[y])
        str(self.iname.currentText())

    def pass_Net_Adap2(self):
        self.iname_2.clear()
        itemnam = str(self.icat_2.currentText())
        query = str('SELECT product_name FROM raw_inventory WHERE product_subcat = "'+itemnam+'";')
        cdb.execute(query)
        edd = cdb.fetchall()
        bad_chars = [';', ')', "(", ","]
        inamm = []
        for uu in range(len(edd)):
            nnd = ''.join((filter(lambda i: i not in bad_chars, edd[uu])))
            inamm.append(nnd)
        self.iname_2.setObjectName("iname")
        for yy in range(len(inamm)):
            self.iname_2.addItem(inamm[yy])
        str(self.iname_2.currentText())        

    def stockcheck(self, action):
        v5 = str(self.iid.currentText())
        v6 = str(self.icat.currentText())
        v66 = str(self.iname.currentText())
        
        if(v5 != " " and (v6 == " " and v66 == " ")):
            qry = str('SELECT stock FROM raw_inventory WHERE product_id = "'+v5+'";')
            cdb.execute(qry)
            rrr = cdb.fetchall()
            bad_chars = [';', ')', "(", ","]
            inamm = []
            for uu in range(len(rrr)):
                rrr[uu] = str(rrr[uu])
                nnd = ''.join((filter(lambda i: i not in bad_chars, rrr[uu])))
                inamm.append(nnd)
            self.tsa.setText(str(inamm[0]))
            inamm.clear()
        
        elif(v6 != " " and v66 != " " and v5 == " "):
            qry = str('SELECT stock FROM raw_inventory WHERE product_name = "'+v66+'";')
            cdb.execute(qry)
            rrr = cdb.fetchall()
            bad_chars = [";", ")", "(", ","]
            inamm = []
            for uu in range(len(rrr)):
                rrr[uu] = str(rrr[uu])
                nnd = ''.join((filter(lambda i: i not in bad_chars, rrr[uu])))
                inamm.append(nnd)
            self.tsa.setText(str(inamm[0]))
            inamm.clear()

        elif(v6 != " " and v66 != " " and v5 != " "):
            qry = str('SELECT stock FROM raw_inventory WHERE product_name = "'+v66+'";')
            cdb.execute(qry)
            rrr = cdb.fetchall()
            qry1 = str('SELECT stock FROM raw_inventory WHERE product_id = "'+v5+'";')
            cdb.execute(qry1)
            rrrr = cdb.fetchall()
            if(rrr == rrrr):
                bad_chars = [';', ')', "(", ","]
                inamm = []
                for uu in range(len(rrr)):
                    rrr[uu] = str(rrr[uu])
                    nnd = ''.join((filter(lambda i: i not in bad_chars, rrr[uu])))
                    inamm.append(nnd)
                    self.tsa.setText(str(inamm[0]))
                    inamm.clear()
            else:
                from PyQt5.QtWidgets import QMessageBox
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("There is an error")
                msg.setInformativeText("You can either select ProductID or select ItemCategory and ItemName\nIf you're selecting both, then make sure both are of a same item")
                msg.setWindowTitle("Oopssiee !!!")
                msg.exec_()
                pass

        else:
            if(v5 != " "):
                qry = str('SELECT stock FROM raw_inventory WHERE product_id = "'+v5+'";')
                cdb.execute(qry)
                rrr = cdb.fetchall()
                bad_chars = [';', ')', "(", ","]
                inamm = []
                for uu in range(len(rrr)):
                    rrr[uu] = str(rrr[uu])
                    nnd = ''.join((filter(lambda i: i not in bad_chars, rrr[uu])))
                    inamm.append(nnd)
                self.tsa.setText(str(inamm[0]))
                inamm.clear()

    def infocheck(self, action):
        v7 = str(self.iid_2.currentText())
        v8 = str(self.icat_2.currentText())
        v9 = str(self.iname_2.currentText())
        
        if(v7 != " " and (v8 == " " and v9 == " ")):
            qry = str('SELECT * FROM raw_inventory WHERE product_id = "'+v7+'";')
            rio = cdb.execute(qry)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(rio):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            #cdb.close()

        
        elif(v8 != " " and v9 != " " and v7 == " "):
            qry = str('SELECT * FROM raw_inventory WHERE product_name = "'+v9+'";')
            rio = cdb.execute(qry)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(rio):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        elif(v8 != " " and v9 != " " and v7 != " "):
            qry2 = str('SELECT * FROM raw_inventory WHERE product_name = "'+v9+'";')
            cdb.execute(qry2)
            rrr = cdb.fetchall()
            qry1 = str('SELECT * FROM raw_inventory WHERE product_id = "'+v7+'";')
            cdb.execute(qry1)
            rrrr = cdb.fetchall()
            if(rrr == rrrr):
                qry = str('SELECT * FROM raw_inventory WHERE product_name = "'+v9+'";')
                rio = cdb.execute(qry)
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(rio):
                    self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else:
                from PyQt5.QtWidgets import QMessageBox
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("There is an error")
                msg.setInformativeText("You can either select ProductID or select ItemCategory and ItemName\nIf you're selecting both, then make sure both are of a same item")
                msg.setWindowTitle("Oopssiee !!!")
                msg.exec_()
                pass

        else:
            if(v7 != " "):
                qry = str('SELECT * FROM raw_inventory WHERE product_id = "'+v7+'";')
                rio = cdb.execute(qry)
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(rio):
                    self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    src = QtWidgets.QMainWindow()
    ui = Ui_src()
    ui.setupUi(src)
    src.show()
    sys.exit(app.exec_())
