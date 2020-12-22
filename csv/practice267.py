import csv

products = []
conf = {}
total = 0

with open('./MyTextFile/products.csv', mode='r', encoding='utf-8', newline='') as fn:
    fr = csv.reader(fn)
    for i in fr:
        products.append({'product': i[0], 'price': i[1], 'stock': i[2]})

with open('./MyTextFile/appConfig.ini', mode='r', encoding='utf-8-sig', newline='') as fn:
    fr = csv.reader(fn)
    for i in fr:
        key = i[0].split('=')[0]
        value = i[0].split('=')[1]
        conf[key] = value

for i in products:
    print('{product:<20} {price:>10{comma}.{decimal}f}'.format(product=i['product'],
                                                               price=float(i['price']) * float(i['stock']),
                                                               comma=',' if conf['comma'] == 'yes' else '',
                                                               decimal=conf['decimal_places']))
    total += float(i['price']) * float(i['stock'])

print('{}'.format(conf['line']) * 40)
print('{:<20} {:>10,.2f} {}'.format('Total Value', total, conf['currency_unit']))
