#!C:\xampp\htdocs\webapi\venv\Scripts\python.exe
import myDatabase
import json
import cgi

print('Content-type:text/html\n')
form = cgi.FieldStorage()
currentID = form.getvalue('id')
db = myDatabase.connectDatabase()
myCursor = db.cursor()
sql_command = 'select ProductID, ProductName, UnitPrice from products where ProductID = {}'.format(currentID)
myCursor.execute(sql_command)
rows = myCursor.fetchall()
result = []
for i in rows:
    data = {
        'id': '{}'.format(i['ProductID']),
        'name': '{}'.format(i['ProductName']),
        'price': '{}'.format(i['UnitPrice'])
    }
    result.append(data)
print(json.dumps(result))
