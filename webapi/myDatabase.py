import pymysql


def connectDatabase():
    myDB = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='northwind_mysql_python',
        cursorclass=pymysql.cursors.DictCursor
    )
    return myDB
