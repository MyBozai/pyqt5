# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_forget_window(object):
    def setupUi(self, forget_window):
        forget_window.setObjectName("forget_window")
        forget_window.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(forget_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(120, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.sid_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.sid_edit.setGeometry(QtCore.QRect(130, 90, 191, 31))
        self.sid_edit.setObjectName("sid_edit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.username_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_edit.setGeometry(QtCore.QRect(130, 140, 191, 31))
        self.username_edit.setObjectName("username_edit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.phone_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_edit.setGeometry(QtCore.QRect(130, 190, 191, 31))
        self.phone_edit.setObjectName("phone_edit")
        self.finding_btn = QtWidgets.QPushButton(self.centralwidget)
        self.finding_btn.setGeometry(QtCore.QRect(150, 240, 91, 31))
        self.finding_btn.setObjectName("finding_btn")
        forget_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(forget_window)
        self.statusbar.setObjectName("statusbar")
        forget_window.setStatusBar(self.statusbar)

        self.retranslateUi(forget_window)
        QtCore.QMetaObject.connectSlotsByName(forget_window)

    def retranslateUi(self, forget_window):
        _translate = QtCore.QCoreApplication.translate
        forget_window.setWindowTitle(_translate("forget_window", "忘记密码"))
        self.label.setText(_translate("forget_window", "验证账号"))
        self.label_2.setText(_translate("forget_window", "账号"))
        self.label_3.setText(_translate("forget_window", "姓名"))
        self.label_4.setText(_translate("forget_window", "联系电话"))
        self.finding_btn.setText(_translate("forget_window", "找回密码"))
