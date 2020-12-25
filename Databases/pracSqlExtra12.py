import sqlite3


def sqlquery(db, myParam):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_commad = '''SELECT Products.ProductId,Products.ProductName,count(OrdersDetails.OrderID) AS "Count" FROM Products
                        INNER JOIN OrdersDetails
                        ON OrdersDetails.ProductId = Products.ProductID
                        GROUP BY Products.ProductName
                        HAVING "Count" > ?;'''
        cursor = conn.execute(sql_commad, myParam)
        found = len(conn.execute(sql_commad, myParam).fetchall())
        print('Found = {}'.format(found))
        print('-' * 50)
        print('{:<2} {}'.format('รหัส','สินค้า'))
        print('-' * 50)
        for i in cursor:
            print('{:<2} {}'.format(i['productid'], i['productname']))


if __name__ == '__main__':
    database = './MyData/Sqlite_Northwind.sqlite3'
    Value = int(input('กรอกจำนวนที่สินค้าขายได้มากกว่า : '))
    p = [Value]
    sqlquery(database, p)
