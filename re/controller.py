from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from UI import Ui_MainWindow
import cv2
import time
import read_img
import numpy as np
from datetime import datetime
import main2
import qimage2ndarray
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
import sys

import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='0000',
                                    database='block')
cursor = connection.cursor()

import pandas as pd 



class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
        self.mode_x= None
        self.handmode=None
        self.endd = False
        # account : 
        self.account = sys.argv[1]
        print("帳號 : ", self.account)
        


    def setup_control(self):
        # TODO
        # self.ui.textEdit.setText('Happy World!')
        #self.ui.pushButton.setText('Print message!')
        self.clicked_counter = 0
        self.ui.pushButton.clicked.connect(self.mode_f)
        self.ui.pushButton_2.clicked.connect(self.mode_s)
        self.ui.pushButton_3.clicked.connect(self.mode_t)
        self.ui.pushButton_4.clicked.connect(self.lh)
        self.ui.pushButton_5.clicked.connect(self.rh)
        self.ui.pushButton_6.clicked.connect(self.main_run)
        self.ui.pushButton_7.clicked.connect(self.displayFrame)
        self.ui.pushButton_8.clicked.connect(sys.exit)
        self.ui.pushButton_9.clicked.connect(self.csv_)


    def mode_f(self): #模式一
        self.mode_x = '1'
    
    def mode_s(self):
        self.mode_x = '2'

    def mode_t(self):
        self.mode_x = '3'
    
    def lh(self): # 左手
        self.handmode = '0'

    def rh(self): # 右手
        self.handmode = '1'
    
    def main_run(self):
        self.time_flag=True
        font = cv2.FONT_HERSHEY_PLAIN
        vc = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        timer1= 60
        print(timer1)
        # 設定分數 與 隨機位置
        name='window_name'
        score2=0
        ISOTIMEFORMAT = '%Hh%Mm%Ss'
        nonum=self.rand_No()
        cnum=self.rand_cNo()

        time_flag= True
        f= False  
        flag = False 
        start_time = time.time()
        t =str( datetime.now().strftime(ISOTIMEFORMAT))
        #month = now.strftime("%m")
        #print("month:", month)
        ###### SQL #########
        connection = mysql.connector.connect(host='localhost',
                                            port='3306',
                                            user='root',
                                            password='0000',
                                            database='block')
        self.cursor = connection.cursor()
        ####################

        #SS="INSERT INTO `blockbd`(`Score`,`Time`,`Mode`,`rl`,`nonum`,`cnum`,`boxes`,`time_`,`posi`) VALUES(%d,%d,%s,%s,%s,%s,%s,%s,%s)" %(0,0,self.mode_x,self.handmode,str(nonum),str(cnum),0,t,'0')
        SS = "INSERT INTO `blockbd2`(`account`,`Score`,`Time`,`Mode`,`rl`,`nonum`,`cnum`,`boxes`,`time_`,`strat_time`,`end_time`,`sixs`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        QQ = (self.account,0,0,self.mode_x,self.handmode,str(nonum),str(cnum),0,t,t,t,"O")
        self.cursor.execute(SS,QQ)
        connection.commit()

        print('self.mode_x',self.mode_x,'self.handmode',self.handmode)
        while self.time_flag==True :
            

            if ((self.mode_x != None)and(self.handmode != None)):
                ###### SQL #########
                connection = mysql.connector.connect(host='localhost',
                                                    port='3306',
                                                    user='root',
                                                    password='0000',
                                                    database='block')
                self.cursor = connection.cursor()
                self.sqllist2 = self.get_sql()
                # nonum = self.sqllist2[5]
                # cnum = self.sqllist2[6]
                # score2 = self.sqllist2[1]
                # modex = self.sqllist2[3]
                # rlx = self.sqllist2[4]
                nonum = self.sqllist2[6]
                cnum = self.sqllist2[7]
                score2 = self.sqllist2[2]
                modex = self.sqllist2[4]
                rlx = self.sqllist2[5]
                dic_rl ={'0':'右盤','1':'左盤'}
                dic_rl2 ={'0':'左盤','1':'右盤'}
                nonum = int(nonum)
                print('nonum',nonum)
                ####################
                account = self.account
                self.frame,self.frame12,self.time_flag,self.alltime,self.score2,self.df = main2.main_strat(account,score2,cnum,nonum,f,self.mode_x,self.handmode,time_flag,flag,vc,timer1,start_time)# main2.strt(self.mode_x,self.handmode)
                f=True
                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                self.frame12 = cv2.cvtColor(self.frame12, cv2.COLOR_BGR2RGB)
                self.frame = qimage2ndarray.array2qimage(self.frame)
                self.frame12 = qimage2ndarray.array2qimage(self.frame12)
                self.ui.label.setPixmap(QPixmap.fromImage(self.frame))
                self.ui.label_2.setPixmap(QPixmap.fromImage(self.frame12))
                
                # self.sqllist1 = self.get_sql()
                self.ui.timertext.setText('已過的時間 :'+str(self.alltime))
                self.ui.scoretext.setText('目前得分 '+str(self.score2 ))
                if modex == '1':
                    t = "請將積木放置 {}".format(dic_rl2[rlx])
                if modex == '2':
                    t = "請將積木放置 {} NO.{} 藍色圓點上".format(dic_rl2[rlx],nonum)
                if modex == '3':
                    t = "請將積木從藍色圓點 從 {} NO.{} 位置, 放置 {} NO.{} 圓點位置 ".format(dic_rl[rlx], nonum,dic_rl2[rlx],nonum)
                self.ui.chart.setText("模式 {} , {} ".format(modex,t))
        self.ui.chart.setText(self.df)
    
    def displayFrame(self):
        vc = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.time_flag=True
        while self.time_flag==True:
            
            # if endd == False:
           # ret, self.frame = cap.read()
            
            #self.frame = cv2.resize(self.frame,(640,560))
            self.frame12=main2.teach_(vc)
            # self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            self.frame12 = cv2.cvtColor(self.frame12, cv2.COLOR_BGR2RGB)
            # print(self.frame12.shape)
            #self.frame = qimage2ndarray.array2qimage(self.frame)
            self.frame12 = qimage2ndarray.array2qimage(self.frame12)
            self.ui.label.setPixmap(QPixmap.fromImage(self.frame12))
            cv2.waitKey(5)
            
        
        vc.release()
        cv2.destroyAllWindows()

    def csv_(self): ##############12/27
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save File","","All Files(*);;Text Files(*.txt)",options = options)                
        if fileName:
            self.filenames = fileName
            self.df.to_csv(fileName+'.csv',index=False)

    # def teach(self):
    #     # timer = QTimer()
    #     # timer.start(10000)
    #     # timer.timeout.connect(self.displayFrame)
    #     self.displayFrame
        
    #     print("OK")
        
        

    def end2(self):
        self.endd = True

    def get_sql(self):
        #with cursor  as cursor1:
        # 查詢資料SQL語法
        command = "SELECT * FROM blockbd2"
        # 執行指令
        self.cursor.execute(command)
        # 取得所有資料
        result = self.cursor.fetchall()
        #print(len(result))
        return result[-1]
    
    def rand_No(self):
        rnum =np.random.randint(1,16,1)
        print("rnum: ", rnum[0])
        return rnum[0]

    def rand_cNo(self):
        cnum =np.random.randint(0,3,1)
        print("cnum: ", cnum[0])
        return cnum[0]

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())

    
            

      

    