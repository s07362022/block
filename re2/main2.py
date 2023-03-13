from sre_constants import SUCCESS
import cv2
import time
import read_img
import numpy as np
from datetime import datetime
import pandas as pd
CONFIDENCE_THRESHOLD = 0.8
NMS_THRESHOLD = 0.4
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
ISOTIMEFORMAT = '%Hh%Mm%Ss' #ISOTIMEFORMAT
class_names = []
with open("F:\\Blocks\\yolo\\obj.names", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]
import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='0000',
                                    database='block')
cursor = connection.cursor()


#net = cv2.dnn.readNet("F:\\Blocks\\yolo\\yolov4-tiny_best.weights", "F:\\Blocks\\yolo\\yolov4-tiny.cfg")
net = cv2.dnn.readNet("F:\\Blocks\\yolo\\yolov7-tiny_last.weights", "F:\\Blocks\\yolo\\yolov7-tiny.cfg")
#net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
#net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)

model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(640, 640), scale=1/255, swapRB=True)
rand_list = []

# def cut_img(image, classes, confs, boxes):
#     cut_img_list = []
#     for (classid, conf, box) in zip(classes, confs, boxes):
#         x, y, w, h = box
#         if x - 20 < 0:
#             x = 21
#         if y - 20 < 0:
#             y = 21
#         #cut_img = image[y - 30:y + h + 30, x - 18:x + w + 25]
#         cut_img = image[y - 20: y + h + 30, x - 10: x + w + 10]
#         cut_img_list.append(cut_img)
#     return cut_img_list[0]

def Iox(box1,box2):
    xmin1,ymin1,xmax1,ymax1=box1 
    xmin2,ymin2,xmax2,ymax2=box2 
    x_overlap = max(0, min(xmax1,xmax2)-max(xmin1,xmin2))
    #print(min(xmax1,xmax2)-max(xmin1,xmin2))
    y_overlap = max(0,abs(min(ymax1,ymax2)-max(ymin1,ymin2)))
    #print(min(ymax1,ymax2)-max(ymin1,ymin2))
    intersection = x_overlap*y_overlap
    #union = (xmax1-xmin1)*(ymax1-ymin1)+(xmax2-xmin2)*(ymax2-ymin2) - intersection
    union= abs((xmax2-xmin2)*(ymax2-ymin2))
    print("IOU: ",float(intersection) /union)
    return float(intersection) /union

# 中心座標
left_sq_x,left_sq_y,left_sq_w,left_sq_h = 320,175,235,310
ringh_sq_x, ringh_sq_y, ringh_sq_w, ringh_sq_h = 10,155,270,330
xy4 = (225, 225) # 右盤
xy8 = (225, 300) # 右盤
xy12 = (225, 375) # 右盤
xy16 = (225, 450) # 右盤
xy3 = (160, 225) #
xy7 = (160, 300)
xy11 = (160, 375)
xy15 = (160, 450)
xy2 = (100, 225)
xy6 = (100, 300)
xy10 = (100, 375)
xy14 = (100, 450)
xy1 = (40, 225) # 右盤左上一 #13
xy5 = (40, 300)
xy9 = (40, 375)
xy13 = (40, 450)
lxy1 = (360, 225)
lxy5 = (360, 300)
lxy9 = (360, 375)
lxy13 = (360, 450)
lxy2 = (420, 225)
lxy6 = (420, 300)
lxy10 = (420, 375)
lxy14 = (420, 450)
lxy3 = (480, 225)
lxy7 = (480, 300)
lxy11 = (480, 375)
lxy15 = (480, 450)
lxy4 = (540, 225)
lxy8 = (540, 300)
lxy12 = (540, 375)
lxy16 = (540, 450)
ringh_sq_xy1=(10,155) #右邊的棋盤左上角
ringh_sq_xy2=(10,456) #右邊的棋盤左下角


# 語音包
import pyttsx3
def Txt2Voice(text):
    
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


############################ 幹12/6 ################
def mode11(x,y,w,h,position_num):   # 左手偵測 IOU 面積範圍

    box1 = [x,y,x+w,y+h]

    if ((x<lxy1[0]<x+w) and (y<lxy1[1]<y+h) ):
        box2=[lxy1[0],lxy1[1],lxy1[0]+20,lxy1[1]+20]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num.append('1')
        return position_num
    if ((x<lxy2[0]<x+w) and (y<lxy2[1]<y+h) ):
        box2=[lxy2[0],lxy2[1],lxy2[0]+25,lxy2[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num.append('2')
        return position_num
    if ((x<lxy3[0]<x+w) and (y<lxy3[1]<y+h) ):
        box2=[lxy3[0],lxy3[1],lxy3[0]+25,lxy3[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num.append('3')
        return position_num
    if ((x<lxy4[0]<x+w) and (y<lxy4[1]<y+h) ):
        box2=[lxy4[0],lxy4[1],lxy4[0]+25,lxy4[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            print('第 4 格 偵測到 ')
            position_num.append('4')
        return position_num
    if ((x<lxy5[0]<x+w) and (y<lxy5[1]<y+h) ):
        box2=[lxy5[0],lxy5[1],lxy5[0]+25,lxy5[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            print('第 5 格 偵測到 ')
            position_num.append('5')
        return position_num
    if ((x<lxy6[0]<x+w) and (y<lxy6[1]<y+h) ):
        box2=[lxy6[0],lxy6[1],lxy6[0]+25,lxy6[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            print('第 6 格 偵測到 ')
            position_num.append('6')
            print(position_num)
        return position_num
    if ((x<lxy7[0]<x+w) and (y<lxy7[1]<y+h) ):
        box2=[lxy7[0],lxy7[1],lxy7[0]+25,lxy7[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            print('第 7 格 偵測到 ')
            position_num.append('7')
            print(position_num)
            return position_num
        return position_num
    if ((x<lxy8[0]<x+w) and (y<lxy8[1]<y+h) ):
        box2=[lxy8[0],lxy8[1],lxy8[0]+25,lxy8[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            print('第 8 格 偵測到 ')
            position_num.append('8')
            print(position_num)
        return position_num
    if ((x<lxy9[0]<x+w) and (y<lxy9[1]<y+h) ):
        box2=[lxy9[0],lxy9[1],lxy9[0]+25,lxy9[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            print('第 9 格 偵測到 ')
            position_num.append('9')
            print(position_num)
        return position_num
    if ((x<lxy10[0]<x+w) and (y<lxy10[1]<y+h) ):
        box2=[lxy10[0],lxy10[1],lxy10[0]+25,lxy10[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            print('第 10 格 偵測到 ')
            position_num.append('10')
            print(position_num)
        return position_num
    if ((x<lxy11[0]<x+w) and (y<lxy11[1]<y+h) ):
        box2=[lxy11[0],lxy11[1],lxy11[0]+25,lxy11[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            print('第 11 格 偵測到 ')
            position_num.append('11')
            print(position_num)
        return position_num
    if ((x<lxy12[0]<x+w) and (y<lxy12[1]<y+h) ):
        box2=[lxy12[0],lxy12[1],lxy12[0]+25,lxy12[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            print('第 12 格 偵測到 ')
            position_num.append('12')
            print(position_num)
        return position_num
    if ((x<lxy13[0]<x+w) and (y<lxy13[1]<y+h) ):
        box2=[lxy13[0],lxy13[1],lxy13[0]+25,lxy13[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            print('第 13 格 偵測到 ')
            position_num.append('13')
            print(position_num)
        return position_num
    if ((x<lxy14[0]<x+w) and (y<lxy14[1]<y+h) ):
        box2=[lxy14[0],lxy14[1],lxy14[0]+25,lxy14[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            print('第 14 格 偵測到 ')
            position_num.append('14')
            print(position_num)
        return position_num
    if ((x<lxy15[0]<x+w) and (y<lxy15[1]<y+h) ):
        box2=[lxy15[0],lxy15[1],lxy15[0]+25,lxy15[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            print('第 15 格 偵測到 ')
            position_num.append('15')
            print(position_num)
        return position_num
    if ((x<lxy16[0]<x+w) and (y<lxy16[1]<y+h) ):
        box2=[lxy16[0],lxy16[1],lxy16[0]+25,lxy16[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            print('第 16 格 偵測到 ')
            position_num.append('16')
            print(position_num)
        return position_num
    return position_num

def mode1(x,y,w,h,position_num1):   # 右手偵測 IOU 面積範圍
    
    box1 = [x,y,x+w,y+h]
    if ((x<xy1[0]<x+w) and (y<xy1[1]<y+h) ):
        box2=[xy1[0],xy1[1],xy1[0]+25,xy1[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num1.append('1')
    elif ((x<xy2[0]<x+w) and (y<xy2[1]<y+h) ):
        box2=[xy2[0],xy2[1],xy2[0]+25,xy2[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num1.append('2')
    elif ((x<xy3[0]<x+w) and (y<xy3[1]<y+h) ):
        box2=[xy3[0],xy3[1],xy3[0]+25,xy3[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num1.append('3')
    elif ((x<xy4[0]<x+w) and (y<xy4[1]<y+h) ):
        box2=[xy4[0],xy4[1],xy4[0]+25,xy4[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num1.append('4')
    elif ((x<xy5[0]<x+w) and (y<xy5[1]<y+h) ):
        box2=[xy5[0],xy5[1],xy5[0]+25,xy5[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num1.append('5')
    elif ((x<xy6[0]<x+w) and (y<xy6[1]<y+h) ):
        box2=[xy6[0],xy6[1],xy6[0]+25,xy6[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num1.append('6')
    elif ((x<xy7[0]<x+w) and (y<xy7[1]<y+h) ):
        box2=[xy7[0],xy7[1],xy7[0]+25,xy7[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num1.append('7')
    elif ((x<xy8[0]<x+w) and (y<xy8[1]<y+h) ):
        box2=[xy8[0],xy8[1],xy8[0]+25,xy8[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num1.append('8')
    elif ((x<xy9[0]<x+w) and (y<xy9[1]<y+h) ):
        box2=[xy9[0],xy9[1],xy9[0]+25,xy9[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num1.append('9')
    elif ((x<xy10[0]<x+w) and (y<xy10[1]<y+h) ):
        box2=[xy10[0],xy10[1],xy10[0]+25,xy10[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num1.append('10')
    elif ((x<xy11[0]<x+w) and (y<xy11[1]<y+h) ):
        box2=[xy11[0],xy11[1],xy11[0]+25,xy11[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num1.append('11')
    elif ((x<xy12[0]<x+w) and (y<xy12[1]<y+h) ):
        box2=[xy12[0],xy12[1],xy12[0]+25,xy12[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num1.append('12')
    elif ((x<xy13[0]<x+w) and (y<xy13[1]<y+h) ):
        box2=[xy13[0],xy13[1],xy13[0]+25,xy13[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num1.append('13')
    elif ((x<xy14[0]<x+w) and (y<xy14[1]<y+h) ):
        box2=[xy14[0],xy14[1],xy14[0]+25,xy14[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num1.append('14')
    elif ((x<xy15[0]<x+w) and (y<xy15[1]<y+h) ):
        box2=[xy15[0],xy15[1],xy15[0]+25,xy15[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num1.append('15')
    elif ((x<xy16[0]<x+w) and (y<xy16[1]<y+h) ):
        box2=[xy16[0],xy16[1],xy16[0]+25,xy16[1]+25]
        iou_s = Iox(box1,box2)
        if iou_s >0.5:
            position_num1.append('16')
    return position_num1

def mode3_to_po2(x,y,w,h,anotherpo):   #在模式三中 右手"偵測"特定位置到 "左邊特定位置" 
    position_num3= anotherpo
    
    #print("判斷", x,x+w,y,y+h)
    #print(xy5[0],xy5[1])
    if ((x<xy1[0]<x+w) and (y<xy1[1]<y+h) ):
        position_num3.append('1')
    if ((x<xy2[0]<x+w) and (y<xy2[1]<y+h) ): 
        position_num3.append('2')
    if((x<xy3[0]<x+w) and (y<xy3[1]<y+h) ):
        position_num3.append('3')
    if ((x<xy4[0]<x+w) and (y<xy4[1]<y+h) ):
        position_num3.append('4')
    if ((x<xy5[0]<x+w) and (y<xy5[1]<y+h) ):
        position_num3.append('5')
    if ((x<xy6[0]<x+w) and (y<xy6[1]<y+h) ):
        position_num3.append('6')
    if ((x<xy7[0]<x+w) and (y<xy7[1]<y+h) ):
        position_num3.append('7')
    if ((x<xy8[0]<x+w) and (y<xy8[1]<y+h) ):
        position_num3.append('8')
    if ((x<xy9[0]<x+w) and (y<xy9[1]<y+h) ):
        position_num3.append('9')
    if ((x<xy10[0]<x+w) and (y<xy10[1]<y+h) ):
        position_num3.append('10')
    if ((x<xy11[0]<x+w) and (y<xy11[1]<y+h) ):
        position_num3.append('11')
    if ((x<xy12[0]<x+w) and (y<xy12[1]<y+h) ):
        position_num3.append('12')
    if ((x<xy13[0]<x+w) and (y<xy13[1]<y+h) ):
        position_num3.append('13')
    if ((x<xy14[0]<x+w) and (y<xy14[1]<y+h) ):
        position_num3.append('14')
    if ((x<xy15[0]<x+w) and (y<xy15[1]<y+h) ):
        position_num3.append('15')
    if ((x<xy16[0]<x+w) and (y<xy16[1]<y+h) ):
        position_num3.append('16')
    print(position_num3)
    return position_num3

def mode3_to_po(x,y,w,h,position_num4):   #在模式三中 左手"偵測"特定位置到 "右邊特定位置" 
    position_num4= position_num4
    x =x -10
    w = w-10
    #print("判斷", x,x+w,y,y+h)
    #print(lxy1[0],lxy1[1])
    if((x<lxy1[0]<x+w) and (y<lxy1[1]<y+h) ):
        position_num4.append('1')
    if ((x<lxy2[0]<x+w) and (y<lxy2[1]<y+h) ): 
        position_num4.append('2')
    if ((x<lxy3[0]<x+w) and (y<lxy3[1]<y+h) ):
        position_num4.append('3')
    if ((x<lxy4[0]<x+w) and (y<lxy4[1]<y+h) ):
        position_num4.append('4')
    if ((x<lxy5[0]<x+w) and (y<lxy5[1]<y+h) ):
        position_num4.append('5')
    if ((x<lxy6[0]<x+w) and (y<lxy6[1]<y+h) ):
        position_num4.append('6')
    if ((x<lxy7[0]<x+w) and (y<lxy7[1]<y+h) ):
        position_num4.append('7')
    if ((x<lxy8[0]<x+w) and (y<lxy8[1]<y+h) ):
        position_num4.append('8')
    if ((x<lxy9[0]<x+w) and (y<lxy9[1]<y+h) ):
        position_num4.append('9')
    if ((x<lxy10[0]<x+w) and (y<lxy10[1]<y+h) ):
        position_num4.append('10')
    if ((x<lxy11[0]<x+w) and (y<lxy11[1]<y+h) ):
        position_num4.append('11')
    if ((x<lxy12[0]<x+w) and (y<lxy12[1]<y+h) ):
        position_num4.append('12')
    if ((x<lxy13[0]<x+w) and (y<lxy13[1]<y+h) ):
        position_num4.append('13')
    if ((x<lxy14[0]<x+w) and (y<lxy14[1]<y+h) ):
        position_num4.append('14')
    if ((x<lxy15[0]<x+w) and (y<lxy15[1]<y+h) ):
        position_num4.append('15')
    if ((x<lxy16[0]<x+w) and (y<lxy16[1]<y+h) ):
        position_num4.append('16')
    return position_num4

def mode1_2(x,y,w,h):
    position_num1= []
    if ((ringh_sq_x<(x+w)<ringh_sq_x+ringh_sq_w) and (ringh_sq_y<(y+h)<ringh_sq_y+ringh_sq_h) ):
        position_num1.append(1)
    else:
        position_num1.append(0)
    return position_num1

def mode1_3(x,y,w,h):
    position_num1= []
    if ((left_sq_x<(x+w)<left_sq_x+ringh_sq_w) and (left_sq_y<(y+h)<left_sq_y+left_sq_h) ):
        position_num1.append(1)
    else:
        position_num1.append(0)
    return position_num1

def mode2(frame12,nonum): #x,y,w,h   #################### 特定位置到特定位置 Change here ################
    #rnum =np.random.randint(1,16,1)
    #print("rnum: ", rnum[0])
    if nonum==1:
        read_img.no1cy(frame12)
        print('請將積木擺放在 No. 1 位置上')
       
    elif nonum==2:
        read_img.no2cy(frame12)
        print('請將積木擺放在 No. 2 位置上')
        
    elif nonum==3:
        read_img.no3cy(frame12)
        print('請將積木擺放在 No. 3 位置上')
        
    elif nonum==4:
        read_img.no4cy(frame12)
        print('請將積木擺放在 No. 4 位置上')
    elif nonum==5:
        read_img.no5cy(frame12)
        print('請將積木擺放在 No. 5 位置上')
    elif nonum==6:
        read_img.no6cy(frame12)
        print('請將積木擺放在 No. 6 位置上')
    elif nonum==7:
        read_img.no7cy(frame12)
        print('請將積木擺放在 No. 7 位置上')
    elif nonum==8:
        read_img.no8cy(frame12)
        print('請將積木擺放在 No. 8 位置上')
    elif nonum==9:
        read_img.no9cy(frame12)
        print('請將積木擺放在 No. 9 位置上')
    elif nonum==10:
        read_img.no10cy(frame12)
        print('請將積木擺放在 No. 10 位置上')
    elif nonum==11:
        read_img.no11cy(frame12)
        print('請將積木擺放在 No. 11 位置上')
    elif nonum==12:
        read_img.no12cy(frame12)
        print('請將積木擺放在 No. 12 位置上')
    elif nonum==13:
        read_img.no13cy(frame12)
        print('請將積木擺放在 No. 13 位置上')
    elif nonum==14:
        read_img.no14cy(frame12)
        print('請將積木擺放在 No. 14 位置上')
    elif nonum==15:
        read_img.no15cy(frame12)
        print('請將積木擺放在 No. 15 位置上')
    elif nonum==16:
        read_img.no16cy(frame12)
        print('請將積木擺放在 No. 16 位置上')
    
def mode2_1(frame,nonum):
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

score2_list  = []
def yolo_dec1(frame,classes, scores, boxes,box_count ,mode_1_1,score2,flag):
    class_list = []
    # score2=0
    print("模式一 被執行------------",type(mode_1_1))
    for (classid, score, box) in zip(classes, scores, boxes):
        x, y, w, h = box
        if x - 31 < 0:
            x = 31
        if y - 18 < 0:
            y = 18

        color = COLORS[int(classid) % len(COLORS)]
        box_count +=1 # 第幾位
        #print('id',box_count)
        label = "%s : %f" % (class_names[classid], score)
        cv2.rectangle(frame, box, color, 2)    #frame 
        title = 'No. %d'%(box_count)
        cv2.putText(frame, title, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)
        class_list.append( classid)
        class_num = np.unique(class_list)
        # 模式一
        score2=int(score2)
        score2init = int(score2)
        #position_num=mode1(x,y,w,h)
        if mode_1_1 == '0':
            print(" mode_1_1 == 0")
            position_num=mode1_2(x,y,w,h)
            if (position_num[0]>0) and (score2<=int(box_count)):
                score2 +=1
    
            ca = position_num[0]>0
            print('右邊棋盤是否有偵測到: ', ca)
            cv2.putText(frame, "Detected BOX in Right  %s  "%(str(position_num)), (40,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
            
        elif mode_1_1== '1':
            print("mode_1_1== 1")
            position_num=mode1_3(x,y,w,h)
            if (position_num[0]>0) and (score2<=box_count):
                score2 +=1
            
            ca = position_num[0]>0
            print('左邊棋盤是否有偵測到: ', ca)
            cv2.putText(frame, "Detected BOX in Left  %s  "%(str(position_num)), (40,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        print("偵測到 No. %s 格有積木 "%(position_num))
        #cv2.putText(frame, "Detected BOX in No.  %s  "%(str(position_num)), (40,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        if position_num[0] != None:
            flag=True
        # if score2init != int(score2):
            # score2_list.append(sc)
    return frame,flag,box_count,score2#len(score2_list)#score2

def yolo_dec2(frame,classes, scores, boxes,box_count,nonum ,mode_1_1,flag,frame12):
    flag = False
    score2=0
    posi = []
    anotherpo=[]
    position_num4=[]
    position_num3=[]
    leavepo=[]
    if mode_1_1 =='0':
        position_num=[]
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

            
            print('nonum= ',nonum)
        
        
            
            box1 = [x,y,x+w,y+h]
            position_num4 = mode3_to_po(x,y,w,h,position_num4) # 偵測左邊棋盤上所有積木是否存在
            anotherpo.extend(position_num4)
            position_num=mode1_2(x,y,w,h)
            if (position_num[0]>0) :
                # haspo = True
                position_num3.append(position_num[0])
            else :
                haspo = False
        hasp = np.where(position_num3 == 1)
        if np.size(hasp) != 0:
            haspo = True
        #read_img.plot_cir(frame12)
        print("anotherpo: ",anotherpo)                         # 偵測到左邊棋盤上的積木
        print("str(nonum)",str(nonum))                         # 我們目標要拿離的積木
        for i in range(1,16):
            if (str(i) not in anotherpo):
                leavepo.append(str(i)) 
        print("leavepo:  " , leavepo)                          # 離開左盤的積木
        
        if ((haspo==True) and (str(nonum) in leavepo) ):
            posi = nonum
            flag = True
            



            ################# 上個版本的_放置特定位置 ##################
            #print(box1)
            # z = 20
            #posi = mode11(x,y,w,h)
            # if nonum==1:
            #     if ((x<xy1[0]<x+w) and (y<xy1[1]<y+h) ):
                    
            #         box2=[xy1[0]-z,xy1[1]-z,xy1[0]+z,xy1[1]+z]
            #         box2x = [xy1[0]-z,xy1[1]-z,40,40]
            #         cv2.rectangle(frame12, box2x, 1, 2)
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 1 格 偵測到 ')
            #             flag = True
            #             posi.append('1')
            # elif nonum==2:
            #     if ((x<xy2[0]<x+w) and (y<xy2[1]<y+h) ):
            #         box2=[xy2[0]-z,xy2[1]-z,xy2[0]+z,xy2[1]+z]
            #         box2x = [xy2[0]-z,xy2[1]-z,40,40]
            #         cv2.rectangle(frame12, box2x, 1, 2)
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 2 格 偵測到 ')
            #             flag = True
            #             posi.append('2')
            # elif nonum==3:
            #     if ((x<xy3[0]<x+w) and (y<xy3[1]<y+h) ):
            #         box2=[xy3[0]-z,xy3[1]-z,xy3[0]+z,xy3[1]+z]
            #         box2x = [xy3[0]-z,xy3[1]-z,40,40]
            #         cv2.rectangle(frame12, box2x, 1, 2)
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 3 格 偵測到 ')
            #             flag = True
            #             posi.append('3')
            # elif nonum==4:
            #     if ((x<xy4[0]<x+w) and (y<xy4[1]<y+h) ):
            #         box2=[xy4[0]-z,xy4[1]-z,xy4[0]+z,xy4[1]+z]
            #         box2x = [xy4[0]-z,xy4[1]-z,40,40]
            #         cv2.rectangle(frame12, box2x, 1, 2)
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 4 格 偵測到 ')
            #             flag = True
            #             posi.append('4')
            # elif nonum==5:
                
            #     if ((x<xy5[0]<x+w) and (y<xy5[1]<y+h) ):
            #         box2=[xy5[0]-z,xy5[1]-z,xy5[0]+z,xy5[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 5 格 偵測到 ')
            #             flag = True
            #             posi.append('5')
            # elif nonum==6:
                
            #     if ((x<xy6[0]<x+w) and (y<xy6[1]<y+h) ):
            #         box2=[xy6[0]-z,xy6[1]-z,xy6[0]+z,xy6[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 6 格 偵測到 ')
            #             flag = True
            #             posi.append('6')
            # elif nonum==7:
                
            #     if ((x<xy7[0]<x+w) and (y<xy7[1]<y+h) ):
            #         box2=[xy7[0]-z,xy7[1]-z,xy7[0]+z,xy7[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 7 格 偵測到 ')
            #             flag = True
            #             posi.append('7')
            # elif nonum==8:
                
            #     if ((x<xy8[0]<x+w) and (y<xy8[1]<y+h) ):
            #         box2=[xy8[0]-z,xy8[1]-z,xy8[0]+z,xy8[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 8 格 偵測到 ')
            #             flag = True
            #             posi.append('8')
            # elif nonum==9:
                
            #     if ((x<xy9[0]<x+w) and (y<xy9[1]<y+h) ):
            #         box2=[xy9[0]-z,xy9[1]-z,xy9[0]+z,xy9[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 9 格 偵測到 ')
            #             flag = True
            #             posi.append('9')
            # elif nonum==10:
                
            #     if ((x<xy10[0]<x+w) and (y<xy10[1]<y+h) ):
            #         box2=[xy10[0]-z,xy10[1]-z,xy10[0]+z,xy10[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 10 格 偵測到 ')
            #             flag = True
            #             posi.append('10')
            # elif nonum==11:
                
            #     if ((x<xy11[0]<x+w) and (y<xy11[1]<y+h) ):
            #         box2=[xy11[0]-z,xy11[1]-z,xy11[0]+z,xy11[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 11 格 偵測到 ')
            #             flag = True
            #             posi.append('11')
            # elif nonum==12:    
            #     if ((x<xy12[0]<x+w) and (y<xy12[1]<y+h) ):
            #         box2=[xy12[0]-z,xy12[1]-z,xy12[0]+z,xy12[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 12 格 偵測到 ')
            #             flag = True
            #             posi.append('12')
            # elif nonum==13:
                
            #     if ((x<xy13[0]<x+w) and (y<xy13[1]<y+h) ):
            #         box2=[xy13[0]-z,xy13[1]-z,xy13[0]+z,xy13[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 13 格 偵測到 ')
            #             flag = True
            #             posi.append('13')
                
            # elif nonum==14:
            #     if ((x<xy14[0]<x+w) and (y<xy14[1]<y+h) ):
            #         box2=[xy14[0]-z,xy14[1]-z,xy14[0]+z,xy14[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 14 格 偵測到 ')
            #             flag = True
            #             posi.append('14')
    
            # elif nonum==15:
                
            #     if ((x<xy15[0]<x+w) and (y<xy15[1]<y+h) ):
            #         box2=[xy15[0]-z,xy15[1]-z,xy15[0]+z,xy15[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 15 格 偵測到 ')
            #             flag = True
            #             posi.append('15')
            # elif nonum==16:
                
            #     if ((x<xy16[0]<x+w) and (y<xy16[1]<y+h) ):
            #         box2=[xy16[0]-z,xy16[1]-z,xy16[0]+z,xy16[1]+z]
            #         iou_s = Iox(box1,box2)
                    
            #         if iou_s >0.5:
            #             print('第 16 格 偵測到 ')
            #             flag = True
            #             posi.append('16')
            ################# 上個版本的_放置特定位置 ##################
            
        if mode_1_1 =='1':
            # box1 = [x,y,x+w,y+h]
            position_num=[]
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

            
            print('nonum= ',nonum)
        
        
            
            box1 = [x,y,x+w,y+h]
            position_num4 = mode3_to_po2(x,y,w,h,position_num4) # 偵測左邊棋盤上所有積木是否存在
            anotherpo.extend(position_num3)
            position_num=mode1_3(x,y,w,h)
            if (position_num[0]>0) :
                # haspo = True
                position_num3.append(position_num[0])
            else :
                haspo = False
        hasp = np.where(position_num3 == 1)
        if np.size(hasp) != 0:
            haspo = True
        #read_img.plot_cir(frame12)
        print("anotherpo: ",anotherpo)                         # 偵測到左邊棋盤上的積木
        print("str(nonum)",str(nonum))                         # 我們目標要拿離的積木
        for i in range(1,16):
            if (str(i) not in anotherpo):
                leavepo.append(str(i)) 
        print("leavepo:  " , leavepo)                          # 離開左盤的積木
        
        if ((haspo==True) and (str(nonum) in leavepo) ):
            posi = nonum
            flag = True

            ################# 上個版本的_放置特定位置 ##################
            # print(box1)
            # z = 20
            #posi = mode11(x,y,w,h)
            # if nonum==1:
            #     if ((x<lxy1[0]<x+w) and (y<lxy1[1]<y+h) ):
                    
            #         box2=[lxy1[0]-z,lxy1[1]-z,lxy1[0]+z,lxy1[1]+z]
            #         box2x = [lxy1[0]-z,lxy1[1]-z,40,40]
            #         cv2.rectangle(frame12, box2x, 1, 2)
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 1 格 偵測到 ')
            #             flag = True
            #             posi.append('1')
            # elif nonum==2:
            #     if ((x<lxy2[0]<x+w) and (y<lxy2[1]<y+h) ):
            #         box2=[lxy2[0]-z,lxy2[1]-z,lxy2[0]+z,lxy2[1]+z]
            #         box2x = [lxy2[0]-z,lxy2[1]-z,40,40]
            #         cv2.rectangle(frame12, box2x, 1, 2)
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 2 格 偵測到 ')
            #             flag = True
            #             posi.append('2')
            # elif nonum==3:
            #     if ((x<lxy3[0]<x+w) and (y<lxy3[1]<y+h) ):
            #         box2=[lxy3[0]-z,lxy3[1]-z,lxy3[0]+z,lxy3[1]+z]
            #         box2x = [lxy3[0]-z,lxy3[1]-z,40,40]
            #         cv2.rectangle(frame12, box2x, 1, 2)
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 3 格 偵測到 ')
            #             flag = True
            #             posi.append('3')
            # elif nonum==4:
            #     if ((x<lxy4[0]<x+w) and (y<lxy4[1]<y+h) ):
            #         box2=[lxy4[0]-z,lxy4[1]-z,lxy4[0]+z,lxy4[1]+z]
            #         box2x = [lxy4[0]-z,lxy4[1]-z,40,40]
            #         cv2.rectangle(frame12, box2x, 1, 2)
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 4 格 偵測到 ')
            #             flag = True
            #             posi.append('4')
            # elif nonum==5:
                
            #     if ((x<lxy5[0]<x+w) and (y<lxy5[1]<y+h) ):
            #         box2=[lxy5[0]-z,lxy5[1]-z,lxy5[0]+z,lxy5[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 5 格 偵測到 ')
            #             flag = True
            #             posi.append('5')
            # elif nonum==6:
                
            #     if ((x<lxy6[0]<x+w) and (y<lxy6[1]<y+h) ):
            #         box2=[lxy6[0]-z,lxy6[1]-z,lxy6[0]+z,lxy6[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 6 格 偵測到 ')
            #             flag = True
            #             posi.append('6')
            # elif nonum==7:
                
            #     if ((x<lxy7[0]<x+w) and (y<lxy7[1]<y+h) ):
            #         box2=[lxy7[0]-z,lxy7[1]-z,lxy7[0]+z,lxy7[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 7 格 偵測到 ')
            #             flag = True
            #             posi.append('7')
            # elif nonum==8:
                
            #     if ((x<lxy8[0]<x+w) and (y<lxy8[1]<y+h) ):
            #         box2=[lxy8[0]-z,lxy8[1]-z,lxy8[0]+z,lxy8[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 8 格 偵測到 ')
            #             flag = True
            #             posi.append('8')
            # elif nonum==9:
                
            #     if ((x<lxy9[0]<x+w) and (y<lxy9[1]<y+h) ):
            #         box2=[lxy9[0]-z,lxy9[1]-z,lxy9[0]+z,lxy9[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 9 格 偵測到 ')
            #             flag = True
            #             posi.append('9')
            # elif nonum==10:
                
            #     if ((x<lxy10[0]<x+w) and (y<lxy10[1]<y+h) ):
            #         box2=[lxy10[0]-z,lxy10[1]-z,lxy10[0]+z,lxy10[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 10 格 偵測到 ')
            #             flag = True
            #             posi.append('10')
            # elif nonum==11:
                
            #     if ((x<lxy11[0]<x+w) and (y<lxy11[1]<y+h) ):
            #         box2=[lxy11[0]-z,lxy11[1]-z,lxy11[0]+z,lxy11[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 11 格 偵測到 ')
            #             flag = True
            #             posi.append('11')
                
            #     if ((x<lxy12[0]<x+w) and (y<lxy12[1]<y+h) ):
            #         box2=[lxy12[0]-z,lxy12[1]-z,lxy12[0]+z,lxy12[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 12 格 偵測到 ')
            #             flag = True
            #             posi.append('12')
            # elif nonum==13:
                
            #     if ((x<lxy13[0]<x+w) and (y<lxy13[1]<y+h) ):
            #         box2=[lxy13[0]-z,lxy13[1]-z,lxy13[0]+z,lxy13[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 13 格 偵測到 ')
            #             flag = True
            #             posi.append('13')
                
            # elif nonum==14:
            #     if ((x<lxy14[0]<x+w) and (y<lxy14[1]<y+h) ):
            #         box2=[lxy14[0]-z,lxy14[1]-z,lxy14[0]+z,lxy14[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 14 格 偵測到 ')
            #             flag = True
            #             posi.append('14')
    
            # elif nonum==15:
                
            #     if ((x<lxy15[0]<x+w) and (y<lxy15[1]<y+h) ):
            #         box2=[lxy15[0]-z,lxy15[1]-z,lxy15[0]+z,lxy15[1]+z]
            #         iou_s = Iox(box1,box2)
            #         if iou_s >0.5:
            #             print('第 15 格 偵測到 ')
            #             flag = True
            #             posi.append('15')
            # elif nonum==16:
                
            #     if ((x<lxy16[0]<x+w) and (y<lxy16[1]<y+h) ):
            #         box2=[lxy16[0]-z,lxy16[1]-z,lxy16[0]+z,lxy16[1]+z]
            #         iou_s = Iox(box1,box2)
                    
            #         if iou_s >0.5:
            #             print('第 16 格 偵測到 ')
            #             flag = True
            #             posi.append('16')
            ################# 上個版本的_放置特定位置 ##################
        if flag == True:
            cv2.putText(frame, "Detected BOX in No.  %s  "%(str(nonum)), (40,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    #print("posi咧",posi)
    return flag,frame,posi


def yolo_dec3(frame,classes, scores, boxes,box_count,nonum,cnum,mode_1_1,flag ):
    flag = False
    posi = []
    anotherpo=[]
    position_num4=[]
    position_num3=[]
    leavepo=[]
    if mode_1_1=='1':
        position_num=[]
        for (classid, score, box) in zip(classes, scores, boxes):
            x, y, w, h = box
            if x - 31 < 0:
                x = 31
            if y - 18 < 0:
                y = 18
            if classid==0:
                cut_img = frame[y - 20: y + h + 90, x - 10: x + w + 10]
            color = COLORS[int(classid) % len(COLORS)]
            box_count +=1 # 第幾位
            print('id',box_count)
            label = "%s " % (class_names[classid])#, : %fscore
            cv2.rectangle(frame, box, color, 2)    #frame 
            #title = 'No. %d'%(box_count)
            #title = 'No. %d'%(classid)
            cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)


            flag = False
            # 如果規定class = 拿取box的class
            #if cnum==classid:
        
            po=mode11(x,y,w,h,position_num)
            position_num4 = mode3_to_po2(x,y,w,h,position_num4)
        #print("po:  ", po)
        anotherpo.extend(position_num4)
        posi.extend(po)
        print("anotherpo: ",anotherpo)
        #print("po:  ", po)
        for i in range(1,16):
            if (str(i) not in anotherpo):
                leavepo.append(str(i))

        print("po:  ", posi)
        print("leavepo:  " , leavepo)
        print("str(nonum)",str(nonum))
        #try:
        if( (str(nonum) in posi) and (str(nonum) in leavepo)):
            print('成功將 %s 放到 No. %s 位置'%(class_names[classid],nonum))
            flag=True
            return flag,po
        else:
            print('失敗')
        #except:
            #pass
        if flag == True:
            cv2.putText(frame, "Detected BOX in No.  %s  "%(str(nonum)), (40,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        
    if mode_1_1=='0':
        position_num=[]
        for (classid, score, box) in zip(classes, scores, boxes):
            x, y, w, h = box
            if x - 31 < 0:
                x = 31
            if y - 18 < 0:
                y = 18
            if classid==0:
                cut_img = frame[y - 20: y + h + 90, x - 10: x + w + 10]
            color = COLORS[int(classid) % len(COLORS)]
            box_count +=1 # 第幾位
            print('id',box_count)
            label = "%s " % (class_names[classid])#, : %fscore
            cv2.rectangle(frame, box, color, 2)    #frame 
            #title = 'No. %d'%(box_count)
            #title = 'No. %d'%(classid)
            cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)


            flag = False
            # 如果規定class = 拿取box的class
            #if cnum==classid:

            po=mode1(x,y,w,h,position_num)
            # po=mode1_2(x,y,w,h)
            position_num3 = mode3_to_po(x,y,w,h,position_num3)
        anotherpo.extend(position_num3)
        posi.extend(po)
        #read_img.plot_cir(frame12)
        print("anotherpo: ",anotherpo)
        print("po:  ", po)
        print("str(nonum)",str(nonum))
        for i in range(1,16):
            if (str(i) not in anotherpo):
                leavepo.append(str(i))

        print("po:  ", po)
        print("leavepo:  " , leavepo)
        #try:
        if( (str(nonum) in posi) and (str(nonum) in leavepo)):
            print('成功將 %s 放到 No. %s 位置'%(class_names[classid],nonum))
            flag=True
            return flag,po,frame
        else:
            print('失敗')
        #except:
            #pass
        if flag == True:
            cv2.putText(frame, "Detected BOX in No.  %s  "%(str(nonum)), (40,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    return flag,posi,frame


def rand_No():
    rnum =np.random.randint(1,16,1)
    print("rnum: ", rnum[0])
    return rnum[0]

def rand_cNo():
    cnum =np.random.randint(0,3,1)
    print("cnum: ", cnum[0])
    return cnum[0]

def score_base(score2):
    base_img=cv2.imread("./smoke_base.jpg")
    str_base = "Congratulations ! Score is  :  %s  "%(score2)
    cv2.putText(base_img, str_base, (250,200), cv2.FONT_HERSHEY_SIMPLEX, 1, 2, 4)
    cv2.imshow("Score base",base_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''
font = cv2.FONT_HERSHEY_PLAIN

# 設置模式 : 
print('=============================')
print('\n 積木復健系統模式選擇 ')
print( '\n 0.校正放置位置  ')
print( '\n 1.簡單放置積木  ')
print( '\n 2.放置積木到特定位置  ')
print( '\n 3.特定積木放特定位置  ')
print( '\n 4. 離開  ')
print('=============================')
Txt2Voice('請輸入模式代號') #語音
mode = input('請輸入模式代號 : ')


# 設定分數 與 隨機位置
name='window_name'
score2=0

nonum=rand_No()
cnum=rand_cNo()
'''
def ds(frame):
    #start = time.time()
    box_count=0
    classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    #end = time.time()
    print('共偵測到 %d 個 '%(len(boxes)))
    #box_tatle = len(boxes)
    
    # 畫棋盤
    read_img.plot_cir(frame)

    start_drawing = time.time()
    for (classid, score, box) in zip(classes, scores, boxes):
        color = COLORS[int(classid) % len(COLORS)]
        label = "%s : %f" % (class_names[classid[0]], score)
        box_count +=1
        x,y,w,h = box[0],box[1],box[2],box[3]
        cv2.rectangle(frame, (x,y), (x+w,y+h), color, 1)
        title = 'No. %d'%(box_count)
        cv2.putText(frame, title, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)
        #cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        # PROCESS
        #process programe
        position_num1 = mode1(x,y,w,h)
        for k in range(len(position_num1)):
            print("偵測到 No. %s 格有積木 "%(position_num1[k]))
        
        tatle_box = "總共有 %d 個積木 "%(len(boxes))
        cv2.putText(frame, tatle_box, (40,40), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)


    end_drawing = time.time()
    
        
    try:
        fps_label = "FPS: %.2f (excluding drawing time of %.2fms)" % (1 / (end - start), (end_drawing - start_drawing) * 1000)
        cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    except:
        pass
    return frame

# vc = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# def sle (account,cnum,nonum,mode,mode_1_1,f):
#     # print('\n 請選擇積木放置位置 : ')
#     # print('\n 右邊棋盤選擇 : 1 ')
#     # print('\n 左邊棋盤選擇 : 2 ')
#     # text = '請選擇積木放置位置'
#     #Txt2Voice(text) #語音
#     #mode_1_1 = str(input('棋盤放置位置: '))
#     start_time = time.time()
#     t =str( datetime.now().strftime(ISOTIMEFORMAT))
#     #month = now.strftime("%m")
#     #print("month:", month)
#     SS = "INSERT INTO `blockbd2`(`account`,`Score`,`Time`,`Mode`,`rl`,`nonum`,`cnum`,`boxes`,`time_`,`strat_time`,`end_time`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#     QQ = (account,score2,alltime,mode,mode_1_1,str(nonum),str(cnum),str(box_count),t,start_timeall,end_time_all)
#     cursor.execute(SS,QQ)
#     connection.commit()
#     print("sle done","   print nonum:",nonum)
#     #connection.close()
#     return mode_1_1,start_time

#def main():


##################
# time_flag= True
# f= False
#################

posi3 = 0
# time_flag= True
# f= False
# nonum=rand_No()
# cnum=rand_cNo()

#   while time_flag==True :
def main_strat(account,score2,cnum,nonum,f,mode,mode_1_1,time_flag,flag,vc,timer1,start_time,start_timeall): 
    cnum = int(cnum)
    # col_list = ['帳號','偏癱測','模式','分數','完成60秒','起始時間','結束時間'] ##############12/27
    # df = pd.DataFrame(columns=col_list)
    #while time_flag==True :
    if time_flag==True :
        print('mode,mode_1_1',mode,mode_1_1)
        (grabbed, frame) = vc.read()
        frame = cv2.resize(frame,(640,560))
        frame12=frame.copy()
        # print(frame.shape)
        ###### SQL #########
        connection = mysql.connector.connect(host='localhost',
                                            port='3306',
                                            user='root',
                                            password='0000',
                                            database='block')

        cursor = connection.cursor()

        ###### SQL ######

        #vc = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        
        # 畫圖
        #read_img.plot_right(frame)

        
        #print(grabbed)
        c = cv2.waitKey(10)
        # if c & 0xFF == ord('q'):
        #     break

        if mode =='1':
            col_list = ['帳號','偏癱測','模式','分數','完成60秒','起始時間','結束時間'] ##############12/27
            df = pd.DataFrame(columns=col_list)
            # start_timeall = str( datetime.now().strftime(ISOTIMEFORMAT))
            #try:
            # print("mode = 1,strat")
            # if f == False:
            #     mode_1_1,start_time=sle (cnum,nonum,mode,mode_1_1,f)
            # f = True
            frame12=frame.copy()
            # read_img.plot_cir(frame12)
            read_img.plot_right(frame12)
            read_img.plot_left(frame12)
            
            
            classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
            box_count =0
            # print("classes",classes)
            frame,flag,box_count,score2=yolo_dec1(frame,classes, scores, boxes,box_count ,mode_1_1,score2,flag)
            #if flag==True:_dec1(classes, scores, boxes,box_count ,mode_1_1,score2)
            #if flag==True:
                #score+=1
            #score = box_count
            cv2.putText(frame, "Score is  %s  "%(str(score2)), (32,65), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 200), 1)
            print('目前得分: ',score2)
            end_time = time.time()
            alltime=(end_time-start_time)* 1
            end_time_all = str( datetime.now().strftime(ISOTIMEFORMAT))
            print( '時間已過:  ',int(alltime))
            cv2.putText(frame, "Time is going on :  %d  "%(int(alltime)), (300,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 120, 0), 1)
            


            if int(alltime)>timer1:
                score_base(score2)
                time_flag=False
                end_time_all = str( datetime.now().strftime(ISOTIMEFORMAT))
                t =str( datetime.now().strftime(ISOTIMEFORMAT))
                SS = "INSERT INTO `blockbd2`(`account`,`Score`,`Time`,`Mode`,`rl`,`nonum`,`cnum`,`boxes`,`time_`,`strat_time`,`end_time`,`sixs`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                QQ = (account,score2,alltime,mode,mode_1_1,str(nonum),str(cnum),str(score2),t,start_timeall,end_time_all,"Y")
                cursor.execute(SS,QQ)
                connection.commit()
                if str(mode_1_1) == '0':
                    mode_1_1_ = '左手'
                else:
                    mode_1_1_ = '右手'
                dic_df  = {"帳號":account,'偏癱測':mode_1_1_,'模式':mode,'分數':str(score2),'完成60秒':"Y",'起始時間':start_timeall,'結束時間':t}
                df=df.append(dic_df,ignore_index=True)
                print(df)
                print(dic_df)
            elif (alltime %1 == 0):
                t = str( datetime.now().strftime(ISOTIMEFORMAT))
                posi='0'
                
                #SS="INSERT INTO `blockbd`(`Score`,`Time`,`Mode`,`rl`,`nonum`,`cnum`,`boxes`,`time_`,`posi`) VALUES(%d,%d,%s,%s,%s,%s,%s,%s,%s)" %(0,0,mode,mode_1_1,str(nonum),str(cnum),0,t,'0')
                pp='0'+str(score2)
                print("PP",pp)
                #if pp == '00':
                    #pp = pp +'0'
                # SS="INSERT INTO `blockbd`(`Score`,`Time`,`Mode`,`rl`,`nonum`,`cnum`,`boxes`,`time_`,`posi`) VALUES(%d,%d,%s,%s,%s,%s,%s,%s,%s)" %(score2,alltime,mode,mode_1_1,str(nonum),str(cnum),str(box_count),t,pp)
                SS = "INSERT INTO `blockbd2`(`account`,`Score`,`Time`,`Mode`,`rl`,`nonum`,`cnum`,`boxes`,`time_`,`strat_time`,`end_time`,`sixs`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                QQ = (account,score2,alltime,mode,mode_1_1,str(nonum),str(cnum),str(score2),t,start_timeall,end_time_all,"N")
                cursor.execute(SS,QQ)
                connection.commit()
                print("data store")
                if str(mode_1_1) == '0':
                    mode_1_1_ = '左手'
                else:
                    mode_1_1_ = '右手'
                dic_df  = {"帳號":account,'偏癱測':mode_1_1_,'模式':mode,'分數':str(score2),'完成60秒':"N",'起始時間':start_timeall,'結束時間':end_time_all}
                df = df.append(dic_df,ignore_index=True)
                print(df)
            #score2 = 0
            #except:
                #pass

        elif mode =='2':
            col_list = ['帳號','偏癱測','模式','分數','完成60秒','起始時間','結束時間'] ##############12/27
            df = pd.DataFrame(columns=col_list)
            # start_timeall = str( datetime.now().strftime(ISOTIMEFORMAT))
            #start_time = time.time()
            #try:        
            # if f == False:
            #     mode_1_1,start_time=sle (cnum,nonum,mode,mode_1_1,f)
            print('F:',f)
            f = True
            frame12=frame.copy()
            #read_img.plot_right(frame12)
            #cv2.putText(frame, "Time is going on :  %d  "%(int(alltime)), (300,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1, 1)
            
            classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
            box_count =0
            # rnum =np.random.randint(1,16,1)
            # print("rnum: ", rnum[0])
            #nonum=rand_No()
            if mode_1_1 =='0':
                mode2_1(frame12,nonum)  # 上個版本 mode2
                print("mode ok")
            else:
                mode2(frame12,nonum) # 上個版本 mode2_1
            flag2 = False
            
            flag2,frame,posi2=yolo_dec2(frame,classes, scores, boxes,box_count,nonum=nonum,mode_1_1=mode_1_1,flag=flag,frame12=frame12) 
            #posi =posi[0]
            posi3 = 0
            if len(posi2)>=1:
                posi3=posi2[-1]
                posi3 = int(posi3)+16
                print("posi:",posi3)
            end_time = time.time()
            end_time_all = str( datetime.now().strftime(ISOTIMEFORMAT))
            alltime=(end_time-start_time)* 1
            print( '時間已過:  ',int(alltime))
            print("posi2:",posi2)
            print("flag2",flag2)
            if flag2 == True:
                score2  = int(score2)
                score2+=1
                
                #################
                connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='0000',
                                    database='block')
                cursor = connection.cursor()
                t = str( datetime.now().strftime(ISOTIMEFORMAT)) ################## nounm 數值有錯
                SS = "INSERT INTO `blockbd2`(`account`,`Score`,`Time`,`Mode`,`rl`,`nonum`,`cnum`,`boxes`,`time_`,`strat_time`,`end_time`,`sixs`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                QQ = (account,score2,alltime,mode,mode_1_1,str(nonum),str(cnum),str(score2),t,start_timeall,end_time_all,"N")
                cursor.execute(SS,QQ)
                connection.commit()
                if str(mode_1_1) == '0':
                    mode_1_1_ = '左手'
                else:
                    mode_1_1_ = '右手'
                dic_df  = {"帳號":account,'偏癱測':mode_1_1_,'模式':mode,'分數':str(score2),'完成60秒':"N",'起始時間':start_timeall,'結束時間':end_time_all}
                df = df.append(dic_df,ignore_index=True)
                print(df)
            
                print("XXXXXXX1")
                #################
                nonum=rand_No()
                while nonum in rand_list:
                    nonum=rand_No()
                rand_list.append(nonum)
                while nonum in rand_list:
                    nonum=rand_No()
                rand_list.append(nonum)
                connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='0000',
                                    database='block')
                cursor = connection.cursor()
                t = str( datetime.now().strftime(ISOTIMEFORMAT)) ################## nounm 數值有錯
                SS = "INSERT INTO `blockbd2`(`account`,`Score`,`Time`,`Mode`,`rl`,`nonum`,`cnum`,`boxes`,`time_`,`strat_time`,`end_time`,`sixs`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                QQ = (account,score2,alltime,mode,mode_1_1,str(nonum),str(cnum),str(score2),t,start_timeall,end_time_all,"N")
                cursor.execute(SS,QQ)
                connection.commit()
            
                print("XXXXXXX1")

            cv2.putText(frame, "Score is  %s  "%(str(score2)), (32,65), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1, 1)
            print('目前得分: ',score2)
            
            
            t = str( datetime.now().strftime(ISOTIMEFORMAT)) 
            #connection.close()
            cv2.putText(frame, "Time is going on :  %d  "%(int(alltime)), (300,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 120, 0), 1)
            if int(alltime)>timer1:#60
                score_base(score2)
                end_time_all = str( datetime.now().strftime(ISOTIMEFORMAT))
                time_flag=False
                t = str( datetime.now().strftime(ISOTIMEFORMAT)) ################## nounm 數值有錯
                SS = "INSERT INTO `blockbd2`(`account`,`Score`,`Time`,`Mode`,`rl`,`nonum`,`cnum`,`boxes`,`time_`,`strat_time`,`end_time`,`sixs`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                QQ = (account,score2,alltime,mode,mode_1_1,str(nonum),str(cnum),str(score2),t,start_timeall,t,"Y")
                cursor.execute(SS,QQ)
                if str(mode) == '0':
                    mode_1_1_ = '左手'
                else:
                    mode_1_1_ = '右手'
                dic_df  = {"帳號":account,'偏癱測':mode_1_1_,'模式':mode,'分數':str(score2),'完成60秒':"Y",'起始時間':start_timeall,'結束時間':t}
                df = df.append(dic_df,ignore_index=True)
                print(df)
            #elif int(alltime) %1 == 0:
                
            
                #connection.close()
            #except:
                #pass
        #ds(frame)
        elif mode == '3':
            col_list = ['帳號','偏癱測','模式','分數','完成60秒','起始時間','結束時間'] ##############12/27
            df = pd.DataFrame(columns=col_list)
            # start_timeall = str( datetime.now().strftime(ISOTIMEFORMAT))
            #try:
            # if f == False:
            #         mode_1_1,start_time=sle (cnum,nonum,mode,mode_1_1,f)
            # f = True
            frame12=frame.copy()
            classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
            print('共偵測到 %d 個 '%(len(boxes)))
            for (classid, score, box) in zip(classes, scores, boxes):
                
                color = COLORS[int(classid) % len(COLORS)]
                #box_count +=1 # 第幾位
                #print('id',box_count)
                label = "%s "% (class_names[classid])#, : %fscore
                cv2.rectangle(frame, box, color, 2)    #frame 
                cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)
             
            #rnum =np.random.randint(1,16,1)
            #print("rnum: ", rnum[0])
            #################################### (12 / 3)mode2(frame12,nonum)
            #cnum =np.random.randint(1,16,1)
            #print("cnum: ", cnum[0])
            mode3(cnum)
            box_count =0
            if mode_1_1 =='0':
                mode2(frame12,nonum)
            else:
                mode2_1(frame12,nonum)
            flag2 = False

            cv2.putText(frame, "Choose No.  %s  BOX in  "%(class_names[cnum]), (40,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5,  (255, 120, 0), 1)
            cv2.putText(frame, "Score is  %s  "%(str(score2)), (32,65), cv2.FONT_HERSHEY_SIMPLEX, 0.5,  (120, 120, 0), 1)
            flag2,po,frame=yolo_dec3(frame,classes, scores, boxes,box_count,nonum=nonum,cnum=cnum ,mode_1_1=mode_1_1,flag=flag)
            end_time = time.time()
            end_time_all = str( datetime.now().strftime(ISOTIMEFORMAT))
            alltime=(end_time-start_time)* 1
            print( '時間已過:  ',int(alltime))
            if flag2 == True:
                score2  = int(score2)
                score2+=1
                posi=nonum#po[0]   12/14修改
                t = str( datetime.now().strftime(ISOTIMEFORMAT))
                connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='0000',
                                    database='block')
                cursor = connection.cursor()
                t = str( datetime.now().strftime(ISOTIMEFORMAT)) ################## nounm 數值有錯
                SS = "INSERT INTO `blockbd2`(`account`,`Score`,`Time`,`Mode`,`rl`,`nonum`,`cnum`,`boxes`,`time_`,`strat_time`,`end_time`,`sixs`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                QQ = (account,score2,alltime,mode,mode_1_1,str(nonum),str(cnum),str(box_count),t,start_timeall,end_time_all,"N")
                cursor.execute(SS,QQ)
                connection.commit()
                nonum=rand_No()
                cnum=rand_cNo()
                while nonum in rand_list:
                    nonum=rand_No()
                rand_list.append(nonum)
                #posi2=0
                t = str( datetime.now().strftime(ISOTIMEFORMAT))
                connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='0000',
                                    database='block')
                cursor = connection.cursor()
                SS = "INSERT INTO `blockbd2`(`account`,`Score`,`Time`,`Mode`,`rl`,`nonum`,`cnum`,`boxes`,`time_`,`strat_time`,`end_time`,`sixs`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                QQ = (account,score2,alltime,mode,mode_1_1,str(nonum),str(cnum),str(score2),t,start_timeall,end_time_all,"N")
                cursor.execute(SS,QQ)
                connection.commit()
                if str(mode_1_1) == '0':
                    mode_1_1_ = '左手'
                else:
                    mode_1_1_ = '右手'
                dic_df  = {"帳號":account,'偏癱測':mode_1_1_,'模式':mode,'分數':str(score2),'完成60秒':"N",'起始時間':start_timeall,'結束時間':end_time_all}
                df = df.append(dic_df,ignore_index=True)
            cv2.putText(frame, "Score is  %s  "%(str(score2)), (32,65), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1, 1)
            print('目前得分: ',score2)
            end_time = time.time()
            alltime=(end_time-start_time)* 1
            print( '時間已過:  ',int(alltime))
            cv2.putText(frame, "Time is going on :  %d  "%(int(alltime)), (300,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 120, 0), 1)
            if alltime>timer1: #60:
                end_time_all = str( datetime.now().strftime(ISOTIMEFORMAT))
                score_base(score2)
                time_flag=False
                t = str( datetime.now().strftime(ISOTIMEFORMAT))
                SS = "INSERT INTO `blockbd2`(`account`,`Score`,`Time`,`Mode`,`rl`,`nonum`,`cnum`,`boxes`,`time_`,`strat_time`,`end_time`,`sixs`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                QQ = (account,score2,alltime,mode,mode_1_1,str(nonum),str(cnum),str(score2),t,start_timeall,t,"Y")
                cursor.execute(SS,QQ)
                if str(mode_1_1) == '0':
                    mode_1_1_ = '左手'
                else:
                    mode_1_1_ = '右手'
                dic_df  = {"帳號":account,'偏癱測':mode_1_1_,'模式':mode,'分數':str(score2),'完成60秒':"Y",'起始時間':start_timeall,'結束時間':t}
                df = df.append(dic_df,ignore_index=True)
                print(df)
                
            #elif alltime %2 == 0:
                #posi=po
                #t = str( datetime.now().strftime(ISOTIMEFORMAT))
                #SS="INSERT INTO `blockbd`(`Score`,`Time`,`Mode`,`rl`,`nonum`,`cnum`,`boxes`,`time_`,`posi`) VALUES(%d,%d,%s,%s,%s,%s,%s,%s,%s)" %(score2,alltime,mode,mode_1_1,str(nonum),str(cnum),str(box_count),t,str(posi))
                #cursor.execute(SS)
                #connection.commit()
                
            #except:
                #pass

        

        else :
            print("退出")
            time_flag=False

        
        #try:
        ##### 影像 串流 ########
        #frame12=frame.copy()
         

        #import sys
        #sys.path.append('F:\\Blocks\\code\\frame_stream\\')
        #from frame_stream import app 
        #app.gen_frames(grabbed, frame12)
        #app.gen_frames2(grabbed, frame12)

        #import say_mqtt 
        #say_mqtt.say(frame=frame,frame12=frame12)
        #say_mqtt.say(frame=frame,frame12=frame12)


        ##### 影像 串流 ########
        #except:
            #pass
        # cv2.imshow(name, frame) 
        # cv2.imshow('fake', frame12)
        c = cv2.waitKey(10)
        # if c & 0xFF == ord('q'):
        #     break
     
        return frame,frame12,time_flag,int(alltime),score2,df


    vc.release()
    cv2.destroyAllWindows()


def teach_(vc):
    
    (grabbed, frame) = vc.read()
    frame = cv2.resize(frame,(640,560))
    frame12=frame.copy()
    frame12=read_img.plot_cir(frame12)
    read_img.plot_right(frame12)
    read_img.plot_left(frame12)
    #cv2.putText(frame12, "Exit : q, keybroad press q :    ", (300,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 120, 0), 1)
    return frame12

#if __name__ == '__main__':
name='window_name'
score2=0
flag =False
#def strt():#(mode,handmode
    #font = cv2.FONT_HERSHEY_PLAIN
    #vc = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    # 設置模式 : 
    # print('=============================')
    # print('\n 積木復健系統模式選擇 ')
    # print( '\n 0.校正放置位置  ')
    # print( '\n 1.簡單放置積木  ')
    # print( '\n 2.放置積木到特定位置  ')
    # print( '\n 3.特定積木放特定位置  ')
    # print( '\n 4. 離開  ')
    # print('=============================')
    # Txt2Voice('請輸入模式代號') #語音
    #mode = input('請輸入模式代號 : ')
    # font = cv2.FONT_HERSHEY_PLAIN
    
    # timer1= 60
    #print(timer1)
    # 設定分數 與 隨機位置
    # name='window_name'
    # score2=0

    #nonum=rand_No()
    #cnum=rand_cNo()

    # time_flag= True
    # f= False  
    # flag = False  
    
    #mode =mode
    #frame12=teach_(vc)
    #print(frame12.shape)

    #frame,frame12,time_flag =main_strat(score2,cnum,nonum,f,mode,handmode,time_flag,flag,vc,timer1)
    #return frame,frame12,time_flag 
    #return frame12
    
    




    

