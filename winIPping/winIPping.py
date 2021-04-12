
import os
from datetime import datetime

resources = []
print('Resources list:')
while True:
    item = input(':')
    if item == '':
        break
    resources.append(item)

repeats = input('Repeats [1]: ').strip()
if repeats == '':
    repeats = '1'

timeOut = input('Timeout [1000]: ').strip()
if timeOut == '':
    timeOut = '1000'

try:
    int(repeats)
    int(timeOut)
except:
    input('\nBad value for option\n')
    exit(1)


fileName = str(datetime.now())[:19].replace(' ','-').replace(':', '-') + '.txt'
f = open(fileName, 'a')

f.write('{}\t{}\t{}\t{}\n'.format('loss','time','IP address','name'))
print('\n{:>6}{:>8}{:>18}      {}\n'.format('loss','time','IP address','name'))
for item in resources:
    res = os.popen(f'ping -n {repeats} -w {timeOut} {item}').read()
    res = res.split()
    if res[1:5] == ['request', 'could', 'not', 'find']:
        f.write(f'-\t-\terror\t{item}\n')
        print(f'     -       -             error      {item}')
        continue
    if res[-12] == 'Packets:':
        f.write(f'{res[-2][1:]}\t-\t')
        print(f'{res[-2][1:]:>6}       -', end='')
    else:
        f.write(f'{res[-17][1:]}\t{res[-1]}\t')
        print(f'{res[-17][1:]:>6}{res[-1]:>8}', end='')
    if res[2] != 'with':
        f.write(f'{res[2][1:-1]}\t{res[1]}\n')
        print(f'{res[2][1:-1]:>18}      {res[1]}')
    else:
        f.write(f'{res[1]}\n')
        print(f'{res[1]:>18}')


f.close()

input(f'\nDone\n\nResults saved in {fileName}\n')
