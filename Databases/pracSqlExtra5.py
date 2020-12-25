import sqlite3


def sqlquery(db, myParam):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_commad = '''SELECT *,UnitPrice * UnitsInStock AS 'Value in Stock' FROM Products
                        WHERE  UnitPrice * UnitsInStock > ? '''
        cursor = conn.execute(sql_commad,myParam)
        for i in cursor:
            print('ID : {}'.format(i['productid']))
            print('Product Name : {}'.format(i['productname']))
            print('Stock Value : {:,.2f}'.format(i['Value in Stock']))
            print('-' * 50)

if __name__ == '__main__':
    database = './MyData/Sqlite_Northwind.sqlite3'
    stockValue = int(input('Input StockValue to want : '))
    p = [stockValue]
    sqlquery(database, p)
