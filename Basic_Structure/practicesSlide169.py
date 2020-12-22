rude_word = ['damm', 'hell', 'ass', 'piss', 'silly', 'idiotic']
comment = input('Please comment our service ').lower()

if any(comment in search for search in rude_word):
    print('Cannot show [', end='')
else:
    print('Can show [', end='')
print('{}]'.format(comment))
