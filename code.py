

from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(13,GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(15,GPIO.OUT, initial= GPIO.LOW)




def redLight():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)

    


def yellowLight():

    GPIO.output(13, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)

    
def greenLight():
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)

def ledsOff():
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 238)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.redButton = QtWidgets.QRadioButton(self.centralwidget)
        self.redButton.setGeometry(QtCore.QRect(40, 70, 131, 51))
        self.redButton.setObjectName("redButton")
        self.yellowButton = QtWidgets.QRadioButton(self.centralwidget)
        self.yellowButton.setGeometry(QtCore.QRect(210, 70, 131, 51))
        self.yellowButton.setObjectName("yellowButton")
        self.greenButton = QtWidgets.QRadioButton(self.centralwidget)
        self.greenButton.setGeometry(QtCore.QRect(380, 70, 131, 51))
        self.greenButton.setObjectName("greenButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(210, 140, 99, 30))
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(ledsOff)
        self.exitButton.clicked.connect(lambda:self.close)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 504, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "LED controller"))
        self.redButton.setText(_translate("MainWindow", "RED"))
        self.yellowButton.setText(_translate("MainWindow", "YELLOW"))
        self.greenButton.setText(_translate("MainWindow", "GREEN"))
        self.exitButton.setText(_translate("MainWindow", "EXIT"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.redButton.clicked.connect(redLight)
    ui.yellowButton.clicked.connect(yellowLight)
    ui.greenButton.clicked.connect(greenLight)
    
    MainWindow.show()
    sys.exit(app.exec_())
