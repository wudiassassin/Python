"""
表名:每月采集器情报
功能:从ths_proces.tabkeikodata_everytime获取2022年每月的第一条数据
    从ths_kspc.tabkeikoalert表获取8月份每天的警告和危险总数
自定义采集器ID

表结构：
targetdate	eqpid	sensorid	unit	dispstatus	maximumvalue	minimumvalue	differencevalue	averagevalue	rate
reportcount	warningcount	riskcount	lsl	lcl	cl	ucl	usl	r_usl

数据示例：
2022-08-01 15:17:52	EM-XL-001	D000005	V	017	78	78	83	1.0	45.0	78	3	74	4.0	83.0	78.0	890.0	87.0	78.0
"""

from io import StringIO

import psycopg2

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
                                options="-c search_path=otherSchema,ths_system")
        # 创建游标
        cur = conn.cursor()
        list2 = []
        sql = "SELECT " + \
              "dispstatus,lslvalue,lclvalue,clvalue,uclvalue,uslvalue,r_uslvalue " + \
              "FROM tabtrendalertmst " + \
              "WHERE sensorid = '" + str(r) + "'" + \
              "ORDER BY dispstatus"
        cur.execute(sql)
        data2 = cur.fetchall()
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
                                options="-c search_path=otherSchema,ths_proces")
        # 创建游标
        cur = conn.cursor()
        list3 = []
        for i in range(1, 13):
            for j in ['1919', '1920', '017', '016']:
                sql = "SELECT " + \
                      "* " + \
                      "FROM tabkeikodata_everytime " + \
                      "WHERE sensorid = '" + str(r) + "' " + \
                      "AND to_char(editdatetime,'yyyy-MM-dd HH24:MI:ss') LIKE '%2022-" + '%02d' % i + "%' " + \
                      "AND dispstatus = '" + str(j) + "'"
                cur.execute(sql)
                data3 = cur.fetchone()
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
                                options="-c search_path=otherSchema,ths_kspc")
        # 创建游标
        cur = conn.cursor()
        list4 = []
        for i in range(1, 13):
            for j in ['1919', '1920', '017', '016']:
                sql = "SELECT " + \
                      "count(alertstatus) " + \
                      "FROM tabkeikoalert " + \
                      "WHERE sensorid = '" + str(r) + "' " + \
                      "AND to_char(regstdatetime,'yyyy-MM-dd HH24:MI:ss') LIKE '%2022-" + '%02d' % i + "%' " + \
                      "AND alertstatus = '02'" + \
                      "AND dispstatus = '" + str(j) + "'" + \
                      "UNION ALL " + \
                      "SELECT " + \
                      "count(alertstatus) " + \
                      "FROM tabkeikoalert " + \
                      "WHERE sensorid = '" + str(r) + "'" + \
                      "AND to_char(regstdatetime,'yyyy-MM-dd HH24:MI:ss') LIKE '%2022-" + '%02d' % i + "%' " + \
                      "AND alertstatus = '03' " + \
                      "AND dispstatus = '" + str(j) + "'"
                cur.execute(sql)
                data4 = cur.fetchall()
                if str(data4) != 'None':
                    if data4[0][0] != 0:
                        list4.append(data4)
        print(list4)
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()

        s = ""
        # 循环创建一个字符串，把数据库每一条数据作为一行
        for i in range(0, len(list3)):
            dstatus = list3[i][1]
            warn = list4[i][0][0]
            risk = list4[i][1][0]
            repot = warn + risk
            if dstatus == '1919':
                unit = 'V'
                j = list2[0][2]
            elif dstatus == '1920':
                unit = 'A'
                j = list2[0][3]
            elif dstatus == '017':
                unit = 'V'
                j = list2[0][1]
            else:
                unit = 'A'
                j = list2[0][0]
                repot = warn + risk

            # 创建一条数据库记录，记录中每个字段间隔符为table（制表符\t）每一行用换行符\n 隔开下一行
            s += str(list3[i][2]) + \
                 "\t" + str(list1[0][0][0]) + \
                 "\t" + str(r) + \
                 "\t" + str(unit) + \
                 "\t" + str(dstatus) + \
                 "\t" + str(int(list3[i][3])) + ".0" + \
                 "\t" + str(int(list3[i][4])) + ".0" + \
                 "\t" + str(int(list3[i][5])) + ".0" + \
                 "\t" + str(int(list3[i][6])) + ".0" + \
                 "\t" + str(round(int(list3[i][6]) / int(j[3]) * 100, 2)) + \
                 "\t" + str(repot) + \
                 "\t" + str(warn) + \
                 "\t" + str(risk) + \
                 "\t" + str(int(j[1])) + ".0" + \
                 "\t" + str(int(j[2])) + ".0" + \
                 "\t" + str(int(j[3])) + ".0" + \
                 "\t" + str(int(j[4])) + ".0" + \
                 "\t" + str(int(j[5])) + ".0" + \
                 "\t" + str(int(j[6])) + ".0" + \
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
        cur.copy_from(f, 'tabkeikodata_monthlyreport', null='', columns=('targetdate', 'eqpid', 'sensorid', 'unit',
                                                            'dispstatus', 'maximumvalue', 'minimumvalue',
                                                            'differencevalue', 'averagevalue',
                                                            'rate', 'reportcount', 'warningcount', 'riskcount', 'lsl',
                                                            'lcl', 'cl', 'ucl', 'usl', 'r_usl'))
        # 提交
        conn.commit()
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()
        print('成功写入数据库')
    else:
        break
