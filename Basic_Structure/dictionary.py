def basicDic():
    studentData = {'Name': 'Malee', 'weight': 90, 'name': 'Malee'}
    studentData['Address'] = 'Pattanakarn 37'
    print('{}'.format(studentData))
    print('{}'.format(type(studentData)))
    studentData['Name'] = 'Somchai'
    print('{}'.format(studentData['Name']))
    del studentData['name']
    print('{}'.format(studentData.__len__()))
    print('{}'.format(studentData))


def traverseDic():
    studentData = {'Name': 'Malee', 'weight': 90}
    print('{}'.format(studentData['Name']))
    for k in studentData.keys():
        print('{}'.format(k))
    for v in studentData.values():
        print('{}'.format(v))
    for k, v in studentData.items():
        print('Key = {}, Value =  {}'.format(k, v))


if __name__ == '__main__':
    # basicDic()
    traverseDic()
