sortlist = []

with open('./MyTextFile/MarvelComics.txt', mode='r', encoding='utf-8') as fn:
    for i in fn:
        sortlist.append(i.strip('\n'))
sortlist = sorted(sortlist, reverse=True)
for i in range(sortlist.__len__()):
    print('{}.) {}'.format(i + 1, sortlist[i]))
