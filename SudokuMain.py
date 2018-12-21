import sys
from pprint import pprint
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication)

class TutorialWindow(QWidget):
    buttonList = []
    def __init__(self):
        super().__init__()
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)        
        lines = self.readPuzzle("puzzle.txt");  
        
        print(lines)
        values = [
            '1', '1', '1', '1', '1', '1', '1', '1', '1',
            '1', '1', '1', '1', '1', '1', '1', '1', '1',
            '1', '1', '1', '1', '1', '1', '1', '1', '1',
            '1', '1', '1', '1', '1', '1', '1', '1', '1',
            '1', '1', '1', '1', '1', '1', '1', '1', '1',
            '1', '1', '1', '1', '1', '1', '1', '1', '1',
            '1', '1', '1', '1', '1', '1', '1', '1', '1',
            '1', '1', '1', '1', '1', '1', '1', '1', '1',
            '1', '1', '1', '1', '1', '1', '1', '1', '1',            
        ]
        
        for i in range(9):
            for j in range(9):
                values[i*9 + j] = lines[i][j]
        
        print (values)
        positions = [(i, j) for i in range(9) for j in range(9)]
        # position is an array of tuples
        #pprint("positions = "+str(positions))
        self.setGeometry(300, 300, 300, 120)
        for position, value in zip(positions, values):
            print("position = " + str(position))
            print("value = " + str(value))
            if value == '':
                continue
            button = QPushButton(value)   
            button.clicked.connect(self.buttonClicked)
            self.buttonList.append(button)
            grid_layout.addWidget(button, *position)
        self.setWindowTitle('Sudoku')
        
    def readPuzzle(self, strfileName):
        with open(strfileName, "r") as ins:
            array = []
            for line in ins:
                lineX = line.split('\n')                
                lineY = lineX[0].split(',')
                array.append(lineY)        
        return array

    def buttonClicked(self):
        sender = self.sender()
        print(sender)
        text = int(sender.text()) + 1
        if(text > 9):
            text = 1
        sender.setText(str(text))
        print(text)
        self.checkCol()
        print('Clicked')
        
    def checkCol(self):
        _colList = []
        for i in range(9):
            _colList.append(int(self.buttonList[i].text()))
        self.checkListFullNumber(_colList)
        print(_colList)
        print('Col')
        
    def checkRơw(self):
        print('Row')

    def checkGrid(self):
        print('Grid')    
    
    def checkListFullNumber(self, arrIn):
        arrIn.sort()
        print('Sort the list:', arrIn)
        for i in range(9):
            #print(i+1, ' so sanh voi ', arrIn[i])            
            if arrIn[i] != i+1:
                print ('Aray check: False')
                return False            
        print('Array check: True')        
        return True        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    tutorial_window = TutorialWindow()
    tutorial_window.show()
    sys.exit(app.exec_())