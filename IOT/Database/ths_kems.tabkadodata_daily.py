"""
表名:设备每日状态统计数据
功能:造8月份的数据
自定义设备ID
采集状态、状态时长和状态次数从表TabKadoData_Real获取

表结构：
eqpid	targetdate	sensorstatus	totaltime	totalcount
设备ID   日期         采集状态         状态时长     状态次数

数据示例：
EM-XL-001	20220528	01	4941	7
"""

import psycopg2
from io import StringIO

while True:
    r = input("请输入设备ID：")
    if r != "exit":
        # 连接数据库
        conn = psycopg2.connect(host='192.168.2.17',
                                port='5432',
                                user="postgres",
                                password="123456",
                                database="iot-mgmt",
                                options="-c search_path=otherSchema,ths_kems")
        # 创建游标
        cur = conn.cursor()
        list1 = []
        for i in range(1, 32):
            for j in [1, 2, 3, 6]:
                sql1 = "SELECT " + \
                      "count(*) " + \
                      "FROM tabkadodata_real " + \
                      "WHERE eqpid = '" + str(r) + "' " + \
                      "AND startdatetime LIKE '%202208" + '%02d' % i + "%'" + \
                      "AND sensorstatus = '0" + str(j) + "'"
                cur.execute(sql1)
                data1 = cur.fetchall()
                list1.append(data1[0][0])
        print(list1)

        list2 = []
        sql2 = "SELECT " + \
              "statustime " + \
              "FROM tabkadodata_real " + \
              "WHERE eqpid = '" + str(r) + "' " + \
              "AND startdatetime = '20220801000000'"
        cur.execute(sql2)
        data2 = cur.fetchall()
        list2.append(data2[0][0])
        print(list2[0])

        s = ""
        # 创建一个[1,1,1,1,2,2,2,2...31,31,31,31]的列表
        list3 = []
        for i in range(1, 32):
            for j in range(4):
                list3.append(i)
        print(list3)
        # 循环创建一个字符串，把数据库每一条数据作为一行
        for i, j, k in zip(list3, [1, 2, 3, 6] * 31, list1):
            # 创建一条数据库记录，记录中每个字段间隔符为table（制表符\t）每一行用换行符\n 隔开下一行
            s += str(r) + \
                 "\t202208" + '%02d' % i + \
                 "\t0" + str(j) + \
                 "\t" + str(list2[0] * k) + \
                 "\t" + str(k) + \
                 "\n"
        # 创建一个内存对象f,StringIO为存储在内存中的文件，格式为满足文件的任意格式
        f = StringIO()
        # 将s数据字符串写入内存
        f.write(s)
        # 把f的游标移到第一位，write方法后，游标会变成最尾，使用StringIO(**)则不会
        f.seek(0)
        # 将内存对象f中的数据写入数据库，参数columns为所有列的元组
        cur.copy_from(f, 'tabkadodata_daily', columns=('eqpid', 'targetdate', 'sensorstatus', 'totaltime',
                                                       'totalcount'))
        # 提交
        conn.commit()
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()
        print('成功写入数据库')
    else:
        break
