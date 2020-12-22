import csv

inputNum = int(input('Enter Number of New Product : '))

productList = []
for i in range(inputNum):
    print('product Number [{}]'.format(i + 1))
    print('=' * 50)
    productname = input('Enter product name   : ')
    price = input('Enter product price  : ')
    stock = input('Enter product stock  : ')
    productList.append([productname, price, stock])
    print()

with open('./MyTextFile/products.csv', mode='a', encoding='utf-8', newline='') as fn:
    fw = csv.writer(fn, delimiter=',')
    fw.writerows(productList)
