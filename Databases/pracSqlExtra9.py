import sqlite3


def sqlquery(db, myParam):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_commad = '''SELECT * FROM report_order
                        WHERE OrderId = ?
                        ORDER BY ProductName'''
        cursor = conn.execute(sql_commad, myParam)
        print('Order ID\t: {}'.format(conn.execute(sql_commad, myParam).fetchone()['OrderID']))
        print('Order Date\t: {}'.format(conn.execute(sql_commad, myParam).fetchone()['OrderDate']))
        print('Customer\t: {}'.format(conn.execute(sql_commad, myParam).fetchone()['ShipName']))
        print('-' * 60)
        count = 1
        total = 0
        for i in cursor:
            print('{:<2}.) {:<35} {:>10,.2f}'.format(count, i['ProductName'], i['Price']))
            count += 1
            total += i['Price']
        print('-' * 60)
        print('{:>26} TOTAL PRICE : {:>10,.2f}'.format('', total))
        print('{:>26} VAT (7%)    : {:>10,.2f}'.format('', total * 0.07))
        print('{:>26} NET PRICE   : {:>10,.2f}'.format('', total * 1.07))
        print('-' * 60)
        print('Send by : {}'.format(conn.execute(sql_commad, myParam).fetchone()['CompanyName']))


def createView(db):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_commad = '''CREATE VIEW IF NOT EXISTS report_order AS SELECT OrdersDetails.OrderId,Orders.OrderDate,Orders.ShipName,Products.ProductName,OrdersDetails.UnitPrice*OrdersDetails.Quantity AS "Price",Shippers.CompanyName FROM OrdersDetails
                        INNER JOIN Orders,Shippers,Products
                        ON OrdersDetails.OrderID = Orders.OrderId AND OrdersDetails.ProductId = Products.ProductID AND Orders.ShipVia = Shippers.ShipperID;'''
        conn.execute(sql_commad)


if __name__ == '__main__':
    database = './MyData/Sqlite_Northwind.sqlite3'
    Value = int(input('กรุณากรอก Order ID ที่ต้องการดูข้อมูล : '))
    p = [Value]
    createView(database)
    sqlquery(database, p)
    print()
