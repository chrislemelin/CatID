import scrapy


class Breed(scrapy.Item):
    breed = scrapy.Field()


class BreedsSpider(scrapy.Spider):
    name = "breeds"
    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_cat_breeds',
    ]


    def parse(self, response):
        breed_table = response.css('table.wikitable')[0]
        for breed in breed_table.css('tr'):
            value = breed.xpath('td/a/text()').extract_first()
            if value != None:
                yield Breed({'breed': value})
