# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy.loader import ItemLoader
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from event.items import EventItem

class SalarazzmatazzSpider(scrapy.Spider):
    name = 'salarazzmatazz'

    allowed_domains = ['www.salarazzmatazz.com']

    start_urls = ['http://www.salarazzmatazz.com']

    def start_requests(self):
            date = datetime.date.today()
            
             # Search for SHOWs
            yield scrapy.Request(
                url=self.start_urls[0]+'/op/conciertos/%02d,%04d' % (date.month, date.year), 
                callback=self.parseShows
            )

    def parseShows(self, response):
        self.logger.info('parse of shows %s', response.url)
        # Loop On events
        items = []
        events = response.selector.css('table.evento')
        for event in events:
            item = EventItem()
            item['name'] = "".join(event.css('td.sala a::text').extract()).encode('utf-8')
            item['url'] = self.start_urls[0] + "".join(event.css('td.sala a::attr(href)').extract()).encode('utf-8')
            item['imgList'] = self.start_urls[0] + "".join(event.css('td.inicial img::attr(src)').extract()).encode('utf-8')
            #item['zone'] = "".join(event.css('td.sala span:first-child ::text').extract()).encode('utf-8')
            item['dateStart'] = "".join(event.css('span.fecha ::text').extract()).encode("utf-8")
            items.append(item)
        return items