import csv

rude_word = set()
comment = []
canshow = []
cannotshow = []

with open('./MyTextFile/rude_word.txt', mode='r', encoding='utf-8') as fn:
    for i in fn:
        rude_word.add(i.lower().strip('\n'))

with open('./MyTextFile/practice-comment.txt', mode='r', encoding='utf-8') as fn:
    for i in fn:
        comment.append(i.lower().strip('\n'))

for i in range(comment.__len__()):
    if set(comment[i].split(' ')).intersection(rude_word).__len__() >= 1:
        cannotshow.append(comment[i])
    else:
        canshow.append(comment[i])

with open('./MyTextFile/canshow.txt', mode='a', encoding='utf-8', newline='') as fn:
    fw = csv.writer(fn, delimiter='\n')
    fw.writerow(canshow)

with open('./MyTextFile/cannotshow.txt', mode='a', encoding='utf-8', newline='') as fn:
    fw = csv.writer(fn, delimiter='\n')
    fw.writerow(cannotshow)
