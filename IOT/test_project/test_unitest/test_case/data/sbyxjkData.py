from test_case.data.database import Database


class sbyxjkdata(Database):

    ths_system = 'ths_system'
    ths_kems = 'ths_kems'

    # 定义查询数据库设备ID和状态
    def eqp_sta_data(self, eqpgrpid):
        """根据输入的设备组ID，查询对应的所有设备ID"""
        conn = self.conn_database(self.ths_system)
        cur = conn.cursor()
        sql = "SELECT " + \
              "eqpid " + \
              "FROM tabeqp " + \
              "WHERE eqpgrpid = '" + eqpgrpid + "' " + \
              "ORDER BY eqpid"
        cur.execute(sql)
        eqpid_data = cur.fetchall()
        cur.close()
        conn.close()

        """根据设备ID，查询对应的状态"""
        conn = self.conn_database(self.ths_kems)
        cur = conn.cursor()
        list_sbyxjk_data = []
        for i in range(int(len(eqpid_data))):
            sql = "SELECT " + \
                  "eqpid,sensorstatus " + \
                  "FROM tabkadodata_real " + \
                  "WHERE eqpid = '" + eqpid_data[i][0] + "' " + \
                  "AND finishdatetime is NULL " + \
                  "ORDER BY eqpid"
            cur.execute(sql)
            status_data = cur.fetchall()
            if status_data:
                # 将状态转为颜色
                if status_data[0][1] == '01':
                    col = 'lime'
                elif status_data[0][1] == '02':
                    col = 'silv'
                elif status_data[0][1] == '03':
                    col = 'red;'
                else:
                    col = 'blue'
                list_sbyxjk_data.append((eqpid_data[i][0], col))
            else:
                list_sbyxjk_data.append((eqpid_data[i][0], 'silv'))
        cur.close()
        conn.close()

        return list_sbyxjk_data, len(list_sbyxjk_data)
