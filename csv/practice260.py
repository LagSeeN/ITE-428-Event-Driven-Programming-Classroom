count = 1
with open('./MyTextFile/ilovesea.txt', mode='r', encoding='utf-8') as fn:
    for i in fn:
        print('{}. - {}'.format(count, i.strip("\n")))
        count += 1
