# -*- coding: utf-8 -*-
from datetime import date

import scrapy
from scrapper.items import EventItem

class EventSpider(scrapy.Spider):
    """
    Spider that returns most important events in Poland
    for current and approaching year
    """
    name = 'event'
    current_year = date.today().year
    allowed_domains = ['www.kalendarzswiat.pl']
    start_urls = [
        'http://www.kalendarzswiat.pl/swieta/{}'.format(current_year),
        'http://www.kalendarzswiat.pl/swieta/{}'.format(current_year + 1),
    ]

    def parse(self, response):
        SELECTOR = '.left-column .tab_easy tr.even, ' + \
                    '.left-column .tab_easy tr.odd'
        events = response.css(SELECTOR)
        items = []

        for event in events:
            item = EventItem()
            item['date'] = event.css('td > div > a').extract()
            item['name'] = event.css('td > a').extract()
            items.append(item)

        return items