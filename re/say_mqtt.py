import paho.mqtt.client as mqtt
import random
import json
import datetime
import time
import base64
# 設置日期時間的格式
ISOTIMEFORMAT = '%m/%d %H:%M:%S'
# 連線設定
# 初始化地端程式
client = mqtt.Client()
# 設定登入帳號密碼
client.username_pw_set("","")
# 設定連線資訊(IP, Port, 連線時間)
client.connect("172.20.10.13", 1883, 60) #自己的IP
'''
while True:
    t0 = random.randint(0,30)
    t = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    payload = {'Temperature' : t0 , 'Time' : t}
    print (json.dumps(payload))
    #要發布的主題和內容
    client.publish("pc/pc", json.dumps(payload)) #訂閱主題
    time.sleep(5)
'''
def say(frame,frame12):
    t = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    b64_code = base64.b64encode(frame).decode()
    b64_code2 = base64.b64encode(frame12).decode()
    payload = {'photo' : b64_code,'photo2' : b64_code2, 'Time' : t}
    #print(json.dumps(payload))
    client.publish("pc/pc", b64_code)#json.dumps(b64_code))