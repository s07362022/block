import cv2
import numpy as np

path = 'F:\\Blocks\\dataset\\images\\810.png'
img = cv2.imread(path)
print('img size: ',img.shape)
#右邊框框 左上(370,120) 右上(530,120) 左下 (370,280) 右下(530,280)
x ,y,w,h= 370,140,160,160
color = (0, 255, 255)

def plot_right(img=img):
    cv2.circle(img,(10, 155), 5, (255, 0, 0), -1) # 圓形1
    cv2.circle(img,(10, 155),1,(250,255,250),-1)

    cv2.circle(img,(280, 155), 5, (255, 0, 0), -1) # 圓形1
    cv2.circle(img,(280, 155),1,(250,255,250),-1)

    cv2.circle(img,(10, 485), 5, (255, 0, 0), -1) # 圓形1
    cv2.circle(img,(10, 485),1,(250,255,250),-1)

    cv2.circle(img,(280, 485), 5, (255, 0, 0), -1) # 圓形1
    cv2.circle(img,(280, 485),1,(250,255,250),-1)

def plot_left(img=img):
    cv2.circle(img,(320, 175), 5, (255, 0, 0), -1) # 圓形1
    cv2.circle(img,(320, 175),1,(250,255,250),-1)

    cv2.circle(img,(555, 175), 5, (255, 0, 0), -1) # 圓形1
    cv2.circle(img,(555, 175),1,(250,255,250),-1)

    cv2.circle(img,(320, 485), 5, (255, 0, 0), -1) # 圓形1
    cv2.circle(img,(320, 485),1,(250,255,250),-1)

    cv2.circle(img,(555, 485), 5, (255, 0, 0), -1) # 圓形1
    cv2.circle(img,(555, 485),1,(250,255,250),-1)
#plot_left(img=img)
left_sq_x,left_sq_y,left_sq_w,left_sq_h = 320,175,235,310
ringh_sq_x, ringh_sq_y, ringh_sq_w, ringh_sq_h = 10,155,270,330
#plot_right(img=img)


def plot_cir(img=img):
    #cv2.rectangle(img, (x,y), (x+w,y+h), color, 1)
    #cv2.line(img, (370, 160), (530, 160), (0, 0, 255), 1)
    cv2.circle(img,(225, 225), 20, (255, 0, 0), -1) # 圓形1
    cv2.circle(img,(225, 225),1,(250,255,250),-1)
    cv2.circle(img,(225, 300), 20, (255, 0, 0), -1)
    cv2.circle(img,(225, 300),1,(250,255,250),-1)
    cv2.circle(img,(225, 375), 20, (255, 0, 0), -1)
    cv2.circle(img,(225, 375), 1, (250,255,250), -1)
    cv2.circle(img,(225, 450), 20, (255, 0, 0), -1)
    cv2.circle(img,(225, 450), 1, (250,255,250), -1)
    cv2.circle(img,(160, 225), 20, (255, 0, 0), -1)
    cv2.circle(img,(160, 225), 1, (250,255,250), -1)
    cv2.circle(img,(160, 300), 20, (255, 0, 0), -1)
    cv2.circle(img,(160, 300), 1, (250,255,250), -1)
    cv2.circle(img,(160, 375), 20, (255, 0, 0), -1)
    cv2.circle(img,(160, 375), 1, (250,255,250), -1)
    cv2.circle(img,(160, 450), 20, (255, 0, 0), -1)
    cv2.circle(img,(160, 450), 1, (250,255,250), -1)


    cv2.circle(img,(100, 225), 20, (255, 0, 0), -1)
    cv2.circle(img,(100, 225), 1, (250,255,250), -1)

    cv2.circle(img,(100, 300), 20, (255, 0, 0), -1)
    cv2.circle(img,(100, 300), 1, (250,255,250), -1)


    cv2.circle(img,(100, 375), 20, (255, 0, 0), -1)
    cv2.circle(img,(100, 375), 1, (250,255,250), -1)


    cv2.circle(img,(100, 450), 20, (255, 0, 0), -1)
    cv2.circle(img,(100, 450), 1, (250,255,250), -1)


    cv2.circle(img,(40, 225), 20, (255, 0, 0), -1)
    cv2.circle(img,(40, 225), 1, (250,255,250), -1)


    cv2.circle(img,(40, 300), 20, (255, 0, 0), -1)
    cv2.circle(img,(40, 300), 1, (250,255,250), -1)

    cv2.circle(img,(40, 375), 20, (255, 0, 0), -1)
    cv2.circle(img,(40, 375), 1, (250,255,250), -1)


    cv2.circle(img,(40, 450), 20, (255, 0, 0), -1)
    cv2.circle(img,(40, 450), 1, (250,255,250), -1)
    lo1cy(img)
    lo2cy(img)
    lo3cy(img)
    lo4cy(img)
    lo5cy(img)
    lo6cy(img)
    lo7cy(img)
    lo8cy(img)
    lo9cy(img)
    lo10cy(img)
    lo11cy(img)
    lo12cy(img)
    lo13cy(img)
    lo14cy(img)
    lo15cy(img)
    lo16cy(img)
    return img
#plot_cir()


def no4cy(img):
    cv2.circle(img,(225, 225), 20, (255, 0, 0), -1) # 圓形1
    cv2.circle(img,(225, 225),1,(250,255,250),-1)
#no1cy(img)
def no8cy(img):
    cv2.circle(img,(225, 300), 20, (255, 0, 0), -1)
    cv2.circle(img,(225, 300),1,(250,255,250),-1)
#no2cy(img)

def no12cy(img):
    cv2.circle(img,(225, 375), 20, (255, 0, 0), -1)
    cv2.circle(img,(225, 375), 1, (250,255,250), -1)
#no3cy(img)
def no16cy(img):
    cv2.circle(img,(225, 450), 20, (255, 0, 0), -1)
    cv2.circle(img,(225, 450), 1, (250,255,250), -1)
#no4cy(img)    

def no3cy(img):
    cv2.circle(img,(160, 225), 20, (255, 0, 0), -1)
    cv2.circle(img,(160, 225), 1, (250,255,250), -1)

def no7cy(img):
    cv2.circle(img,(160, 300), 20, (255, 0, 0), -1)
    cv2.circle(img,(160, 300), 1, (250,255,250), -1)

def no11cy(img):
    cv2.circle(img,(160, 375), 20, (255, 0, 0), -1)
    cv2.circle(img,(160, 375), 1, (250,255,250), -1)

def no15cy(img):
    cv2.circle(img,(160, 450), 20, (255, 0, 0), -1)
    cv2.circle(img,(160, 450), 1, (250,255,250), -1)

def no2cy(img):
    cv2.circle(img,(100, 225), 20, (255, 0, 0), -1)
    cv2.circle(img,(100, 225), 1, (250,255,250), -1)
#no8cy(img)
def no6cy(img):
    cv2.circle(img,(100, 300), 20, (255, 0, 0), -1)
    cv2.circle(img,(100, 300), 1, (250,255,250), -1)

def no10cy(img):
    cv2.circle(img,(100, 375), 20, (255, 0, 0), -1)
    cv2.circle(img,(100, 375), 1, (250,255,250), -1)

def no14cy(img):
    cv2.circle(img,(100, 450), 20, (255, 0, 0), -1)
    cv2.circle(img,(100, 450), 1, (250,255,250), -1)

def no1cy(img):
    cv2.circle(img,(40, 225), 20, (255, 0, 0), -1)
    cv2.circle(img,(40, 225), 1, (250,255,250), -1)

def no5cy(img):
    cv2.circle(img,(40, 300), 20, (255, 0, 0), -1)
    cv2.circle(img,(40, 300), 1, (250,255,250), -1)

def no9cy(img):
    cv2.circle(img,(40, 375), 20, (255, 0, 0), -1)
    cv2.circle(img,(40, 375), 1, (250,255,250), -1)

def no13cy(img):
    cv2.circle(img,(40, 450), 20, (255, 0, 0), -1)
    cv2.circle(img,(40, 450), 1, (250,255,250), -1)


def lo16cy(img):
    cv2.circle(img,(540, 450), 20, (255, 0, 0), -1)
    cv2.circle(img,(540, 450), 1, (250,255,250), -1)

def lo15cy(img):
    cv2.circle(img,(480, 450), 20, (255, 0, 0), -1)
    cv2.circle(img,(480, 450), 1, (250,255,250), -1)

def lo14cy(img):
    cv2.circle(img,(420, 450), 20, (255, 0, 0), -1)
    cv2.circle(img,(420, 450), 1, (250,255,250), -1)

def lo13cy(img):
    cv2.circle(img,(360, 450), 20, (255, 0, 0), -1)
    cv2.circle(img,(360, 450), 1, (250,255,250), -1)

def lo12cy(img):
    cv2.circle(img,(540, 375), 20, (255, 0, 0), -1)
    cv2.circle(img,(540, 375), 1, (250,255,250), -1)

def lo8cy(img):
    cv2.circle(img,(540, 300), 20, (255, 0, 0), -1)
    cv2.circle(img,(540, 300), 1, (250,255,250), -1)


def lo4cy(img):
    cv2.circle(img,(540, 225), 20, (255, 0, 0), -1)
    cv2.circle(img,(540, 225), 1, (250,255,250), -1)

def lo3cy(img):
    cv2.circle(img,(480, 225), 20, (255, 0, 0), -1)
    cv2.circle(img,(480, 225), 1, (250,255,250), -1)

def lo7cy(img):
    cv2.circle(img,(480, 300), 20, (255, 0, 0), -1)
    cv2.circle(img,(480, 300), 1, (250,255,250), -1)

def lo11cy(img):
    cv2.circle(img,(480, 375), 20, (255, 0, 0), -1)
    cv2.circle(img,(480, 375), 1, (250,255,250), -1)

def lo10cy(img):
    cv2.circle(img,(420, 375), 20, (255, 0, 0), -1)
    cv2.circle(img,(420, 375), 1, (250,255,250), -1)

def lo6cy(img):
    cv2.circle(img,(420, 300), 20, (255, 0, 0), -1)
    cv2.circle(img,(420, 300), 1, (250,255,250), -1)

def lo2cy(img):
    cv2.circle(img,(420, 225), 20, (255, 0, 0), -1)
    cv2.circle(img,(420, 225), 1, (250,255,250), -1)

def lo9cy(img):
    cv2.circle(img,(360, 375), 20, (255, 0, 0), -1)
    cv2.circle(img,(360, 375), 1, (250,255,250), -1)
#lo3cy(img)
def lo5cy(img):
    cv2.circle(img,(360, 300), 20, (255, 0, 0), -1)
    cv2.circle(img,(360, 300), 1, (250,255,250), -1)

def lo1cy(img):
    cv2.circle(img,(360, 225), 20, (255, 0, 0), -1)
    cv2.circle(img,(360, 225), 1, (250,255,250), -1)

# 中心座標 
'''
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
'''
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
#cv2.imshow('img',img)
#cv2.waitKey( 0 )
#cv2.destroyAllWindows()