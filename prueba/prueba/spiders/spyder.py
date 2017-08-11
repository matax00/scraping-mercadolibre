import scrapy
from scrapy.spiders import CrawlSpider, Rule 
from scrapy.linkextractors import LinkExtractor 
from prueba.items import PruebaItem 
from scrapy.exceptions import CloseSpider



class PruebaSpider(CrawlSpider):
	name = 'prueba'
	item_count = 0
	allowed_domain = ['https://www.mercadolibre.com.ve/']
	start_urls = ['https://perfil.mercadolibre.com.ve/GLOBAL+RETAIL']
	rules = { 
				Rule(LinkExtractor(allow =(), restrict_xpaths = ('//li/a[@class="nextLink"]')), callback = 'parse_item', follow = False)
	}

	def parse_item(self, response):
		prueba_item = PruebaItem()

		prueba_item['producto'] = response.xpath('//p[@class="feedback-item-data"]/span/text()').extract()
		prueba_item['fecha'] = response.xpath('//div[@class="feedback-date"]/span/text()').extract()
		self.item_count += 1
		if self.item_count > 200000:
			raise CloseSpider('item_exceeded')
		yield prueba_item

#class PruebaSpider(CrawlSpider):
#	name = 'prueba'
#	item_count = 0
#	allowed_domain = ['http://www.directorionacionalautopartista.co']
#	start_urls = ['http://www.directorionacionalautopartista.co/index.php?id_category=3&controller=category', 
#		 	'http://www.directorionacionalautopartista.co/index.php?id_category=46&controller=category', 
#		 	'http://www.directorionacionalautopartista.co/index.php?id_category=47&controller=category',
#		 	'http://www.directorionacionalautopartista.co/index.php?id_category=48&controller=category']
#	rules = { 
#	Rule(LinkExtractor(allow =(), restrict_xpaths =('//section/div/ul[@class="tree dhtml"]/li[@class="selected_li"]/a[@class="selected"]'))),
#	Rule(LinkExtractor(allow =(), restrict_xpaths =('//li[@class="selected_li"]/ul/li/a'))),
#	Rule(LinkExtractor(allow =(), restrict_xpaths =('//li[@class="selected_li"]/ul/li/ul/li/a'))),
#	Rule(LinkExtractor(allow =(), restrict_xpaths =('//li[@class="selected_li"]/ul/li/ul/li/ul/li/a'))),
#	Rule(LinkExtractor(allow =(), restrict_xpaths =('//div[@class="button-container"]/a')), 
#													callback = 'parse_item', follow = False)
#	}


#	def parse_item(self, response):
#		prueba_item = PruebaItem()
#
#		prueba_item['tienda'] = response.xpath('//h1/text()').extract()
#		prueba_item['informacion'] = response.xpath('//div[@class="rte"]/text()').extract()
#		prueba_item['categorias'] = response.xpath('//div[@class="breadcrumb clearfix"]/span/a/text()').extract()
#		self.item_count += 1
#		if self.item_count > 200000:
#			raise CloseSpider('item_exceeded')
#		yield prueba_item