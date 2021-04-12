
import os

ip_lst = []

while True:
    elem = input(':')
    if elem == '':
        break
    ip_lst.append(elem)

res_lst = []
for ip in ip_lst:
    res = os.popen('ping -n 1 -w 1000 ' + ip + ' | findstr Packets').read()
    if res == '':
        res_lst.append((ip, 'error'))
    else:
        res_lst.append((ip, res.split()[-2][1:]))

print('ip - loss')
for res in res_lst:
    print(res[0] + ' - ' + res[1])


input()

