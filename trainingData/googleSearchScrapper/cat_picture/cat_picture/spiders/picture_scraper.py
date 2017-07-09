import scrapy
import os, errno
import urllib
from scrapy.utils.response import open_in_browser
import json
import sys
import requests

class PictureItem(scrapy.Item):
    pic = scrapy.Field()


class PictureSpider(scrapy.Spider):
    name = "pictures"
    image_counter = 0
    breed_count = 0

    def __init__(self, start=-1, end=-1, quantity = 100, *args, **kwargs):
        super(PictureSpider, self).__init__(*args, **kwargs)
        self.start = int(start)
        self.end = int(end)
        self.quantity = int(quantity)

        with open('../../../breeds/breeds.json') as data_file:
            breeds_json = json.load(data_file)

        self.breeds = []
        self.breed_counter = 0
        json_breed_counter = 0
        self.start_urls = []

        for breed_item in breeds_json:
            if self.end == json_breed_counter:
                break
            if json_breed_counter >= self.start:
                breed = breed_item['breed']
                print breed
                self.breeds.append(breed)
                self.start_urls.append('https://www.google.com/search?tbm=isch&q='+ breed.replace(" ","+")+'+cat')
                try:
                    os.makedirs('data/'+breed)
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise
            json_breed_counter += 1


    def parse(self, response):
        imageTable = response.css("table.images_table")
        for tr in imageTable.css("tr"):
            for href in tr.css('img::attr(src)').extract():
                #print(href)
                try:
                    f = open('data/'+self.breeds[self.breed_counter]+'/'+str(self.image_counter)+'.png','wb')
                    #f = open(str(self.image_counter)+'.png','wb')

                    f.write(requests.get(href.encode()).content)
                    f.close()
                    sys.stdout.write('.')
                    sys.stdout.flush()

                except IOError as ex:
                    e = sys.exc_info()[0]
                    print(ex)
                self.image_counter += 1

                if self.image_counter == self.quantity:
                    print('\n'+self.breeds[self.breed_counter])
                    self.image_counter = 0
                    self.breed_counter += 1
                    return
        next_page = response.css('td.b a.fl::attr("href")').extract_first()

        if(response == None):
            raise ValueError("cant find next page")
        yield response.follow(next_page, self.parse)
