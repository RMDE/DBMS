from gui import *
from db_manager import *
from event import *
import register
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,
        QTextEdit,QLabel,QPushButton, QApplication,QMainWindow, QAction, qApp,
        QHBoxLayout, QVBoxLayout,QGridLayout,QLineEdit)
from PyQt5.QtGui import QFont,QIcon,QPixmap,QPalette,QColor
from PyQt5.QtCore import QCoreApplication,Qt
import re
import os
from time import sleep
from student import student
from teacher import teacher
from manager import manager
from worker import worker

name = None
passwd = None
line1 = None
line2 = None

# 显示登陆界面    
def login(log,sql):
    global name,passwd,line1,line2,gui,mysql
    gui = log
    mysql = sql
    gui.resize(600,400) # 窗口大小
    gui.center() # 窗口位置
    gui.setWindowTitle('信息管理系统') # 窗口标题
    gui.setWindowOpacity(0.97)
    lbl = gui.Label("登录",250,30,70,100,"#6DDF6D",50)
    lbl.setAutoFillBackground(False)
    lbl1 = gui.Label("",100,120,50,50)
    lbl1.setStyleSheet("QLabel{background:white;}")
    lbl1.setPixmap(Load("login.jpg",lbl1.width()/3*2,lbl1.height()/3*2))
    lbl2 = gui.Label("",100,190,50,50)
    lbl2.setStyleSheet("QLabel{background:white;}")
    lbl2.setPixmap(Load("passwd.jpg",lbl2.width()/3*2,lbl2.height()/3*2))
    line1 = gui.Input(150,120,"学号/工号",50,350)
    line2 = gui.Input(150,190,"密码",50,350)
    line2.setEchoMode(QLineEdit.Password)
    btn = gui.Button('登录',100,270,show_login_status,50,400,"white","#6DDF6D",30)
    btn1 = gui.Button('没有账号？注册一个',400,340,jump2reg,50,200,"black",None,15)
    gui.show()

# 跳转到注册窗口
def jump2reg():
    sleep(1)
    reg = Gui()
    register.register(reg,mysql)
    gui.close()

# 跳转界面
def jump():
    global name
    reg = Gui()
    if re.match("S",name):
        student(reg,mysql,name)
        gui.close()
    elif re.match("T",name):
        teacher(reg,mysql,name)
        gui.close()
    elif re.match("W",name):
        worker(reg,mysql,name)
        gui.close()
    elif re.match("M",name):
        manager(reg,mysql,name)
        gui.close()
    gui.close()

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
                jump()
            else:
                Error(gui,"密码错误")
        elif flag==True and res==[]:
            Error(gui,"用户名不存在")
        else:
            Error(gui,"数据库操作错误")


if __name__=='__main__':
    global mysql,gui
    app = QApplication(sys.argv)
    mysql = None
    mysql = mydb("localhost","root","123456")
    gui = Gui()
    login(gui,mysql)
    sys.exit(app.exec_())
