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
    global name,gui,mysql,date
    gui = log
    mysql = sql
    name = ID
    gui.resize(1920,1080) # 窗口大小
    gui.center() # 窗口位置
    gui.setWindowTitle('学生界面') # 窗口标题
    gui.setWindowOpacity(0.98)
    head1 = gui.Label("",0,0,150,1920)
    head1.setStyleSheet("QLabel{background:#4DBF4D}")
    head2 = gui.Label("",0,150,50,1920)
    head2.setStyleSheet("QLabel{background:#3DAF3D}")
    head3 = gui.Label("",0,150,3,1920)
    head3.setStyleSheet("QLabel{background:#6DDF6D}")
    title1 = gui.Label("教务信息管理系统",30,30,70,500,"white",50)
    title2 = gui.Label("Educational Information Administration System",30,95,50,500,"white",20)
    character1 = gui.Label("学生",1450,55,60,100,"white",30)
    character2 = gui.Label(name,1800,60,50,100,"white",25)
    character3 = gui.Label("",1700,60,50,50,"white",30)
    character3.setScaledContents(True)
    character3.setPixmap(Load("student.jpg",character3.width(),character3.height()))
    character3.setStyleSheet("QLabel{border-radius:25px;}")

    #line1 = gui.Input(150,120,"学号/工号",50,350)
    #line2 = gui.Input(150,190,"密码",50,350)
    #btn = gui.Button('登录',100,270,show_login_status,50,400,"white","#6DDF6D",30)
    btn1 = gui.Button('个人信息',0,200,show_info,60,400,"gray","white",26);
    btn2 = gui.Button('个人课表',0,260,show_course,60,400,"gray","white",26);
    btn3 = gui.Button('考试安排',0,320,show_exam,60,400,"gray","white",26);
    btn4 = gui.Button('成绩查询',0,380,show_grade,60,400,"gray","white",26);
    btn5 = gui.Button('选修课程',0,440,search_course,60,400,"gray","white",26);
    btn6 = gui.Button('教师查询',0,500,search_teacher,60,400,"gray","white",26);
    btn7 = gui.Button('借阅书籍',0,560,borrow_book,60,400,"gray","white",26);
    btn8 = gui.Button('缴纳电费',0,620,charge,60,400,"gray","white",26);
    tail = gui.Label("",0,680,400,400)
    tail.setStyleSheet("QLabel{background:white;}")
    lbl = gui.Label(">>>校历",500,250,50,100,"black",25)
    lbl1 = gui.Label("",500,300,2,1420)
    lbl1.setStyleSheet("QLabel{background:gray;}")
    cal = gui.Calendar(600,400,400,800)
    time = gui.Timer(550,850)
    Emot = gui.Label("",1500,700,300,300)
    character3.setScaledContents(True)
    Emot.setPixmap(Load("Emot1.jpg",Emot.width(),Emot.height()))

    gui.show()

def show_info():
    pass

def show_course():
    pass

def show_exam():
    pass

def show_grade():
    pass

def search_course():
    pass

def search_teacher():
    pass

def borrow_book():
    pass

def charge():
    pass


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
