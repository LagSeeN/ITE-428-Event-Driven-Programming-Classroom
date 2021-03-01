#!C:\xampp\htdocs\webapi\venv\Scripts\python.exe
import myDatabase
import json
import cgi

print('Content-type:text/html\n')
form = cgi.FieldStorage()
currentID = form.getvalue('id')
db = myDatabase.connectDatabase()
myCursor = db.cursor()
sql_command = '''SELECT `order details`.`OrderId`,orders.OrderDate,orders.ShipName,products.ProductName,`order details`.`UnitPrice`*`order details`.`Quantity` AS "Price",shippers.CompanyName FROM `order details`
                 INNER JOIN orders ON `order details`.`OrderID` = orders.OrderID
                 INNER JOIN shippers ON orders.ShipVia = shippers.ShipperID
                 INNER JOIN products ON `order details`.`ProductId` = products.ProductID
                 WHERE `order details`.`OrderID` = {}
                 ORDER BY ProductName;'''.format(currentID)
myCursor.execute(sql_command)
rows = myCursor.fetchall()
result = []
for i in rows:
    data = {
        'OrderId': '{}'.format(i['OrderId']),
        'OrderDate': '{}'.format(i['OrderDate']),
        'ShipName': '{}'.format(i['ShipName']),
        'ProductName': '{}'.format(i['ProductName']),
        'Price': '{}'.format(i['Price']),
        'CompanyName': '{}'.format(i['CompanyName'])
    }
    result.append(data)
print(json.dumps(result))
