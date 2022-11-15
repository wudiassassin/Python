import pymysql


def database():
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print('Database version:', data)
    cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
    db.close()


def table():
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
    cursor = db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, ' \
          'age INT NOT NULL, PRIMARY KEY (id ))'
    cursor.execute(sql)
    db.close()


def insert():
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
    cursor = db.cursor()

    data = {
        'id': '20120002',
        'name': 'Bob',
        'age': 20
    }
    table = 'students'
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    print(sql)
    try:
        if cursor.execute(sql, tuple(data.values())):
            print('Successful')
            db.commit()
    except:
        print('Failed')
        db.rollback()
    db.close()


def update():
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
    cursor = db.cursor()

    data = {
        'id': '20120002',
        'name': 'jordan',
        'age': 21
    }
    table = 'students'
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
                                                                                          values=values)
    update = ','.join([" {key} = %s".format(key=key) for key in data])
    sql += update
    print(sql)
    try:
        if cursor.execute(sql, tuple(data.values())*2):
            print('Successful')
            db.commit()
    except:
        print('Failed')
        db.rollback()
    db.close()


def delete():
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
    cursor = db.cursor()

    table = 'students'
    condition = 'age > 20'
    sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
    print(sql)
    try:
        if cursor.execute(sql):
            print('Successful')
            db.commit()
    except:
        print('Failed')
        db.rollback()
    db.close()


def select():
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
    cursor = db.cursor()

    table = 'students'
    field = '*'
    condition = 'age >= 20'
    sql = 'SELECT {field} FROM {table} WHERE {condition}'.format(table=table, field=field, condition=condition)
    print(sql)
    try:
        cursor.execute(sql)
        print('Count:', cursor.rowcount)
        row = cursor.fetchone()
        while row:
            print('Row:', row)
            row = cursor.fetchone()
    except:
        print('Error')
    db.close()


select()
