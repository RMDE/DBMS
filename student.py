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


# 显示学生用户界面    
def student(log,sql,ID):
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
    Emot = gui.Label("",1500,700,300,300)
    Emot.setPixmap(Load("Emot1.jpg",Emot.width(),Emot.height()))
    gui.show()


# 显示框架
def show_frame(gui):
    global btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8
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
    character1 = gui.Label("学生",1400,55,60,100,"white",30)
    character2 = gui.Label(name,1750,60,50,150,"white",25)
    character3 = gui.Label("",1700,60,50,50,"white",30)
    character3.setScaledContents(True)
    character3.setPixmap(Load("student.jpg",character3.width(),character3.height()))
    character3.setStyleSheet("QLabel{border-radius:25px;}")
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

# 显示个人信息
def show_info():
    global name,mysql,gui,btn1,line2,line8,line9,info
    gui = Gui()
    show_frame(gui)
    [info,flag] = mysql.show_info(name)
    btn1 = gui.Button('个人信息',0,200,show_info,60,400,"gray","#DFDFDF",26);
    btn1.setEnabled(False)
    lbl1 = gui.Label("学号: ",700,250,50,120,size=25)
    lbl2 = gui.Label("姓名: ",1200,250,50,120,size=25)
    lbl3 = gui.Label("性别: ",700,350,50,120,size=25)
    lbl4 = gui.Label("班级: ",1200,350,50,120,size=25)
    lbl5 = gui.Label("专业: ",700,450,50,120,size=25)
    lbl6 = gui.Label("学院: ",1200,450,50,120,size=25)
    lbl7 = gui.Label("宿舍: ",700,550,50,120,size=25)
    lbl8 = gui.Label("电话: ",1200,550,50,120,size=25)
    lbl9 = gui.Label("生日: ",700,650,50,120,size=25)

    if flag == False:
        Error(gui,info)
    else:
        line1 = gui.Label(info[0][0],820,250,50,200)
        line2 = gui.Input(1350,250,info[0][1],50,200)
        line3 = gui.Label(info[0][2],820,350,50,200)
        line4 = gui.Label(info[0][3],1320,350,50,200)
        line5 = gui.Label(info[0][4],820,450,50,200)
        line6 = gui.Label(college[int(info[0][5])-1],1320,450,50,300)
        line7 = gui.Label(info[0][6],820,550,50,200)
        line8 = gui.Input(1350,550,info[0][7],50,200)
        line9 = gui.Input(850,650,info[0][8].strftime('%Y-%m-%d'),50,200)
    
        commit = gui.Button("更新信息",1000,800,update_info,50,300,"white","#6DDF6D",25)
    Emot = gui.Label("",1500,700,300,300)
    Emot.setPixmap(Load("Emot3.jpg",Emot.width(),Emot.height()))
    gui.show()


# 显示个人课程
def show_course():
    global name,mysql,gui
    gui = Gui()
    show_frame(gui)
    btn2 = gui.Button('个人课表',0,260,show_course,60,400,"gray","#DFDFDF",26);
    btn2.setEnabled(False)
    # 课程表
    l1 = gui.Label("节次/周次",500,250,40,120,back="#ADFFAD") 
    l2 = gui.Label("星期一",620,250,40,180,back="#ADFFAD")
    l3 = gui.Label("星期二",800,250,40,180,back="#ADFFAD")
    l4 = gui.Label("星期三",980,250,40,180,back="#ADFFAD")
    l5 = gui.Label("星期四",1160,250,40,180,back="#ADFFAD")
    l6 = gui.Label("星期五",1340,250,40,180,back="#ADFFAD")
    l7 = gui.Label("星期六",1520,250,40,180,back="#ADFFAD")
    l8 = gui.Label("星期日",1700,250,40,180,back="#ADFFAD")
    l9 = gui.Label("第一二节",500,290,100,120,back="#ADADFF")
    l10 = gui.Label("第三四节",500,390,100,120,back="#ADADFF")
    l11 = gui.Label("第五六节",500,490,100,120,back="#ADADFF")
    l12 = gui.Label("第七八节",500,590,100,120,back="#ADADFF")
    courses = []
    for i in range(4):
        for j in range(7):
            courses.append(gui.Label("",620+j*180,290+100*i,100,180,size=25,back="#DFDFDF"))
    
    [res,flag] = mysql.show_course(condition="id in (select course from choose where student ={!r})".format(name))
    if flag==False:
        Error(gui,res)
    else:
        for i in range(len(res)):
            for x in range(len(schedule)):
                if schedule[x] in res[i][5]:
                    courses[x].setText(res[i][1])
                    courses[x].setStyleSheet("QLabel{background:#FFADAD;color:white;font-size:25px;font-family:宋体;font-weight:bold;}")
        title = ["课程编号","课程名称","授课老师","学分","课程类别","考试形式"]
        if 60+len(res)*40 > 300:
            height = 300
        else:
            height = 60+len(res)*40
        table = gui.Table(500,700,height,1380,len(res),6,title)
        for i in range(len(res)):
            for j in range(5):
                table.setItem(i,j,QTableWidgetItem(str(res[i][j])))
            [teacher,flag] = mysql.get_name(res[i][2])
            table.setItem(i,2,QTableWidgetItem(teacher[0][0]))
            table.setItem(i,5,QTableWidgetItem(str(res[i][6])))
    l13 = gui.Label("",500,390,2,1380,back="#EFEFEF")
    l14 = gui.Label("",500,490,2,1380,back="#EFEFEF")
    l15 = gui.Label("",500,590,2,1380,back="#EFEFEF")
    l16 = gui.Label("",620,290,400,2,back="#EFEFEF")
    l17 = gui.Label("",800,290,400,2,back="#EFEFEF")
    l18 = gui.Label("",980,290,400,2,back="#EFEFEF")
    l19 = gui.Label("",1160,290,400,2,back="#EFEFEF")
    l20 = gui.Label("",1340,290,400,2,back="#EFEFEF")
    l21 = gui.Label("",1520,290,400,2,back="#EFEFEF")
    l22 = gui.Label("",1700,290,400,2,back="#EFEFEF")
    Emot = gui.Label("",100,750,200,200)
    Emot.setPixmap(Load("Emot4.jpg",Emot.width(),Emot.height()))
    gui.show()

# 显示考试信息
def show_exam():
    global name,mysql,gui
    gui = Gui()
    show_frame(gui)
    btn3 = gui.Button('考试安排',0,320,show_exam,60,400,"gray","#DFDFDF",26);
    btn3.setEnabled(False)
    [res,flag] = mysql.show_test(name)
    if flag==False:
        Error(gui,res)
    else:
        if res==[]:
            lbl = gui.Label("你最近未安排任何考试.",500,300,40,400,size=30)
        else:
            if 60+len(res)*40 > 600:
                height = 600
            else:
                height = 60+len(res)*40
            title = ["课程编号","课程名称","考试形式","考试时间","考试地点"]
            table = gui.Table(500,300,height,1380,len(res),5,title)
            for i in range(len(res)):
                for j in range(5):
                    table.setItem(i,j,QTableWidgetItem(str(res[i][j])))
    Emot = gui.Label("",1500,700,300,300)
    Emot.setPixmap(Load("Emot8.jpg",Emot.width(),Emot.height()))
    gui.show()


# 显示成绩
def show_grade():
    global name,mysql,gui
    gui = Gui()
    show_frame(gui)
    btn4 = gui.Button('成绩查询',0,380,show_grade,60,400,"gray","#DFDFDF",26);
    btn4.setEnabled(False)
    [res,avg,flag] = mysql.show_grade(name)
    if flag==False:
        Error(gui,res)
    else:
        if res==[]:
            lbl = gui.Label("你还没有任何成绩哦.",500,300,40,400,size=30)
            lbl = gui.Label("平均绩点: "+str(0.0),1600,250,80,250,size=30)
        else:
            lbl = gui.Label("平均绩点: "+str(int(avg[0][0])/20),1600,250,80,250,size=30)
            if 60+len(res)*40 > 500:
                height = 500
            else:
                height = 60+len(res)*40
            title = ["课程名称","学分","考试成绩"]
            table = gui.Table(500,350,height,1380,len(res),3,title)
            for i in range(len(res)):
                for j in range(3):
                    table.setItem(i,j,QTableWidgetItem(str(res[i][j])))
    Emot = gui.Label("",1500,700,300,300)
    Emot.setPixmap(Load("Emot9.jpg",Emot.width(),Emot.height()))
    gui.show()

# 选课
def search_course():
    global name,mysql,gui,c1,c2,c3,c4,table
    gui = Gui()
    show_frame(gui)
    btn5 = gui.Button('选修课程',0,440,search_course,60,400,"gray","#DFDFDF",26);
    btn5.setEnabled(False)
    lbl = gui.Label("筛选条件",460,250,50,120,size=25)
    l1 = gui.Label("课程编号:",650,250,50,100)
    c1 = gui.Input(750,250,h=50,w=130,txt="例如：C0001")
    l2 = gui.Label("课程名称:",900,250,50,100)
    c2 = gui.Input(1000,250,h=50,w=130,txt="例如：高数")
    l3 = gui.Label("授课老师:",1150,250,50,100)
    c3 = gui.Input(1250,250,h=50,w=130)
    l4 = gui.Label("所属学院:",1400,250,50,100)
    coll =["所有"]
    for x in college:
        coll.append(x)
    c4 = gui.Combo(17,1500,250,50,240,coll)
    btn1 = gui.Button("搜索",1750,250,search,50,100,"white","#6DDF6D",25)
    [res,flag] = mysql.show_course(condition="id not in (select course from choose where student={!r})".format(name))
    if flag==False:
        Error(gui,res)
    else:
        if 60+len(res)*40 > 600:
            height = 600
        else:
            height = 60+len(res)*45
        title = ["课程编号","课程名称","授课老师","所属类别","学分","上课时间","考试类型","操作"]
        table = gui.Table(500,350,height,1380,len(res),8,title)
        table.clicked.connect(find)
        for i in range(len(res)):
            for j in range(7):
                table.setItem(i,j,QTableWidgetItem(str(res[i][j])))
            [teacher,flag] = mysql.get_name(res[i][2])
            table.setItem(i,2,QTableWidgetItem(teacher[0][0]))
            button = gui.Button("选课",100,100,choose,10,10)
            table.setCellWidget(i,7,button)
        count = table.columnCount()
        for i in range(len(res),count):
            for j in range(7):
                table.setItem(i,j,QTableWidgetItem(""))

    Emot = gui.Label("",1500,800,200,400)
    Emot.setPixmap(Load("Emot7.jpg",Emot.width(),Emot.height()))
    gui.show()

# 搜索课程按钮
def search():
    global c1,c2,c3,c4,table
    condition = []
    if c1.text() != "":
        condition.append("id={!r}".format(c1.text()))
    if c2.text() != "":
        condition.append("name={!r}".format(c2.text()))
    if c3.text() != "":
        [res,flag] = mysql.get_id(c3.text(),"T")
        if flag == False:
            Error(gui,res)
            return
        ID = "teacher in ("
        for x in res:
            ID = ID+"{!r},".format(x[0])
        ID = ID[:len(ID)-1]+')'
        condition.append(ID)
    if c4.currentText() != "所有":
        for i in range(len(college)): # 将学院名转化为学院id
            if college[i]==c4.currentText():
                condition.append("teacher in (select id from teacher where college={!r})".format(str(i+1)))
    if condition!=[]:
        config = ""
        for x in range(len(condition)-1):
            config = config+condition[x]+" and "
        config = config+condition[len(condition)-1]+" and "+"id not in (select course from choose where student={!r})".format(name)
    else:
        config = "id not in (select course from choose where student={!r})".format(name)
    [res,flag] = mysql.show_course(condition=config)
    if flag==False:
        Error(gui,res)
    else:
        for i in range(len(res)):
            for j in range(7):
                table.setItem(i,j,QTableWidgetItem(str(res[i][j])))
            [teacher,flag] = mysql.get_name(res[i][2])
            table.setItem(i,2,QTableWidgetItem(teacher[0][0]))
            button = gui.Button("选课",100,100,choose,10,10)
            table.setCellWidget(i,7,button)
        count = table.columnCount()
        for i in range(len(res),count):
            for j in range(8):
                table.setItem(i,j,QTableWidgetItem(""))
            table.setCellWidget(i,7,None)

# 定位点击单元格
def find(index):
    global column,row
    column = index.column()
    row = index.row()
    print(column,row)

# 选课按钮
def choose():
    global gui,mysql,table
    button = gui.sender()
    x = button.frameGeometry().x()
    y = button.frameGeometry().y()
    item = QTableWidget.indexAt(table,QPoint(x,y))
    row = item.row()
    course_id = table.item(row,0).text()
    [res,flag] = mysql.update_choose(name,course_id)
    if flag == True:
        Info(gui,"恭喜选课成功！")
        search()
    else:
        Error(gui,res)

# 搜索老师
def search_teacher():
    global name,mysql,gui
    gui = Gui()
    show_frame(gui)
    btn6 = gui.Button('教师查询',0,500,search_teacher,60,400,"gray","#DFDFDF",26);
    btn6.setEnabled(False)
    pass
    gui.show()


# 借阅书籍
def borrow_book():
    global name,mysql,gui
    gui = Gui()
    show_frame(gui)
    btn7 = gui.Button('借阅书籍',0,560,borrow_book,60,400,"gray","#DFDFDF",26);
    btn7.setEnabled(False)
    pass
    gui.show()


# 缴纳电费
def charge():
    global name,mysql,gui
    gui = Gui()
    show_frame(gui)
    btn8 = gui.Button('缴纳电费',0,620,charge,60,400,"gray","#DFDFDF",26);
    btn8.setEnabled(False)
    pass
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
        arg2 = args[7]
    if arg3 == "":
        arg3 = args[8].strftime('%Y-%m-%d')
    [res,flag] = mysql.update_student(args[0],arg1,args[2],args[3],args[4],args[5],arg2,arg3)
    if flag == True:
        Info(gui,"信息修改成功")
    else:
        Error(gui,res)


if __name__=='__main__':
    global mysql,gui,ID,name
    mysql = None
    app = QApplication(sys.argv)
    mysql = mydb("localhost","root","123456")
    mysql.init_data()
    gui = Gui()
    ID = "S1620101"
    name = ID
    search_course()
    sys.exit(app.exec_())
