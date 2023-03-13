
from sys import flags
import cv2
import time
import numpy as np
CONFIDENCE_THRESHOLD = 0.2
NMS_THRESHOLD = 0.4
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

class_names = []
with open("F:\\Blocks\\yolo\\obj.names", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

#vc = cv2.VideoCapture("demo.mp4")

#net = cv2.dnn.readNet("F:\\Blocks\\yolo\\yolov4-tiny_best.weights", "F:\\Blocks\\yolo\\yolov4-tiny.cfg")
net = cv2.dnn.readNet("F:\\Blocks\\yolo\\yolov4-tiny_4class.weights", "F:\\Blocks\\yolo\\yolov4-tiny4calsss.cfg")
#net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
#net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)

frame = cv2.imread("F:\\Blocks\\dataset\\images\\810.png")

# ringt_frame = frame[:,321:]
# cv2.imshow('right_frame',ringt_frame )
classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
# classes, scores, boxes = model.detect(ringt_frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
box_count = 0
score2=0

# 設定座標點格子
import read_img
read_img.plot_right(frame)
# 中心座標 
xy1 = (225, 225)
xy2 = (225, 300)
xy3 = (225, 375)
xy4 = (225, 450)
xy5 = (160, 225)
xy6 = (160, 300)
xy7 = (160, 375)
xy8 = (160, 450)
xy9 = (100, 225)
xy10 = (100, 300)
xy11 = (100, 375)
xy12 = (100, 450)
xy13 = (40, 225)
xy14 = (40, 300)
xy15 = (40, 375)
xy16 = (40, 450)
lxy1 = (360, 225)
lxy2 = (360, 300)
lxy3 = (360, 370)
lxy4 = (360, 450)
lxy5 = (420, 225)
lxy6 = (420, 300)
lxy7 = (420, 375)
lxy8 = (420, 450)
lxy9 = (480, 225)
lxy10 = (480, 300)
lxy11 = (480, 375)
lxy12 = (480, 450)
lxy13 = (540, 225)
lxy14 = (540, 300)
lxy15 = (540, 375)
lxy16 = (540, 450)
left_sq_x,left_sq_y,left_sq_w,left_sq_h = 320,175,235,310
ringh_sq_x, ringh_sq_y, ringh_sq_w, ringh_sq_h = 10,155,270,330 

# 語音包
import pyttsx3
def Txt2Voice(text):
    
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# 設置模式 : 
print('=============================')
print('\n 積木復健系統模式選擇 ')
print( '\n 1.簡單放置積木  ')
print( '\n 2.放置積木到特定位置  ')
print( '\n 3.特定積木放特定位置  ')
print('=============================')
#Txt2Voice('請輸入模式代號') #語音

mode = input('請輸入模式代號 : ')

def rand_No():
    rnum =np.random.randint(1,16,1)
    print("rnum: ", rnum[0])
    return rnum[0]

def rand_cNo():
    cnum =np.random.randint(1,16,1)
    print("cnum: ", cnum[0])
    return cnum[0]
def mode1(x,y,w,h):
    position_num1= []
    if ((x<xy1[0]<x+w) and (y<xy1[1]<y+h) ):
        #print('x: ',x, ' x+w: ',w+x)
        #print('y: ',y, ' y+h: ',y+h)
        #print('第 1 格 偵測到 ')
        position_num1.append('1')
    elif ((x<xy2[0]<x+w) and (y<xy2[1]<y+h) ):
        #print('x: ',x, ' x+w: ',w+x)
        #print('y: ',y, ' y+h: ',y+h)
        #print('第 2 格 偵測到 ')
        position_num1.append('2')
    elif ((x<xy3[0]<x+w) and (y<xy3[1]<y+h) ):
        #print('x: ',x, ' x+w: ',w+x)
        #print('y: ',y, ' y+h: ',y+h)
        #print('第 3 格 偵測到 ')
        position_num1.append('3')
    elif ((x<xy4[0]<x+w) and (y<xy4[1]<y+h) ):
        #print('x: ',x, ' x+w: ',w+x)
        #print('y: ',y, ' y+h: ',y+h)
        #print('第 4 格 偵測到 ')
        position_num1.append('4')
    elif ((x<xy5[0]<x+w) and (y<xy5[1]<y+h) ):
        #print('x: ',x, ' x+w: ',w+x)
        #print('y: ',y, ' y+h: ',y+h)
        #print('第 5 格 偵測到 ')
        position_num1.append('5')
    elif ((x<xy6[0]<x+w) and (y<xy6[1]<y+h) ):
        #print('x: ',x, ' x+w: ',w+x)
        #print('y: ',y, ' y+h: ',y+h)
        #print('第 6 格 偵測到 ')
        position_num1.append('6')
    elif ((x<xy7[0]<x+w) and (y<xy7[1]<y+h) ):
        #print('x: ',x, ' x+w: ',w+x)
        #print('y: ',y, ' y+h: ',y+h)
        #print('第 7 格 偵測到 ')
        position_num1.append('7')
    elif ((x<xy8[0]<x+w) and (y<xy8[1]<y+h) ):
        #print('x: ',x, ' x+w: ',w+x)
        #print('y: ',y, ' y+h: ',y+h)
        #print('第 8 格 偵測到 ')
        position_num1.append('8')
    elif ((x<xy9[0]<x+w) and (y<xy9[1]<y+h) ):
        #print('x: ',x, ' x+w: ',w+x)
        #print('y: ',y, ' y+h: ',y+h)
        #print('第 9 格 偵測到 ')
        position_num1.append('9')
    elif ((x<xy10[0]<x+w) and (y<xy10[1]<y+h) ):
        #print('x: ',x, ' x+w: ',w+x)
        #print('y: ',y, ' y+h: ',y+h)
        #print('第 10 格 偵測到 ')
        position_num1.append('10')
    elif ((x<xy11[0]<x+w) and (y<xy11[1]<y+h) ):
        #print('x: ',x, ' x+w: ',w+x)
        #print('y: ',y, ' y+h: ',y+h)
        #print('第 11 格 偵測到 ')
        position_num1.append('11')
    elif ((x<xy12[0]<x+w) and (y<xy12[1]<y+h) ):
        #print('x: ',x, ' x+w: ',w+x)
        #print('y: ',y, ' y+h: ',y+h)
        #print('第 12 格 偵測到 ')
        position_num1.append('12')
    elif ((x<xy13[0]<x+w) and (y<xy13[1]<y+h) ):
        #print('x: ',x, ' x+w: ',w+x)
        #print('y: ',y, ' y+h: ',y+h)
        #print('第 13 格 偵測到 ')
        position_num1.append('13')
    elif ((x<xy14[0]<x+w) and (y<xy14[1]<y+h) ):
        #print('x: ',x, ' x+w: ',w+x)
        #print('y: ',y, ' y+h: ',y+h)
        #print('第 14 格 偵測到 ')
        position_num1.append('14')
    elif ((x<xy15[0]<x+w) and (y<xy15[1]<y+h) ):
        #print('x: ',x, ' x+w: ',w+x)
        #print('y: ',y, ' y+h: ',y+h)
        #print('第 15 格 偵測到 ')
        position_num1.append('15')
    elif ((x<xy16[0]<x+w) and (y<xy16[1]<y+h) ):
        # print('x: ',x, ' x+w: ',w+x)
        # print('y: ',y, ' y+h: ',y+h)
        #print('第 16 格 偵測到 ')
        position_num1.append('16')
    else:
        return None
    return position_num1[0]
    
def mode2(nonum): #x,y,w,h
    #rnum =np.random.randint(1,16,1)
    #print("rnum: ", rnum[0])
    if nonum==1:
        read_img.no1cy(frame)
        print('請將積木擺放在 No. 1 位置上')
        #if ((x<xy1[0]<x+w) and (y<xy1[1]<y+h) ):
            #print('第 1 格 偵測到 ')
        #else:
            #print('沒有放正確位置')
    elif nonum==2:
        read_img.no2cy(frame)
        print('請將積木擺放在 No. 2 位置上')
        #if ((x<xy2[0]<x+w) and (y<xy2[1]<y+h) ):
            #print('第 2 格 偵測到 ')
        #else:
            #print('沒有放正確位置')
    elif nonum==3:
        read_img.no3cy(frame)
        print('請將積木擺放在 No. 3 位置上')
        #if ((x<xy3[0]<x+w) and (y<xy3[1]<y+h) ):
            #print('第 3 格 偵測到 ')
        #else:
            #print('沒有放正確位置')
    elif nonum==4:
        read_img.no4cy(frame)
        print('請將積木擺放在 No. 4 位置上')
    elif nonum==4:
        read_img.no4cy(frame)
        print('請將積木擺放在 No. 4 位置上')
    elif nonum==5:
        read_img.no5cy(frame)
        print('請將積木擺放在 No. 5 位置上')
    elif nonum==6:
        read_img.no6cy(frame)
        print('請將積木擺放在 No. 6 位置上')
    elif nonum==7:
        read_img.no7cy(frame)
        print('請將積木擺放在 No. 7 位置上')
    elif nonum==8:
        read_img.no8cy(frame)
        print('請將積木擺放在 No. 8 位置上')
    elif nonum==9:
        read_img.no9cy(frame)
        print('請將積木擺放在 No. 9 位置上')
    elif nonum==10:
        read_img.no10cy(frame)
        print('請將積木擺放在 No. 10 位置上')
    elif nonum==11:
        read_img.no11cy(frame)
        print('請將積木擺放在 No. 11 位置上')
    elif nonum==12:
        read_img.no12cy(frame)
        print('請將積木擺放在 No. 12 位置上')
    elif nonum==13:
        read_img.no13cy(frame)
        print('請將積木擺放在 No. 13 位置上')
    elif nonum==14:
        read_img.no14cy(frame)
        print('請將積木擺放在 No. 14 位置上')
    elif nonum==15:
        read_img.no15cy(frame)
        print('請將積木擺放在 No. 15 位置上')
    elif nonum==16:
        read_img.no16cy(frame)
        print('請將積木擺放在 No. 16 位置上')

def mode2_1(nonum):
    if nonum==1:
        read_img.lo1cy(frame)
        print('請將積木擺放在 No. 1 位置上')
    elif nonum==2:
        read_img.lo2cy(frame)
        print('請將積木擺放在 No. 2 位置上')
    elif nonum==3:
        read_img.lo3cy(frame)
        print('請將積木擺放在 No. 3 位置上')
    elif nonum==4:
        read_img.lo4cy(frame)
        print('請將積木擺放在 No. 4 位置上')
    elif nonum==4:
        read_img.lo4cy(frame)
        print('請將積木擺放在 No. 4 位置上')
    elif nonum==5:
        read_img.lo5cy(frame)
        print('請將積木擺放在 No. 5 位置上')
    elif nonum==6:
        read_img.lo6cy(frame)
        print('請將積木擺放在 No. 6 位置上')
    elif nonum==7:
        read_img.lo7cy(frame)
        print('請將積木擺放在 No. 7 位置上')
    elif nonum==8:
        read_img.lo8cy(frame)
        print('請將積木擺放在 No. 8 位置上')
    elif nonum==9:
        read_img.lo9cy(frame)
        print('請將積木擺放在 No. 9 位置上')
    elif nonum==10:
        read_img.lo10cy(frame)
        print('請將積木擺放在 No. 10 位置上')
    elif nonum==11:
        read_img.lo11cy(frame)
        print('請將積木擺放在 No. 11 位置上')
    elif nonum==12:
        read_img.lo12cy(frame)
        print('請將積木擺放在 No. 12 位置上')
    elif nonum==13:
        read_img.lo13cy(frame)
        print('請將積木擺放在 No. 13 位置上')
    elif nonum==14:
        read_img.lo14cy(frame)
        print('請將積木擺放在 No. 14 位置上')
    elif nonum==15:
        read_img.lo15cy(frame)
        print('請將積木擺放在 No. 15 位置上')
    elif nonum==16:
        read_img.lo16cy(frame)
        print('請將積木擺放在 No. 16 位置上')

def mode3(cnum):
    if cnum==0:
        print('請將拿取 圖0 積木')
    elif cnum==1:
        print('請將拿取 圖1 積木')
    elif cnum==2:
        print('請將拿取 圖2 積木')
    elif cnum==3:
        print('請將拿取 圖3 積木')
    elif cnum==4:
        print('請將拿取 圖4 積木')
    elif cnum==5:
        print('請將拿取 圖5 積木')
    elif cnum==6:
        print('請將拿取 圖6 積木')
    elif cnum==7:
        print('請將拿取 圖7 積木')
    elif cnum==8:
        print('請將拿取 圖8 積木')
    elif cnum==9:
        print('請將拿取 圖9 積木')
    elif cnum==10:
        print('請將拿取 透圖0 積木')
    elif cnum==11:
        print('請將拿取 透圖橫放3 積木')
    elif cnum==12:
        print('請將拿取 黃圖 積木')
    elif cnum==13:
        print('請將拿取 紅圖 積木')
    elif cnum==14:
        print('請將拿取 綠圖 積木')
    elif cnum==15:
        print('請將拿取 藍圖 積木')
    else:
        print('Error')
def mode1_2(x,y,w,h): #右
    position_num1= []
    print('ringh_sq_x',ringh_sq_x+ringh_sq_w ,' (x+w)' ,(x+w),'(y+h)//2 ', (y+h),'ringh_sq_y ',ringh_sq_y+ringh_sq_h)
    if ((ringh_sq_x<(x+w)<ringh_sq_x+ringh_sq_w) and (ringh_sq_y<(y+h)<ringh_sq_y+ringh_sq_h) ):
        position_num1.append(1)
    else:
        position_num1.append(0)
    return position_num1

def mode1_3(x,y,w,h): #左
    position_num1= []
    if ((left_sq_x<(x+w)<left_sq_x+ringh_sq_w) and (left_sq_y<(y+h)<left_sq_y+left_sq_h) ):
        position_num1.append(1)
    else:
        position_num1.append(0)
    return position_num1

def yolo_dec1(classes, scores, boxes,box_count,mode_1_1,score2 ):
    for (classid, score, box) in zip(classes, scores, boxes):
        x, y, w, h = box
        #if x - 31 < 0:
            #x = 31
        #if y - 18 < 0:
            #y = 18
        #if classid==0:
            #cut_img = frame[y - 20: y + h + 90, x - 10: x + w + 10]
        color = COLORS[int(classid) % len(COLORS)]
        box_count +=1 # 第幾位
        #print('id',box_count)
        label = "%s : %f" % (class_names[classid], score)
        cv2.rectangle(frame, box, color, 2)    #frame 
        title = 'No. %d'%(box_count)
        cv2.putText(frame, title, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)
        '''
        # 模式一
        position_num=mode1(x,y,w,h)
        # print('po: ',position_num[0] )
        read_img.plot_cir(frame)
        # for k in range(len(position_num1)):
        print("偵測到 No. %s 格有積木 "%(position_num))
        cv2.putText(frame, "Detected BOX in No.  %s  "%(str(position_num)), (40,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        '''
        # 模式一
        #position_num=mode1(x,y,w,h)
        if mode_1_1 == '1':
            position_num=mode1_2(x,y,w,h)
            if position_num[0]>0:
                #Txt2Voice('右邊棋盤有偵測到')
                score2 +=1
            ca = position_num[0]>0
            print('右邊棋盤是否有偵測到: ', ca)
            
            cv2.putText(frame, "Detected BOX in Right  %s  "%(str(ca)), (40,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        elif mode_1_1== '2':
            position_num=mode1_3(x,y,w,h)
            if position_num[0]>0:
                score2 +=1
            ca = position_num[0]>0
            print('左邊棋盤是否有偵測到: ', ca)
            cv2.putText(frame, "Detected BOX in Left  %s  "%(str(position_num)), (40,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        #print("偵測到 No. %s 格有積木 "%(position_num))
        #cv2.putText(frame, "Detected BOX in No.  %s  "%(str(position_num)), (40,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        if position_num[0] != None:
            flag=True
    # Txt2Voice('偵測到 %s 個'%(box_count)) # 語音
    return frame,flag,box_count,score2

def yolo_dec2(classes, scores, boxes,box_count,nonum ,mode_1_1):
    for (classid, score, box) in zip(classes, scores, boxes):
        x, y, w, h = box
        if x - 31 < 0:
            x = 31
        if y - 18 < 0:
            y = 18
        #if classid==0:
            #cut_img = frame[y - 20: y + h + 90, x - 10: x + w + 10]
        color = COLORS[int(classid) % len(COLORS)]
        box_count +=1 # 第幾位
        #print('id',box_count)
        label = "%s : %f" % (class_names[classid], score)
        cv2.rectangle(frame, box, color, 2)    #frame 
        title = 'No. %d'%(box_count)
        cv2.putText(frame, title, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)

        flag = False
        print('nonum= ',nonum)
        if mode_1_1 =='2':
            print('mode2')
            if nonum==1:
                if ((x<lxy1[0]<x+w) and (y<lxy1[1]<y+h) ):
                    print('第 1 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(lxy1)
                    print(x,x+w,y,y+h)
            elif nonum==2:
                
                if ((x<lxy2[0]<x+w) and (y<lxy2[1]<y+h) ):
                    print('第 2 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(lxy2)
                    print(x,x+w,y,y+h)
            elif nonum==3:
                if ((x<lxy3[0]<x+w) and (y<xly3[1]<y+h) ):
                    print('第 3 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(lxy3)
                    print(x,x+w,y,y+h)
            elif nonum==4:
                
                if ((x<lxy4[0]<x+w) and (y<lxy4[1]<y+h) ):
                    print('第 4 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(lxy4)
                    print(x,x+w,y,y+h)
            elif nonum==5:
                
                if ((x<lxy5[0]<x+w) and (y<lxy5[1]<y+h) ):
                    print('第 5 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(lxy5)
                    print(x,x+w,y,y+h)
            elif nonum==6:
                
                if ((x<lxy6[0]<x+w) and (y<lxy6[1]<y+h) ):
                    print('第 6 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(lxy4)
                    print(x,x+w,y,y+h)
            elif nonum==7:
                
                if ((x<lxy7[0]<x+w) and (y<lxy7[1]<y+h) ):
                    print('第 7 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(lxy7)
                    print(x,x+w,y,y+h)
            elif nonum==8:
                
                if ((x<lxy8[0]<x+w) and (y<lxy8[1]<y+h) ):
                    print('第 8 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(lxy8)
                    print(x,x+w,y,y+h)
            elif nonum==9:
                
                if ((x<lxy9[0]<x+w) and (y<lxy9[1]<y+h) ):
                    print('第 9 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(lxy9)
                    print(x,x+w,y,y+h)
            elif nonum==10:
                
                if ((x<lxy10[0]<x+w) and (y<lxy10[1]<y+h) ):
                    print('第 10 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(lxy10)
                    print(x,x+w,y,y+h)
            elif nonum==11:
                
                if ((x<lxy11[0]<x+w) and (y<lxy11[1]<y+h) ):
                    print('第 11 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(lxy11)
                    print(x,x+w,y,y+h)
            elif nonum==12:
                
                if ((x<lxy12[0]<x+w) and (y<lxy12[1]<y+h) ):
                    print('第 12 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(lxy12)
                    print(x,x+w,y,y+h)
            elif nonum==13:
                
                if ((x<lxy13[0]<x+w) and (y<lxy13[1]<y+h) ):
                    print('第 13 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(lxy13)
                    print(x,x+w,y,y+h)
            elif nonum==14:
                
                if ((x<lxy14[0]<x+w) and (y<lxy14[1]<y+h) ):
                    print('第 14 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(lxy14)
                    print(x,x+w,y,y+h)
            elif nonum==15:
                
                if ((x<lxy15[0]<x+w) and (y<lxy15[1]<y+h) ):
                    print('第 15 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(lxy15)
                    print(x,x+w,y,y+h)
            elif nonum==16:
                
                if ((x<lxy16[0]<x+w) and (y<lxy16[1]<y+h) ):
                    print('第 16 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(lxy16)
                    print(x,x+w,y,y+h)
        if mode_1_1 =='1':
            print('mode1')
            if nonum==1:
                if ((x<xy1[0]<x+w) and (y<xy1[1]<y+h) ):
                    print('第 1 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(xy1)
                    print(x,x+w,y,y+h)
            elif nonum==2:
                
                if ((x<xy2[0]<x+w) and (y<xy2[1]<y+h) ):
                    print('第 2 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(xy2)
                    print(x,x+w,y,y+h)
            elif nonum==3:
                if ((x<xy3[0]<x+w) and (y<xy3[1]<y+h) ):
                    print('第 3 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(xy3)
                    print(x,x+w,y,y+h)
            elif nonum==4:
                
                if ((x<xy4[0]<x+w) and (y<xy4[1]<y+h) ):
                    print('第 4 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(xy4)
                    print(x,x+w,y,y+h)
            elif nonum==5:
                
                if ((x<xy5[0]<x+w) and (y<xy5[1]<y+h) ):
                    print('第 5 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(xy5)
                    print(x,x+w,y,y+h)
            elif nonum==6:
                
                if ((x<xy6[0]<x+w) and (y<xy6[1]<y+h) ):
                    print('第 6 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(xy4)
                    print(x,x+w,y,y+h)
            elif nonum==7:
                
                if ((x<xy7[0]<x+w) and (y<xy7[1]<y+h) ):
                    print('第 7 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(xy7)
                    print(x,x+w,y,y+h)
            elif nonum==8:
                
                if ((x<xy8[0]<x+w) and (y<xy8[1]<y+h) ):
                    print('第 8 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(xy8)
                    print(x,x+w,y,y+h)
            elif nonum==9:
                
                if ((x<xy9[0]<x+w) and (y<xy9[1]<y+h) ):
                    print('第 9 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(xy9)
                    print(x,x+w,y,y+h)
            elif nonum==10:
                
                if ((x<xy10[0]<x+w) and (y<xy10[1]<y+h) ):
                    print('第 10 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(xy10)
                    print(x,x+w,y,y+h)
            elif nonum==11:
                
                if ((x<xy11[0]<x+w) and (y<xy11[1]<y+h) ):
                    print('第 11 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(xy11)
                    print(x,x+w,y,y+h)
            elif nonum==12:
                
                if ((x<xy12[0]<x+w) and (y<xy12[1]<y+h) ):
                    print('第 12 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(xy12)
                    print(x,x+w,y,y+h)
            elif nonum==13:
                
                if ((x<xy13[0]<x+w) and (y<xy13[1]<y+h) ):
                    print('第 13 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(xy13)
                    print(x,x+w,y,y+h)
            elif nonum==14:
                
                if ((x<xy14[0]<x+w) and (y<xy14[1]<y+h) ):
                    print('第 14 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(xy14)
                    print(x,x+w,y,y+h)
            elif nonum==15:
                
                if ((x<xy15[0]<x+w) and (y<xy15[1]<y+h) ):
                    print('第 15 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(xy15)
                    print(x,x+w,y,y+h)
            elif nonum==16:
                
                if ((x<xy16[0]<x+w) and (y<xy16[1]<y+h) ):
                    print('第 16 格 偵測到 ')
                    flag = True
                else:
                    #print('沒有放正確位置')
                    print(xy16)
                    print(x,x+w,y,y+h)
    return flag
def yolo_dec3(classes, scores, boxes,box_count,nonum,cnum ):
    for (classid, score, box) in zip(classes, scores, boxes):
        x, y, w, h = box
        if x - 31 < 0:
            x = 31
        if y - 18 < 0:
            y = 18
        #if classid==0:
            #cut_img = frame[y - 20: y + h + 90, x - 10: x + w + 10]
        color = COLORS[int(classid) % len(COLORS)]
        box_count +=1 # 第幾位
        #print('id',box_count)
        label = "%s : %f" % (class_names[classid], score)
        cv2.rectangle(frame, box, color, 2)    #frame 
        title = 'No. %d'%(box_count)
        cv2.putText(frame, title, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)

        flag = False
        # 如果規定class = 拿取box的class
        if cnum==classid:
            print("id:", classid,' cnum: ',cnum)
            po=mode1(x,y,w,h)
            #print('po: ',type(po), po, ' nonum: ',type(str(nonum)),nonum)
            if po == str(nonum):
                print('成功將 %s 放到 No. %s 位置'%(classid,nonum))
                flag=True
                return flag,frame
            else:
                print('失敗')
    return flag,frame
#process programe
nonum=rand_No()
cnum=rand_cNo()
if mode =='1':
    #try:
    print('\n 請選擇積木放置位置 : ')
    print('\n 右邊棋盤選擇 : 1 ')
    print('\n 左邊棋盤選擇 : 2 ')
    text = '請選擇積木放置位置'
    Txt2Voice(text) #語音
    mode_1_1 = str(input('棋盤放置位置: '))
    frame12=frame.copy()
    # read_img.plot_cir(frame12)
    read_img.plot_right(frame12)
    
    classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    box_count =0
    frame,flag,box_count,score2=yolo_dec1(classes, scores, boxes,box_count ,mode_1_1,score2)
    #if flag==True:
        #score+=1
    # score = box_count
    cv2.putText(frame, "Score is  %s  "%(str(score2)), (32,65), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1, 1)
    print('目前得分: ',score2)
            
           
    #except:
        #pass

######## 差左邊 ###############
elif mode =='2': 
    print('\n 請選擇積木放置位置 : ')
    print('\n 右邊棋盤選擇 : 1 ')
    print('\n 左邊棋盤選擇 : 2 ')
    text = '請選擇積木放置位置'
    #Txt2Voice(text) #語音
    mode_1_1 = str(input('棋盤放置位置: '))
    start_time = time.time()
    classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    box_count =0
    #rnum =np.random.randint(1,4,1)
    #print("rnum: ", rnum[0])
    if mode_1_1 =='1':
        mode2(nonum)
    else:
        mode2_1(nonum)
    flag2 = False
    flag2=yolo_dec2(classes, scores, boxes,box_count,nonum=nonum ,mode_1_1=mode_1_1)
    cv2.putText(frame, "Score is  %s  "%(str(score2)), (32,65), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1, 1)
    print('目前得分: ',score2)
elif mode == '3':

    classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    start_time=time.time()
    #rnum =np.random.randint(1,16,1)
    #print("rnum: ", rnum[0])
    mode2(nonum)
    #cnum =np.random.randint(1,16,1)
    #print("cnum: ", cnum[0])
    mode3(cnum)
    flag2,frame=yolo_dec3(classes, scores, boxes,box_count,nonum=nonum,cnum=cnum )
    if flag2 == True:
        score2+=1
        nonum=rand_No()
        cnum=rand_cNo()
    print('目前得分: ',score2)
    end_time = time.time()
    alltime=(end_time-start_time)* 1
    print(alltime)
    if alltime>60:
        time_flag=False    



print('共偵測到 %d 個 '%(len(boxes)))
box_tatle = len(boxes)
'''

# 抓取一個一個位置/執行mode
try:
    for (classid, score, box) in zip(classes, scores, boxes):
        x, y, w, h = box
        if x - 31 < 0:
            x = 31
        if y - 18 < 0:
            y = 18
        #if classid==0:
            #cut_img = frame[y - 20: y + h + 90, x - 10: x + w + 10]
        color = COLORS[int(classid) % len(COLORS)]
        box_count +=1 # 第幾位
        print('id',classid)
        label = "%s : %f" % (class_names[classid], score)
        cv2.rectangle(frame, box, color, 2)    #frame 
        title = 'No. %d'%(box_count)
        #cv2.putText(frame, title, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1) #frame
        cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)
        
        #process programe
        #if mode =='1':
            #position_num=mode1(x,y,w,h)
            #print('po: ',position_num[0] )
            #read_img.plot_cir(frame)
            # for k in range(len(position_num1)):
            #print("偵測到 No. %s 格有積木 "%(position_num))
            #cv2.putText(frame, "Detected BOX in No.  %s  "%(str(position_num)), (40,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    
        #elif mode =='2':
            #position_num1 = mode2(x,y,w,h)
        
            

except:
    pass

'''
end_drawing = time.time()
import imutils
cv2.imshow("detections", imutils.resize(frame, width=840,height=640))
# cv2.imshow('right_frame',ringt_frame )
#cv2.imshow("object", imutils.resize(cut_img, width=200,height=200))
cv2.waitKey(0)
cv2.destroyAllWindows()














