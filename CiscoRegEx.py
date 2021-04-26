#!/usr/bin/env python3
# CiscoRegEx v2.0 beta
# Developed by Alexander Khotsianivskiy


print('Enter IP / network / IP range:')
lst = []
while True:
    raw = input('').strip()
    if raw == '':
        break
    try:
        if '-' in raw:
            raw = raw.split('-')
            raw[0] = raw[0].split('.')
            lastOct = int(raw[0][-1])
            mask = int(raw[1]) + 1 - lastOct
            if mask <= 0:
                print(' wrong IP range')
                continue
        elif '/' in raw:
            raw = raw.split('/')
            raw[0] = raw[0].split('.')
            lastOct = int(raw[0][-1])
            mask = 2**(32 - int(raw[1]))
            if lastOct/mask != lastOct//mask:
                lastOct = lastOct - lastOct % mask
                print(f' network repair: x.x.x.{lastOct}/{raw[1]}')
        else:
            raw = [raw.split('.'), '-']
            lastOct = int(raw[0][-1])
            mask = 1
        if lastOct + mask > 256:
            print(' wrong entry')
            continue
        raw.append(lastOct)
        raw.append(mask)
        lst.append(raw)
    except:
        print(' unknown error')


endLst = []

for i in lst:
    prEnd = '\.'.join(i[0][:-1]) + '\.'
    if i[3] == 256:
        endLst.append(prEnd)
        continue

    lastLst = [f'{x:03d}' for x in range(i[2], i[2]+i[3])]

    l3 = []

    pr3 = []
    for j in lastLst:
        j = j[0:2]
        if j not in pr3:
            pr3.append(j)

    for j in pr3:
        elem = ''
        for k in lastLst:
            if j == k[0:2]:
                elem = elem + k[2]
        if len(elem) > 1:
            l3.append(f'{j}[{elem[0]}-{elem[-1]}]')
        else:
            l3.append(j + elem)

    if l3[-1] == '25[0-5]':
        l3[-1] = '25[0-9]'

    l2 = []

    pr2 = []
    for j in l3:
        j = j[0]+j[2:]
        if j not in pr2:
            pr2.append(j)

    for j in pr2:
        elem = ''
        for k in l3:
            if j == k[0]+k[2:]:
                elem = elem + k[1]
        if len(elem) > 1:
            l2.append(f'{j[0]}[{elem[0]}-{elem[-1]}]{j[1:]}')
        else:
            l2.append(j[0] + elem + j[1:])

    for j in range(len(l2)):
        if l2[j][0] == '0':
            l2[j] = l2[j][1:] + '_'

    for j in range(len(l2)):
        if l2[j][0] == '0':
            l2[j] = l2[j][1:]

    if len(l2[0]) != 6:
        if l2[0][:2] == '[0':
            l2[0] = '[1' + l2[0][2:]
            l2.insert(0, '[0-9]_')

    for j in l2:
        endLst.append(prEnd + j)


print('Cisco Regular Expressions:')
for i in endLst:
    print(i)


print('\nCommon Regular Expressions:')
for i in endLst:
    if '_' == i[-1]:
        print(i[:-1] + '\\D')
    else:
        print(i)


while True:
    end = input('\n\nEnter "ok" to exit... ').lower()
    if end == 'ok':
        break
