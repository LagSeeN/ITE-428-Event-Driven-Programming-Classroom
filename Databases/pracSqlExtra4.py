import sqlite3


def sqlquery(db):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_commad = '''SELECT DISTINCT Region,count(DISTINCT Country) As Country ,count(DISTINCT City) As City FROM Customers 
                        GROUP By Region 
                        ORDER By City DESC'''
        cursor = conn.execute(sql_commad)
        print('{}'.format('Show Customers by Region'))
        print('-' * 50)
        print('{:<25} {:<15} {:<15}'.format('Region', 'Country','City'))
        print('-' * 50)
        for i in cursor:
            print('{:<30} {:<10} {:<15}'.format(i['Region'], i['Country'],i['City']))


if __name__ == '__main__':
    database = './MyData/Sqlite_Northwind.sqlite3'
    sqlquery(database)
