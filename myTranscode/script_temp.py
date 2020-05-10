import os

dlt = input('Part to change: ')

ld = os.listdir()

ft = ['.ac3', '.m4a', '.srt', '.dts', '.thd', '.mka']


for one in ld:
    for two in ft:
        if two in one:
            oneNew = one.replace(dlt, 'track0')
            oneNew = oneNew.replace(' Ukrainian', '.ukr')
            oneNew = oneNew.replace(' Russian', '.rus')
            oneNew = oneNew.replace(' English', '.eng')
            oneNew = oneNew.replace(' {', '.[').replace('}', ']')
            oneNew = oneNew.replace(' ', '.')
            os.system(f'ren "{one}" "{oneNew}"')
            break


input('\nDone\n')
