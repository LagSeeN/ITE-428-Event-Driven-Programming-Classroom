import math


def line():
    print("-" * 50)


def CalBMI(w, h):
    bmi = w / ((h / 100) ** 2)
    return bmi


def linestar():
    print("*" * 50)


def showmenu():
    linestar()
    print('{:>25}'.format('MENU'))
    linestar()
    print('C or c Area of Circle')
    print('S or s Area of Rectangle')
    linestar()


def circle(r):
    return math.pi * r ** 2


def rectangle(w, l):
    return w * l


def calToPercent(num, maxnum, percent):
    return (num / maxnum) * percent


def calGrade(point):
    if point >= 97:
        return 'A+'
    elif point >= 93:
        return 'A'
    elif point >= 90:
        return 'A-'
    elif point >= 87:
        return 'B+'
    elif point >= 83:
        return 'B'
    elif point >= 80:
        return 'B-'
    elif point >= 77:
        return 'C+'
    elif point >= 73:
        return 'C'
    elif point >= 70:
        return 'C-'
    elif point >= 67:
        return 'D+'
    elif point >= 63:
        return 'D'
    elif point >= 60:
        return 'D-'
    return 'F'


def reducePrice(price, percent):
    return (price * percent) / 100


if __name__ == '__main__':
    print('Danupol')
