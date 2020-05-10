
import os
from json import loads

fn = input('Input file: ')
# ---- input ----

fld = fn[0:-4] + '_tmp'
os.system(f'mkdir "{fld}"')
os.system(f'mkvextract "{fn}" chapters "{fld}/chapters.xml"')

info = os.popen(f'ffprobe "{fn}" -v quiet -print_format json -show_streams -show_format').read()
with open(f'{fld}/info.json', 'w') as f:
    f.write(info)

info = info.encode('ansi').decode('utf8')
info = info.replace('subrip','srt')
info = info.replace('vorbis','ogg')
info = info.replace('|','-').replace('/','-')

info = loads(info)
trNum = len(info['streams'])
endCom = f'ffmpeg -i "{fn}"'

for tr in range(trNum):
    if info['streams'][tr]['codec_type'] == 'video':
        if info['streams'][tr]['disposition']['attached_pic'] != 0:
            endCom = endCom + f" -map 0:{tr} -c copy {fld}/{info['streams'][tr]['tags']['filename']}"
        continue 
    endCom = endCom + f" -map 0:{tr} -c copy \"{fld}/track{tr:02d}."
    endCom = endCom + info['streams'][tr]['tags']['language']
    startF = round(float(info['streams'][tr]['start_time'])*1000)
    if startF != 0:
        endCom = endCom + f".{startF}ms"
    if 'title' in info['streams'][tr]['tags']:
        endCom = endCom + '.[' + info['streams'][tr]['tags']['title'] + ']'
    endCom = endCom + f".{info['streams'][tr]['codec_name']}\""


print('\nNext command is going to be run:\n\n' + endCom + '\n')
run = input('Run? [y/N] ').strip().lower()
# ---- input ----
if run == 'y':
    os.system(endCom)

input('\nDone\n')
