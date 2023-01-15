from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from UI3 import Ui_MainWindow
import qimage2ndarray
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QGridLayout, QLineEdit)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
import get11
import mysql.connector
import datetime
import controller
import controller2

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
        self.logflag = False
        self.username_list=[]#get_sql1()
        self.password2_list =[]#get_sql2()

        self.ui.log.clicked.connect(self.login_) 
        self.ui.can.clicked.connect(sys.exit)
        self.ui.res.clicked.connect(self.reg)
        
        
        
        self.ui.pas_lo.setEchoMode(QLineEdit.Password)  # 隱藏密碼
        
        
        

        self.setup_control()
    

    def setup_control(self):
        # TODO
        # self.ui.textEdit.setText('Happy World!')
        #self.ui.pushButton.setText('Print message!')
        self.clicked_counter = 0
        self.account_1 = self.ui.acc_lo.toPlainText()
        self.pas_1 = self.ui.pas_lo.text()
    
    def get_sql01(self):
        #with cursor  as cursor1:
        # 查詢資料SQL語法
        username_list= []
        command = "SELECT `username` FROM UserRgeisters  "
        # 執行指令
        cursor.execute(command)
        # 取得所有資料
        result = cursor.fetchall()
        for i in range(len(result)):
            username_list.append(result[i][0])
        return username_list
    
    def get_sql02(self):
        password_list=[]
        #with cursor  as cursor1:
        # 查詢資料SQL語法
        command = "SELECT `password2` FROM UserRgeisters  "
        # 執行指令
        cursor.execute(command)
        # 取得所有資料
        result = cursor.fetchall()
        for i in range(len(result)):
            password_list.append(result[i][0])
        
        return password_list
    
    def login_(self):
        self.password2_list= self.get_sql02()
        self.username_list = self.get_sql01()
        self.account_1 = self.ui.acc_lo.toPlainText()
        self.pas_1 = self.ui.pas_lo.text()
        # self.get_sql02
        print("acc",self.account_1)
        print("pas",self.pas_1 )
        print("user list: ", self.username_list)
        print("pass list: ", self.password2_list)
        #self.username_list=self.get_sql01
        #self.password2_list=self.get_sql02
        if self.account_1 in self.username_list:
            if self.pas_1 in self.password2_list:
                self.logflag = True
        
        else:
            self.ui.label_4.setText('請確認帳號與密碼是否正確')
        if self.logflag == True:
            self.run()
            # window = MainWindow_controller()
            # window.close()

    def reg(self):
        import os
        window.close()
        os.system('python controller2.py')
    
    def run(self):
        import os
        window.close()
        os.system('python controller.py')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())