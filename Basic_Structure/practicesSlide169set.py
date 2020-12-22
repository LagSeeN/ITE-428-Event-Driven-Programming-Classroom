rude_word = ['damm', 'hell', 'ass', 'piss', 'silly', 'idiotic']
comment = input('Please comment our service ').lower()

if set(comment.split(' ')).intersection(set(rude_word)).__len__() >= 1:
    print('Cannot show [', end='')
else:
    print('Can show [', end='')
print('{}]'.format(comment))
