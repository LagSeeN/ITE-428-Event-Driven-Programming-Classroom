import sqlite3


def sqlquery(db):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_commad = '''SELECT DISTINCT Country,count(*) As No FROM Suppliers  
                        GROUP BY Country 
                        ORDER By No DESC'''
        cursor = conn.execute(sql_commad)
        print('{:<15} {:<15}'.format('Supplier','No. of Company'))
        print('-'*50)
        for i in cursor:
            print('{:<20} {:<30}'.format(i['Country'],i['No']))



if __name__ == '__main__':
    database = './MyData/Sqlite_Northwind.sqlite3'
    sqlquery(database)
