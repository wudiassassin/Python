"""
表名:标准值设置
功能:添加采集器各项目标准值
自定义设备ID
随机interval

表结构：
sensorid	dispstatus	lslvalue	lclvalue	clvalue	uclvalue	uslvalue	r_uslvalue	delflg	updateuserid	updatedate
采集器ID    属性CD

数据示例：
EM-MH-001	1919	40.00000000	60.00000000	80.00000000	90.00000000	100.00000000	110.00000000	0	jzd	2022-02-09 18:16:22
"""

import psycopg2
from io import StringIO
import time

while True:
    s = ""
    r = input("请输入采集器ID：")
    if r != "exit":
        listj = ['1919', '1920', '017', '016']
        listk = [(190, 200, 210, 220, 230, 240), (0, 5, 10, 15, 20, 25),
                 (190, 200, 210, 220, 230, 240), (0, 5, 10, 15, 20, 25)]
        # 循环创建一个字符串，把数据库每一条数据作为一行
        for i in range(4):
            # 创建一条数据库记录，记录中每个字段间隔符为table（制表符\t）每一行用换行符\n 隔开下一行
            s += str(r) + \
                 "\t" + str(listj[i]) + \
                 "\t" + str(listk[i][0]) + ".00000000" + \
                 "\t" + str(listk[i][1]) + ".00000000" + \
                 "\t" + str(listk[i][2]) + ".00000000" + \
                 "\t" + str(listk[i][3]) + ".00000000" + \
                 "\t" + str(listk[i][4]) + ".00000000" + \
                 "\t" + str(listk[i][5]) + ".00000000" + \
                 "\t0" + \
                 "\tadmin" + \
                 "\t" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + \
                 "\n"
        # 创建一个内存对象f,StringIO为存储在内存中的文件，格式为满足文件的任意格式
        f = StringIO()
        # 将s数据字符串写入内存
        f.write(s)
        # 把f的游标移到第一位，write方法后，游标会变成最尾，使用StringIO(**)则不会
        f.seek(0)
        # 连接数据库
        conn = psycopg2.connect(host='192.168.2.17',
                                port='5432',
                                user="postgres",
                                password="123456",
                                database="iot-mgmt",
                                options="-c search_path=otherSchema,ths_system")
        # 创建游标
        cur = conn.cursor()
        # 将内存对象f中的数据写入数据库，参数columns为所有列的元组
        cur.copy_from(f, 'tabtrendalertmst', null='', columns=('sensorid', 'dispstatus', 'lslvalue', 'lclvalue',
                                                               'clvalue', 'uclvalue', 'uslvalue', 'r_uslvalue',
                                                               'delflg', 'updateuserid', 'updatedate'))
        # 提交
        conn.commit()
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()
        print('成功写入数据库')
    else:
        break
