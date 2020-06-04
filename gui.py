import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,
        QTextEdit,QLabel,QPushButton, QApplication,QMainWindow, QAction, qApp,
        QHBoxLayout, QVBoxLayout,QGridLayout,QLineEdit)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication

class Gui(QWidget):
    def __init__(self):
        super().__init__()

    # 创建标签
    def Label(self,txt,x,y,h=None,w=None):
        lbl = QLabel(self)
        if h==None:
            lbl.resize(lbl.sizeHint())
        else:
            lbl.resize(w,h)
        lbl.move(x,y)
        lbl.setText(txt)
        lbl.setStyleSheet("QLabel{background:white;}""QLabel{color:rgb(200,200,200);font-size:10px;font-weight:bold;font-family:宋体;}")
        return lbl

    # 创建输入框
    def Input(self,x,y,txt=None,h=None,w=None):
        line = QLineEdit(self)
        line.move(x,y)
        line.resize(w,h)
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
    def Button(self,name,x,y,event,h=None,w=None):
        btn = QPushButton(name,self)
        if h==None:
            btn.resize(btn.sizeHint())
        else:
            btn.resize(w,h)
        btn.move(x,y)
        btn.clicked.connect(event)
        return btn

    # 退出确认
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',"Are you sure to quit?", 
                QMessageBox.Yes |QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())
