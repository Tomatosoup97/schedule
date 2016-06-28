# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class EventPipeline(object):
    def process_item(self, item, spider):
        """
        Extract data from gathered html
        """
        # Extract date
        date = str(item['date'])
        start = date.find('data-date') + 10 # add 10 to omit 'data-date'
        end = date.find('">') # closing tag
        item['date'] = date[start:end]

        # Extract name
        name = str(item['name'])
        start = name.find('">') + 2 # add 2 to omit '">'
        end = name.find('</a>')
        item['name'] = name[start:end]

        return item