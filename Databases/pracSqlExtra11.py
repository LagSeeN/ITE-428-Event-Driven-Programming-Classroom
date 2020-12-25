import sqlite3


def sqlquery(db):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_commad = '''SELECT  *,UnitPrice-(SELECT avg(UnitPrice) FROM Products) AS 'More AVG' FROM Products 
                        WHERE UnitPrice > (SELECT avg(UnitPrice) FROM Products) 
                        GROUP By ProductId 
                        ORDER BY UnitPrice DESC; '''
        cursor = conn.execute(sql_commad)
        print('-'*100)
        print('{:<3} {:<45} {:<20} {:<20}'.format('รหัส','สินค้า','ราคาสินค้า','ราคาสูงกว่าราคาเฉลี่ย'))
        print('-' * 100)
        for i in cursor:
            print('{:<3} {:<40} {:>10,.2f} {:>15,.2f}'.format(i['ProductID'],i['ProductName'],i['UnitPrice'],i['More AVG']))


if __name__ == '__main__':
    database = './MyData/Sqlite_Northwind.sqlite3'
    sqlquery(database)
