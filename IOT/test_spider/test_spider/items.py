# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class SbyxjkItem(Item):
    collection = 'sbyxjk'

    eqpid = Field()
    color = Field()


class GcglItem(Item):
    collection = 'gcgl'

    affiliationID = Field()
    affiliation = Field()
    remarks = Field()
    delFlg = Field()





