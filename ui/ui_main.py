# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(228, 538)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vbox_main = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vbox_main.setContentsMargins(0, 0, 0, 0)
        self.vbox_main.setSpacing(0)
        self.vbox_main.setObjectName("vbox_main")
        self.tabw_main = QtWidgets.QTableWidget(self.centralwidget)
        self.tabw_main.setObjectName("tabw_main")
        self.tabw_main.setColumnCount(0)
        self.tabw_main.setRowCount(0)
        self.vbox_main.addWidget(self.tabw_main)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_excel = QtWidgets.QPushButton(self.centralwidget)
        self.bt_excel.setObjectName("bt_excel")
        self.horizontalLayout_2.addWidget(self.bt_excel)
        self.vbox_main.addLayout(self.horizontalLayout_2)
        self.bt_save = QtWidgets.QPushButton(self.centralwidget)
        self.bt_save.setObjectName("bt_save")
        self.vbox_main.addWidget(self.bt_save)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_excel.setText(_translate("MainWindow", "Excel表"))
        self.bt_save.setText(_translate("MainWindow", "保存修改"))