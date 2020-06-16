'''
author : RMDE
function : gui tools
'''

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,
        QTextEdit,QLabel,QPushButton, QApplication,QMainWindow, QAction, qApp,
        QHBoxLayout, QVBoxLayout,QGridLayout,QLineEdit,QRadioButton,QComboBox,QCalendarWidget,QFrame,QTableWidget)
from PyQt5.QtGui import QFont,QIcon,QBrush,QColor
from PyQt5.QtCore import QCoreApplication,Qt,QRect,QDate,QDateTime,QTimer

class Gui(QWidget):
    def __init__(self):
        self.time = None
        super().__init__()
    
    # 创建下拉框
    def Combo(self,num,x,y,h,w,text):
        combo = QComboBox(self)
        combo.setGeometry(QRect(x,y,w,h))
        #combo.setStyleSheet("QComboBox{border:gray;background:white;font-size:20;}")
        for i in range(num):
            combo.addItem(text[i])
        return combo


    # 创建标签
    def Label(self,txt,x,y,h=None,w=None,font="black",size=20,back="none"):
        lbl = QLabel(self)
        if h==None:
            lbl.resize(lbl.sizeHint())
        else:
            lbl.resize(w,h)
        lbl.move(x,y)
        lbl.setText(txt)
        lbl.setAlignment(Qt.AlignCenter)
        size = str(size)+"px"
        lbl.setStyleSheet("QLabel{border:none;background:%s;font-size:%s;color:%s;font-weight:bold;font-family:宋体;}"%(back,size,font))
        return lbl

    # 创建输入框
    def Input(self,x,y,txt=None,h=None,w=None):
        line = QLineEdit(self)
        line.move(x,y)
        line.resize(w,h)
        line.setStyleSheet('''
            QLineEdit{border:none;}''')
        if txt!=None:
            line.setPlaceholderText(txt) # 在输入前给予提示
        return line

    # 窗口居中
    def center(self):
        qr = self.frameGeometry() # 获取窗口几何图形
        cp = QDesktopWidget().availableGeometry().center() # 算出屏幕中心点
        qr.moveCenter(cp) # 移动矩形中心点
        self.move(qr.topLeft()) # 移动应用窗口与矩形重合

    # 按钮创建
    def Button(self,name,x,y,event,h=None,w=None,font="black",back="white",size=20):
        btn = QPushButton(name,self)
        if h==None:
            btn.resize(btn.sizeHint())
        else:
            btn.resize(w,h)
        btn.move(x,y)
        size = str(size)+"px"
        btn.setStyleSheet('''
            QPushButton{color:%s;background:%s;border-radius:5px;font-size:%s;}
            QPushButton:hover{background:#DFDFDF;}'''%(font,back,size))
        btn.clicked.connect(event)
        return btn

    # 退出确认
    def closeEvent(self, event):
        '''reply = QMessageBox.question(self, 'Message',"Are you sure to quit?", 
                QMessageBox.Yes |QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()'''
        if self.time!=None:
            self.time.stop()
        event.accept()

    # 日历
    def Calendar(self,x,y,h,w):
        cal = QCalendarWidget(self)
        cal.setMinimumDate(QDate(1988,1,1))
        cal.setMaximumDate(QDate(2088,1,1))
        cal.setGridVisible(True)
        cal.move(x,y)
        cal.resize(w,h)
        return cal

    # 时间显示器
    def Timer(self,x,y):
    	self.lbl = self.Label("",x,y,50,500,25)
    	self.time = QTimer()
    	self.time.timeout.connect(self.show_time)
    	self.time.start(1000)
    	return self.lbl

    # 动态编辑时间
    def show_time(self):
    	time = QDateTime.currentDateTime()
    	timeDisplay = time.toString("yyyy-MM-dd dddd hh:mm:ss ")
    	self.lbl.setText("当前时间"+timeDisplay)

    # 创建表格
    def Table(self,x,y,h,w,row=4,col=3,title=None):
        table = QTableWidget(self)
        table.resize(w,h)
        table.move(x,y)
        table.setRowCount(row)
        table.setColumnCount(col)
        table.horizontalHeader().setVisible(True)
        table.verticalHeader().setVisible(True)
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setDefaultSectionSize(w/col)
        table.verticalHeader().setStretchLastSection(True)
        table.setFrameShape(QFrame.NoFrame)
        if title==None:
            title = [str(x+1) for x in range(col)]
        no = [str(x+1) for x in range(row)]
        table.setVerticalHeaderLabels(no)
        table.setHorizontalHeaderLabels(title)
        return table


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    ex.Table(1,1,100,200,4,3)
    ex.show()
    sys.exit(app.exec_())
