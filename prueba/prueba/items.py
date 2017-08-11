# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PruebaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    	
    #Otra informacion
    #categoria = scrapy.field()
    #dir1 = scrapy.field()
    #dir2 = scrapy.field()
    #categoria_direccion = scrapy.field()
    #subcategoria_direccion = scrapy.field()
    # Informacion de las tiendas
    tienda = scrapy.Field()
    informacion = scrapy.Field()
    categorias = scrapy.Field()

    #Para ML
    producto = scrapy.Field()
    fecha = scrapy.Field()