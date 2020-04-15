# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tambah.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TambahData(object):
    def setupUi(self, TambahData):
        TambahData.setObjectName("TambahData")
        TambahData.resize(562, 272)
        self.centralwidget = QtWidgets.QWidget(TambahData)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 311, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 70, 311, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 110, 311, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 150, 311, 24))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 190, 141, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Add = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Add.setObjectName("Add")
        self.horizontalLayout.addWidget(self.Add)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(310, 190, 161, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Reset = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Reset.setObjectName("Reset")
        self.horizontalLayout_2.addWidget(self.Reset)
        TambahData.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TambahData)
        self.statusbar.setObjectName("statusbar")
        TambahData.setStatusBar(self.statusbar)

        self.retranslateUi(TambahData)
        QtCore.QMetaObject.connectSlotsByName(TambahData)

    def retranslateUi(self, TambahData):
        _translate = QtCore.QCoreApplication.translate
        TambahData.setWindowTitle(_translate("TambahData", "Tambah Data"))
        self.label.setText(_translate("TambahData", "No "))
        self.label_2.setText(_translate("TambahData", "Nama"))
        self.label_3.setText(_translate("TambahData", "Kelas"))
        self.label_4.setText(_translate("TambahData", "No Absen"))
        self.Add.setText(_translate("TambahData", "Add"))
        self.Reset.setText(_translate("TambahData", "Reset"))
