"""
表名:采集器警报表
功能:从ths_proces.tabkeikodata_everytime表获取8月份的数据
自定义采集器ID
根据采集器ID获取设备ID、设备名、采集器名和标准值
随机alertstatus、alertkind、occurrencestatus、alertdatastatus

表结构：
alertdatano	regstdatetime	eqpid	sensorid	dispstatus	alertstatus	alertkind	occurrencestatus	alertdatastatus
resultvalue	sensorname	eqpname	unit	lslvalue	lclvalue	clvalue	uclvalue	uslvalue	r_uslvalue	notes
dispflg	noticeid	title	alertlevel	alertmessage	mizucheckflg	updateuserid	updatedate

数据示例：
5563	2022-08-18 16:18:40	EM-XL-001	EM-XL-001	1919	03	52	02	05
295.00000000	数控火焰切割机1#	数控火焰切割机1#	V	180.00000000	195.00000000	220.00000000	230.00000000	240.00000000	250.00000000
"""

from io import StringIO

import psycopg2
import random

while True:
    r = input("请输入采集器ID：")
    if r != "exit":
        # 连接数据库
        conn = psycopg2.connect(host='192.168.2.17',
                                port='5432',
                                user="postgres",
                                password="123456",
                                database="iot-mgmt",
                                options="-c search_path=otherSchema,ths_system")
        # 创建游标
        cur = conn.cursor()
        list1 = []
        sql = "SELECT " + \
              "eqp.eqpid,eqp.eqpname,sen.sensorname " + \
              "FROM tabsensormst AS sen " + \
              "LEFT JOIN tabeqp AS eqp " + \
              "ON eqp.eqpid = sen.eqpid " + \
              "WHERE sen.sensorid = '" + str(r) + "'"
        cur.execute(sql)
        data = cur.fetchall()
        if str(data) != 'None':
            list1.append(data)
        print(list1)
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()

        # 连接数据库
        conn = psycopg2.connect(host='192.168.2.17',
                                port='5432',
                                user="postgres",
                                password="123456",
                                database="iot-mgmt",
                                options="-c search_path=otherSchema,ths_kspc")
        # 创建游标
        cur = conn.cursor()
        list2 = []
        sql = "SELECT " + \
              "alertdatano " + \
              "FROM tabkeikoalert " + \
              "ORDER BY alertdatano DESC"
        cur.execute(sql)
        data2 = cur.fetchone()
        if str(data2) != 'None':
            list2.append(data2)
        print(list2)
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()

        # 连接数据库
        conn = psycopg2.connect(host='192.168.2.17',
                                port='5432',
                                user="postgres",
                                password="123456",
                                database="iot-mgmt",
                                options="-c search_path=otherSchema,ths_system")
        # 创建游标
        cur = conn.cursor()
        list3 = []
        sql = "SELECT " + \
              "dispstatus,lslvalue,lclvalue,clvalue,uclvalue,uslvalue,r_uslvalue " + \
              "FROM tabtrendalertmst " + \
              "WHERE sensorid = '" + str(r) + "'" + \
              "ORDER BY dispstatus"
        cur.execute(sql)
        data3 = cur.fetchall()
        if str(data3) != 'None':
            list3.append(data3)
        print(list3)
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()

        # 连接数据库
        conn = psycopg2.connect(host='192.168.2.17',
                                port='5432',
                                user="postgres",
                                password="123456",
                                database="iot-mgmt",
                                options="-c search_path=otherSchema,ths_proces")
        # 创建游标
        cur = conn.cursor()
        list4 = []
        sql = "SELECT " + \
              "* " + \
              "FROM tabkeikodata_everytime " + \
              "WHERE sensorid = '" + str(r) + "'" + \
              "AND to_char(editdatetime,'yyyy-MM-dd HH24:MI:ss') LIKE '%2022-08%'"
        cur.execute(sql)
        data4 = cur.fetchall()
        if str(data4) != 'None':
            list4.append(data4)
        print(list4)
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()

        s = ""
        # 循环创建一个字符串，把数据库每一条数据作为一行
        for i in range(0, len(list4[0])):
            dstatus = list4[0][i][1]
            if dstatus == '1919':
                unit = 'V'
                j = list3[0][2]
            elif dstatus == '1920':
                unit = 'A'
                j = list3[0][3]
            elif dstatus == '017':
                unit = 'V'
                j = list3[0][1]
            else:
                unit = 'A'
                j = list3[0][0]
            astatus = random.choices(['02', '03'])
            akind = random.choices(['01', '02', '11', '12', '51', '52', '61', '62'])
            ostatus = random.choices(['01', '02', '03', '04'])
            adstatus = random.choices(['01', '02', '03', '04', '05'])
            if adstatus[0] == '01':
                resvalue = list4[0][i][3]
            elif adstatus[0] == '02':
                resvalue = list4[0][i][4]
            elif adstatus[0] == '03':
                resvalue = list4[0][i][5]
            elif adstatus[0] == '04':
                resvalue = list4[0][i][6]
            else:
                resvalue = j[3]

            # 创建一条数据库记录，记录中每个字段间隔符为table（制表符\t）每一行用换行符\n 隔开下一行
            s += str(int(list2[0][0]) + i + 1) + \
                 "\t" + str(list4[0][i][2]) + \
                 "\t" + str(list1[0][0][0]) + \
                 "\t" + str(r) + \
                 "\t" + str(dstatus) + \
                 "\t" + str(astatus[0]) + \
                 "\t" + str(akind[0]) + \
                 "\t" + str(ostatus[0]) + \
                 "\t" + str(adstatus[0]) + \
                 "\t" + str(resvalue) + \
                 "\t" + str(list1[0][0][2]) + \
                 "\t" + str(list1[0][0][1]) + \
                 "\t" + str(unit) + \
                 "\t" + str(j[1]) + \
                 "\t" + str(j[2]) + \
                 "\t" + str(j[3]) + \
                 "\t" + str(j[4]) + \
                 "\t" + str(j[5]) + \
                 "\t" + str(j[6]) + \
                 "\t" + \
                 "\t" + \
                 "\t" + \
                 "\t" + \
                 "\t" + \
                 "\t" + \
                 "\t" + \
                 "\t" + \
                 "\t" + \
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
                                options="-c search_path=otherSchema,ths_kspc")
        # 创建游标
        cur = conn.cursor()
        # 将内存对象f中的数据写入数据库，参数columns为所有列的元组
        cur.copy_from(f, 'tabkeikoalert', null='', columns=('alertdatano', 'regstdatetime', 'eqpid', 'sensorid',
                                                            'dispstatus', 'alertstatus', 'alertkind',
                                                            'occurrencestatus', 'alertdatastatus',
                                                            'resultvalue', 'sensorname', 'eqpname', 'unit', 'lslvalue',
                                                            'lclvalue', 'clvalue',
                                                            'uclvalue', 'uslvalue', 'r_uslvalue', 'notes', 'dispflg',
                                                            'noticeid', 'title', 'alertlevel',
                                                            'alertmessage', 'mizucheckflg', 'updateuserid',
                                                            'updatedate'))
        # 提交
        conn.commit()
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()
        print('成功写入数据库')
    else:
        break
