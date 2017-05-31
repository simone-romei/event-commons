# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EventItem(scrapy.Item):  
	# Structure
	id = scrapy.Field()
	# What 
	name = scrapy.Field()
	url = scrapy.Field()
	imgList = scrapy.Field()
	imgDetail = scrapy.Field()
	# When
	dateStart = scrapy.Field()
	dateEnd = scrapy.Field()
	# Where
	country = scrapy.Field()
	city = scrapy.Field()
	locality = scrapy.Field()
	address = scrapy.Field()
	coordinate = scrapy.Field()
	place = scrapy.Field()
	zone = scrapy.Field()
	# Spider
	spiderName = scrapy.Field()
	spiderSource = scrapy.Field()
	# Extra
	extras = scrapy.Field()
