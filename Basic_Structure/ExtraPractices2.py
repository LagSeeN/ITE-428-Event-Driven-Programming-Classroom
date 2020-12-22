import json

import requests

url = 'https://data.go.th/dataset/84954e4a-3302-4b05-9dfc-c636f30b62ab/resource/31ddd8a7-c99a-43eb-8c2e-9644ddb1608b/download/university.json'
r = requests.get(url)

myData = json.loads(r.content)

myData = myData['features']

# print('{}'.format(myData))
# print('{}'.format(type(myData)))
# print('{}'.format(len(myData)))

print('{}'.format('-' * 30))
print('{}'.format('สถาบันอุดมศึกษาเอกชน'))
print('{}'.format('-' * 30))

count = 1
for i in myData:
    if i['properties']['type'] == '3':
        print('{}.) {} {}'.format(count, i['properties']['name'], i['properties']['web']))
        count += 1
