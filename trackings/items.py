# -*- coding: utf-8 -*-

from datetime import datetime
from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, MapCompose, Join
from unicodedata import normalize


class ItemTrack(Item):
    tracking_number = Field()
    event = Field()
    description = Field()
    location = Field()
    timestamp = Field()

class ItemTrackLoader(ItemLoader):
    default_item_class = ItemTrack
    default_input_processor = MapCompose(lambda s: normalize('NFKC', s),
                                         str.strip)
    default_output_processor = Compose(Join(' '), str.strip)
    timestamp_out = Compose(Join(' '),
                            lambda d: datetime.strptime(d, '%d/%m/%Y %H:%M'))
