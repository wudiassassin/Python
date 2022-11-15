"""
表名:
cnc_flame_cm：数控火焰切割机数据表
electric_energy：电能表解析数据表
flowmeter：流量计数据表
four_roll_plate_machine：四星辊卷板机数据表
paint_sprayer：喷漆机(内壁、外壁)数据表
sa_sand_blasting_room：半自动喷砂房数据表
sandblasting：喷砂(内抛、外抛)数据表
three_roll_plate_machine：三星辊卷板机数据表
vocs_exhaust：VOCs废气排风数据表
weld_platform：焊接平台数据表
weld_trolley：焊接小车数据表

功能:造8月份的数据，2分钟间隔
选择往哪张采集器种类表里插数据
自定义采集器编号
数据的[项目CD，项目名称，单位] 和 项目值随机

表结构：
eqpid	 eqpname	 receivetime	itemcode	itemname	itemvalue	unit	isreadflg
设备id   设备名称      接收时间         项目CD      项目名称      项目值       单位     已读标识(0:未读,1:已读)

数据示例：
EM-XL-001	数控火焰切割机1#	2022-07-08 23:51:47.779884	017	焊接电压	38.20000000	V
"""

import psycopg2
from io import StringIO
import random
import sys

while True:
    s = ""
    print("1.cnc_flame_cm：数控火焰切割机数据表")
    print("2.electric_energy：电能表解析数据表")
    print("3.flowmeter：流量计数据表")
    print("4.four_roll_plate_machine：四星辊卷板机数据表")
    print("5.paint_sprayer：喷漆机(内壁、外壁)数据表")
    print("6.sa_sand_blasting_room：半自动喷砂房数据表")
    print("7.sandblasting：喷砂(内抛、外抛)数据表")
    print("8.three_roll_plate_machine：三星辊卷板机数据表")
    print("9.vocs_exhaust：VOCs废气排风数据表")
    print("10.weld_platform：焊接平台数据表")
    print("11.weld_trolley：焊接小车数据表")
    print("12.exit：退出")
    q = input("请选择采集器种类：")
    if q == "1":
        q = 'cnc_flame_cm'
    elif q == "2":
        q = 'electric_energy'
    elif q == "3":
        q = 'flowmeter'
    elif q == "4":
        q = 'four_roll_plate_machine'
    elif q == "5":
        q = 'paint_sprayer'
    elif q == "6":
        q = 'sa_sand_blasting_room'
    elif q == "7":
        q = 'sandblasting'
    elif q == "8":
        q = 'three_roll_plate_machine'
    elif q == "9":
        q = 'vocs_exhaust'
    elif q == "10":
        q = 'weld_platform'
    elif q == "11":
        q = 'weld_trolley'
    else:
        sys.exit()

    r = input("请输入设备ID：")
    if r != "exit":
        conn = psycopg2.connect(host='192.168.2.17',
                                port='5432',
                                user="postgres",
                                password="123456",
                                database="iot-mgmt",
                                options="-c search_path=otherSchema,ths_system")
        # 创建游标
        cur = conn.cursor()
        listr = []
        sql = "SELECT " + \
               "sensorname " + \
               "FROM tabsensormst " + \
               "WHERE sensorid = '" + str(r) + "' "
        cur.execute(sql)
        data = cur.fetchall()
        listr.append(data[0][0])
        print(listr[0])
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()

        listj = [('1919', '电压', 'V'), ('1920', '电流', 'A'), ('017', '焊接电压', 'V'), ('016', '焊接电流', 'A')]
        listk = [(200, 210, 220, 230), (5, 10, 15, 20), (200, 210, 220, 230), (5, 10, 15, 20)]
        # 循环创建一个字符串，把数据库每一条数据作为一行
        for i_1 in range(1, 32,2):
            for i_2 in range(0, 24):
                for i_3 in range(0, 60,60):
                    m = random.choice([0, 1, 2, 3])
                    n = random.choice([0, 1, 2, 3])
                    # 创建一条数据库记录，记录中每个字段间隔符为table（制表符\t）每一行用换行符\n 隔开下一行
                    s += str(r) + \
                         "\t" + str(listr[0]) + \
                         "\t2022-08-" + '%02d' % i_1 + " " + '%02d' % i_2 + ":" + '%02d' % i_3 + ":00" + \
                         "\t" + str(listj[m][0]) + \
                         "\t" + str(listj[m][1]) + \
                         "\t" + str(listk[m][n]) + \
                         "\t" + str(listj[m][2]) + \
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
                                options="-c search_path=otherSchema,ths_analyze")
        # 创建游标
        cur = conn.cursor()
        # 将内存对象f中的数据写入数据库，参数columns为所有列的元组
        cur.copy_from(f, q, null='', columns=('eqpid', 'eqpname', 'receivetime', 'itemcode',
                                                               'itemname', 'itemvalue', 'unit', 'isreadflg'))
        # 提交
        conn.commit()
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()
        print('成功写入数据库')
    else:
        break
