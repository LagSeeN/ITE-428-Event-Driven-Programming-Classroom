import csv

fireList = []
warningFire = ''
deadEveryYear = ''
injuredLessEverYear = ''


def line():
    print('-' * 100)


if __name__ == '__main__':

    with open('./MyTextFile/fire.csv', mode='r', encoding='utf-8-sig', newline='') as fn:
        fr = csv.DictReader(fn)
        for i in fr:
            fireList.append(i)

    line()

    print('\tค่าเฉลี่ย การเกิดเหตุการณ์เพลิงไหม้ ปี 2555-2557')

    line()

    for c, v in enumerate(
            sorted(fireList, key=lambda k: ((int(k['fire55']) + int(k['fire56']) + int(k['fire57'])) / 3),
                   reverse=True)):
        print('{:>3}.) {} จำนวน {:.2f} ครั้ง'.format(c + 1, v['month'],
                                                     (int(v['fire55']) + int(v['fire56']) + int(v['fire57'])) / 3))
    line()

    for i in fireList:
        if int(i['fire56']) > int(i['fire55']) and int(i['fire57']) > int(i['fire56']):
            warningFire += i['month'] + ' , '

    for i in fireList:
        if int(i['dead55']) != 0 and int(i['dead56']) != 0 and int(i['dead57']) != 0:
            deadEveryYear += i['month'] + ' , '

    for i in fireList:
        if int(i['injury55']) > int(i['injury56']) and int(i['injury56']) > int(i['injury57']):
            injuredLessEverYear += i['month'] + ' , '

    print('เดือนที่ต้องระวังเนื่องจากมีเหตุการณ์ไฟไหม้มากขึ้นทุกปีที่ผ่านมา คือ {}'.format(warningFire[0:-2]))
    line()
    print('เดือนที่ที่มีคนตายทุกปี คือ {}'.format(deadEveryYear[0:-2]))
    line()
    print('เดือนที่คนเจ็บลดลงทุกปี คือ {}'.format(injuredLessEverYear[0:-2]))
    line()
