import os

fn = input('Input file: ')
# ---- input ----

fld = fn.replace('\\','/').split('/')[-1][0:-4] + '_tmp'

print('\nInput resolution:')
os.system(f'ffprobe "{fn}" -select_streams v:0 -show_entries stream=width,height -of default=nw=1 -v quiet')

print('''

My resolutions

DAR 2:1
a - 800x400
b - 1024x512
c - 1088x544

DAR 16:9
d - 768x432
e - 1024x576
''')

resTable = {
    'a': (800, 400),
    'b': (1024, 512),
    'c': (1088, 544),
    'd': (768, 432),
    'e': (1024, 576)
}

while True:
    res = input('Choose resolution: [a/b/c/d/e or WxH] ')
    if res in resTable:
        res = resTable[res]
        break
    else:
        try:
            res = res.split('x')
            res = (int(res[0]), int(res[1]))
            break
        except:
            print('wrong input')
# ---- input ----



q = input('Choose QSV intelligent quality: [17] ').strip()
# ---- input ----
if q == '':
    q = 17
else:
    q = round(float(q),2)


ct = input('Cut from top: [0] ').strip()
# ---- input ----
if ct == '':
    ct = 0
else: ct = int(ct)

cb = input('Cut from bottom: [0] ').strip()
# ---- input ----
if cb == '':
    cb = 0
else:
    cb = int(cb)

fCrop = ''
if ct != 0 or cb != 0:
    fCrop = f'crop=h=ih-({ct}+{cb}):y={ct},'


endCom = f'ffmpeg -hwaccel dxva2 -i "{fn}" -vf {fCrop}crop=ih*{res[0]}/{res[1]}:ih,scale={res[0]}x{res[1]}:flags=lanczos -aspect {res[0]}:{res[1]} -an -sn -pix_fmt yuv420p -f yuv4mpegpipe - | \
QSVEncC64 --y4m -i - --codec hevc --quality best --colormatrix bt709 --colorprim bt709 --transfer bt709 --fallback-rc --icq {q} --sar 1:1 -o "{fld}/video.mkv"'

print('\nNext command is going to be run:\n\n' + endCom + '\n')


queue = input('Add to queue? [y/N] ').strip().lower()
# ---- input ----
if queue == 'y':
    with open('script_workqueue.txt', 'a') as f:
        f.write(f'mkdir "{fld}"\n')
        f.write(endCom + '\n')
    input('\nDone\n')
    exit(0)

run = input('Run? [y/N] ').strip().lower()
# ---- input ----
if run == 'y':
    os.system(f'mkdir "{fld}"')
    os.system(endCom)


input('\nDone\n')
