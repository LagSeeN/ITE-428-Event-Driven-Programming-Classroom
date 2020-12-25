import sqlite3


def sqlquery(db):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_commad = '''SELECT Employees.FirstName||' '||Employees.LastName||' , '||Employees.TitleOfCourtesy As 'Name',count(OrderId) As 'Order' FROM Employees
                        LEFT OUTER JOIN Orders
                        ON Employees.EmployeeID = Orders.EmployeeId
                        GROUP By 1
                        ORDER By count(OrderId); '''
        cursor = conn.execute(sql_commad)
        count = 1
        for i in cursor:
            print('{}.) {:<30} {:>10}'.format(count, i['Name'], i['Order']))
            count += 1


if __name__ == '__main__':
    database = './MyData/Sqlite_Northwind.sqlite3'
    sqlquery(database)
