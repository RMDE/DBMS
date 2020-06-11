from gui import *
from db_manager import *
from event import *
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,
        QTextEdit,QLabel,QPushButton, QApplication,QMainWindow, QAction, qApp,
        QHBoxLayout, QVBoxLayout,QGridLayout,QLineEdit,QRadioButton,QButtonGroup)
from PyQt5.QtGui import QFont,QIcon,QPixmap,QPalette,QColor
from PyQt5.QtCore import QCoreApplication,Qt
import os
from login import *
from time import sleep

# 管理人员注册界面
def register_manager(reg):
    global gui,line1,line2,sex,line3,line4,line5,line6,line7,line8
    gui = reg
    gui.resize(700,900) # 窗口大小
    gui.center() # 窗口位置
    gui.setWindowTitle('注册') # 窗口标题
    gui.setWindowOpacity(0.97)
    lbl = gui.Label("管理人员注册",200,10,100,300,"#6DDF6D",50)
    lbl.setAutoFillBackground(False)
    lbl1 = gui.Label("     工号: ",70,120,50,120,size=25)
    lbl2 = gui.Label("     姓名: ",70,200,50,120,size=25)
    lbl3 = gui.Label("     性别: ",70,280,50,120,size=25)
    lbl4 = gui.Label("     邮箱: ",70,360,50,120,size=25)
    lbl5 = gui.Label("     电话: ",70,440,50,120,size=25)
    lbl6 = gui.Label("     生日: ",70,520,50,120,size=25)
    lbl7 = gui.Label("     密码: ",70,600,50,120,size=25)
    lbl8 = gui.Label(" 确认密码: ",70,680,50,120,size=25)

    line1 = gui.Input(200,120,"必填/格式:M0001",50,350)
    line2 = gui.Input(200,200,"必填",50,350)
    
    sex1 = QRadioButton("女",gui)
    sex1.move(230,295)
    sex2 = QRadioButton("男",gui)
    sex2.move(330,295)
    sex = QButtonGroup(gui)
    sex.addButton(sex1,1)
    sex.addButton(sex2,2)
    sex.buttonClicked.connect(get_sex)

    line3 = ""
    line4 = gui.Input(200,360,"选填",50,350)
    line5 = gui.Input(200,440,"选填",50,350)
    line6 = gui.Input(200,520,"选填",50,350)
    line7 = gui.Input(200,600,"必填",50,350)
    line8 = gui.Input(200,680,"必填",50,350)
    line7.setEchoMode(QLineEdit.Password)
    line8.setEchoMode(QLineEdit.Password)

    btn = gui.Button('注册',100,810,show_regM_status,50,500,"white","#6DDF6D",30)
    btn = gui.Button('< 返回',10,10,return_login,30,60,"black",None,20)
    gui.show()

# 工作人员注册界面
def register_worker(reg):
    global gui,line1,line2,sex,line3,line4,line5,line6,line7
    gui = reg
    gui.resize(700,800) # 窗口大小
    gui.center() # 窗口位置
    gui.setWindowTitle('注册') # 窗口标题
    gui.setWindowOpacity(0.97)
    lbl = gui.Label("工作人员注册",200,10,100,300,"#6DDF6D",50)
    lbl.setAutoFillBackground(False)
    lbl1 = gui.Label("     工号: ",70,120,50,120,size=25)
    lbl2 = gui.Label("     姓名: ",70,200,50,120,size=25)
    lbl3 = gui.Label("     性别: ",70,280,50,120,size=25)
    lbl4 = gui.Label("     电话: ",70,360,50,120,size=25)
    lbl5 = gui.Label("     生日: ",70,440,50,120,size=25)
    lbl6 = gui.Label("     密码: ",70,520,50,120,size=25)
    lbl7 = gui.Label(" 确认密码: ",70,600,50,120,size=25)

    line1 = gui.Input(200,120,"必填/格式:W0001",50,350)
    line2 = gui.Input(200,200,"必填",50,350)
    
    sex1 = QRadioButton("女",gui)
    sex1.move(230,295)
    sex2 = QRadioButton("男",gui)
    sex2.move(330,295)
    sex = QButtonGroup(gui)
    sex.addButton(sex1,1)
    sex.addButton(sex2,2)
    sex.buttonClicked.connect(get_sex)

    line3 = ""
    line4 = gui.Input(200,360,"选填",50,350)
    line5 = gui.Input(200,440,"选填",50,350)
    line6 = gui.Input(200,520,"必填",50,350)
    line7 = gui.Input(200,600,"必填",50,350)
    line6.setEchoMode(QLineEdit.Password)
    line7.setEchoMode(QLineEdit.Password)

    btn = gui.Button('注册',100,710,show_regW_status,50,500,"white","#6DDF6D",30)
    btn = gui.Button('< 返回',10,10,return_login,30,60,"black",None,20)
    gui.show()

# 教师注册界面    
def register_teacher(reg):
    global gui,line1,line2,sex,line3,line4,line5,line6,line7,line8,line9
    gui = reg
    gui.resize(700,1000) # 窗口大小
    gui.center() # 窗口位置
    gui.setWindowTitle('注册') # 窗口标题
    gui.setWindowOpacity(0.97)
    lbl = gui.Label("教师注册",200,10,100,300,"#6DDF6D",50)
    lbl.setAutoFillBackground(False)
    lbl1 = gui.Label("     工号: ",70,120,50,120,size=25)
    lbl2 = gui.Label("     姓名: ",70,200,50,120,size=25)
    lbl3 = gui.Label("     性别: ",70,280,50,120,size=25)
    lbl4 = gui.Label("     邮箱: ",70,360,50,120,size=25)
    lbl5 = gui.Label("     电话: ",70,440,50,120,size=25)
    lbl6 = gui.Label("     学院: ",70,520,50,120,size=25)
    lbl7 = gui.Label("     生日: ",70,600,50,120,size=25)
    lbl8 = gui.Label("     密码: ",70,680,50,120,size=25)
    lbl9 = gui.Label(" 确认密码: ",70,760,50,130,size=25)

    line1 = gui.Input(200,120,"必填/格式:T160001",50,350)
    line2 = gui.Input(200,200,"必填",50,350)
    
    sex1 = QRadioButton("女",gui)
    sex1.move(230,295)
    sex2 = QRadioButton("男",gui)
    sex2.move(330,295)
    sex = QButtonGroup(gui)
    sex.addButton(sex1,1)
    sex.addButton(sex2,2)
    sex.buttonClicked.connect(get_sex)

    line3 = "" # 防止性别未选择
    line4 = gui.Input(200,360,"选填/格式:name@xxx.edu.cn",50,350)
    line5 = gui.Input(200,440,"选填",50,350)
    line6 = gui.Combo(16,200,520,50,350,college)
    line7 = gui.Input(200,600,"选填",50,350)
    line8 = gui.Input(200,680,"必填",50,350)
    line9 = gui.Input(200,760,"必填",50,350)
    line8.setEchoMode(QLineEdit.Password)
    line9.setEchoMode(QLineEdit.Password)

    btn = gui.Button('注册',100,910,show_regT_status,50,500,"white","#6DDF6D",30)
    btn = gui.Button('< 返回',10,10,return_login,30,60,"black",None,20)
    gui.show()

# 学生注册界面
def register_student(reg):
    global gui,line1,line2,sex,line3,line4,line5,line6,line7,line8,line9,line10
    gui = reg
    gui.resize(700,1000) # 窗口大小
    gui.center() # 窗口位置
    gui.setWindowTitle('注册') # 窗口标题
    gui.setWindowOpacity(0.97)
    lbl = gui.Label("学生注册",200,10,100,300,"#6DDF6D",50)
    lbl.setAutoFillBackground(False)
    lbl1 = gui.Label("     学号: ",70,120,50,120,size=25)
    lbl2 = gui.Label("     姓名: ",70,200,50,120,size=25)
    lbl3 = gui.Label("     性别: ",70,280,50,120,size=25)
    lbl4 = gui.Label("     班级: ",70,360,50,120,size=25)
    lbl5 = gui.Label("     专业: ",70,440,50,120,size=25)
    lbl6 = gui.Label("     学院: ",70,520,50,120,size=25)
    lbl7 = gui.Label("     电话: ",70,600,50,120,size=25)
    lbl8 = gui.Label("     生日: ",70,680,50,120,size=25)
    lbl9 = gui.Label("     密码: ",70,760,50,120,size=25)
    lbl10 = gui.Label(" 确认密码: ",70,840,50,130,size=25)

    line1 = gui.Input(200,120,"必填/格式:S1620101",50,350)
    line2 = gui.Input(200,200,"必填",50,350)
    
    sex1 = QRadioButton("女",gui)
    sex1.move(230,295)
    sex2 = QRadioButton("男",gui)
    sex2.move(330,295)
    sex = QButtonGroup(gui)
    sex.addButton(sex1,1)
    sex.addButton(sex2,2)
    sex.buttonClicked.connect(get_sex)

    line3 = "" # 防止性别未选择
    line4 = gui.Input(200,360,"必填/格式:16201",50,350)
    line5 = gui.Input(200,440,"必填",50,350)
    line6 = gui.Combo(16,200,520,50,350,college)
    line7 = gui.Input(200,600,"选填",50,350)
    line8 = gui.Input(200,680,"选填",50,350)
    line9 = gui.Input(200,760,"必填",50,350)
    line10 = gui.Input(200,840,"必填",50,350)
    line9.setEchoMode(QLineEdit.Password)
    line10.setEchoMode(QLineEdit.Password)

    btn = gui.Button('注册',100,910,show_regS_status,50,500,"white","#6DDF6D",30)
    btn = gui.Button('< 返回',10,10,return_login,30,60,"black",None,20)
    gui.show()

# 获取性别单选按钮值
def get_sex(btn):
    global sex,line3
    if sex.checkedId()==1:
        line3 = "female"
    elif sex.checkedId()==2:
        line3 = "male"
     
# 显示学生注册成功状态
def show_regS_status():
    global mysql,gui,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10
    for i in range(len(college)): # 将学院名转化为学院id
        if college[i]==line6.currentText():
            col = str(i+1)
    args = []
    args.append(line1.text())
    args.append(line2.text())
    args.append(line3)
    args.append(line4.text())
    args.append(line5.text())
    args.append(col)
    args.append(line7.text())
    args.append(line8.text())
    args.append(line9.text())
    args.append(line10.text())

    for i in range(len(args)):
        if args[i]=="" or args[i]==None:
            if i in [0,1,3,4,5,8,9]:
                Info(gui,"必填项不得为空")
                return
            else:
                args[i]=None
    if args[8]!=args[9]:
        Info(gui,"两次输入的密码不一致，请重新输入。")
        return
    room,flag = mysql.create_student(args[0],args[1],args[3],args[4],args[5],args[8],args[2],args[6],args[7])
    if flag==True:
        Info(gui,"注册成功,你的房间号为: {}".format(room))
        return_login()
    else:
        Error(gui,"数据库操作错误: {}".format(room))

# 显示教师注册成功状态
def show_regT_status():
    global mysql,gui,line1,line2,line3,line4,line5,line6,line7,line8,line9
    for i in range(len(college)): # 将学院名转化为学院id
        if college[i]==line6.currentText():
            col = str(i+1)
    args = []
    args.append(line1.text())
    args.append(line2.text())
    args.append(line3)
    args.append(line4.text())
    args.append(line5.text())
    args.append(col)
    args.append(line7.text())
    args.append(line8.text())
    args.append(line9.text())

    for i in range(len(args)):
        if args[i]=="" or args[i]==None:
            if i in [0,1,7,8]:
                Info(gui,"必填项不得为空")
                return
            else:
                args[i]=None
    if args[7]!=args[8]:
        Info(gui,"两次输入的密码不一致，请重新输入。")
        return
    res,flag = mysql.create_teacher(args[0],args[1],args[7],args[2],args[3],args[4],args[5],args[6])
    if flag==True:
        Info(gui,"注册成功")
        return_login()
    else:
        Error(gui,"数据库操作错误: {}".format(res))

# 显示工作人员注册成功状态
def show_regW_status():
    global mysql,gui,line1,line2,line3,line4,line5,line6,line7
    args = []
    args.append(line1.text())
    args.append(line2.text())
    args.append(line3)
    args.append(line4.text())
    args.append(line5.text())
    args.append(line6.text())
    args.append(line7.text())

    for i in range(len(args)):
        if args[i]=="" or args[i]==None:
            if i in [0,1,5,6]:
                Info(gui,"必填项不得为空")
                return
            else:
                args[i]=None
    if args[5]!=args[6]:
        Info(gui,"两次输入的密码不一致，请重新输入。")
        return
    res,flag = mysql.create_worker(args[0],args[1],args[5],args[2],args[3],args[4])
    if flag==True:
        Info(gui,"注册成功")
        return_login()
    else:
        Error(gui,"数据库操作错误: {}".format(res))

# 显示管理人员注册成功状态
def show_regM_status():
    global mysql,gui,line1,line2,line3,line4,line5,line6,line7,line8
    args = []
    args.append(line1.text())
    args.append(line2.text())
    args.append(line3)
    args.append(line4.text())
    args.append(line5.text())
    args.append(line6.text())
    args.append(line7.text())
    args.append(line8.text())

    for i in range(len(args)):
        if args[i]=="" or args[i]==None:
            if i in [0,1,6,7]:
                Info(gui,"必填项不得为空")
                return
            else:
                args[i]=None
    if args[6]!=args[7]:
        Info(gui,"两次输入的密码不一致，请重新输入。")
        return
    res,flag = mysql.create_manager(args[0],args[1],args[6],args[2],args[3],args[4],args[5])
    if flag==True:
        Info(gui,"注册成功")
        return_login()
    else:
        Error(gui,"数据库操作错误: {}".format(res))

# 返回到登录界面
def return_login():
    '''
    再建窗口
    '''
    sleep(1)
    log = Gui()
    gui.close()
    login(log,mysql)

# 注册进入界面
def register(reg,sql):
    global code,gui,mysql
    gui = reg
    mysql = sql

    gui.resize(600,400) # 窗口大小
    gui.center() # 窗口位置
    gui.setWindowTitle('注册') # 窗口标题
    gui.setWindowOpacity(0.97)
    lbl = gui.Label("角色",250,30,70,100,"#6DDF6D",50)
    lbl.setAutoFillBackground(False)
    btn1 = gui.Button('学生',125,100,input_codeS,50,350,"white","#6DDF6D",30)
    btn2 = gui.Button('教师',125,170,input_codeT,50,350,"white","#6DDF6D",30)
    btn3 = gui.Button('工作人员',125,240,input_codeW,50,350,"white","#6DDF6D",30)
    btn4 = gui.Button('管理人员',125,310,input_codeM,50,350,"white","#6DDF6D",30)
    btn = gui.Button('< 返回',10,10,return_login,30,60,"black",None,20)
    gui.show()

# 学生输入注册码
def input_codeS():
    global character
    character = "S"
    input_code()

# 教师输入注册码
def input_codeT():
    global character
    character = "T"
    input_code()

# 工作人员输入注册码
def input_codeW():
    global character
    character = "W"
    input_code()


# 管理员输入注册码
def input_codeM():
    global character
    character = "M"
    input_code()

# 注册码输入界面
def input_code():
    global line1,newCode
    '''
    创建新的窗口
    '''
    newCode = Gui()
    newCode.resize(600,300) # 窗口大小
    newCode.center() # 窗口位置
    newCode.setWindowTitle('邀请码输入') # 窗口标题
    newCode.setWindowOpacity(0.97)
    lbl = newCode.Label("邀请码",200,30,70,200,"#6DDF6D",50)
    lbl.setAutoFillBackground(False)
    line1 = newCode.Input(125,120,"注册邀请码",50,350)
    btn1 = newCode.Button('确定',400,240,dump_code,50,100,"white","#6DDF6D",30)
    btn2 = newCode.Button('取消',100,240,cancel,50,100,"white","#6DDF6D",30)
    newCode.show()

# 取消该窗口
def cancel():
    '''
    关闭邀请码界面
    '''
    newCode.close()

# 查看邀请码是否正确
def dump_code():
    global line1,character
    code = line1.text()
    if code=="123":
        '''
        新建窗口并运行对应的register
        '''
        sleep(1)
        reg = Gui()
        gui.close()
        newCode.close()
        if character=="S":
            register_student(reg)
        elif character=="T":
            register_teacher(reg)
        elif character=="W":
            register_worker(reg)
        else:
            register_manager(reg)
    else:
        Info(newCode,"邀请码错误！")

if __name__=='__main__':
    global mysql,gui
    #mysql = mydb("localhost","root","123456")
    #mysql.init_data()
    app = QApplication(sys.argv)
    gui = Gui()
    register_student(gui,mysql)
    #input_code()
    sys.exit(app.exec_())
