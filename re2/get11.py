import mysql.connector
from datetime import datetime

connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='0000',
                                    database='block')

cursor = connection.cursor()
# w1 = 's07362022@gmail.com'
# w2 = 'harden'
# w3 = 'caca3661537'
# SS="INSERT INTO `UserRgeisters2`(`email`,`username`,`password2`) VALUES(%s,%s,%s)" %("s073gmail","ssas","sss")
# cursor.execute("INSERT INTO `UserRgeisters2`(`email`,`username`,`password2`) VALUES(%s,%s,%s)",(w1,w2,w3))
# connection.commit()
def insert():
    ISOTIMEFORMAT = '%Hh%Mm%Ss'
    t =str( datetime.now().strftime(ISOTIMEFORMAT))
    # SS="INSERT INTO `UserRgeisters`(`email`,`username`,`password2`) VALUES(%s,%s,%s)" %(str(a),str(b),str(c))
    # cursor.execute()
    # connection.commit()
    SS = "INSERT INTO `blockbd2`(`account`,`Score`,`Time`,`Mode`,`rl`,`nonum`,`cnum`,`boxes`,`time_`,`strat_time`,`end_time`,`sixs`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #SS="INSERT INTO `blockbd2`(`account,`Score`,`Time`,`Mode`,`rl`,`nonum`,`cnum`,`boxes`,`time_`,`strat_time`,`end_time`) VALUES(%s,%d,%s,%s,%s,%s,%s,%s,%s,%s,%s)",('caca3661537',0,'56','1','0','10','3','5',t,t,t)
    cursor.execute(SS,('caca3661537','0','56','1','0','10','3','5',t,t,t,"0"))
    connection.commit()

def get_sql():
    #with cursor  as cursor1:
    # 查詢資料SQL語法
    command = "SELECT * FROM blockbd"
    # 執行指令
    cursor.execute(command)
    # 取得所有資料
    result = cursor.fetchall()
    #print(type(result))
    #print(len(result))
    return result[-1][1]

insert()