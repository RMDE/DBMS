from gui import *
from db_manager import *
from event import *
import register
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,
        QTextEdit,QLabel,QPushButton, QApplication,QMainWindow, QAction, qApp,
        QHBoxLayout, QVBoxLayout,QGridLayout,QLineEdit,QButtonGroup,QTableWidgetItem)
from PyQt5.QtGui import QFont,QIcon,QPixmap,QPalette,QColor
from PyQt5.QtCore import QCoreApplication,Qt,QPoint
import re
import os
from time import sleep


# 显示用户界面    
def worker(log,sql,ID):
    global name,gui,mysql
    gui = log
    mysql = sql
    name = ID
    show_frame(gui)
    lbl = gui.Label(">>>校历",500,250,50,100,"black",25)
    lbl1 = gui.Label("",500,300,2,1420)
    lbl1.setStyleSheet("QLabel{background:gray;}")
    cal = gui.Calendar(600,400,400,800)
    time = gui.Timer(550,850)
    gui.show()


# 显示框架
def show_frame(gui):
    global btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8
    gui.resize(1920,1080) # 窗口大小
    gui.center() # 窗口位置
    gui.setWindowTitle('工作人员界面') # 窗口标题
    gui.setWindowOpacity(0.98)
    head1 = gui.Label("",0,0,150,1920)
    head1.setStyleSheet("QLabel{background:#4DBF4D}")
    head2 = gui.Label("",0,150,50,1920)
    head2.setStyleSheet("QLabel{background:#3DAF3D}")
    head3 = gui.Label("",0,150,3,1920)
    head3.setStyleSheet("QLabel{background:#6DDF6D}")
    title1 = gui.Label("教务信息管理系统",30,30,70,500,"white",50)
    title2 = gui.Label("Educational Information Administration System",30,95,50,500,"white",20)
    character1 = gui.Label("工作人员",1400,55,60,150,"white",30)
    character2 = gui.Label(name,1750,60,50,150,"white",25)
    character3 = gui.Label("",1700,60,50,50,"white",30)
    character3.setScaledContents(True)
    character3.setPixmap(Load("student.jpg",character3.width(),character3.height()))
    character3.setStyleSheet("QLabel{border-radius:25px;}")
    btn1 = gui.Button('个人信息',0,200,show_info,60,400,"gray","white",26);
    btn2 = gui.Button('宿舍管理',0,260,show_department,60,400,"gray","white",26);
    btn3 = gui.Button('搜索宿舍',0,320,search_department,60,400,"gray","white",26);
    tail = gui.Label("",0,380,700,400)
    tail.setStyleSheet("QLabel{background:white;}")

# 显示个人信息
def show_info():
    global name,mysql,gui,btn1,line2,line8,line9,info
    gui = Gui()
    show_frame(gui)
    [info,flag] = mysql.show_info(name)
    btn1 = gui.Button('个人信息',0,200,show_info,60,400,"gray","#DFDFDF",26);
    btn1.setEnabled(False)
    lbl1 = gui.Label("工号: ",700,250,50,120,size=25)
    lbl2 = gui.Label("姓名: ",1200,250,50,120,size=25)
    lbl3 = gui.Label("性别: ",700,350,50,120,size=25)
    lbl8 = gui.Label("电话: ",1200,350,50,120,size=25)
    lbl9 = gui.Label("生日: ",700,450,50,120,size=25)
    lbl10 = gui.Label("薪水: ",1200,450,50,120,size=25)

    if flag == False:
        Error(gui,info)
    else:
        line1 = gui.Label(info[0][0],820,250,50,200)
        line2 = gui.Input(1350,250,info[0][1],50,200)
        line3 = gui.Label(info[0][2],820,350,50,200)
        line8 = gui.Input(1350,350,info[0][3],50,200)
        line9 = gui.Input(820,450,info[0][4].strftime('%Y-%m-%d'),50,200)
        line10 = gui.Label(str(info[0][5]),1350,450,50,200)
    
        commit = gui.Button("更新信息",1000,800,update_info,50,300,"white","#6DDF6D",25)
    gui.show()

# 修改个人信息
def update_info():
    global info,gui,mysql,line2,line8,line9
    args = info[0]
    arg1 = line2.text()
    arg2 = line8.text()
    arg3 = line9.text()
    if arg1 == "":
        arg1 = args[1]
    if arg2 == "":
        arg2 = args[3]
    if arg3 == "":
        arg3 = args[4].strftime('%Y-%m-%d')
    [res,flag] = mysql.update_worker(args[0],arg1,args[2],arg2,arg3,args[4])
    if flag == True:
        Info(gui,"信息修改成功")
    else:
        Error(gui,res)

# 显示管理的宿舍
def show_department():
    global name,mysql,gui
    gui = Gui()
    show_frame(gui)
    btn2 = gui.Button('宿舍管理',0,260,show_department,60,400,"gray","#DFDFDF",26);
    btn2.setEnabled(False)
    [res,flag] = mysql.show_department(name)
    if flag==False:
        Error(gui,res)
    else:
        if res==[]:
            lbl = gui.Label("你尚未管理任何宿舍.",500,300,40,400,size=30)
        else:
            if 60+len(res)*40 > 600:
                height = 600
            else:
                height = 60+len(res)*40
            title = ["楼栋编号","所属区域","可容纳人数"]
            table = gui.Table(500,300,height,1380,len(res),3,title)
            for i in range(len(res)):
                for j in range(3):
                    table.setItem(i,j,QTableWidgetItem(str(res[i][j])))
    gui.show()

# 搜索宿舍
def search_department():
    global name,mysql,gui,c1,c2,c3,table1
    gui = Gui()
    show_frame(gui)
    btn3 = gui.Button('搜索宿舍',0,320,search_department,60,400,"gray","#DFDFDF",26);
    btn3.setEnabled(False)
    lbl = gui.Label("筛选条件",460,250,50,120,size=25)
    l1 = gui.Label("楼栋编号:",650,250,50,100)
    c1 = gui.Input(750,250,h=50,w=130,txt="例如：1")
    l2 = gui.Label("所处区域:",900,250,50,120)
    c2 = gui.Input(1020,250,h=50,w=130,txt="例如：东区")
    l3 = gui.Label("管理员:",1170,250,50,100)
    c3 = gui.Input(1270,250,h=50,w=130,txt="例如：孙赫")
    btn1 = gui.Button("搜索",1500,250,search,50,100,"white","#6DDF6D",25)
    [res,flag] = mysql.search_department()
    if flag==False:
        Error(gui,res)
    else:
        if 60+len(res)*40 > 600:
            height = 600
        else:
            height = 60+len(res)*45
        title = ["楼栋编号","所属区域","管理员","可容纳人数"]
        table1 = gui.Table(500,350,height,1380,len(res),4,title)
        for i in range(len(res)):
            for j in range(4):
                table1.setItem(i,j,QTableWidgetItem(str(res[i][j])))
            manager_name = mysql.get_name(res[i][2])
            table1.setItem(i,2,QTableWidgetItem(manager_name[0][0][0]))
        count = table1.rowCount()
        for i in range(len(res),count):
            for j in range(4):
                table1.setItem(i,j,QTableWidgetItem(""))
    gui.show()

# 搜索宿舍按钮
def search():
    global c1,c2,c3,table1
    condition = []
    if c1.text() != "":
        condition.append("id={!r}".format(c1.text()))
    if c2.text() != "":
        condition.append("area={!r}".format(c2.text()))
    if c3.text() != "":
        manager_name = c3.text()
        manager_id = mysql.get_id(manager_name,"W")
        condition.append("manager={!r}".format(manager_id[0][0][0]))
    if condition!=[]:
        config = ""
        for x in range(len(condition)-1):
            config = config+condition[x]+" and "
        config = config+condition[len(condition)-1]
    else:
        config = None
    [res,flag] = mysql.search_department(condition=config)
    if flag==False:
        Error(gui,res)
    else:
        for i in range(len(res)):
            for j in range(4):
                table1.setItem(i,j,QTableWidgetItem(str(res[i][j])))
            manager_name = mysql.get_name(res[i][2])
            table1.setItem(i,2,QTableWidgetItem(manager_name[0][0][0]))
        count = table1.rowCount()
        for i in range(len(res),count):
            for j in range(4):
                table1.setItem(i,j,QTableWidgetItem(""))

if __name__=='__main__':
    global mysql,gui,ID,name
    mysql = None
    app = QApplication(sys.argv)
    mysql = mydb("localhost","root","123456")
    #mysql.init_data()
    gui = Gui()
    ID = "W0001"
    name = ID
    worker(gui,mysql,ID)
    sys.exit(app.exec_())
