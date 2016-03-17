# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:56:33 2015

@author: lcorman
"""



from PyQt4 import QtCore, QtGui#, Qt
from mbedOven import Ui_MainWindow
from time import sleep, localtime
import ConfigParser
import os
import sys
import serial

class MainWindow(QtGui.QMainWindow):
    """

    GUI control

    """
    
    def __init__(self):
        """

        Creates main window and connects camera

        """
#        Setup Main window
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
#        Setup state of oven
        self.stateOven = False
        self.ui.AlimOff.setEnabled(self.stateOven)
        self.ui.AlimOn.setEnabled(not self.stateOven)
        self.ui.CurrentValueValue.setText('0.0')
        
#        Load config file
        self.config = ConfigParser.RawConfigParser()
        if not os.path.isfile('configMbedOven.cfg'):      
            writeConfigFileDefault()
        self.config.read('configMbedOven.cfg')
        self.serdev = []
        if sys.platform.startswith('linux'):
            self.serdev = self.config.get('General Parameters','mbed port linux')
        elif sys.platform.startswith('win'):
            self.serdev = self.config.getint('General Parameters','mbed port windows')
        self.valueOn = self.config.getfloat('General Parameters','value on (V, <3.3V)')/3.3
        self.valueOff = self.config.getfloat('General Parameters','value off (V, <3.3V)')/3.3
        self.startHour = self.config.getfloat('General Parameters','hour start')
        
#        Open the mbed
        self.openMbed()
        
#        Last hour check
        self.lastHourCheck = localtime().tm_hour + localtime().tm_min/60.
        
#        Timer to check if one should power up the oven
        sleep(2)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.check_time)
        self.timer.start(15000)
        
        
        
    
        
    
    def closeEvent(self,event):
        """

        Closes the camera and the sockets when closing the main window

        """
        self.serialPort.close()
        return
        
    def openMbed(self):
#        serdev = '/dev/ttyACM1'
        self.serialPort = serial.Serial(self.serdev)
        
    def check_time(self):
        oldHour = self.lastHourCheck
        today = localtime().tm_wday;
        self.lastHourCheck = localtime().tm_hour + localtime().tm_min/60.
        if (oldHour<=self.startHour) and (self.lastHourCheck>self.startHour)  and not (today==5) and not (today==6):
            self.on_AlimOn_clicked()
            print "Turned on"
    
#==============================================================================
#     Callback functions
#==============================================================================
    

    @QtCore.pyqtSignature("")
    def on_AlimOff_clicked(self):
        """

        Inverts the value of the takePictureWithCicero boolean and enables/disables thee right buttons.

        """
        self.stateOven = False
        self.ui.AlimOff.setEnabled(self.stateOven)
        self.ui.AlimOn.setEnabled(not self.stateOven)
        self.ui.CurrentValueValue.setText(str(self.valueOff*3.3)+'V')
        self.serialPort.write(str(self.valueOff)+'\n')
        sleep(0.5)
        self.serialPort.write('off\n')
        return
            

    @QtCore.pyqtSignature("")            
    def on_AlimOn_clicked(self):
        """

        If button clicked takes snapshot and displays it. Skips if a current camera is not selected.

        """
        self.stateOven = True
        self.ui.AlimOff.setEnabled(self.stateOven)
        self.ui.AlimOn.setEnabled(not self.stateOven)
        self.ui.CurrentValueValue.setText(str(self.valueOn*3.3)+'V')
        self.serialPort.write(str(self.valueOn)+'\n')
        sleep(0.5)
        self.serialPort.write('on\n')
        return
        
        
def writeConfigFileDefault():
    """

    Writes a first config file in case it does not already exist

    """
    config = ConfigParser.RawConfigParser()
    
    config.add_section('General Parameters')
    config.set('General Parameters','mbed port linux','/dev/ttyACM3')
    config.set('General Parameters','mbed port windows','4')
    config.set('General Parameters','value on (V, <3.3V)','1.0')
    config.set('General Parameters','value off (V, <3.3V)','0.3')
    config.set('General Parameters','hour start','7.5')
    
    with open('configMbedOven.cfg','w') as configfile:
        config.write(configfile)
    return
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())