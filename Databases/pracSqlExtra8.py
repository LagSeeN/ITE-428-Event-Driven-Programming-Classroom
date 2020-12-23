import sqlite3


def readDemo(db):
    with (sqlite3.connect(db)) as conn:
        conn.row_factory = sqlite3.Row
        sql_commad = '''SELECT Suppliers.CompanyName, Categories.CategoryName, count(ProductId), avg(UnitPrice) FROM Suppliers
                        INNER JOIN Categories,Products
                        ON Products.SupplierId = Suppliers.SupplierID AND Products.CategoryId = Categories.CategoryID
                        GROUP BY 1,2; '''
        cursor = conn.execute(sql_commad)
        for i in cursor:
            print('{} ({}) No.of Product = {} (Average price = {:.2f})'.format(i['CompanyName'],i['CategoryName'],i['count(ProductId)'],i['avg(UnitPrice)']))


if __name__ == '__main__':
    database = './MyData/Sqlite_Northwind.sqlite3'
    readDemo(database)
