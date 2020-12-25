import sqlite3


def readDemo(db):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_commad = '''SELECT Orders.ShipCountry, Count(Orders.OrderId) AS 'No. Order',sum(OrdersDetails.UnitPrice*OrdersDetails.Quantity) AS 'Net Price', sum(OrdersDetails.UnitPrice*OrdersDetails.Quantity)/Count(Orders.OrderId) AS 'Price/Order' FROM OrdersDetails
                        INNER JOIN Orders,Customers
                        ON OrdersDetails.OrderID = Orders.OrderId AND Orders.CustomerId = Customers.CustomerId
                        GROUP BY 1
                        ORDER BY 4 DESC; '''
        cursor = conn.execute(sql_commad)
        print('{}'.format('Show Customer by Sales'))
        print('-'*100)
        print('{:<20} {:<20} {:<20} {:<20}'.format('Country','No.Of Order','NET Price','Price/Order'))
        print('-' * 100)
        for i in cursor:
            print('{:<20} {:>7} {:>23,.2f} {:>20,.2f}'.format(i['ShipCountry'],i['No. Order'],i['Net Price'],i['Price/Order']))


if __name__ == '__main__':
    database = './MyData/Sqlite_Northwind.sqlite3'
    readDemo(database)
