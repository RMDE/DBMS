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

'''
待实现：
	1. 课程学生名单
	2. 课程成绩录入
	3. 创建新课程
	4. 安排课程考试
'''

# 显示用户界面    
def teacher(log,sql,ID):
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
    gui.setWindowTitle('教师界面') # 窗口标题
    gui.setWindowOpacity(0.98)
    head1 = gui.Label("",0,0,150,1920)
    head1.setStyleSheet("QLabel{background:#4DBF4D}")
    head2 = gui.Label("",0,150,50,1920)
    head2.setStyleSheet("QLabel{background:#3DAF3D}")
    head3 = gui.Label("",0,150,3,1920)
    head3.setStyleSheet("QLabel{background:#6DDF6D}")
    title1 = gui.Label("教务信息管理系统",30,30,70,500,"white",50)
    title2 = gui.Label("Educational Information Administration System",30,95,50,500,"white",20)
    character1 = gui.Label("教师",1400,55,60,100,"white",30)
    character2 = gui.Label(name,1750,60,50,150,"white",25)
    character3 = gui.Label("",1700,60,50,50,"white",30)
    character3.setScaledContents(True)
    character3.setPixmap(Load("student.jpg",character3.width(),character3.height()))
    character3.setStyleSheet("QLabel{border-radius:25px;}")
    btn1 = gui.Button('个人信息',0,200,show_info,60,400,"gray","white",26);
    btn2 = gui.Button('教授课程',0,260,show_course,60,400,"gray","white",26);
    btn3 = gui.Button('搜索课程',0,320,search_course,60,400,"gray","white",26);
    btn4 = gui.Button('借阅书籍',0,380,borrow_book,60,400,"gray","white",26);
    btn5 = gui.Button('已借书籍',0,440,show_book,60,400,"gray","white",26);
    tail = gui.Label("",0,500,580,400)
    tail.setStyleSheet("QLabel{background:white;}")

# 显示个人信息
def show_info():
    global name,mysql,gui,btn1,line2,line8,line9,line10,info
    gui = Gui()
    show_frame(gui)
    [info,flag] = mysql.show_info(name)
    btn1 = gui.Button('个人信息',0,200,show_info,60,400,"gray","#DFDFDF",26);
    btn1.setEnabled(False)
    lbl1 = gui.Label("工号: ",700,250,50,120,size=25)
    lbl2 = gui.Label("姓名: ",1200,250,50,120,size=25)
    lbl3 = gui.Label("性别: ",700,350,50,120,size=25)
    lbl6 = gui.Label("学院: ",1200,350,50,120,size=25)
    lbl7 = gui.Label("薪资: ",700,450,50,120,size=25)
    lbl10 = gui.Label("邮箱: ",1200,450,50,120,size=25)
    lbl8 = gui.Label("电话: ",700,550,50,120,size=25)
    lbl9 = gui.Label("生日: ",1200,550,50,120,size=25)

    if flag == False:
        Error(gui,info)
    else:
        line1 = gui.Label(info[0][0],820,250,50,200)
        line2 = gui.Input(1350,250,info[0][1],50,200)
        line3 = gui.Label(info[0][2],820,350,50,200)
        line6 = gui.Label(college[int(info[0][5])-1],1320,350,50,230)
        line7 = gui.Label(str(info[0][7]),820,450,50,200)
        line10 = gui.Input(1350,450,info[0][3],50,200)
        line8 = gui.Input(850,550,info[0][4],50,200)
        line9 = gui.Input(1350,550,info[0][6].strftime('%Y-%m-%d'),50,200)
    
        commit = gui.Button("更新信息",1000,800,update_info,50,300,"white","#6DDF6D",25)
    gui.show()


# 显示个人课程
def show_course():
    global name,mysql,gui
    gui = Gui()
    show_frame(gui)
    btn2 = gui.Button('教授课程',0,260,show_course,60,400,"gray","#DFDFDF",26);
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
    
    [res,flag] = mysql.show_course(condition="teacher ={!r}".format(name))
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
    gui.show()

# 搜索课程
def search_course():
    global name,mysql,gui,c1,c2,c3,c4,table
    gui = Gui()
    show_frame(gui)
    btn3 = gui.Button('搜索课程',0,320,search_course,60,400,"gray","#DFDFDF",26);
    btn3.setEnabled(False)
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
    btn1 = gui.Button("搜索",1750,250,search1,50,100,"white","#6DDF6D",25)
    [res,flag] = mysql.show_course()
    if flag==False:
        Error(gui,res)
    else:
        if 60+len(res)*40 > 600:
            height = 600
        else:
            height = 60+len(res)*45
        title = ["课程编号","课程名称","授课老师","所属类别","学分","上课时间","考试类型","操作"]
        table = gui.Table(500,350,height,1380,len(res),7,title)
        table.clicked.connect(find)
        for i in range(len(res)):
            for j in range(7):
                table.setItem(i,j,QTableWidgetItem(str(res[i][j])))
            [teacher,flag] = mysql.get_name(res[i][2])
            table.setItem(i,2,QTableWidgetItem(teacher[0][0]))
        count = table.rowCount()
        for i in range(len(res),count):
            for j in range(7):
                table.setItem(i,j,QTableWidgetItem(""))
    gui.show()

# 搜索课程按钮
def search1():
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
        config = config+condition[len(condition)-1]
    else:
        config = None
    [res,flag] = mysql.show_course(condition=config)
    if flag==False:
        Error(gui,res)
    else:
        for i in range(len(res)):
            for j in range(7):
                table.setItem(i,j,QTableWidgetItem(str(res[i][j])))
            [teacher,flag] = mysql.get_name(res[i][2])
            table.setItem(i,2,QTableWidgetItem(teacher[0][0]))
        count = table.rowCount()
        for i in range(len(res),count):
            for j in range(7):
                table.setItem(i,j,QTableWidgetItem(""))

# 定位点击单元格
def find(index):
    global column,row
    column = index.column()
    row = index.row()

# 借阅书籍
def borrow_book():
    global name,mysql,gui,c1,c2,c3,table
    gui = Gui()
    show_frame(gui)
    btn4 = gui.Button('借阅书籍',0,380,borrow_book,60,400,"gray","#DFDFDF",26);
    btn4.setEnabled(False)
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
    btn1 = gui.Button("搜索",1500,250,search3,50,100,"white","#6DDF6D",25)
    [res,flag] = mysql.show_book(condition="id not in (select book from borrow where person={!r})".format(name))
    if flag==False:
        Error(gui,res)
    else:
        if 60+len(res)*40 > 500:
            height = 500
        else:
            height = 60+len(res)*45
        title = ["书籍编号","书名","作者","类型","年份","可借阅/总储备","操作"]
        table = gui.Table(500,350,height,1380,len(res),7,title)
        table.clicked.connect(find)
        for i in range(len(res)):
            for j in range(5):
                table.setItem(i,j,QTableWidgetItem(str(res[i][j])))
            table.setItem(i,5,QTableWidgetItem(str(res[i][6])+"/"+str(res[i][5])))
            button = gui.Button("借阅",100,100,choose2,10,10)
            table.setCellWidget(i,6,button)
        count = table.rowCount()
        for i in range(len(res),count):
            for j in range(7):
                table.setItem(i,j,QTableWidgetItem(""))

    gui.show()

# 搜索图书按钮
def search3():
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
        config = config+condition[len(condition)-1]+" and "+"id not in (select book from borrow where person={!r})".format(name)
    else:
        config = "id not in (select book from borrow where person={!r})".format(name)
    [res,flag] = mysql.show_book(condition=config)
    if flag==False:
        Error(gui,res)
    else:
        for i in range(len(res)):
            for j in range(5):
                table.setItem(i,j,QTableWidgetItem(str(res[i][j])))
            table.setItem(i,5,QTableWidgetItem(str(res[i][6])+"/"+str(res[i][5])))
            button = gui.Button("借阅",100,100,choose2,10,10)
            table.setCellWidget(i,6,button)
        count = table.rowCount()
        for i in range(len(res),count):
            for j in range(6):
                table.setItem(i,j,QTableWidgetItem(""))
            table.setCellWidget(i,6,None)

# 借书按钮
def choose2():
    global gui,mysql,table
    [res,flag] = mysql.get_fee(name)
    if flag == False:
    	Error(gui,res)
    elif res[0][0]!=None: # 无欠费书籍
    	Info(gui,"当前有逾期未归还书籍，请先缴费！")
    	return
    button = gui.sender()
    x = button.frameGeometry().x()
    y = button.frameGeometry().y()
    item = QTableWidget.indexAt(table,QPoint(x,y))
    row = item.row()
    book_id = table.item(row,0).text()
    [res,flag] = mysql.update_borrow(name,book_id)
    if flag == True:
        Info(gui,"恭喜借阅成功！")
        search3()
    else:
        Error(gui,res)

# 显示已借阅书籍
def show_book():
    global name,mysql,gui,table
    gui = Gui()
    show_frame(gui)
    btn5 = gui.Button('已借书籍',0,440,show_book,60,400,"gray","white",26);
    btn5.setEnabled(False)
    lbl = gui.Label(">>>已借书籍",500,250,50,150,"black",25)
    lbl1 = gui.Label("",500,300,2,1420)
    lbl1.setStyleSheet("QLabel{background:gray;}")
    [res,flag] = mysql.show_fee(name)
    if flag==False:
        Error(gui,res)
    elif res == []:
    	pass
    else:
        if 60+len(res)*40 > 400:
            height = 400
        else:
            height = 60+len(res)*45
        title = ["书籍编号","书名","借阅日期","应还日期","操作"]
        table = gui.Table(500,350,height,1380,len(res),5,title)
        table.clicked.connect(find)
        for i in range(len(res)):
            table.setItem(i,0,QTableWidgetItem(str(res[i][0])))
            table.setItem(i,1,QTableWidgetItem(str(res[i][1])))
            table.setItem(i,2,QTableWidgetItem(str(res[i][2])))
            table.setItem(i,3,QTableWidgetItem(str(res[i][3])))
            button = gui.Button("归还",100,100,choose3,10,10)
            table.setCellWidget(i,4,button)
        count = table.rowCount()
        for i in range(len(res),count):
            for j in range(4):
                table.setItem(i,j,QTableWidgetItem(""))
            table.setCellWidget(i,4,None)

    lbl2 = gui.Label(">>>逾期缴费",500,750,50,150,"black",25)
    lbl3 = gui.Label("",500,800,2,700)
    lbl3.setStyleSheet("QLabel{background:gray;}")
    lbl4 = gui.Label("应缴纳费用： ",500,860,50,200,"black",25)
    btn = gui.Button("缴费",900,860,charge_fee,50,100,"white","#6DDF6D",25)
    [res,flag] = mysql.get_fee(name)
    if flag == False:
    	Error(gui,res)
    	fee = "NAN"
    elif res[0][0] == None:
    	fee = "0.00"
    	btn.setEnabled(False)
    else:
    	fee = str(float(res[0][0])*0.5)
    lbl5 = gui.Label(fee+"  元",700,860,50,130,"black",25)
    

    gui.show()

# 逾期缴费
def charge_fee():
	[res,flag] = mysql.delete_borrow(name)
	if flag == True:
		Info(gui,"缴费成功!")
		show_book()
	else:
		Error(gui,res)

# 还书按钮
def choose3():
    global gui,mysql,table
    button = gui.sender()
    x = button.frameGeometry().x()
    y = button.frameGeometry().y()
    item = QTableWidget.indexAt(table,QPoint(x,y))
    row = item.row()
    book_id = table.item(row,0).text()
    [res,flag] = mysql.return_book(name,book_id)
    if flag == True:
        Info(gui,"恭喜归还成功！")
        show_book()
    else:
        Error(gui,res)

# 修改个人信息
def update_info():
    global info,gui,mysql,line2,line8,line9,line10
    args = info[0]
    arg1 = line2.text()
    arg2 = line8.text()
    arg3 = line9.text()
    arg4 = line10.text()
    if arg1 == "":
        arg1 = args[1]
    if arg2 == "":
        arg2 = args[4]
    if arg3 == "":
        arg3 = args[6].strftime('%Y-%m-%d')
    if arg4 == "":
    	arg4 = args[3]
    [res,flag] = mysql.update_teacher(args[0],arg1,args[2],arg4,arg2,args[5],arg3,args[7])
    if flag == True:
        Info(gui,"信息修改成功")
    else:
        Error(gui,res)

if __name__=='__main__':
    global mysql,gui,ID,name
    mysql = None
    app = QApplication(sys.argv)
    mysql = mydb("localhost","root","123456")
    #mysql.init_data()
    gui = Gui()
    ID = "T160002"
    name = ID
    teacher(gui,mysql,ID)
    sys.exit(app.exec_())
