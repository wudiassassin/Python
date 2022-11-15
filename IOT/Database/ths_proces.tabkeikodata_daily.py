"""
表名:每日采集数据表
功能:从tabkeikodata_everytime获取8月的每日的第一条数据插入
自定义采集器ID

表结构：
sensorid	dispstatus	targetdate	maximumvalue	minimumvalue	differencevalue	averagevalue	parameter	triggersensorid	startdatetime	enddatetime	sumvalue

数据示例：
EM-XL-001  1919	 2022-02-17 16:06:55	42.00000000	-8.00000000	50.00000000	17.00000000	0
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
                                options="-c search_path=otherSchema,ths_proces")
        # 创建游标
        cur = conn.cursor()
        list1 = []
        for i in range(1, 32):
            for j in ['1919', '1920', '017', '016']:
                sql = "SELECT " + \
                      "* " + \
                      "FROM tabkeikodata_everytime " + \
                      "WHERE sensorid = '" + str(r) + "' " + \
                      "AND to_char(editdatetime,'yyyy-MM-dd HH24:MI:ss') LIKE '%2022-08-" + '%02d' % i + "%' " + \
                      "AND dispstatus = '" + str(j) + "'"
                cur.execute(sql)
                data = cur.fetchone()
                if str(data) != 'None':
                    list1.append(data)
        print(list1)

        s = ""
        # 循环创建一个字符串，把数据库每一条数据作为一行
        for i in range(0, len(list1)):
            # 创建一条数据库记录，记录中每个字段间隔符为table（制表符\t）每一行用换行符\n 隔开下一行
            s += str(r) + \
                 "\t" + str(list1[i][1]) + \
                 "\t" + str(list1[i][2]) + \
                 "\t" + str(list1[i][3]) + \
                 "\t" + str(list1[i][4]) + \
                 "\t" + str(list1[i][5]) + \
                 "\t" + str(list1[i][6]) + \
                 "\t" + str(list1[i][7]) + \
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
        # 将内存对象f中的数据写入数据库，参数columns为所有列的元组
        cur.copy_from(f, 'tabkeikodata_daily', null='', columns=('sensorid', 'dispstatus', 'targetdate', 'maximumvalue',
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
