import scrapy
from scrapy.utils.response import open_in_browser


class Breed(scrapy.Item):
    breed = scrapy.Field()


class BreedsSpider(scrapy.Spider):
    name = "breeds"
    start_urls = [
        'http://fifeweb.org/wp/breeds/breeds_prf_stn.php',
    ]


    def parse(self, response):
        #open_in_browser(response)
        table = response.css('#sp')
        #print(table)
        #print('-----------------')


        for a in range(13,64):
            xpath = 'tr:nth-child('+str(a)+') > td:nth-child(2)::text'
            #sp > tbody > tr:nth-child(15) > td:nth-child(2)


            value = table.css(xpath).extract_first()
            print(value)
            if value != None:
                yield Breed({'breed': value[1:]})

        '''
        breed_table = response.css('table.wikitable')[0]
        for breed in breed_table.css('tr'):
            value = breed.xpath('td/a/text()').extract_first()
            if value != None:
                yield Breed({'breed': value})
        '''
