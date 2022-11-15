"""
表名:维护记录表ex
功能:从ths_kemr.tabmaintrecord获取maintctgry=02的maintrecordid
自定义设备ID

表结构：
maintrecordid	exitemkey	exitemseq	exvalue	excomment	delflg	updateuserid	updatedate	updatecnt

数据示例：
252	OilLevel001	1	38		0	sys		1
"""

import psycopg2
from io import StringIO
import random

while True:
    s = ""
    r = input("请输入设备ID：")
    if r != "exit":
        # 连接数据库
        conn = psycopg2.connect(host='192.168.2.17',
                                port='5432',
                                user="postgres",
                                password="123456",
                                database="iot-mgmt",
                                options="-c search_path=otherSchema,ths_kemr")
        # 创建游标
        cur = conn.cursor()
        list1 = []
        sql = "SELECT " + \
              "maintrecordid " + \
              "FROM tabmaintrecord " + \
              "WHERE equipcd = '" + str(r) + "' " + \
              "AND maintctgry = '02'"
        cur.execute(sql)
        data1 = cur.fetchall()
        if str(data1) != 'None':
            list1.append(data1)
        print(list1)
        # 关闭游标
        cur.close()

        for i in range(0, int(len(list1[0]))):
            for j in ['OilUse001', 'OilLevel001']:
                exvalue = random.choice(range(0, 100))
                # 创建一条数据库记录，记录中每个字段间隔符为table（制表符\t）每一行用换行符\n 隔开下一行
                s += str(int(list1[0][i][0])) + \
                     "\t" + j + \
                     "\t1" + \
                     "\t" + str(exvalue) + \
                     "\t" + \
                     "\t0" + \
                     "\tsys" + \
                     "\t" + \
                     "\t1" + \
                     "\n"
        # 创建一个内存对象f,StringIO为存储在内存中的文件，格式为满足文件的任意格式
        f = StringIO()
        # 将s数据字符串写入内存
        f.write(s)
        # 把f的游标移到第一位，write方法后，游标会变成最尾，使用StringIO(**)则不会
        f.seek(0)
        # 创建游标
        cur = conn.cursor()
        # 将内存对象f中的数据写入数据库，参数columns为所有列的元组
        cur.copy_from(f, 'tabmaintrecordex', null='', columns=('maintrecordid', 'exitemkey', 'exitemseq', 'exvalue', 'excomment',
                                                    'delflg', 'updateuserid', 'updatedate', 'updatecnt'))
        # 提交
        conn.commit()
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()
        print('成功写入数据库')
    else:
        break
