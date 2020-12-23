import sqlite3


def readDemo(db, myParam):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_commad = '''SELECT CategoryName, count(ProductId) As 'Count Product', sum(UnitPrice * UnitsInStock) As 'Sum of Value' FROM Categories
                        LEFT OUTER JOIN Products
                        ON Categories.CategoryID = Products.CategoryId
                        GROUP By CategoryName
                        HAVING sum(UnitPrice * UnitsInStock) > ?
                        ORDER By sum(UnitPrice * UnitsInStock); '''
        cursor = conn.execute(sql_commad, myParam)
        found = len(conn.execute(sql_commad, myParam).fetchall())
        print('\nFound {} Category(s)'.format(found))
        count = 1
        for i in cursor:
            print('{}.) {:<20} {:>3} PD. {:>10,.2f} Baht'.format(count, i['CategoryName'], i['Count Product'],
                                                                 i['Sum of Value']))
            count += 1


if __name__ == '__main__':
    database = './MyData/Sqlite_Northwind.sqlite3'
    stockValue = int(input('See Value of Stock by Category > : '))
    p = [stockValue]
    readDemo(database, p)
