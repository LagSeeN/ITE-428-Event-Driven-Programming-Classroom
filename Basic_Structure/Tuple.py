import math


def basicTuple():
    weight = (80, 45, 68, 79, 96)
    print('{}'.format(weight))
    print('{}'.format(type(weight)))
    print('{}'.format(weight[0]))
    for i in weight:
        print('-- {}'.format(i))
    for i in range(len(weight)):
        print('** {}'.format(weight[i]))
    for i, v in enumerate(weight):
        print('-- {} | {}'.format(i, v))
    print('Long = {}'.format(len(weight)))
    print('Long = {}'.format(weight.__len__()))
    print('SORT = {}'.format(sorted(weight)))
    print('SORT = {}'.format(sorted(weight, reverse=True)))
    print('MAX = {}'.format(max(weight)))
    print('MIN = {}'.format(min(weight)))


def applyTyple():
    print('Thai', 'Nichi', 'Institute', sep='*')


def sumByTyple1(*num):
    # print('{}'.format(num))
    sum = 0
    for i in num:
        sum += i
    return sum


def sumByTyple2(*num):
    # print('{}'.format(num))
    sum = 0
    for i in num:
        sum += i
    avg = sum / num.__len__()
    return sum, avg


def sumByTyple3(*num, digit):
    # print('{}'.format(num))
    sum = 0
    for i in num:
        sum += i
    avg = sum / num.__len__()
    if digit == 2:
        avg = '{:.2f}'.format(avg)
    return sum, avg


def practicesSlide143():
    point1 = 5, 5
    point2 = (2, 1)
    # find distance between two points
    ans = math.sqrt(((point1[1] - point1[0]) ** 2) + ((point2[1] - point2[0]) ** 2))
    print("Distance between two points = {0}".format(ans))


def practicesSlide145():
    weight = (62.5, 78, 50, 42, 84, 65.5, 48, 53.5, 43)
    print('Maximum weight of {} persons = {}'.format(weight.__len__(), max(weight)))
    print('Minimum weight of {} persons = {}'.format(weight.__len__(), min(weight)))
    sum = 0
    above = 0
    below = 0
    equal = 0
    for i in weight:
        sum += i
    avg = sum / weight.__len__()
    for i in weight:
        if i > avg:
            above += 1
        elif i == avg:
            equal += 1
        else:
            below += 1
    print('Average weight of {} persons = {}'.format(weight.__len__(), avg))
    print('No. of weight above average    = {}'.format(above))
    print('No. of weight below average    = {}'.format(below))
    print('No. of weight equal to average = {}'.format(equal))


def practicesSlide151():
    x, y = checkNumber(17, 22, 35, 55, 67, 38, 98, 109, 10, 5, 77, see="max-min")
    print("MAXIMUM = {0}\nMINIMUM = {1}".format(x, y))
    x, y = checkNumber(12, 99, 34, 67, 21, 98, 13, see="ab-bl-av")
    print("ABOVE AVERAGE = {0}\nBELOW AVERAGE = {1}".format(x, y))


def checkNumber(*num, see):
    if see == 'max-min':
        return max(num), min(num)
    if see == 'ab-bl-av':
        above = 0
        below = 0
        sum = 0
        for i in num:
            sum += i
        avg = sum / num.__len__()
        for i in num:
            if i > avg:
                above += 1
            else:
                below += 1
        return above, below
    return


if __name__ == '__main__':
    # print('{}'.format(sumByTyple1(10, 25, 69, 78, 45, 18, 51, 69)))
    # print('{}'.format(sumByTyple2(10, 25, 69, 78, 45, 18)))
    # S, A = sumByTyple3(10, 25, 69, 78, 45, 18, digit=2)
    # print('SUM = {}'.format(S))
    # print('AVERAGE = {}'.format(A))
    practicesSlide143()
    practicesSlide145()
    practicesSlide151()
