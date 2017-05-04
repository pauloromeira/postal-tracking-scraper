# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader.processors import Compose, Join, TakeFirst
from datetime import datetime
from unicodedata import normalize

# class Item(Item):
#     tracking_number = Field()
#     description = Field()

class ItemTrack(Item):
    tracking_number = Field()
    title = Field()
    description = Field()
    location = Field(
            output_processor =
                Compose(TakeFirst(), lambda l: normalize('NFKC', l))
            )
    timestamp = Field(
            output_processor = 
                Compose(Join(' '),
                        lambda d: datetime.strptime(d, '%d/%m/%Y %H:%M'))
                )
