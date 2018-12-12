# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:12:40 2018

@author: Liam
"""

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import (QPushButton, QApplication)

import sys
        
class Ui(QtWidgets.QDialog):
    grid00 = [
        ["pushButton_00_00",	"pushButton_00_01",	"pushButton_00_02"],
        ["pushButton_00_10",	"pushButton_00_11",	"pushButton_00_12"],
        ["pushButton_00_20",	"pushButton_00_21",	"pushButton_00_22"]
        ]
    grid01 = [
        ["pushButton_01_00",	"pushButton_01_01",	"pushButton_01_02"],
        ["pushButton_01_10",	"pushButton_01_11",	"pushButton_01_12"],
        ["pushButton_01_20",	"pushButton_01_21",	"pushButton_01_22"]
        ]
    grid02 = [
        ["pushButton_02_00",	"pushButton_02_01",	"pushButton_02_02"],
        ["pushButton_02_10",	"pushButton_02_11",	"pushButton_02_12"],
        ["pushButton_02_20",	"pushButton_02_21",	"pushButton_02_22"]
        ]
    
    grid10 = [
        ["pushButton_10_00",	"pushButton_10_01",	"pushButton_10_02"],
        ["pushButton_10_10",	"pushButton_10_11",	"pushButton_10_12"],
        ["pushButton_10_20",	"pushButton_10_21",	"pushButton_10_22"]
        ]
    grid11 = [
        ["pushButton_11_00",	"pushButton_11_01",	"pushButton_11_02"],
        ["pushButton_11_10",	"pushButton_11_11",	"pushButton_11_12"],
        ["pushButton_11_20",	"pushButton_11_21",	"pushButton_11_22"]
        ]
    grid12 = [
        ["pushButton_12_00",	"pushButton_12_01",	"pushButton_12_02"],
        ["pushButton_12_10",	"pushButton_12_11",	"pushButton_12_12"],
        ["pushButton_12_20",	"pushButton_12_21",	"pushButton_12_22"]
        ]
    
    grid20 = [
        ["pushButton_20_00",	"pushButton_20_01",	"pushButton_20_02"],
        ["pushButton_20_10",	"pushButton_20_11",	"pushButton_20_12"],
        ["pushButton_20_20",	"pushButton_20_21",	"pushButton_20_22"]
        ]
    grid21 = [
        ["pushButton_21_00",	"pushButton_21_01",	"pushButton_21_02"],
        ["pushButton_21_10",	"pushButton_21_11",	"pushButton_21_12"],
        ["pushButton_21_20",	"pushButton_21_21",	"pushButton_21_22"]
        ]
    grid22 = [
        ["pushButton_22_00",	"pushButton_22_01",	"pushButton_22_02"],
        ["pushButton_22_10",	"pushButton_22_11",	"pushButton_22_12"],
        ["pushButton_22_20",	"pushButton_22_21",	"pushButton_22_22"]
        ]
    gridTotal = [
            [grid00, grid01, grid02], [grid10, grid11, grid12], [grid20, grid21, grid22]
            ]
    
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('guiSudoku.ui', self)
        #self.line = self.findChild(QPushButton, 'pushButton_50')                
        #btArray[0][0] = self.findChild(QPushButton, self.grid00[0][0])
        #btArray[0][0].clicked.connect(self.ok_handler)
        self.mappingButton()
        self.show()
        
    def mappingButton(self):
        btArray = [[0 for i in range(3)] for i in range(3)]        
        for i in range(3):
            for j in range(3):
                btArray[i][j] = self.findChild(QPushButton, self.grid00[i][j])
                btArray[i][j].clicked.connect(self.pushButton00_handler)       
                
    def pushButton00_handler(self):        
        print(self.grid00[0][0])    
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())