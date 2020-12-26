import sqlite3


def sqlquery(db, myParam):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''SELECT * FROM Products  WHERE ProductId = ?'''
        print('Product Name\t: {}'.format(conn.execute(sql_command, myParam).fetchone()['ProductName']))
        print('Price\t\t\t: {}'.format(conn.execute(sql_command, myParam).fetchone()['UnitPrice']))
        print('Stock\t\t\t: {}'.format(conn.execute(sql_command, myParam).fetchone()['UnitsInStock']))


def checkdata(db, p):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''SELECT EXISTS(SELECT * FROM Products WHERE ProductId = ?);'''
        return conn.execute(sql_command, p).fetchone()[0]


def stopProduct(db, p):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_command = '''UPDATE Products
                         SET Discontinued = 1
                         WHERE ProductId = ?;'''
        conn.execute(sql_command, p)
        conn.commit()


if __name__ == '__main__':
    database = './MyData/Sqlite_Northwind.sqlite3'
    Value = int(input('กรุณากรอกรหัสสินค้า : '))
    p = [Value]
    if checkdata(database, p):
        sqlquery(database, p)
        stopSale = True if input('ต้องการหยุดขายสินค้าหรือไม่ [Yes/No] : ').lower() == 'yes' else False
        if stopSale:
            stopProduct(database, p)
            print('{}'.format('หยุดขายเสร็จแล้ว'))
    else:
        print('{}'.format('ไม่มีรหัสสินค้านี้'))
