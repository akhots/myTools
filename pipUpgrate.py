import sys
import os

lst = os.popen('pip list').read()
print(lst + '\n')
lst = lst.split('\n')[2:-1]

for one in lst:
    print(one)
    res = os.popen('pip install -U ' + one.split()[0]).read()
    print(res + '\n\n')

lst = os.popen('pip list').read()
print(lst)

input()
