from Mylibrary import linestar, showmenu, circle, rectangle

showmenu()
menu = input('Enter Your Choice : ')
linestar()
ans = 0
if menu == 'C' or menu == 'c':
    radius = float(input('Please Input Radius : '))
    linestar()
    ans = circle(radius)
elif menu == 'S' or menu == 's':
    width = float(input('Please Input Width : '))
    length = float(input('Please Input Length : '))
    linestar()
    ans = rectangle(width, length)
print('AREA = {:.2f}'.format(ans))
linestar()
