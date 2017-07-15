import scrapy
import os, errno
import urllib
from scrapy.utils.response import open_in_browser
import sys
import requests

class PictureSpider(scrapy.Spider):
    name = "pictures"
    image_counter = 0
    breed_count = 0

    def __init__(self,quantity = 60, breed='', *args, **kwargs):
        super(PictureSpider, self).__init__(*args, **kwargs)
        self.quantity = int(quantity)
        self.breed = breed

        self.breeds = []
        self.start_urls = []


        self.start_urls.append('https://www.google.com/search?tbm=isch&q='+ breed.replace(" ","+")+'+cat')
        try:
            os.makedirs('data/'+breed)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise


    def parse(self, response):
        imageTable = response.css("table.images_table")
        for tr in imageTable.css("tr"):
            for href in tr.css('img::attr(src)').extract():
                #print(href)
                try:
                    f = open('data/'+self.breed+'/'+str(self.image_counter)+'.jpg','wb')
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
                    print('\n'+self.breed)
                    self.image_counter = 0
                    return
        next_page = response.css('td.b a.fl::attr("href")')
        next_page = next_page[len(next_page)-1].extract()

        if(response == None):
            raise ValueError("cant find next page")
        yield response.follow(next_page, self.parse)
