# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reset.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_reset_window(object):
    def setupUi(self, reset_window):
        reset_window.setObjectName("reset_window")
        reset_window.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(reset_window)
        self.centralwidget.setObjectName("centralwidget")
        self.set_btn = QtWidgets.QPushButton(self.centralwidget)
        self.set_btn.setGeometry(QtCore.QRect(160, 240, 91, 31))
        self.set_btn.setObjectName("set_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(140, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.sid_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.sid_edit.setGeometry(QtCore.QRect(120, 90, 191, 31))
        self.sid_edit.setText("")
        self.sid_edit.setObjectName("sid_edit")
        self.password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit.setGeometry(QtCore.QRect(120, 140, 191, 31))
        self.password_edit.setText("")
        self.password_edit.setObjectName("password_edit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.check_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.check_edit.setGeometry(QtCore.QRect(120, 190, 191, 31))
        self.check_edit.setText("")
        self.check_edit.setObjectName("check_edit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        reset_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(reset_window)
        self.statusbar.setObjectName("statusbar")
        reset_window.setStatusBar(self.statusbar)

        self.retranslateUi(reset_window)
        QtCore.QMetaObject.connectSlotsByName(reset_window)

    def retranslateUi(self, reset_window):
        _translate = QtCore.QCoreApplication.translate
        reset_window.setWindowTitle(_translate("reset_window", "设置账号"))
        self.set_btn.setText(_translate("reset_window", "设置"))
        self.label.setText(_translate("reset_window", "找回密码"))
        self.label_2.setText(_translate("reset_window", "账号"))
        self.label_3.setText(_translate("reset_window", "密码"))
        self.label_4.setText(_translate("reset_window", "确认密码"))
