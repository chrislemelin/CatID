from apiclient.discovery import build
import os, errno
import urllib
import json
import sys
import requests
import config

quantity_of_pics = 10
start = -1
end = -1

if len(sys.argv) == 2:
    end = int(sys.argv[1])
    #print(end+' 1')

if len(sys.argv) == 3:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    #print(end+' 2')


with open('../../breeds/breeds.json') as data_file:
    breeds_json = json.load(data_file)

breeds = []
breed_counter = 0

for breed_item in breeds_json:
    if end == breed_counter:
        break
    if breed_counter >= start:
        breeds.append(breed_item['breed'])
        #print(breed_item['breed'])
    breed_counter = breed_counter+1

for breed in breeds:
    try:
        os.makedirs('data/'+breed)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

service = build("customsearch", "v1",
               developerKey=config.api_key)

for breed in breeds:
    res = service.cse().list(
        q=breed+' cat',
        cx=config.cx,
        searchType='image',
        imgType='photo',
        num=quantity_of_pics,
        fileType='png',
        safe= 'off'
    ).execute()

    if not 'items' in res:
        print 'No result !!\nres is: {}'.format(res)
    else:
        pic_counter = 0
        print(breed)
        for item in res['items']:
            print(pic_counter)
            try:
                f = open('data/'+breed+'/'+str(pic_counter)+'.png','wb')
                f.write(requests.get(item['link'].encode()).content)
                f.close()
                #urllib.urlretrieve(item['link'].encode(),'data/'+breed+'/'+str(pic_counter)+'.png')
            except error:
                print(error)
            pic_counter = pic_counter+1
