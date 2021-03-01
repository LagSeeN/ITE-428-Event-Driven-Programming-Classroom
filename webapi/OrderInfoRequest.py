#!C:\xampp\htdocs\webapi\venv\Scripts\python.exe
import requests
import json
import cgi
import datetime

print('Context-type:text/html\n')
form = cgi.FieldStorage()
# webservice = 'https://lagseen.me/webapi/OrderInfoService.py'
webservice = 'localhost/webapi/OrderInfoService.py'
sendParameter = {'id': form.getvalue('oid')}
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
    print('<H1><center>ไม่มีข้อมูล Order ID ดังกล่าว</center></H1>')
else:
    print('<table>')
    print('<tr>')
    print('<th colspan="1">{}</th>'.format('Order ID\t:'))
    print('<th colspan="3">{}</th>'.format(data[0]['OrderId']))
    print('</tr>')
    print('<tr>')
    print('<th colspan="1">{}</th>'.format('Order Date\t:'))
    print('<th colspan="3">{}</th>'.format(data[0]['OrderDate'].split(" ")[0]))
    print('</tr>')
    print('<tr>')
    print('<th colspan="1">{}</th>'.format('Customer\t:'))
    print('<th colspan="3">{}</th>'.format(data[0]['ShipName']))
    print('</tr>')
    print('<tr>')
    print('<th colspan="4">{}</th>'.format('<hr>'))
    print('</tr>')
    count = 1
    total = 0
    for y in range(data.__len__()):
        print('<tr>')
        print('<th colspan="3">{}.) {}</th>'.format(count, data[y]['ProductName']))
        print('<th colspan="1"><p align="right">{:,.2f}<p></th>'.format(float(data[y]['Price'])))
        print('</tr>')
        count += 1
        total += float(data[y]['Price'])
    print('</tr>')
    print('<tr>')
    print('<th colspan="4">{}</th>'.format('<hr>'))
    print('</tr>')
    print('<tr>')
    print('<th colspan="2"><p align="right">{}<p></th>'.format('TOTAL PRICE\t:'))
    print('<th colspan="2"><p align="right">{:,.2f}<p></th>'.format(total))
    print('</tr>')
    print('<tr>')
    print('<th colspan="2"><p align="right">{}<p></th>'.format('VAT (7%)\t:'))
    print('<th colspan="2"><p align="right">{:,.2f}<p></th>'.format(total * 0.07))
    print('</tr>')
    print('<tr>')
    print('<th colspan="2"><p align="right">{}<p></th>'.format('NET PRICE\t:'))
    print('<th colspan="2"><p align="right">{:,.2f}<p></th>'.format(total * 1.07))
    print('</tr>')
    print('<tr>')
    print('<th colspan="4">{}</th>'.format('<hr>'))
    print('</tr>')
    print('<tr>')
    print('<th colspan="4">Send by : {}</th>'.format(data[0]['CompanyName']))
    print('</tr>')
    print('</table>')
print('</body>')
print('</html>')
