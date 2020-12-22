import sqlite3


def readDemo(db, myParam):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_commad = '''SELECT ProductName,UnitPrice,CategoryName FROM Products
                        LEFT OUTER JOIN Categories
                        ON Categories.CategoryID = Products.CategoryId
                        WHERE Categories.CategoryName like ?
                        ORDER By ProductName;'''
        cursor = conn.execute(sql_commad, myParam)
        found = len(conn.execute(sql_commad, myParam).fetchall())
        print('{} Found {} Record(s)'.format(myParam[0],found))
        count = 1
        for i in cursor:
            print('{:>3}.) {:<40} : {:>10,.2f} Baht'.format(count,i['ProductName'],i['UnitPrice']))
            count = count + 1


if __name__ == '__main__':
    database = './MyData/Sqlite_Northwind.sqlite3'
    category = input('Enter your category name to see  : ')
    print()
    p = [category]
    readDemo(database, p)
