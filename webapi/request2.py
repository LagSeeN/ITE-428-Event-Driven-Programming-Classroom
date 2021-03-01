#!C:\xampp\htdocs\webapi\venv\Scripts\python.exe
import requests
import json
import cgi

print('Context-type:text/html\n')
form = cgi.FieldStorage()
# webservice = 'https://lagseen.me/webapi/service2.py'
webservice = 'localhost/webapi/service2.py'
sendParameter = {'id': form.getvalue('pid')}
r = requests.get(url=webservice, params=sendParameter)
data = json.loads(r.content)
print('<html>')
print('<head>')
print('<title>My Py Web</title>')
print('<meta charset="UTF-8">')
print('</head>')
print('<style>')
print('''table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 50%;
  margin-left: auto;
  margin-right: auto;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}''')
print('</style>')
print('<body>')
if data.__len__() == 0:
    print('<H1><center>ไม่พบรหัสนี้</center></H1>')
else:
    print('<table>')
    print('<tr>')
    print('<th>{}</th>'.format('ProductID'))
    print('<th>{}</th>'.format('ProductName'))
    print('<th>{}</th>'.format('Price'))
    print('</tr>')
    for y in range(data.__len__()):
        print('<tr>')
        print('<th>{}</th>'.format(data[y]['id']))
        print('<th>{}</th>'.format(data[y]['name']))
        print('<th><p align="right">{:,.2f}<p></th>'.format(float(data[y]['price'])))
        print('</tr>')
    print('</table>')
print('</body>')
print('</html>')
