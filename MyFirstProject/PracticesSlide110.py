from Mylibrary import linestar, reducePrice

price = float(input('Price of car : '))
percent = int(input('Input depreciation pre year (%) : '))
year = int(input('Input How many year you want to see : '))

print()
linestar()
print('Price of Car = {:,.2f} BAHT'.format(price))
linestar()
for i in range(year):
    reduce = reducePrice(price, percent)
    price -= reduce
    print('After use {} Year : Reduce = {:,.2f} BAHT Price = {:,.2f} BAHT'.format(i + 1, reduce, price))
linestar()
