"""
表名:维护计划表
功能:从ths_kemr.tabmaintrecord获取数据
自定义设备ID

表结构：
maintplanid	companycd	maintplanno	maintplantitle	maintctgry	equipcd	equipsite	startdate	enddate	repeattype
repeatvalue1	repeatvalue2	formcd	plannedstarttime	plannedworktime	plannedworkuserid	plannedcost	plannedcomment
infoneedflg	infocomment	autogenerateflg	approvalflg	approvalid	activeflg	delflg	updateuserid	updatedate	updatecnt

数据示例：
221	C01		标题	01	EM-XL-002	部位	2022-09-29 00:00:00	2022-09-30 00:00:00	0							2		1
通知信息	0	0	0	0	0			0
"""

import psycopg2
from io import StringIO
import random
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
              "* " + \
              "FROM tabmaintrecord " + \
              "WHERE equipcd = '" + str(r) + "' " + \
              "ORDER BY maintrecordid"
        cur.execute(sql)
        data1 = cur.fetchall()
        if str(data1) != 'None':
            list1.append(data1)
        print(list1)
        # 关闭游标
        cur.close()
        for i in range(len(list1[0])):
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
            s += str(int(list1[0][i][7])) + \
                 "\tC01" + \
                 "\t" + (list1[0][i][2])[0:12] + \
                 "\t" + list1[0][i][3] + \
                 "\t" + list1[0][i][4] + \
                 "\t" + list1[0][i][8] + \
                 "\t" + list1[0][i][9] + \
                 "\t" + str(list1[0][i][11]) + \
                 "\t" + str(list1[0][i][12]) + \
                 "\t0" + \
                 "\t" + \
                 "\t" + \
                 "\t" + list1[0][i][20] + \
                 "\t0" + \
                 "\t0" + \
                 "\t" + \
                 "\t" + \
                 "\t" + \
                 "\t0" + \
                 "\t" + \
                 "\t0" + \
                 "\t0" + \
                 "\t0" + \
                 "\t1" + \
                 "\t0" + \
                 "\t" + list1[0][i][26] + \
                 "\t" + str(list1[0][i][27]) + \
                 "\t0" + \
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
        cur.copy_from(f, 'tabmaintplan', null='',
                      columns=('maintplanid', 'companycd', 'maintplanno', 'maintplantitle', 'maintctgry',
                               'equipcd', 'equipsite', 'startdate', 'enddate', 'repeattype',
                               'repeatvalue1', 'repeatvalue2', 'formcd', 'plannedstarttime', 'plannedworktime',
                               'plannedworkuserid', 'plannedcost', 'plannedcomment', 'infoneedflg',
                               'infocomment', 'autogenerateflg', 'approvalflg', 'approvalid', 'activeflg', 'delflg',
                               'updateuserid', 'updatedate', 'updatecnt'))
        # 提交
        conn.commit()
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        conn.close()
        print('成功写入数据库')
    else:
        break
