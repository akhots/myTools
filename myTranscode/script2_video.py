import os

fn = input('Input file: ')
# ---- input ----

fld = fn[0:-4] + '_tmp'

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

def x5param(xy,q=18,b=24000,k=None):
    x, y = xy[0], xy[1]
    if k == None:
        k = 0.7 + (591872 - x*y)/265000*0.05
    return round(b / (1920*1080) * x*y * k * (18/q) / 10) * 10, k


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



q = input('Choose quality: [18] ').strip()
# ---- input ----
if q == '':
    q = 18
else:
    q = round(float(q),2)

br = x5param(res,q=q)[0]
mbr = input(f'Choose maximum bitrate: [{br}] ').strip()
# ---- input ----
if mbr != '':
    br = round(float(mbr))



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


endCom = f'ffmpeg -hwaccel dxva2 -i "{fn}" -vf {fCrop}crop=ih*{res[0]}/{res[1]}:ih,scale={res[0]}x{res[1]}:flags=lanczos -an -sn -c:v libx265 \
-x265-params crf={q}:vbv-maxrate={br}:vbv-bufsize={br}:range=limited:colorprim=bt709:transfer=bt709:colormatrix=bt709 "{fld}/video.mkv"'

print('\nNext command is going to be run:\n\n' + endCom + '\n')

run = input('Run? [y/N] ').strip().lower()
# ---- input ----
if run == 'y':
    os.system(f'mkdir {fld}')
    os.system(endCom)


input('\nDone\n')
