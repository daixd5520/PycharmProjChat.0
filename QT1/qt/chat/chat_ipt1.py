#大程序中用的这一份
from PyQt5 import QtCore, QtGui, QtWidgets,QtNetwork
import sys
# import requests
# import json
# import numpy as np
# import math
from qt.chat import getRes as gRes

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("快和小Q聊天吧!")
        Dialog.resize(582, 434)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 361, 51))
        self.label.setStyleSheet("color: rgb(100, 200, 200);\n"
"font: 16pt \"黑体\";\n"
"text-decoration: none;")
        self.label.setObjectName("dialog")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 80, 501, 181))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(40, 310, 401, 41))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit.setStyleSheet("font: 14pt \"黑体\";\n")
        self.pushButton_ = QtWidgets.QPushButton(Dialog)
        self.pushButton_.setGeometry(QtCore.QRect(480, 320, 75, 23))
        self.pushButton_.setStyleSheet("font: 14pt \"黑体\";\n""background-color: rgb(225, 255, 0);")
        self.pushButton_.setObjectName("pushButton_")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 280, 54, 12))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 280, 71, 16))
        self.label_3.setStyleSheet("font: 75 12pt \"Aharoni\";")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "小Q聊天"))
        self.label.setText(_translate("Dialog", "快和小Q聊天吧!"))
        self.pushButton_.setText(_translate("Dialog", "发送"))
        self.label_3.setText(_translate("Dialog", "输入框"))
        self.pushButton_.clicked.connect(self.get_response)

    # @staticmethod
    def get_response(self):
        print("点击发送按钮")
        enterstr = self.plainTextEdit_2.toPlainText()
        m=gRes.getRes(enterstr)
        s=">>你:"+enterstr+"\n"+m
        self.plainTextEdit.setPlainText(s)
        return s

    def getRes(self,entstr):
        lst = ["推荐", "好吃", "饭", "菜"]
        # byeLst = ["拜拜", "不聊了", "不说了", "再见"]
        mystr = entstr
        canUseMine = -1
        for name in lst:
            if name in mystr:
                canUseMine = 1
                break
        if (canUseMine == 1):
            s = gRes.myChat()
        else:
            s = gRes.apiUsing(mystr)
        return s

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        main = QtWidgets.QMainWindow()
        mainwindow = Ui_Dialog()
        mainwindow.setupUi(main)
        main.show()
        sys.exit(app.exec())