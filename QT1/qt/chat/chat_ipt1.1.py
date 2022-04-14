from PyQt5 import QtCore, QtGui, QtWidgets,QtNetwork
import sys
import requests
import json


def Api(entstr):
    baidu_server = 'https://aip.baidubce.com/oauth/2.0/token?'  # 获取token的server
    grant_type = 'client_credentials'
    client_id = 'xzc2rLD2SsZRn5G2vCkB5rCX'  # API KEY
    client_secret = '2IY87wubtTe2IOEKYEqZDzTEGg7g3zmg'  # Secret KEY
    # 合成请求token的url
    url = baidu_server + 'grant_type=' + grant_type + '&client_id=' + client_id + '&client_secret=' + client_secret
    # 获取token
    res = requests.get(url).text
    data = json.loads(res)  # 将json格式转换为字典格式
    token = data['access_token']
    access_token = token
    q = entstr
    url = 'https://aip.baidubce.com/rpc/2.0/unit/service/chat?access_token=' + access_token  # 不用动
    post_data = "{\"log_id\":\"UNITTEST_10000\",\"version\":\"2.0\",\"service_id\":\"S65015\",\"session_id\":\"\",\"request\":{\"query\":\"%s\",\"user_id\":\"88888\",\"query_info\":{\"type\":\"TEXT\",\"source\":\"KEYBOARD\"}}}}" % (
        q)

    headers = {'content-type': 'application/x-www-form-urlencoded'}  # 不用管
    response = requests.post(url, data=post_data.encode('utf-8'), headers=headers)
    if response:
        r = response.json()
        saying = r["result"]["response_list"][1]["action_list"][0]["say"]  # 擦，这个json层级真难找。。
    return saying

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("快和小Q聊天吧!")
        Dialog.resize(582, 434)
        #self.manager = QtNetwork(self)
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
        self.pushButton_.clicked.connect(self.clickButton)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "小Q聊天"))
        self.label.setText(_translate("Dialog", "快和小Q聊天吧!"))
        self.pushButton_.setText(_translate("Dialog", "发送"))
        self.label_3.setText(_translate("Dialog", "输入框"))

    def clickButton(self):
        self.get_response()

    @staticmethod
    def get_response(self):
            print('jinru')
            entrstr = self.plainTextEdit_2.toPlainText()
            ans = self.Api(entrstr)
            #r = requests.post(url, data=data).json()
            result = ">> 我：{0}\n \n>> 小Q：{1}#^_^# \n".format(entrstr, ans)
            self.plainTextEdit.setPlainText(result)
            #print(ans)
        #return result