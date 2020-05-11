import os

f = open('script_workqueue.txt')

while True:
    endCom = f.readline()
    if endCom == '':
        f.close()
        input('\nDone\n')
        exit(0)
    print('\n' + endCom)
    os.system(endCom)


f.close()
input('\nDone\n')
