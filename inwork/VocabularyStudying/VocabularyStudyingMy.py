# Version 2

from random import shuffle


print('Enter vocabulary:\n')

voc = []
while True:
    word = input(': ').strip()
    if word == '':
        break
    if ' - ' not in word:
        print('Incorrect input!')
        continue
    while '  ' in word:
        word = word.replace('  ', ' ')
    voc.append(word.split(' - '))


if voc == []:
    input('\nNo vocabulary!')
    exit()


if input('\nChange direction? [N/y] ').strip().lower() == 'y':
    a, b = 0, 1
else:
    a, b = 1, 0


print('')
shuffle(voc)
hit = 0
vocLen = len(voc)

for word in voc:
    print('Translate: ' + word[a])
    ensw = input('Enter:     ').lower()
    if ensw == word[b]:
        print('Correct!                :):):)\n' + '-'*32)
        hit += 1
    else:
        print('Wrong!                  :(')
        print('Correct:   ' + word[b] + '\n' + '-'*32)


score = round((hit/vocLen)*100)

print('\n\nYOU SCORE - ' + str(round(score)) + ' / 100')

while True:
    if input('\nEnter "ok" to exit...\n').strip().lower() == 'ok':
        print('\nBye!\n')
        break

