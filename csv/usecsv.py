import csv


def writeCSV(FN):
    with open(FN, mode='a', encoding='utf-8', newline='') as fn:
        fw = csv.writer(fn, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        data = ['Malee', 90, 40]
        fw.writerow(data)
        data1 = [['Lay', 50, 40], ['Lay2', 20, 40]]
        fw.writerows(data1)


def readCSV(FN):
    with open(FN, mode='r', encoding='utf-8', newline='') as fn:
        fr = csv.reader(fn)
        for i in fr:
            print('{}'.format(i))


def readCsvDict(FN):
    with open(FN, mode='r', encoding='utf-8-sig', newline='') as fn:
        fr = csv.DictReader(fn)
        for i in fr:
            print('{}'.format(i))


if __name__ == '__main__':
    # filename = './MyTextFile/useCsv.csv'
    filename = './MyTextFile/fire.csv'
    # writeCSV(filename)
    # readCSV(filename)
    readCsvDict(filename)
