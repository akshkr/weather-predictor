# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from read_1 import *
import read_2 as r2

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(910, 490)
        Form.setWindowOpacity(1.0)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(109, 109, 109);\n"
"background-color: rgb(91, 91, 91);")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(30, 110, 181, 231))
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(47, 47, 47);\n"
"border-color: rgb(227, 227, 227);")
        self.listWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        #item = QtWidgets.QListWidgetItem()
        #self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(0, 50, 941, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 379, 101, 51))
        self.pushButton_3.setStyleSheet("background-color: rgb(122, 122, 122);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(20, 450, 421, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(Form)
        self.progressBar_2.setGeometry(QtCore.QRect(470, 450, 421, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 70, 441, 411))
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 310, 101, 50))
        self.pushButton_5.setStyleSheet("background-color: rgb(122, 122, 122);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(140, 310, 101, 50))
        self.pushButton.setStyleSheet("background-color: rgb(122, 122, 122);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 101, 17))
        self.label.setObjectName("label")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(10, 300, 421, 71))
        self.frame_5.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.raise_()
        self.pushButton_5.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(460, 70, 441, 411))
        self.frame_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 310, 101, 50))
        self.pushButton_6.setStyleSheet("background-color: rgb(122, 122, 122);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.listWidget_3 = QtWidgets.QListWidget(self.frame_3)
        self.listWidget_3.setGeometry(QtCore.QRect(20, 50, 181, 111))
        self.listWidget_3.setStyleSheet("color: rgb(241, 241, 241);\n"
"background-color: rgb(47, 47, 47);")
        self.listWidget_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_3)
        self.listWidget_2.setGeometry(QtCore.QRect(240, 50, 181, 201))
        self.listWidget_2.setStyleSheet("color: rgb(243, 234, 255);\n"
"background-color: rgb(47, 47, 47);")
        self.listWidget_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 310, 101, 50))
        self.pushButton_2.setStyleSheet("background-color: rgb(122, 122, 122);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 310, 101, 50))
        self.pushButton_4.setStyleSheet("background-color: rgb(122, 122, 122);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 111, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(240, 20, 101, 17))
        self.label_3.setObjectName("label_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setGeometry(QtCore.QRect(230, 10, 201, 251))
        self.frame_6.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setObjectName("frame_6")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setGeometry(QtCore.QRect(10, 10, 201, 171))
        self.frame_7.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setObjectName("frame_7")
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setGeometry(QtCore.QRect(10, 300, 421, 71))
        self.frame_8.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setObjectName("frame_8")
        self.frame_8.raise_()
        self.frame_7.raise_()
        self.frame_6.raise_()
        self.pushButton_6.raise_()
        self.listWidget_3.raise_()
        self.listWidget_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_4.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 0, 131, 51))
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 100, 201, 251))
        self.frame.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setObjectName("frame")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 201, 251))
        self.frame_4.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setObjectName("frame_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 0, 31, 61))
        self.label_5.setObjectName("label_5")
        self.frame_2.raise_()
        self.frame.raise_()
        self.frame_3.raise_()
        self.listWidget.raise_()
        self.line_2.raise_()
        self.pushButton_3.raise_()
        self.progressBar.raise_()
        self.progressBar_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #working code
        self.u = 0.0
        #list widget click and store in variable -> select year 1
        self.listWidget.itemClicked.connect(self.ClckLW)

        #list widget 3 -> select month 2
        self.listWidget_3.itemClicked.connect(self.ClickRW1)

        #list widget 2 -> select year 2
        self.listWidget_2.itemClicked.connect(self.ClickRW2)

        #pushButton -> Get Graph 1
        self.pushButton.clicked.connect(self.push3)

        #pushButton5 -> Get Data 1
        self.pushButton_5.clicked.connect(self.push6)

        #pushButton3 -> Get Comparison 1
        self.pushButton_3.clicked.connect(self.push0)

        #pushButton2 -> Get Graph 2
        self.pushButton_2.clicked.connect(self.push4)

        #pushButton4 -> Get comparison 2
        self.pushButton_4.clicked.connect(self.push5)

        #pushbutton6 -> Get Data 2
        self.pushButton_6.clicked.connect(self.push7)


    #click List Widget
    def ClckLW(self, item):
    	self.x = int(item.text())
    	return self.x

    #click List widget month 2
    def ClickRW1(self, item):
        self.y = item.text()
        if self.y == "June":
            self.u = 0
        elif self.y == "July":
            self.u = 1
        elif self.y == "August":
            self.u = 2
        else:
            self.u = 3


    #click List Widget Year 2
    def ClickRW2(self, item):
    	self.z = int(item.text())
    	return self.z


    #click Get Comparison 1 button
    def push0(self):
    	self.complete = 0
    	while self.complete<100.0:
    		self.complete += 0.00005
    		self.progressBar.setValue(self.complete)
    	plot_rain_comp(self.x)

    #click get Graph1 button
    def push3(self):
    	self.complete = 0
    	while self.complete<100.0:
    		self.complete += 0.00005
    		self.progressBar.setValue(self.complete)
    	plot_rain(self.x)

    #Click Get Graph 2 button
    def push4(self):
    	self.complete = 0
    	while self.complete<100.0:
    		self.complete += 0.00005
    		self.progressBar_2.setValue(self.complete)
    	r2.plot_rain2(self.z, self.u)

    #Click Get comparison 2 button
    def push5(self):
        self.complete = 0
        while self.complete<100.0:
            self.complete += 0.00005
            self.progressBar_2.setValue(self.complete)
        r2.plot_rain_comp2(self.z, self.u)

    #Click Get data 1
    def push6(self):
        self.complete = 0
        while self.complete<100.0:
            self.complete += 0.00005
            self.progressBar.setValue(self.complete)
        writecsv(self.x)

    #Click Get data 2
    def push7(self):
        self.complete = 0
        while self.complete<100.0:
            self.complete += 0.00005
            self.progressBar_2.setValue(self.complete)
        r2.writecsv2(self.z, self.u)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Weather Predictor"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "2010"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "2011"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "2012"))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "2013"))
        #item = self.listWidget.item(4)
        #item.setText(_translate("Form", "2014"))
        item = self.listWidget.item(4)
        item.setText(_translate("Form", "2015"))
        item = self.listWidget.item(5)
        item.setText(_translate("Form", "2016"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_3.setText(_translate("Form", "Get Comparison"))
        self.pushButton_5.setText(_translate("Form", "Get Data"))
        self.pushButton.setText(_translate("Form", "Get Graph"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#f0eff0;\">Select Year : </span></p></body></html>"))
        self.pushButton_6.setText(_translate("Form", "Get Data"))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        item = self.listWidget_3.item(0)
        item.setText(_translate("Form", "June"))
        item = self.listWidget_3.item(1)
        item.setText(_translate("Form", "July"))
        item = self.listWidget_3.item(2)
        item.setText(_translate("Form", "August"))
        item = self.listWidget_3.item(3)
        item.setText(_translate("Form", "September"))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("Form", "2010"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("Form", "2011"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("Form", "2012"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("Form", "2013"))
        #item = self.listWidget_2.item(4)
        #item.setText(_translate("Form", "2014"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("Form", "2015"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("Form", "2016"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("Form", "Get Graph"))
        self.pushButton_4.setText(_translate("Form", "Get Comparison"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#e3e3e3;\">Select Month : </span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#ececec;\">Select Year : </span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Ingenious</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<img src=\"logo.png\" alt=\"Mountain View\" style=\"width:10px;height:22px;\">"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

