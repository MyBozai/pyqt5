# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_manage_window(object):
    def setupUi(self, manage_window):
        manage_window.setObjectName("manage_window")
        manage_window.resize(800, 594)
        self.centralwidget = QtWidgets.QWidget(manage_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 130, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(370, 130, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.name_label.setFont(font)
        self.name_label.setText("")
        self.name_label.setObjectName("name_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(290, 30, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.loss_logout_btn = QtWidgets.QPushButton(self.centralwidget)
        self.loss_logout_btn.setGeometry(QtCore.QRect(500, 280, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.loss_logout_btn.setFont(font)
        self.loss_logout_btn.setObjectName("loss_logout_btn")
        self.infos_btn = QtWidgets.QPushButton(self.centralwidget)
        self.infos_btn.setGeometry(QtCore.QRect(140, 280, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.infos_btn.setFont(font)
        self.infos_btn.setObjectName("infos_btn")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(340, 430, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.change_pwd_btn = QtWidgets.QPushButton(self.centralwidget)
        self.change_pwd_btn.setGeometry(QtCore.QRect(500, 150, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.change_pwd_btn.setFont(font)
        self.change_pwd_btn.setObjectName("change_pwd_btn")
        manage_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(manage_window)
        self.statusbar.setObjectName("statusbar")
        manage_window.setStatusBar(self.statusbar)

        self.retranslateUi(manage_window)
        QtCore.QMetaObject.connectSlotsByName(manage_window)

    def retranslateUi(self, manage_window):
        _translate = QtCore.QCoreApplication.translate
        manage_window.setWindowTitle(_translate("manage_window", "饭卡管理系统"))
        self.label_2.setText(_translate("manage_window", "你好，管理员："))
        self.label.setText(_translate("manage_window", "饭卡管理系统"))
        self.loss_logout_btn.setText(_translate("manage_window", "挂失和注销"))
        self.infos_btn.setText(_translate("manage_window", "用户信息"))
        self.back_btn.setText(_translate("manage_window", "退出登录"))
        self.change_pwd_btn.setText(_translate("manage_window", "修改密码"))
