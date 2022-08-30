import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.button1 = QtWidgets.QPushButton('Games')
        self.button2 = QtWidgets.QPushButton('Settings')
        self.button3 = QtWidgets.QPushButton('Quit')
        self.button3.clicked.connect(self.Quit)
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
    
    
    @QtCore.Slot()
    
    def Quit(self):
        app.quit()
        
    
 #if __name__ == "__main__":
app = QtWidgets.QApplication([])
widget = MainWindow()
widget.setStyleSheet("""
                     background-color: #262626;
                     color: #FFFFFF;
                     font-family: Titillium;
                     font-size: 20px;
                     """)
widget.resize(600, 400)
widget.show()
  
sys.exit(app.exec())