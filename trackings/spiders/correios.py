# -*- coding: utf-8 -*-
import scrapy


class CorreiosSpider(scrapy.Spider):
    name = "correios"
    allowed_domains = ["correios.com.br"]
    start_urls = ['http://correios.com.br/']

    def parse(self, response):
        pass
