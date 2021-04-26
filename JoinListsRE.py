
print('Enter 1st list:')
lst1 = []
while True:
    item = input()
    if item == '':
        break
    lst1.append(item)


print('Enter 2st list:')
lst2 = []
while True:
    item = input()
    if item == '':
        break
    lst2.append(item)

print('\nResult:\n')

from re import search


for i in lst1:
    for j in lst2:
        if search(j, i):
            print(i)


while True:
    end = input('\n\nDone\n\nEnter "ok" to exit... ').lower()
    if end == 'ok':
        break
