import sqlite3


def readDemo(db, myParam):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_commad = '''SELECT *,UnitPrice * UnitsInStock AS 'Value in Stock' FROM Products
                        WHERE UnitPrice > ? 
                        AND UnitsInStock < ?
                        ORDER By UnitPrice DESC'''
        cursor = conn.execute(sql_commad, myParam)
        found = len(conn.execute(sql_commad, myParam).fetchall())
        print('FOUND = {}'.format(found))
        count = 1
        for i in cursor:
            print('No.{}'.format(count))
            print('Product ID\t\t: {}'.format(i['productid']))
            print('Product Name\t: {}'.format(i['productname']))
            print('Unit Price\t\t: {:,.2f}'.format(i['unitprice']))
            print('Stock\t\t\t: {:,.2f}'.format(i['unitsinstock']))
            print('Value in Stock  : {:,.2f}'.format(i['Value in Stock']))
            print('-' * 50)
            count = count + 1

def newCategories(db,myParam):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_commad = '''INSERT INTO "Categories" VALUES (?,?,?);'''
        conn.execute(sql_commad,myParam)
        conn.commit()

if __name__ == '__main__':
    database = './MyData/Sqlite_Northwind.sqlite3'
    # unitprice = input('Input UnitPrice > to want : ')
    # unitsinstock = input('Input UnitsInStock < to want : ')
    # p = [unitprice, unitsinstock]
    # readDemo(database, p)
    newCategories(database,[10,'Computer','PC Accessory'])
