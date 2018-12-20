import sys
from pprint import pprint
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication)

class TutorialWindow(QWidget):
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    tutorial_window = TutorialWindow()
    tutorial_window.show()
    sys.exit(app.exec_())