Price = int(input('Enter Price of Product  : '))
Amout = int(input('Enter Amount of Product : '))

print('Total Price : {}\nTotal Price + Vat : {}'.format(Price*Amout,(Price*Amout)*1.07))

print('Total Price : {}\nTotal Price + Vat : {:>30,.2f}'.format(Price*Amout,(Price*Amout)*1.07))