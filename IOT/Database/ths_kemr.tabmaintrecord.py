"""
表名:维护记录表
功能:造10月份的数据，每天3条
自定义设备ID

表结构：
maintrecordid	companycd	maintno	mainttitle	maintctgry	maintstatus1	maintstatus2	maintplanid	equipcd	equipsite
plannedworkflg	plannedworkstartdate	plannedworkenddate	plannedworkuserid	plannedcost	plannedinformationid
workstartdate	workenddate	workuserid	cost	formcd	formver	approvalflg	approvalid	activeflg	delflg	updateuserid
updatedate	updatecnt	commenceflg	prevmaintrecordid	planneddate	alertid

数据示例：
163	C01	0103181654470001	testData	04	02	00	216	EM-XL-001	EM-XL-001	0	2022-09-09 00:00:00	2022-09-09 00:00:00
0	2022-09-09 00:00:00	2022-09-09 00:00:00			F30001	1	0	0	1	0	admin	2022-09-09 07:33:49.958277	1
1	0	20220909	0
"""
import loc as loc
import psycopg2
from io import StringIO
import random
import time
import radar

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
              "ORDER BY maintrecordid DESC"
        cur.execute(sql)
        data1 = cur.fetchone()
        if str(data1) != 'None':
            list1.append(data1)
        print(list1)
        # 关闭游标
        cur.close()

        # 创建游标
        cur = conn.cursor()
        list2 = []
        sql = "SELECT " + \
              "maintplanid " + \
              "FROM tabmaintplan " + \
              "ORDER BY maintplanid DESC"
        cur.execute(sql)
        data2 = cur.fetchone()
        if str(data2) != 'None':
            list2.append(data2)
        print(list2)
        # 关闭游标
        cur.close()

        k = 1
        for i in range(1, 31):
            # 创建一条数据库记录，记录中每个字段间隔符为table（制表符\t）每一行用换行符\n 隔开下一行
            status = random.choice(['01', '02', '03', '04'])
            if status == '01':
                title = '保养'
            elif status == '02':
                title = '检查'
            elif status == '03':
                title = '修理'
            else:
                title = '故障'
            s += str(list1[0][0] + k) + \
                 "\tC01" + \
                 "\t" + status + "0000000" + '%03d' % k + "0001" + \
                 "\t" + str(r) + title + '%02d' % k + \
                 "\t" + status + \
                 "\t02" + \
                 "\t00" + \
                 "\t" + str(list2[0][0] + k) + \
                 "\t" + str(r) + \
                 "\t" + str(r) + \
                 "\t0" + \
                 "\t2022-10-" + '%02d' % i + " 00:00:00" + \
                 "\t2022-10-" + '%02d' % (i + 1) + " 00:00:00" + \
                 "\t" + \
                 "\t" + \
                 "\t0" + \
                 "\t2022-10-" + '%02d' % i + " " + str(radar.random_time()) + \
                 "\t" + \
                 "\t" +  \
                 "\t" + \
                 "\tF30001" + \
                 "\t1" + \
                 "\t0" + \
                 "\t0" + \
                 "\t0" + \
                 "\t0" + \
                 "\tadmin" + \
                 "\t" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + \
                 "\t1" + \
                 "\t1" + \
                 "\t0" + \
                 "\t202210" + '%02d' % i + \
                 "\t0" + \
                 "\n"
            k = k + 1

        # 创建一个内存对象f,StringIO为存储在内存中的文件，格式为满足文件的任意格式
        f = StringIO()
        # 将s数据字符串写入内存
        f.write(s)
        # 把f的游标移到第一位，write方法后，游标会变成最尾，使用StringIO(**)则不会
        f.seek(0)
        # 创建游标
        cur = conn.cursor()
        # 将内存对象f中的数据写入数据库，参数columns为所有列的元组
        cur.copy_from(f, 'tabmaintrecord', null='',
                      columns=('maintrecordid', 'companycd', 'maintno', 'mainttitle', 'maintctgry',
                               'maintstatus1', 'maintstatus2', 'maintplanid', 'equipcd', 'equipsite',
                               'plannedworkflg', 'plannedworkstartdate', 'plannedworkenddate',
                               'plannedworkuserid', 'plannedcost', 'plannedinformationid', 'workstartdate',
                               'workenddate', 'workuserid', 'cost', 'formcd', 'formver', 'approvalflg',
                               'approvalid', 'activeflg', 'delflg', 'updateuserid', 'updatedate',
                               'updatecnt', 'commenceflg', 'prevmaintrecordid', 'planneddate', 'alertid'))
        # 提交
        conn.commit()
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()
        print('成功写入数据库')
    else:
        break
