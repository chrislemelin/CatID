import os
import json
import sys

quantity = 100
start = -1
end = -1

if len(sys.argv) == 2:
    breed = sys.argv[1]
    #print(end+' 1')

if len(sys.argv) == 3:
    breed = sys.argv[1]
    quantity = int(sys.argv[2])

if len(sys.argv) == 4:
    breed = sys.argv[1]
    quantity = int(sys.argv[2])
    end = int(sys.argv[3])

if len(sys.argv) == 5:
    breed = sys.argv[1]
    quantity = int(sys.argv[2])
    start = int(sys.argv[3])
    ends = int(sys.argv[4])

with open('../../breeds/breeds.json') as data_file:
    breeds_json = json.load(data_file)

breeds = []
breed_counter = 0

for breed_item in breeds_json:
    if end == breed_counter:
        break
    if breed_counter >= start:
        breeds.append(breed_item['breed'])
    breed_counter = breed_counter+1

for breed in breeds:
    try:
        os.makedirs('data/'+breed)
    except OSError as e:
        pass
        #print(e)

for breed in breeds:
    os.system('scrapy crawl pictures -a breed="'+breed+'" -a quantity='+str(quantity))
