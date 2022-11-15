"""
表名:采集器属性表
功能:添加采集器属性
自定义设备ID
随机interval

表结构：
sensorgrpid	 prep_cd	prep_name	remarks	 updateuserid	 updatedate	 interval
采集器租ID    属性CD      属性名称      备注     更新者            更新时间     采集间隔（秒）

数据示例：
SKQGJ-TP	1919	电压				30
"""

import psycopg2
from io import StringIO
import random

while True:
    s = ""
    r = input("请输入采集器组ID：")
    if r != "exit":
        listj = ['1919', '1920', '017', '016']
        listk = ['电压', '电流', '焊接电压', '焊接电流']
        # 循环创建一个字符串，把数据库每一条数据作为一行
        for j, k in zip(listj, listk):
            m = random.choice([30, 60, 90, 120])
            # 创建一条数据库记录，记录中每个字段间隔符为table（制表符\t）每一行用换行符\n 隔开下一行
            s += str(r) + \
                 "\t" + str(j) + \
                 "\t" + str(k) + \
                 "\t" + \
                 "\t" + \
                 "\t" + \
                 "\t" + str(m) + \
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
        cur.copy_from(f, 'tabsensorprep', null='', columns=('sensorgrpid', 'prep_cd', 'prep_name', 'remarks',
                                                               'updateuserid', 'updatedate', 'interval'))
        # 提交
        conn.commit()
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()
        print('成功写入数据库')
    else:
        break
