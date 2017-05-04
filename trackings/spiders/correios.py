# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest
from scrapy.loader import ItemLoader
from trackings.items import ItemTrack
from datetime import datetime


class CorreiosSpider(scrapy.Spider):
    name = 'correios'
    allowed_domains = ['correios.com.br']

    def __init__(self, trackings, *args, **kwargs):
        super(CorreiosSpider, self).__init__(*args, **kwargs)
        self.tracking_numbers = trackings

    def start_requests(self):
        url='http://www2.correios.com.br/sistemas/rastreamento/resultado.cfm'
        headers={ 'Referer':'http://www.correios.com.br/para-voce' }

        for tracking_number in self.tracking_numbers.split(';'):
            tracking_number = tracking_number.strip()
            formdata={ 'objetos': tracking_number }
            meta = { 'tracking_number': tracking_number }

            yield FormRequest(url, meta=meta, headers=headers, formdata=formdata)

    def parse(self, response):
        for event in response.css('table.listEvent.sro tr'):
            loader = ItemLoader(ItemTrack(), event)
            loader.add_value('tracking_number',
                             response.meta['tracking_number'])

            *timestamp, location = \
                    loader.get_css('td.sroDtEvent ::text', re='[^\s].*[^\s]')

            loader.add_value('location', location)
            loader.add_value('timestamp', timestamp)
            import ipdb; ipdb.set_trace()

            yield loader.load_item()
