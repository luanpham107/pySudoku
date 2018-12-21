#!/usr/bin/python -u
# -*- coding: utf-8 -*-


#+=================================================================+
#|                      pySudokuSolver 1.3                         |
#+=================================================================+
#|                                                                 |
#|       +-------------------------------------------------+       |
#|       |     Author   : पुष्पक दगड़े  (Pushpak Dagade)        |       |
#|       |     Email    : guanidene@gmail.com              |       |
#|       +-------------------------------------------------+       |
#|                                                                 |
#+=================================================================+

"""
A small graphical application for solving any Sudoku puzzle, almost
instantaneously.
"""

# Set appropriate PyQt4 api
import sip
sip.setapi('QString', 2)      # avoid PyQt4.QString class altogether
sip.setapi('QVariant', 2)

from PyQt5 import QtGui
from mainwindow import MainWindow
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication, QLabel)
__author__ = u"पुष्पक दगड़े (Pushpak Dagade)"
__version__ = '1.3'


if __name__ == "__main__":
    app = QApplication(['Sudoku Solver'])
    app.setOrganizationName('')
    app.setApplicationName('pySudokuSolver')
    widget = MainWindow()
    widget.show()
    exit(app.exec_())
