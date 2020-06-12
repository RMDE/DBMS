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

name = None
passwd = None
line1 = None
line2 = None

# 显示学生用户界面    
def student(log,sql,ID):
    global name,gui,mysql
    gui = log
    mysql = sql
    name = ID
    gui.resize(1920,1080) # 窗口大小
    gui.center() # 窗口位置
    gui.setWindowTitle('学生界面') # 窗口标题
    gui.setWindowOpacity(0.98)
    head1 = gui.Label("",0,0,150,1920,"white",50)
    head1.setStyleSheet("QLabel{background:#4DBF4D}")
    head2 = gui.Label("",0,150,50,1920,"white",50)
    head2.setStyleSheet("QLabel{background:#3DAF3D}")
    head3 = gui.Label("",0,150,3,1920,"white",50)
    head3.setStyleSheet("QLabel{background:#6DDF6D}")
    title1 = gui.Label("教务信息管理系统",30,30,70,500,"white",50)
    title2 = gui.Label("Educational Information Administration System",30,95,50,500,"white",20)
    character1 = gui.Label("学生",1450,55,60,100,"white",30)
    character2 = gui.Label(name,1800,60,50,100,"white",25)
    character3 = gui.Label("",1700,60,50,50,"white",30)
    character3.setPixmap(Load("student.jpg",character3.width(),character3.height()))

    #lbl1 = gui.Label("",100,120,50,50)
    #lbl1.setStyleSheet("QLabel{background:white;}")
    #lbl1.setPixmap(Load("login.jpg",lbl1.width()/3*2,lbl1.height()/3*2))
    #lbl2 = gui.Label("",100,190,50,50)
    #lbl2.setStyleSheet("QLabel{background:white;}")
    #lbl2.setPixmap(Load("passwd.jpg",lbl2.width()/3*2,lbl2.height()/3*2))
    #line1 = gui.Input(150,120,"学号/工号",50,350)
    #line2 = gui.Input(150,190,"密码",50,350)
    #btn = gui.Button('登录',100,270,show_login_status,50,400,"white","#6DDF6D",30)
    gui.show()

if __name__=='__main__':
    global mysql,gui,ID
    mysql = None
    app = QApplication(sys.argv)
    #mysql = mydb("localhost","root","123456")
    #mysql.init_data()
    gui = Gui()
    ID = "1620101"
    student(gui,mysql,ID)
    sys.exit(app.exec_())
