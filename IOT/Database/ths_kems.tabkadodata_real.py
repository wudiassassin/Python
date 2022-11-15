"""
表名:设备实时状态数据
功能:造8月份的数据
自定义设备ID和时间间隔（固定）
随机采集状态（01:运行/02:停止/03:故障/06:待机）
将最后一条数据的finishdatetime和statustime设为null

表结构：
eqpid	startdatetime	finishdatetime	statustime	sensorstatus
设备ID   开始时间         结束时间          状态时长     采集状态

数据示例：
EM-XL-001	20220803170000	20220803200000	10800	02
"""

import psycopg2
from io import StringIO
import random

while True:
    s = ""
    r = input("请输入设备ID：")
    if r != "exit":
        t = input("请输入时间间隔(1-23)：")
        listj = list(range(0, 24, int(t)))
        listk = list(range(int(t) - 1, 24, int(t)))
        # 循环创建一个字符串，把数据库每一条数据作为一行
        for i in range(1, 32):
            for j, k in zip(listj, listk):
                m = random.choice([1, 2, 3, 6])
                # 创建一条数据库记录，记录中每个字段间隔符为table（制表符\t）每一行用换行符\n 隔开下一行
                s += str(r) +\
                     "\t202208" + '%02d' % i + '%02d' % j + "0000" + \
                     "\t202208" + '%02d' % i + '%02d' % k + "5959" + \
                     "\t" + str(int(t) * 3600-1) + \
                     "\t0" + str(m) + \
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
                                options="-c search_path=otherSchema,ths_kems")
        # 创建游标
        cur = conn.cursor()
        # 将内存对象f中的数据写入数据库，参数columns为所有列的元组
        cur.copy_from(f, 'tabkadodata_real', columns=('eqpid', 'startdatetime', 'finishdatetime', 'statustime',
                                                               'sensorstatus'))
        # 提交
        conn.commit()

        cur = conn.cursor()
        sql = "UPDATE tabkadodata_real SET " + \
              "finishdatetime = NULL," + \
              "statustime = NULL " + \
              "WHERE eqpid = '" + str(r) + "' "\
              "AND finishdatetime = '20220831" + str(listk[-1]) + "5959'"

        cur.execute(sql)
        conn.commit()

        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()
        print('成功写入数据库')
    else:
        break
