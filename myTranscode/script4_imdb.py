
import requests
from json import loads

link = input('Link to movie on IMDb: ').split('/')[4]
# ---- input ----

url = 'http://www.omdbapi.com/?apikey=4ddf953e&i&plot=full&i=' + link

r = requests.get(url)
open('imdb.json', 'wb').write(r.content)
dct = loads(r.text)

print(f"\n{dct['Title']} ({dct['Year']})")

while True:
    w = input('\nEnter width of picture: [512] ').strip()
    if w == '':
        w = '512'
    postUrl = dct['Poster'].replace('300.jpg','') + w + '.jpg'
    pic = requests.get(postUrl)
    print('Size of picture will be {} KB'.format(round(int(pic.headers['Content-Length'])/1024)))
    ens = input('Does it fit? [Y/n] ').strip().lower()
    if ens == 'y' or ens == '':
        open('cover.jpg', 'wb').write(pic.content)
        break
# ---- input ----


input('\nDone\n')
