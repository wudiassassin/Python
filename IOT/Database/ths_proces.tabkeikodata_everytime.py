"""
表名:实时采集数据表
功能:造8月份的数据
自定义采集器ID
maximumvalue、minimumvalue、differencevalue、averagevalue根据设置tabtrendalertmst表设置的值范围内随机

表结构：
sensorid	dispstatus	editdatetime	maximumvalue	minimumvalue	differencevalue	averagevalue	parameter	triggersensorid	startdatetime	enddatetime	sumvalue

数据示例：
EM-XL-001  1919	 2022-02-17 16:06:55	42.00000000	-8.00000000	50.00000000	17.00000000	0
"""

import psycopg2
from io import StringIO
import random

while True:
    s = ""
    r = input("请输入采集器ID：")
    if r != "exit":
        # (190, 200, 210, 220, 230, 240), (0, 5, 10, 15, 20, 25)
        listj = ['1919', '1920', '017', '016']
        # 循环创建一个字符串，把数据库每一条数据作为一行
        for i_1 in range(1, 32):
            for i_2 in range(0, 24):
                for i_3 in range(0, 60, 10):
                    m = random.choice([0, 1, 2, 3])
                    if m == 0 or m == 2:
                        maxvalue = random.choice(range(215, 236))
                        minvalue = random.choice(range(185, 206))
                        diffvalue = random.choice(range(235, 246))
                        avgvalue = random.choice(range(210, 221))
                    else:
                        maxvalue = random.choice(range(12, 24))
                        minvalue = random.choice(range(-3, 9))
                        diffvalue = random.choice(range(23, 29))
                        avgvalue = random.choice(range(10, 16))
                    # 创建一条数据库记录，记录中每个字段间隔符为table（制表符\t）每一行用换行符\n 隔开下一行
                    s += str(r) + \
                         "\t" + str(listj[m]) + \
                         "\t2022-08-" + '%02d' % i_1 + " " + '%02d' % i_2 + ":" + '%02d' % i_3 + ":00" + \
                         "\t" + str(maxvalue) + ".00000000" + \
                         "\t" + str(minvalue) + ".00000000" + \
                         "\t" + str(diffvalue) + ".00000000" + \
                         "\t" + str(avgvalue) + ".00000000" + \
                         "\t0" + \
                         "\t" + \
                         "\t" + \
                         "\t" + \
                         "\t" + \
                         "\n"
        # 创建一个内存对象f,StringIO为存储在内存中的文件，格式为满足文件的任意格式
        f = StringIO()
        # 将s数据字符串写入内
        f.write(s)
        # 把f的游标移到第一位，write方法后，游标会变成最尾，使用StringIO(**)则不会
        f.seek(0)
        # 连接数据库
        conn = psycopg2.connect(host='192.168.2.17',
                                port='5432',
                                user="postgres",
                                password="123456",
                                database="iot-mgmt",
                                options="-c search_path=otherSchema,ths_proces")
        # 创建游标
        cur = conn.cursor()
        # 将内存对象f中的数据写入数据库，参数columns为所有列的元组
        cur.copy_from(f, 'tabkeikodata_everytime', null='', columns=('sensorid', 'dispstatus', 'editdatetime', 'maximumvalue',
                                                               'minimumvalue', 'differencevalue', 'averagevalue', 'parameter',
                                                               'triggersensorid', 'startdatetime', 'enddatetime',
                                                                     'sumvalue'))
        # 提交
        conn.commit()
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()
        print('成功写入数据库')
    else:
        break
