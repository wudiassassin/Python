# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class DaoubanItem(Item):
    collection = 'douban'

    index = Field()
    image = Field()
    title = Field()
    director = Field()
    time = Field()
    score = Field()







