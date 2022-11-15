import psycopg2


class Database(object):
    """
    数据库基础类，用于所有表的继承
    """

    # 初始化连结数据库参数
    def __init__(self, host='192.168.2.17', port='5432',
                 user='postgres', password='123456',
                 database='iot-mgmt', options='-c search_path=otherSchema,'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.options = options

    # 定义数据库连接
    def conn_database(self, Schema):
        return psycopg2.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database,
                                   options=self.options+Schema)
