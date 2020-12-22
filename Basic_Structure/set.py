def basicSet():
    print('{}'.format(scoreClass1))
    print('TYPE {}'.format(type(scoreClass1)))
    print('LONG {}'.format(scoreClass1.__len__()))
    for i in scoreClass1:
        print('{}'.format(i))


def operatonSet():
    print('Class 1 {}'.format(scoreClass2))
    print('Class 2 {}'.format(scoreClass1))
    print('{}'.format(scoreClass1 & scoreClass2))
    print('{}'.format(scoreClass1.intersection(scoreClass2)))
    print('{}'.format(scoreClass1 | scoreClass2))
    print('{}'.format(scoreClass1.union(scoreClass2)))
    print('{}'.format(scoreClass1 - scoreClass2))
    print('{}'.format(scoreClass2 - scoreClass1))
    print('{}'.format(scoreClass1.difference(scoreClass2)))
    print('{}'.format(scoreClass2 ^ scoreClass1))


def createSet():
    scoreClass3 = set()
    print('{}'.format(type(scoreClass3)))
    scoreClass3.add(152)
    scoreClass3.update({125, 153})
    print('{}'.format(scoreClass3))
    try:
        scoreClass3.remove(10)
    except:
        print('ไม่มีข้อมูล')
    scoreClass3.discard(153)
    scoreClass3.clear()
    print('{}'.format(scoreClass3))


def castStructure():
    # tuple , list , set
    print('{}'.format(scoreClass1))
    scoreClass1toList = list(scoreClass1)
    print('{}'.format(scoreClass1toList))


if __name__ == '__main__':
    scoreClass1 = {10, 52, 36, 50, 81, 10, 100}
    scoreClass2 = {10, 52, 36, 23, 56, 14}
    # basicSet()
    # operatonSet()
    # createSet()
    castStructure()
