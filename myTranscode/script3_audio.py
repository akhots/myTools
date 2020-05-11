import os

lstdr = os.listdir()
print('Work folder list:')
for dr in lstdr:
    if "_tmp" == dr[-4:]:
        print(dr)

fld = input('\nEnter work folder: ')

os.system('dir ' + fld)

tfl = []
print('\n\nInput audio track files')
while True:
    tf = input(': ')
    if tf == '':
        break
    tfl.append(tf)
# ---- input ----

qrd = {
    '5': '54',
    '6': '64',
    '7': '73',
    '8': '82',
    '9': '91'
}

print('''\n5 - q54\n6 - q64\n7 - q73\n8 - q82\n9 - q91''')
qr = input('Choose quality: ')
# ---- input ----

endComLst = []
for tf in tfl:
    for q in qr:
        endComLst.append(f'ffmpeg -i "{fld}/{tf}" -c:a pcm_s24le -f wav - | qaac64 - --tvbr {qrd[q]} -o "{fld}/{tf}.q{qrd[q]}.m4a"')


print('\nNext command is going to be run:\n')
for endCom in endComLst:
    print('\n' + endCom)


queue = input('\nAdd to queue? [y/N] ').strip().lower()
# ---- input ----
if queue == 'y':
    with open('script_workqueue.txt', 'a') as f:
        for endCom in endComLst:
            f.write(endCom + '\n')
    input('\nDone\n')
    exit(0)

run = input('\nRun? [y/N] ').strip().lower()
# ---- input ----
if run == 'y':
    for endCom in endComLst:
        os.system(endCom)


input('\nDone\n')


'''
NOTES

q0
q9
q18
q27
q36
q45
q54
q64
q73
q82
q91
q100
q109
q118
q127
'''
