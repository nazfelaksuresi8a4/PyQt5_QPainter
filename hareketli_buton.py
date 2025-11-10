from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
import sys as _s

class mainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.dx = 2
        self.dy = 3
        
        self.x_axis = 0
        self.y_axis = 0

        self.cube_width = 100
    
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(15)
    
    def paintEvent(self,a0):
        painter = QPainter(self)
        painter.setPen(QPen(QColor('Red'),5))

        painter.drawRect(self.x_axis,self.y_axis,self.cube_width,self.cube_width)

        self.x_axis += self.dx
        self.y_axis += self.dy

        if self.x_axis + self.cube_width >= self.width() or self.x_axis <= 1:
            self.dx = -self.dx
        
        if self.y_axis + self.cube_width >= self.height() or self.y_axis <= 2:
            self.dy = -self.dy

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = mainWidget()
        layout = QVBoxLayout()
        self.widget.setLayout(layout)

        self.btn = QPushButton(self,text='bana tıkla')
        self.btn.setStyleSheet('background-color:gray;color:white;font-size:15px')

        self.setCentralWidget(self.widget)

        timer = QTimer(self)
        timer.timeout.connect(self.igniter)
        timer.start(10)
    
    def igniter(self):
        self.btn.move(self.widget.x_axis,self.widget.y_axis)
        self.btn.resize(self.widget.cube_width,self.widget.cube_width)

if __name__ == "__main__":
    sp = QApplication(_s.argv)
    sw = MainWindow()
    sw.show()
    _s.exit(sp.exec_())
