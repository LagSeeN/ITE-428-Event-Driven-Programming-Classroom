import sqlite3


def readDemo(db, myParam, order):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_commad = '''SELECT ProductName,UnitPrice FROM Products
                        WHERE UnitPrice >= ? AND UnitPrice <= ?
                        ORDER By UnitPrice {};'''.format(order)
        cursor = conn.execute(sql_commad, myParam)
        found = len(conn.execute(sql_commad, myParam).fetchall())
        print('Found {} Record(s)'.format(found))
        count = 1
        for i in cursor:
            print('{:>3}.) {:<40} : {:>10,.2f} Baht'.format(count, i['ProductName'], i['UnitPrice']))
            count = count + 1


if __name__ == '__main__':
    database = './MyData/Sqlite_Northwind.sqlite3'
    start = 0
    end = 0
    while True:
        start = int(input('Enter start price you want to see  : '))
        end = int(input('Enter end price you want to see  : '))
        if start < end: break
        print('{}'.format('>> Enter price should be more than Start price <<'))
    while True:
        order = int(input('Sort price : [1] Ascending [2] Descending \nSelect [1] or [2] '))
        if order == 1 or order == 2: break
    print()
    p = [start, end]
    readDemo(database, p, 'ASC' if order == 1 else 'DESC')
