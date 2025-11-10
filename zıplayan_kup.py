from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
import sys as _s

class mainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.dx = 2       #x eksen için artış/azalış değişkeni
        self.dy = 3       #y ekseni için artış/azalış değişkeni
        
        self.x_axis = 0   #x ekseni  
        self.y_axis = 0   #y ekseni

        self.cube_width = 100  #küp genişliği / uzunlugu
    
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(15)
    
    def paintEvent(self,a0):
        painter = QPainter(self)                #çizim renderer'ı
        painter.setPen(QPen(QColor('Red'),5))   #kalem ayarları

        painter.drawRect(self.x_axis,self.y_axis,self.cube_width,self.cube_width)    #her seferinde koordita göre kare çiz

        self.x_axis += self.dx        #her seferinde değişkenin pozitif/negatif olmasına bakmaksızın üzerine ekleyerek koordinatı güncelle
        self.y_axis += self.dy

        if self.x_axis + self.cube_width >= self.width() or self.x_axis <= 1:    #eğer x koordinatı + küp genişliği pencere genişliğine eşitse yada büyükse VEYA x ekseni dx'in katı olmayan bir sayı olan 1'e eşit yada küçükse: dx'i -dx yap yani self.dx = -self.dx şeklinde dx in kuvvetini negatif yöne uygula
            self.dx = -self.dx
        
        if self.y_axis + self.cube_width >= self.height() or self.y_axis <= 2:  #buradada yukarıdaki mekanizmanın aynısı var ancak burada x yerine y için yapılmış
            self.dy = -self.dy



if __name__ == "__main__":
    sp = QApplication(_s.argv)
    sw = mainWidget()
    sw.show()
    _s.exit(sp.exec_())

#BU KOD FLAGLERİ KULLANMADAN SADECE NEGATİV VE POZİTİF KUVVETERİ KULLANARAK SEKEN BİR KÜP ANİMASYONU OLUŞTURMAMIZA OLANAK TANIR AKSİ HALDE FLAG İLE YAPILSAYDI DAHA KISITLAYICI VE VERİMSİZ BİR KOD OLURDU
