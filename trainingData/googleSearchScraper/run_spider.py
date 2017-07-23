import os
import json
import sys
import argparse

DEFAULT_JSON_PATH = '../../breeds/breeds_FIFe.json'
DEFAULT_OUT_PATH = '~'

parser = argparse.ArgumentParser()
parser.parse_args()

parser.add_argument("--out_path", type=str, default=DEFAULT_OUT_PATH,
                    help="where to output the pictures")

parser.add_argument("--json_path", type=str, default=DEFAULT_JSON_PATH,
                    help="location of breeds json file")

args = parser.parse_args()

if (DEFAULT_OUT_PATH == args.out_path):
    str_list = args.json_path.split('/')
    args.out_path = str_list[len(str_list)-1]


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

with open(args.json_path) as data_file:
    breeds_json = json.load(data_file)

breeds = []
breed_counter = 0

for breed_item in breeds_json:
    if end == breed_counter:
        break
    if breed_counter >= start:
        breeds.append(breed_item['breed'])
    breed_counter = breed_counter+1
'''
for breed in breeds:
    try:
        os.makedirs(args.out_path+'/'+breed)
    except OSError as e:
        pass
        #print(e)
'''

for breed in breeds:


    os.system('scrapy crawl pictures -a breed="'+breed+'" -a quantity='+str(quantity)
        +' -a out_path="'+args.out_path+'"')
