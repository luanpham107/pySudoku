# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:12:40 2018
@author: Liam
"""

from PyQt5 import uic, QtWidgets
from PyQt5 import Qt
from PyQt5.QtWidgets import (QPushButton, QApplication, QTableWidget)

import sys
        
class Ui(QtWidgets.QDialog):
    
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('guiTable.ui', self)
        #self.line = self.findChild(QPushButton, 'pushButton_50')                
        table1 = self.findChild(QTableWidget, 'tableWidget')
        print(table1.currentRow())
        table1.clicked.connect(self.mouseClickOnTable_handler)
        self.show()
        
    def mouseClickOnTable_handler(self):
        print('Mouse Clicked')
        
    def myfunction(self):
        print('enter my function')
        
    def keyPressEvent(self, e):
        if e.key() == Qt.KeyEscape:
            self.close()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())