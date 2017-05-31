# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pysolr
from scrapy.exceptions import DropItem


class EventSpider(object):
    def process_item(self, item, spider):
    	item['spiderName'] = spider.name
        item['spiderSource'] = spider.start_urls[0]        
        return item

class EventValidator(object):
    def process_item(self, item, spider):
    	# URL
    	if 'url' not in item or not item['name'] or not item['name'].strip():
    		raise DropItem("Missing URL in %s" % item)
    	# Name
    	if 'name' in item and item['name'] and item['name'].strip():
    		item['name'] = item['name'].strip().lower()
    	else:
    		raise DropItem("Missing name in %s" % item)
    	# Zone
    	if 'zone' in item and item['zone'] and item['zone'].strip():
    		item['zone'] = item['zone'].strip().lower()
    	return item

class EventSolrWriter(object):
	def open_spider(self, spider):
		self.client = pysolr.Solr('http://192.168.99.100:8983/solr/eventCore', timeout=10)

	def process_item(self, item, spider):
		self.client.add([{
			'id':item['url']

			}])



