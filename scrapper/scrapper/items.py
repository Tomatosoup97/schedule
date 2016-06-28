# -*- coding: utf-8 -*-
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EventItem(scrapy.Item):
    name = scrapy.Field()
    date = scrapy.Field()