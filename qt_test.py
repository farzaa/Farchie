import serial
import serial.tools.list_ports
import sys
from detective import Detective
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush

class user_interface(QWidget):
    
    def __init__(self):
        super().__init__()
        self.red = QColor(255, 0, 0);
        self.green = QColor(0, 255, 0);

        self.txt_color = QColor(255, 0, 0);
        self.sleep_color = QColor(255, 0, 0);
        self.focused_color = QColor(255, 0, 0);
        self.initUI()
        ardu_port = None
        for open_port in list(serial.tools.list_ports.comports()):
            if "usbmodem" in open_port.device:
                ardu_port = open_port.device

        self.ser = serial.Serial(ardu_port, 9600)
        
    def initUI(self):      

        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Colours')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)

    def drawRectangles(self, qp):
      
        col = QColor(0, 0, 0)
        col.setNamedColor('#000')
        qp.setPen(col)

        qp.setBrush(self.focused_color)
        qp.drawRect(10, 15, 30, 30)
        qp.drawText(0, 70, "Focused") 
              
        qp.setBrush(self.sleep_color)
        qp.drawRect(70, 15, 30, 30)
        qp.drawText(60, 70, "Sleeping")

        qp.setBrush(self.txt_color)
        qp.drawRect(130, 15, 30, 30)
        qp.drawText(120, 70, "Texting")

        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(250, 15, 30, 30)

    def change_colors(self, txt, sleep, focused):
        print (sleep)
        if txt:
            self.txt_color = QColor(0, 255, 0)
            self.ser.write(b't')
        else:
            self.txt_color = QColor(255, 0, 0)
        
        if sleep == None:
            return

        if sleep:
            self.sleep_color = QColor(0, 255, 0)
            self.ser.write(b's')
        else:
            self.sleep_color = QColor(255, 0, 0)
            self.ser.write(b'r')

        if focused:
            self.focused_color = QColor(0, 255, 0)
            self.ser.write(b'f')
        else:
            self.focused_color = QColor(255, 0, 0)
            self.ser.write(b'g')

        self.update()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ui = user_interface()
    d = Detective(ui)
    d.track_faces()
    sys.exit(app.exec_())