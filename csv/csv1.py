def basicTextFile(FN):
    fn = open(FN, mode='a')
    fn.write('Malee')
    fn.close()


def createCSV(FN):
    with open(FN, mode='a', encoding='utf-8') as fn:
        fn.write('{},{},{}\n'.format('Malee', 80, 20))


def readCSV(FN):
    list = ''
    weight = 0
    age = 0
    count = 0
    with open(FN, mode='r', encoding='utf-8') as fn:
        for i in fn:
            list = i.strip('\n').split(',')
            print('คุณชื่อ {}'.format(list[0]))
            print('คุณหนัก {}'.format(list[1]))
            print('คุณอายุ {}'.format(list[2]))
            print('-' * 50)
            weight += int(list[1])
            age += int(list[2])
            count += 1
        print('หนักเฉลี่ย {:.2f}'.format(weight / count))
        print('อายุเฉลี่ย {:.2f}'.format(age / count))


if __name__ == '__main__':
    filename = './MyTextFile/test.csv'
    # basicTextFile(filename)
    # createCSV(filename)
    readCSV(filename)
