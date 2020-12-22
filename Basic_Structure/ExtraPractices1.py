import json

import requests

url = 'https://data.go.th/dataset/9bccd66e-8b14-414d-93d5-da044569350c/resource/70e1ac97-edfe-4751-8965-6bbe16fb21b4/download/data_station.json'
r = requests.get(url)

myData = json.loads(r.content)

# print('{}'.format(myData))
# print('{}'.format(type(myData)))
# print('{}'.format(len(myData)))

for i in myData:
    print('{} {}'.format(i['station_code'],i['name']))
    print('{:<4} {} / {}'.format('',i['en_name'],i['chname']))
    if(i['lat'] != 0):
        print('{:<4} ({} , {})'.format('',i['lat'],i['long']))
    print()