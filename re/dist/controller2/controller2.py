from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from UI2 import Ui_MainWindow
import qimage2ndarray
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QGridLayout, QLineEdit)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
import get11
import mysql.connector
import datetime

import controller3

connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='0000',
                                    database='user')

cursor = connection.cursor()
class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.account_ = None
        self.pas1 = None 
        self.pass2 = None 
        self.email_ = None 
        self.accflg = False
        self.pasflg = False 
        self.emailflg = False

        self.ui.res.clicked.connect(self.resgister) 
        self.ui.end.clicked.connect(sys.exit)
        self.ui.login0.clicked.connect(self.login_)
        
        
        self.ui.pas.setEchoMode(QLineEdit.Password)  # 隱藏密碼
        self.ui.pas2.setEchoMode(QLineEdit.Password) # 隱藏密碼
        

        self.setup_control()

    

    def setup_control(self):
        # TODO
        # self.ui.textEdit.setText('Happy World!')
        #self.ui.pushButton.setText('Print message!')
        self.clicked_counter = 0
        self.account_ = self.ui.acc.toPlainText()
        # print(self.account_)
    def resgister(self):
        self.account_ = self.ui.acc.toPlainText()
        if (self.account_ != '' ):
            self.accflg = True 
        else :
            self.ui.label_6acc.setText('請確認帳號')
        self.pas1 = self.ui.pas.text()
        self.pass2 = self.ui.pas2.text()
        
        if (self.pas1 != '' ):
            self.pasflg =( self.pas1==self.pass2)
        elif  (self.pas1 == '' ):
            self.ui.label_5pas.setText = ('請確認密碼')
            self.pasflg = False
        
        
        self.email_ = self.ui.em.toPlainText()
        if (self.email_ != '' ):
            self.emailflg = True 
        else:
            self.ui.label_5.setText('請確認 Email ')
        # print(self.email_)
        if ( self.accflg == True & self.pasflg==True &self.emailflg==True):
            self.ui.label_6.setText('註冊成功 !')
            print(str(self.email_),str(self.account_),str(self.pas1))
            #SS="INSERT INTO `UserRgeisters`(`email`,`username`,`password2`) VALUES(%s,%s,%s)" %("s07326@gmail.com","ssas","sss")
            cursor.execute(cursor.execute("INSERT INTO `UserRgeisters`(`email`,`username`,`password2`) VALUES(%s,%s,%s)",(str(self.email_),str(self.account_),str(self.pas1))))
            connection.commit()
    
    def login_(self):
        import os
        window.close()
        os.system('python controller3.py') 

        #ui_hello.show()
        #window.close()
    

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #ui_hello = controller3.MainWindow_controller()
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())


        
                

        
