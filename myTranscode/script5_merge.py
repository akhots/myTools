import os
import re
from json import loads

dirLst = os.listdir()

trLst = []
for tr in dirLst:
    if tr[0:5] == 'track':
        trLst.append(tr)

langLst = []
forcLst = []
tnLst = []
for tr in trLst:
    langLst.append(tr.split('.')[1])
    if 'force' in tr.lower():
        forcLst.append(True)
    else:
        forcLst.append(False)
    if '[' in tr and ']' in tr:
        tnLst.append(tr.split('[')[1].split(']')[0])
    else:
        tnLst.append('')

try:
    with open('imdb.json') as f:
       imdb = f.read()
    imdb = loads(imdb)
    mn = f"{imdb['Title']} ({imdb['Year']})"
except:
    mn = input('Enter movie/year for generateding filename: ')
# ---- input ----


fn = mn.replace('(','').replace(')','')
fn = re.sub(' |\.|\(|\)|:|\/', '.', fn)

print(f'Title: {mn}')
if input('Change title? [y/N] ').strip().lower() == 'y':
    mn = input('Enter title: ')
# ---- input ----

langSet = []
for lang in langLst:
    if lang not in langSet:
        langSet.append(lang)

for lang in langSet:
    fn = fn + '.' + lang.title()

rip = input('\nRip type: [DBRip] ').strip()
# ---- input ----
if rip == '':
    rip = 'DBRip'

fn = fn + f'.{rip}.mkv'

print(f'\nFilename: {fn}')
if input('Change file name? [y/N] ').strip().lower() == 'y':
    fn = input('Enter filename: ')
# ---- input ----

cover = ''
if "cover.jpg" in os.listdir():
    cover = ' --attach-file cover.jpg'

endCom = f'mkvmerge -o {fn} --title "{mn}" -A -S -T --no-global-tags video.mkv{cover}'

for n in range(len(trLst)):
    curTn = ''
    if tnLst[n] != '':
        curTn = f' --track-name 0:"{tnLst[n]}"'
    noDef = ''
    if n > 1 and forcLst[n] != True:
        noDef = ' --default-track 0:False'
    endCom = endCom + f' --no-global-tags --language 0:{langLst[n]} --forced-track 0:{forcLst[n]}{curTn}{noDef} "{trLst[n]}"'

print('\n' + endCom)

run = input('\nRun? [Y/n]').lower()
if run =='y' or run == '':
    os.system(endCom)


input('\nDone\n')
