import psycopg2


# 定义查询数据库时间
def jjt_data():
    conn = psycopg2.connect(host='192.168.2.17',
                            port='5432',
                            user="postgres",
                            password="123456",
                            database="iot-mgmt",
                            options="-c search_path=otherSchema,ths_kems")
    cur = conn.cursor()
    list_jjt_data = []
    for i in ['01', '06', '02', '03']:
        sql = "SELECT " + \
              "CAST(totaltime as INT) " + \
              "FROM tabkadodata_daily " + \
              "WHERE eqpid = 'EM-XL-001' " + \
              "AND targetdate = '20220801' " + \
              "AND sensorstatus = '" + i + "'"
        cur.execute(sql)
        data = cur.fetchall()
        # 将时间转为小时，四舍五入保留一位小数
        list_jjt_data.append(str(round(data[0][0] / 3600, 1)))
    # 将时间转换为小时
    cur.close()
    conn.close()
    return list_jjt_data
