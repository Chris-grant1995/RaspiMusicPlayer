#!/usr/bin/python3
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QSize    
from pygame import mixer 


class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.position = None
        self.setMinimumSize(QSize(640, 480))    
        self.setWindowTitle("Hello world - pythonprogramminglanguage.com") 
        self.setStyleSheet("background-color:'#121212'")
        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)   

        # gridLayout = QGridLayout(self)     
        layout = QHBoxLayout(self)
        centralWidget.setLayout(layout)
          
        self.exit_button = QPushButton('Exit', self)
        layout.addWidget(self.exit_button)
        self.exit_button.clicked.connect(self.exit_click)

        self.play_button = QPushButton('Play', self)
        # play_button.setIcon(QtGui.QIcon('play.jpg'))
        self.play_button.setStyleSheet("background-image: url('play.jpg'); border: none;")
        layout.addWidget(self.play_button)
        self.play_button.clicked.connect(self.play_click)

        prev_button = QPushButton('Prev', self)
        layout.addWidget(prev_button)
        prev_button.clicked.connect(self.exit_click)

        next_button = QPushButton('Next', self)
        layout.addWidget(next_button)
        next_button.clicked.connect(self.exit_click)

        # title = QLabel("Hello World from PyQt", self) 
        # title.setAlignment(QtCore.Qt.AlignCenter) 
        # gridLayout.addWidget(title, 0, 0)
    @pyqtSlot()
    def exit_click(self):
        print('PyQt5 button click')
        sys.exit(0)

    @pyqtSlot()
    def play_click(self):
        print("Play Clicked")
        
        if("Play" in self.play_button.text()):
            if(self.position != None):
                mixer.music.unpause()
            else:
                mixer.music.load('test.mp3')
                mixer.music.play()
            self.play_button.setText("Pause")
        else:
            self.position = mixer.music.get_pos()
            mixer.music.pause()
            self.play_button.setText("Play")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.showFullScreen()
    mixer.init()
    sys.exit( app.exec_() )