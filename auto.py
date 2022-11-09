from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import cv2
from PyQt5.QtCore import Qt
import pyautogui
import win32com.shell.shell as shell
import os, sys
from PyQt5.QtCore import QThread
from PyQt5 import QtCore, QtWidgets
from pynput.keyboard import Key, Listener, KeyCode

class MyThread(QThread):
    keyPressed = QtCore.pyqtSignal(KeyCode)
    def __init__(self):
        super().__init__()
        self.thr_run = True
        self.listener = Listener(on_press=self.on_press)
        # self.listener = Listener(on_release=self.on_release)
    
    def on_press(self, key):
        # self.keyPressed.emit(key)
        if key==Key.f8:
            self.thr_run = False
        elif key==Key.f7:
            self.thr_run = True
            self.start()

    def stop_monitoring(self):
        self.listener.stop()

    def start_monitoring(self):
        self.listener.start()


    def thread_stop(self):
        self.thr_run = False

    def run(self):
        self.thr_run = True

        while True:
            while self.thr_run == True:
                pyautogui.keyDown('alt')
                pyautogui.keyDown('1')
                pyautogui.keyUp('1')
                pyautogui.keyUp('alt')
                cv2.waitKey(1000)
            cv2.waitKey(1)


        
                


    

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('1번무기 자동 버스트', self)
        btn1.pressed.connect(self.btn_clicked_1)
        btn2 = QPushButton('중지', self)
        btn2.pressed.connect(self.btn_clicked_2)
        btn3 = QPushButton('종료', self)
        btn3.pressed.connect(QCoreApplication.instance().quit)
        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        self.setLayout(vbox)
        self.setWindowTitle('오토 버스터')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        

        self.Thread1 = MyThread()

        self.Thread1.start_monitoring()

    def btn_clicked_1(self):
        self.Thread1.start()

    def btn_clicked_2(self):
        self.Thread1.thread_stop()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())