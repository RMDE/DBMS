from gui import *
from db_manager import *
from event import *
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,
        QTextEdit,QLabel,QPushButton, QApplication,QMainWindow, QAction, qApp,
        QHBoxLayout, QVBoxLayout,QGridLayout,QLineEdit)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication
    
name = None
passwd = None
line1 = None
line2 = None

# 显示登陆界面    
def login(gui):
    global name,passwd,line1,line2
    gui.resize(600,400) # 窗口大小
    gui.center() # 窗口位置
    gui.setWindowTitle('信息管理系统') # 窗口标题
    gui.setWindowIcon(QIcon('Element/Icon.jpg')) # 应用图标
    lbl = gui.Label("登录",250,60,70,100)
    line1 = gui.Input(150,150,"学号/工号",50,350)
    line2 = gui.Input(150,220,"密码",50,350)
    line2.setEchoMode(QLineEdit.Password)
    btn = gui.Button('登录',100,300,show_login_status,50,400)
    gui.show()

# 显示登录成功状态
def show_login_status():
    global name,passwd,line1,line2,mysql,gui
    name = line1.text()
    passwd = line2.text()
    if name=="" or passwd=="":
        Info(gui,"用户名或密码不能为空")
    else:
        res,flag = mysql.get_passwd(name)
        if flag==True and res!=[]:
            res = res[0][0]
            if passwd == res:
                Info(gui,"登录成功")
            else:
                Error(gui,"密码错误")
        elif flag==True and res==[]:
            Error(gui,"用户名不存在")
        else:
            Error(gui,"数据库操作错误")


if __name__=='__main__':
    global mysql,gui
    app = QApplication(sys.argv)
    mysql = mydb("localhost","root","123456")
    mysql.init_data()
    gui = Gui()
    login(gui)
    sys.exit(app.exec_())
