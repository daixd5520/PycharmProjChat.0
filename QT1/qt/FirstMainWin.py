import sys
import requests
from PyQt5 import QtGui,QtCore,QtWidgets

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
import mainwin
from vip import vip_ui, vip_y
from qt.chat import chat_ui
from qt.chat import chat_ipt1

class FirstMainWin(QMainWindow):
    def __init__(self, parent = None):
        super(FirstMainWin, self).__init__(parent)

        # 设置主窗口标题
        self.setWindowTitle('第一个交互界面')

        # 设置窗口尺寸
        self.resize(400, 300)

        self.status = self.statusBar()
        # self.status.showMessage('只存在5秒', 5000)


class Vip_dialog5(QMainWindow):
    def __init__(self, parent = None):
        super(Vip_dialog5, self).__init__(parent)

        # 设置窗口尺寸
        self.resize(400, 300)

        self.status = self.statusBar()
        # self.status.showMessage('只存在5秒', 5000)


class Vip_y_dialog5(QMainWindow):
    def __init__(self, parent = None):
        super(Vip_y_dialog5, self).__init__(parent)

        # 设置窗口尺寸
        self.resize(400, 300)

        self.status = self.statusBar()
        # self.status.showMessage('只存在5秒', 5000)

class Chat_dialog(QMainWindow):
    def __init__(self, parent = None):
        super(Chat_dialog,self).__init__(parent)

        self.resize(400,300)
        self.status = self.statusBar()

class Chat_1_dialog(QMainWindow):
    def __init__(self, parent = None):
        super(Chat_1_dialog,self).__init__(parent)

        self.resize(400,300)
        self.status = self.statusBar()

def Vip_handleCalc():
    print('已点击会员按钮')
    dialog5 = vip_ui.Ui_Dialog()
    dialog5.setupUi(vip_child)
    # 设置主窗口标题
    vip_child.setWindowTitle('会员界面')
    dialog5.pushButton.clicked.connect(Vip_y_handleCalc)
    vip_child.show()

def Vip_y_handleCalc():
    print('已点击我是会员按钮')
    dialog = vip_y.Ui_Dialog()
    dialog.setupUi(vip_y_child)
    # 设置主窗口标题
    vip_y_child.setWindowTitle('会员界面')
    vip_y_child.show()

def Chat_handleCalc():
    print('已点击聊天按钮')
    dialog = chat_ui.Ui_MainWindow()
    dialog.setupUi(chat_child)
    #设置主窗口标题
    chat_child.setWindowTitle('聊天')
    dialog.pushButton_2.clicked.connect(Chat_1_handleCalc)
    chat_child.show()#聊天点进去第一个界面（选择语音还是手写）

def Chat_1_handleCalc():
    print('已点击打字输入按钮')
    dialog = chat_ipt1.Ui_Dialog()#小Q聊天界面
    dialog.setupUi(chat_1_child)
    chat_1_child.setWindowTitle('打字输入')
    chat_1_child.show()
    # if(dialog.pushButton_.clicked()==1):
    #         dialog.get_response()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 主界面
    main = FirstMainWin()
    ui = mainwin.Ui_MainWindow()
    ui.setupUi(main)

    # 子界面及其他下级界面
    vip_child = Vip_dialog5()
    vip_y_child = Vip_y_dialog5()
    chat_child = Chat_dialog()
    chat_1_child = Chat_1_dialog()

    # 主界面调用按键
    ui.pushButton_5.clicked.connect(Vip_handleCalc)
    ui.pushButton.clicked.connect(Chat_handleCalc)

    # 主界面设置应用程序图标
    app.setWindowIcon(QIcon('./image/jlu.ico'))
    main.setWindowTitle('第一个交互界面')

    # 显示主界面
    main.show()

    sys.exit(app.exec_())
