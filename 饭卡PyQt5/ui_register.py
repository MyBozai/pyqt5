# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_register_window(object):
    def setupUi(self, register_window):
        register_window.setObjectName("register_window")
        register_window.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(register_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(170, 20, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.password_edit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit_2.setGeometry(QtCore.QRect(130, 190, 191, 31))
        self.password_edit_2.setObjectName("password_edit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.username_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_edit.setGeometry(QtCore.QRect(130, 90, 191, 31))
        self.username_edit.setObjectName("username_edit")
        self.password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit.setGeometry(QtCore.QRect(130, 140, 191, 31))
        self.password_edit.setObjectName("password_edit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.register_btn = QtWidgets.QPushButton(self.centralwidget)
        self.register_btn.setGeometry(QtCore.QRect(170, 240, 91, 31))
        self.register_btn.setObjectName("register_btn")
        register_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(register_window)
        self.statusbar.setObjectName("statusbar")
        register_window.setStatusBar(self.statusbar)

        self.retranslateUi(register_window)
        QtCore.QMetaObject.connectSlotsByName(register_window)

    def retranslateUi(self, register_window):
        _translate = QtCore.QCoreApplication.translate
        register_window.setWindowTitle(_translate("register_window", "注册"))
        self.label.setText(_translate("register_window", "注册"))
        self.label_2.setText(_translate("register_window", "账号"))
        self.label_4.setText(_translate("register_window", "确认密码"))
        self.label_3.setText(_translate("register_window", "密码"))
        self.register_btn.setText(_translate("register_window", "注册"))
