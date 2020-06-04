from gui import *
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,
        QTextEdit,QLabel,QPushButton, QApplication,QMainWindow, QAction, qApp,
        QHBoxLayout, QVBoxLayout,QGridLayout,QLineEdit)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication
    
name = None
passwd = None

# 显示登陆界面    
def login(gui):
    gui.resize(600,400) # 窗口大小
    gui.center() # 窗口位置
    gui.setWindowTitle('信息管理系统') # 窗口标题
    gui.setWindowIcon(QIcon('Element/Icon.jpg')) # 应用图标
    btn = gui.Button('登录',300,100,show_login_status)
    lbl = gui.Label("test",100,100,20,100)
    line = gui.Input("xxx",300,300,20,100)
    gui.show()

# 显示登录成功状态
def show_login_status():
    global name,passwd
    if name==None or passwd==None:
        print("no")

if __name__=='__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    login(gui)
    sys.exit(app.exec_())
