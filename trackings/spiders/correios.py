# -*- coding: utf-8 -*-

import scrapy
from scrapy import FormRequest
from trackings.items import ItemTrackLoader


class CorreiosSpider(scrapy.Spider):
    name = 'correios'
    allowed_domains = ['correios.com.br']
    custom_settings = { 'RETRY_TIMES': 5 }

    def __init__(self, trackings, *args, **kwargs):
        super(CorreiosSpider, self).__init__(*args, **kwargs)
        self.tracking_numbers = trackings

    def start_requests(self):
        url = 'http://www2.correios.com.br/sistemas/' \
              'rastreamento/resultado_semcontent.cfm'

        for tracking_number in self.tracking_numbers.split(';'):
            tracking_number = tracking_number.strip()
            formdata={ 'objetos': tracking_number }
            meta = { 'tracking_number': tracking_number }

            yield FormRequest(url,
                              meta=meta,
                              formdata=formdata)

    def parse(self, response):
        for track in response.css('table.listEvent.sro tr'):
            loader = ItemTrackLoader(selector=track)
            loader.add_value('tracking_number',
                             response.meta['tracking_number'])

            *timestamp, location = \
                    loader.get_css('td.sroDtEvent ::text', re='[^\s].*[^\s]')

            loader.add_value('location', location)
            loader.add_value('timestamp', timestamp)
            loader.add_css('event', 'td.sroLbEvent>strong::text')
            loader.add_css('description', 'td.sroLbEvent::text')

            yield loader.load_item()
