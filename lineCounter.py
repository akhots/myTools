#!/usr/bin/env python3
# lineCounter v1.2
# Developed by Alexander Khotsianivskiy

dct = {}
print('Enter lines:')
while True:
    st = input('').strip()
    if st == '':
        break
    if st in dct:
        dct[st] += 1
    else:
        dct[st] = 1

# --- input ---


lst = list(dct.keys())
lst.sort()
dctI = {}
for i in lst:
    dctI[i] = dct[i]


lstK = list(dct.keys())
lstV = list(dct.values())
lstVK = []
for i in range(len(lstV)):
    lstVK.append((lstV[i], lstK[i]))

lstVK.sort()
dctQ = {}
for i in lstVK:
    dctQ[i[1]] = i[0]


def prRes(dct):
    print()
    for k,v in dct.items():
        print(f'{v:<4}  {k}')


print('Results:')
trigger = '0'
prRes(dct)

while trigger in ('','0','1','2','3'):
    print('\n Press 1 to sort by items\n Press 2 to sort by quantity\n' +
        ' Press 3 to show items only')
    trigger = input().strip()
    if trigger == '0':
        prRes(dct)
    elif trigger == '1':
        prRes(dctI)
    elif trigger == '2':
        prRes(dctQ)
    elif trigger == '3':
        print()
        for i in dct:
            print(i)
