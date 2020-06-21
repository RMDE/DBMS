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
def manager(log,sql,ID):
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
    gui.setWindowTitle('管理人员界面') # 窗口标题
    gui.setWindowOpacity(0.98)
    head1 = gui.Label("",0,0,150,1920)
    head1.setStyleSheet("QLabel{background:#4DBF4D}")
    head2 = gui.Label("",0,150,50,1920)
    head2.setStyleSheet("QLabel{background:#3DAF3D}")
    head3 = gui.Label("",0,150,3,1920)
    head3.setStyleSheet("QLabel{background:#6DDF6D}")
    title1 = gui.Label("教务信息管理系统",30,30,70,500,"white",50)
    title2 = gui.Label("Educational Information Administration System",30,95,50,500,"white",20)
    character1 = gui.Label("管理人员",1400,55,60,150,"white",30)
    character2 = gui.Label(name,1750,60,50,150,"white",25)
    character3 = gui.Label("",1700,60,50,50,"white",30)
    character3.setScaledContents(True)
    character3.setPixmap(Load("student.jpg",character3.width(),character3.height()))
    character3.setStyleSheet("QLabel{border-radius:25px;}")
    btn1 = gui.Button('个人信息',0,200,show_info,60,400,"gray","white",26)
    btn2 = gui.Button('学生管理',0,260,manager_student,60,400,"gray","white",26)
    btn3 = gui.Button('教师管理',0,320,manager_teacher,60,400,"gray","white",26)
    btn4 = gui.Button('工作人员管理',0,380,manager_worker,60,400,"gray","white",26)
    btn5 = gui.Button('书籍管理',0,440,manager_book,60,400,"gray","white",26)
    tail = gui.Label("",0,500,580,400)
    tail.setStyleSheet("QLabel{background:white;}")

# 显示个人信息
def show_info():
    global name,mysql,gui,btn1,line2,line4,line8,line9,info
    gui = Gui()
    show_frame(gui)
    [info,flag] = mysql.show_info(name)
    btn1 = gui.Button('个人信息',0,200,show_info,60,400,"gray","#DFDFDF",26);
    btn1.setEnabled(False)
    lbl1 = gui.Label("工号: ",700,250,50,120,size=25)
    lbl2 = gui.Label("姓名: ",1200,250,50,120,size=25)
    lbl3 = gui.Label("性别: ",700,350,50,120,size=25)
    lbl4 = gui.Label("邮箱: ",1200,350,50,120,size=25)
    lbl8 = gui.Label("电话: ",700,450,50,120,size=25)
    lbl9 = gui.Label("生日: ",1200,450,50,120,size=25)

    if flag == False:
        Error(gui,info)
    else:
        line1 = gui.Label(info[0][0],820,250,50,200)
        line2 = gui.Input(1350,250,info[0][1],50,200)
        line3 = gui.Label(info[0][2],820,350,50,200)
        line4 = gui.Input(1350,350,info[0][3],50,200)
        line8 = gui.Input(820,450,info[0][4],50,200)
        line9 = gui.Input(1350,450,info[0][5].strftime('%Y-%m-%d'),50,200)
    
        commit = gui.Button("更新信息",1000,800,update_info,50,300,"white","#6DDF6D",25)
    gui.show()

# 修改个人信息
def update_info():
    global info,gui,mysql,line2,line4,line8,line9
    args = info[0]
    arg1 = line2.text()
    arg2 = line4.text()
    arg3 = line8.text()
    arg4 = line9.text()
    if arg1 == "":
        arg1 = args[1]
    if arg2 == "":
        arg2 = args[3]
    if arg3 == "":
        arg3 = args[4]
    if arg4 == "":
        arg4 = args[5].strftime('%Y-%m-%d')
    [res,flag] = mysql.update_manager(args[0],arg1,args[2],arg2,arg3,arg4)
    if flag == True:
        Info(gui,"信息修改成功")
    else:
        Error(gui,res)

# 管理学生
def manager_student():
    global name,mysql,gui,c1,c2,c3,c4,table1
    gui = Gui()
    show_frame(gui)
    btn2 = gui.Button('学生管理',0,260,manager_student,60,400,"gray","white",26)
    btn2.setEnabled(False)
    l1 = gui.Label("课程编号:",650,250,50,100)
    c1 = gui.Input(750,250,h=50,w=130,txt="例如：S1620101")
    l2 = gui.Label("课程名称:",900,250,50,100)
    c2 = gui.Input(1000,250,h=50,w=130,txt="例如：叶曦")
    l3 = gui.Label("所属班级:",1150,250,50,100)
    c3 = gui.Input(1250,250,h=50,w=130,txt="例如：16201")
    l4 = gui.Label("所属学院:",1400,250,50,100)
    coll =["所有"]
    for x in college:
        coll.append(x)
    c4 = gui.Combo(17,1500,250,50,240,coll)
    btn1 = gui.Button("搜索",1750,250,search1,50,100,"white","#6DDF6D",25)
    [res,flag] = mysql.search_student(segment="id,name,sex,class,profession,college,room,phone")
    if flag==False:
        Error(gui,res)
    else:
        if 60+len(res)*40 > 600:
            height = 600
        else:
            height = 60+len(res)*45
        title = ["编号","姓名","性别","班级","专业","所属学院","宿舍","联系方式"]
        table1 = gui.Table(500,350,height,1380,len(res),8,title)
        for i in range(len(res)):
            for j in range(8):
                table1.setItem(i,j,QTableWidgetItem(str(res[i][j])))
            table1.setItem(i,5,QTableWidgetItem(str(college[int(res[i][5])-1])))
        count = table1.rowCount()
        for i in range(len(res),count):
            for j in range(8):
                table1.setItem(i,j,QTableWidgetItem(""))
    gui.show()

# 搜索学生按钮
def search1():
    global c1,c2,c3,c4,table1
    condition = []
    if c1.text() != "":
        condition.append("id={!r}".format(c1.text()))
    if c2.text() != "":
        condition.append("name={!r}".format(c2.text()))
    if c3.text() != "":
        condition.append("class={!r}".format(c3.text()))
    if c4.currentText() != "所有":
        for i in range(len(college)): # 将学院名转化为学院id
            if college[i]==c4.currentText():
                condition.append("college={!r}".format(str(i+1)))
    if condition!=[]:
        config = ""
        for x in range(len(condition)-1):
            config = config+condition[x]+" and "
        config = config+condition[len(condition)-1]
    else:
        config = None
    [res,flag] = mysql.search_student(segment="id,name,sex,class,profession,college,room,phone",condition=config)
    if flag==False:
        Error(gui,res)
    else:
        for i in range(len(res)):
            for j in range(8):
                table1.setItem(i,j,QTableWidgetItem(str(res[i][j])))
            table1.setItem(i,5,QTableWidgetItem(str(college[int(res[i][5])-1])))
        count = table1.rowCount()
        for i in range(len(res),count):
            for j in range(8):
                table1.setItem(i,j,QTableWidgetItem(""))

# 管理教师
def manager_teacher():
    global name,mysql,gui,c1,c2,c3,table1
    gui = Gui()
    show_frame(gui)
    btn3 = gui.Button('教师管理',0,320,manager_teacher,60,400,"gray","white",26)
    btn3.setEnabled(False)
    lbl = gui.Label("筛选条件",460,250,50,120,size=25)
    l1 = gui.Label("教师编号:",650,250,50,100)
    c1 = gui.Input(750,250,h=50,w=130,txt="例如：T160001")
    l2 = gui.Label("教师姓名:",900,250,50,100)
    c2 = gui.Input(1000,250,h=50,w=130,txt="例如：陈秉")
    l3 = gui.Label("所属学院:",1150,250,50,100)
    coll =["所有"]
    for x in college:
        coll.append(x)
    c3 = gui.Combo(17,1200,250,50,240,coll)
    btn1 = gui.Button("搜索",1550,250,search2,50,100,"white","#6DDF6D",25)
    [res,courses,flag] = mysql.search_teacher(segment="id,name,sex,email,phone,college")
    if flag==False:
        Error(gui,res)
    else:
        if 60+len(res)*40 > 600:
            height = 600
        else:
            height = 60+len(res)*45
        title = ["教师编号","姓名","性别","邮箱","联系方式","所属学院","教授课程"]
        table1 = gui.Table(500,350,height,1380,len(res),7,title)
        for i in range(len(res)):
            for j in range(5):
                table1.setItem(i,j,QTableWidgetItem(str(res[i][j])))
            table1.setItem(i,5,QTableWidgetItem(str(college[int(res[i][5])-1])))
            table1.setItem(i,6,QTableWidgetItem(str(courses[i])))
        count = table1.rowCount()
        for i in range(len(res),count):
            for j in range(7):
                table1.setItem(i,j,QTableWidgetItem(""))
    gui.show()

# 搜索教师按钮
def search2():
    global c1,c2,c3,table1
    condition = []
    if c1.text() != "":
        condition.append("id={!r}".format(c1.text()))
    if c2.text() != "":
        condition.append("name={!r}".format(c2.text()))
    if c3.currentText() != "所有":
        for i in range(len(college)): # 将学院名转化为学院id
            if college[i]==c3.currentText():
                condition.append("college={!r}".format(str(i+1)))
    if condition!=[]:
        config = ""
        for x in range(len(condition)-1):
            config = config+condition[x]+" and "
        config = config+condition[len(condition)-1]
    else:
        config = None
    [res,courses,flag] = mysql.search_teacher(segment="id,name,sex,email,phone,college",condition=config)
    if flag==False:
        Error(gui,res)
    else:
        for i in range(len(res)):
            for j in range(5):
                table1.setItem(i,j,QTableWidgetItem(str(res[i][j])))
            table1.setItem(i,5,QTableWidgetItem(str(college[int(res[i][5])-1])))
            table1.setItem(i,6,QTableWidgetItem(str(courses[i])))
        count = table1.rowCount()
        for i in range(len(res),count):
            for j in range(7):
                table1.setItem(i,j,QTableWidgetItem(""))

# 管理工作人员
def manager_worker():
    global name,mysql,gui,c1,c2,c3,table1
    gui = Gui()
    show_frame(gui)
    btn4 = gui.Button('工作人员管理',0,380,manager_worker,60,400,"gray","white",26)
    btn4.setEnabled(False)
    lbl = gui.Label("筛选条件",460,250,50,120,size=25)
    l1 = gui.Label("编号:",650,250,50,100)
    c1 = gui.Input(750,250,h=50,w=130,txt="例如：W0001")
    l2 = gui.Label("姓名:",900,250,50,100)
    c2 = gui.Input(1000,250,h=50,w=130,txt="例如：孙赫")
    btn1 = gui.Button("搜索",1200,250,search3,50,100,"white","#6DDF6D",25)
    [res,flag] = mysql.search_worker()
    if flag==False:
        Error(gui,res)
    else:
        if 60+len(res)*40 > 600:
            height = 600
        else:
            height = 60+len(res)*45
        title = ["编号","姓名","性别","联系方式","生日"]
        table1 = gui.Table(500,350,height,1380,len(res),5,title)
        for i in range(len(res)):
            for j in range(5):
                table1.setItem(i,j,QTableWidgetItem(str(res[i][j])))
        count = table1.rowCount()
        for i in range(len(res),count):
            for j in range(5):
                table1.setItem(i,j,QTableWidgetItem(""))
    gui.show()

# 搜索工作人员按钮
def search3():
    global c1,c2,c3,table1
    condition = []
    if c1.text() != "":
        condition.append("id={!r}".format(c1.text()))
    if c2.text() != "":
        condition.append("name={!r}".format(c2.text()))
    if condition!=[]:
        config = ""
        for x in range(len(condition)-1):
            config = config+condition[x]+" and "
        config = config+condition[len(condition)-1]
    else:
        config = None
    [res,flag] = mysql.search_worker(condition=config)
    if flag==False:
        Error(gui,res)
    else:
        for i in range(len(res)):
            for j in range(5):
                table1.setItem(i,j,QTableWidgetItem(str(res[i][j])))
        count = table1.rowCount()
        for i in range(len(res),count):
            for j in range(5):
                table1.setItem(i,j,QTableWidgetItem(""))

# 管理书籍
def manager_book():
    global name,mysql,gui,c1,c2,c3,table
    gui = Gui()
    show_frame(gui)
    btn5 = gui.Button('书籍管理',0,440,manager_book,60,400,"gray","white",26)
    btn5.setEnabled(False)
    lbl = gui.Label("筛选条件",460,250,50,120,size=25)
    l1 = gui.Label("书籍编号:",650,250,50,100)
    c1 = gui.Input(750,250,h=50,w=130,txt="例如：B000001")
    l2 = gui.Label("书名:",900,250,50,100)
    c2 = gui.Input(1000,250,h=50,w=130,txt="例如：高等数学")
    l3 = gui.Label("所属学院:",1150,250,50,100)
    coll =["所有"]
    for x in college:
        coll.append(x)
    c3 = gui.Combo(17,1250,250,50,240,coll)
    btn1 = gui.Button("搜索",1500,250,search4,50,100,"white","#6DDF6D",25)
    [res,flag] = mysql.show_book(condition="id not in (select book from borrow where person={!r})".format(name))
    if flag==False:
        Error(gui,res)
    else:
        if 60+len(res)*40 > 500:
            height = 500
        else:
            height = 60+len(res)*45
        title = ["书籍编号","书名","作者","类型","年份","可借阅/总储备"]
        table = gui.Table(500,350,height,1380,len(res),6,title)
        for i in range(len(res)):
            for j in range(5):
                table.setItem(i,j,QTableWidgetItem(str(res[i][j])))
            table.setItem(i,5,QTableWidgetItem(str(res[i][6])+"/"+str(res[i][5])))
        count = table.rowCount()
        for i in range(len(res),count):
            for j in range(6):
                table.setItem(i,j,QTableWidgetItem(""))

    gui.show()

# 搜索图书按钮
def search4():
    global c1,c2,c3,table
    condition = []
    if c1.text() != "":
        condition.append("id={!r}".format(c1.text()))
    if c2.text() != "":
        condition.append("name={!r}".format(c2.text()))
    if c3.currentText() != "所有":
        for i in range(len(college)): # 将学院名转化为学院id
            if college[i]==c3.currentText():
                condition.append("type={!r}".format(str(i+1)))
    if condition!=[]:
        config = ""
        for x in range(len(condition)-1):
            config = config+condition[x]+" and "
        config = config+condition[len(condition)-1]
    else:
        config = None
    [res,flag] = mysql.show_book(condition=config)
    if flag==False:
        Error(gui,res)
    else:
        for i in range(len(res)):
            for j in range(5):
                table.setItem(i,j,QTableWidgetItem(str(res[i][j])))
            table.setItem(i,5,QTableWidgetItem(str(res[i][6])+"/"+str(res[i][5])))
        count = table.rowCount()
        for i in range(len(res),count):
            for j in range(6):
                table.setItem(i,j,QTableWidgetItem(""))


if __name__=='__main__':
    global mysql,gui,ID,name
    mysql = None
    app = QApplication(sys.argv)
    mysql = mydb("localhost","root","123456")
    #mysql.init_data()
    gui = Gui()
    ID = "M0001"
    name = ID
    manager(gui,mysql,ID)
    sys.exit(app.exec_())
