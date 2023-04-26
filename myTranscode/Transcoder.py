#!/usr/bin/env python3
# Transcoder v0.1 alpha
# Developed by Alexander Khotsianivskiy

from os import popen,system
from json import loads

fn = input('Input file: ')
# ---- input ----

info = popen(f'ffprobe "{fn}" -print_format json -show_format -show_streams -v quiet').read()
info = loads(info)

width = info['streams'][0]['width']
height = info['streams'][0]['height']
kpx = round(width*height/1000)

avg_rate = info['streams'][0]['avg_frame_rate']
avg_rate = avg_rate.split('/')
avg_rate = round( int(avg_rate[0]) / int(avg_rate[1]) , 3)

codec = info['streams'][0]['codec_name']


if width < height:
    vert = True
elif 'side_data_list' in info['streams'][0]:
    if info['streams'][0]['side_data_list'][0]['rotation'] == -90:
        vert = True
        width,height = height,width
else:
    vert = False


print(f'{width:>6} x {height:<4} ({kpx:>4} KPixels)  {avg_rate:>3} fps  {codec}')


resTable = {
    'a': 1280,
    'b': 1024,
    'c': 768,
}

def whp(le, vert=vert, width=width, height=height):
    if not vert:
        w = le
        h = round(le * height/width) //2*2
    elif vert:
        h = le
        w = round(le * width/height) //2*2
    p = round(w*h/1000)
    return (w, h, p)


def brCalc(w,h):
    return round(8000 / (1920*1080) * (w*h))



for i in resTable:
    resTable[i] = whp(resTable[i])


print('\nMy resolutions:')

for k,v in resTable.items():
    print(f'{k}  {v[0]:>4} x {v[1]:<4} ({v[2]} KPixels)')


res = input('\nChoose resolution: [a/b/c or longest edge] ').strip()
# ---- input ----

if not res:
    w,h,p = width,height,kpx
elif res == 'a' or res == 'b' or res == 'c':
    w,h,p = resTable[res]
else:
    try:
        w,h,p = whp(int(res))
    except:
        input(' wrong input')
        exit(1)


print(f'{w:>6} x {h:<4} ({p} KPixels)')

format = fn.split('.')[-1].lower()
nfn = fn[0:-(len(format)+1)] + '-out.' + format

br = brCalc(w,h)

comm = f'''
ffmpeg ^
-hide_banner ^
-hwaccel dxva2 ^
-i "{fn}" ^
-vf scale={w}x{h}:flags=lanczos ^
-vsync 0 ^
-c:v libx265 -preset 6 ^
-x265-params crf=20:vbv-maxrate={br}:vbv-bufsize={br} ^
-c:a copy ^
-movflags use_metadata_tags ^
-map_metadata 0 ^
"{nfn}"
'''

print(comm)

comm = comm.replace('^\n', '').strip()

while True:
    run = input('Run? [y/n] ').strip().lower()
    if run == 'y':
        system(comm)
        break
    if run == 'n':
        break

# ---- input ----

input('\nDone\n')
