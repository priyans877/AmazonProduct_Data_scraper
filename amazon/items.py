# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_rating = scrapy.Field()  
    product_rating_count = scrapy.Field()  
    product_Bank_offer_cont = scrapy.Field()  
    pass

class reviitem(scrapy.Item):
    ProfileName=scrapy.Field()
    StarText=scrapy.Field()
    Title=scrapy.Field()
    URL=scrapy.Field()
    Review=scrapy.Field()
    pass
