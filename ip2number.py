#!/usr/bin/env python3

lst = []
while True:
    st = input(': ').strip()
    if st == '':
        break
    st = st.split('.')
    if len(st) != 4:
        lst.append('wrong ip')
        continue
    try:
        st = [int(i) for i in st]
        lst.append(st[0]*256**3 + st[1]*256**2 + st[2]*256 + st[3])
    except:
        lst.append('wrong ip')
        


print('\n'*2)

for i in lst:
    print(i)


while True:
    end = input('\n\nDone\n\nEnter "ok" to exit... ').lower()
    if end == 'ok':
        break
