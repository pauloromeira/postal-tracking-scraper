# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest
from scrapy.loader import ItemLoader
from trackings.items import ItemTrack
from datetime import datetime


class CorreiosSpider(scrapy.Spider):
    name = 'correios'
    allowed_domains = ['correios.com.br']

    def start_requests(self):
        url='http://www2.correios.com.br/sistemas/rastreamento/resultado.cfm'
        headers={ 'Referer':'http://www.correios.com.br/para-voce' }
        formdata={ 'objetos': '<tracking-number>' }

        yield FormRequest(url, headers=headers, formdata=formdata)

    def parse(self, response):
        for event in response.css('table.listEvent.sro tr'):
            loader = ItemLoader(ItemTrack(), event)
            *timestamp, location = \
                    loader.get_css('td.sroDtEvent ::text', re='[^\s].*[^\s]')

            loader.add_value('location', location)
            loader.add_value('timestamp', timestamp)
            import ipdb; ipdb.set_trace()

            yield loader.load_item()
