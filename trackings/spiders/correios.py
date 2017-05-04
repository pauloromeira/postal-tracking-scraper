# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest


class CorreiosSpider(scrapy.Spider):
    name = 'correios'
    allowed_domains = ['correios.com.br']

    def start_requests(self):
        url='http://www2.correios.com.br/sistemas/rastreamento/resultado.cfm'
        headers={ 'Referer':'http://www.correios.com.br/para-voce' }
        formdata={ 'objetos': '<tracking-number>' }

        yield FormRequest(url, headers=headers, formdata=formdata)

    def parse(self, response):
        from scrapy.shell import open_in_browser
        open_in_browser(response)
