import pymssql
import time

connect = pymssql.connect('192.168.2.38', 'sa', '123456', 'iot-mgmt')  # 建立连接
if connect:
    print("begin at:", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

cursor = connect.cursor()

insert = "INSERT INTO ths_system.test(id, name) VALUES ('{}', '{}')"

start = 1
for i in range(1000000):
    id = start + i
    name = "test" + str(id)
    sql = insert.format(id, name)
    cursor.execute(sql)  # 执行sql语句
    connect.commit()

cursor.close()
connect.close()

print("complete at:", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
