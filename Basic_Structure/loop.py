def forRange():
    for i in range(1, 13):
        print("2 x {} = {}".format(i, 2 * i))


def whileLoop(number):
    i = 1
    while i < 13:
        print("{} x {} = {}".format(number, i, number * i))
        i += 1


def doWhileLoop(number):
    i = 1
    while True:
        print("{} x {} = {}".format(number, i, number * i))
        i += 1
        if i == 13:
            break


def forEach():
    color = ['red', 'orange', 'pink']
    for i in color:
        print('{}'.format(i))


def practicesSlide112():
    i = int(input('Enter i'))
    j = int(input('Enter j'))
    n = int(input('Ener n'))
    count = 0
    total = 0
    print('({}-10)^{}x{} ='.format(i, n, i), end=' ')
    while True:
        print('({}-10)^{}x{}'.format(i + count, n, i + count), end=' ')
        total += ((((i + count) - 10) ** n) * (i + count))
        if i + count == j:
            print('\nTotal = {}'.format(total))
            break
        else:
            print('+', end=' ')
        count += 1


if __name__ == '__main__':
    practicesSlide112()
