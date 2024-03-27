import scrapy
from scrapy import Request
import re
from ..items import reviitem


class ReviewsSpider(scrapy.Spider):
    name = 'reviews'

    def start_requests(self):
        start_url=["https://www.amazon.in/LG-inches-Ultra-Smart-65A3PSA/dp/B0C8JN4NX4/ref=sr_1_1?crid=CJ692UKGDIH7&dib=eyJ2IjoiMSJ9.2TjsBeUlfbUHatdkaaF3vQs4KT3_ILOHifuRTobE1YMR2W0nJdqdYfYXj3aNVD2q3R-1OKs7bh6UpDiwzc0cmHK_brLn7DWyPthINuwZt1X4hgUauRGiHQy3l-UM_jbiUUU1j-U53pP9nqwMPlxVFWm5GUpLLCr9gd-CM8y4y9tXPTH_DOt5dtpWN4qT8Cd0nbKAcp_f4OWzo0MhV6Dib64YVitGY7HmnFGaksusTDKem_p4gL5VzaQfQy0j6J9zdDI9AtFb0Po4dNqGZLu-S0CfD6HJ3EI_QNPJlrSJEHg.Fh0F6BSY2v9KDMIIrocxdS6UF48WTicM2RRZW2uIUHk&dib_tag=se&keywords=lg%2Boled%2Bc2x%2B65&qid=1709285912&s=electronics&sprefix=lg%2Boled%2Bc2%2Celectronics%2C558&sr=1-1&th=1"]
        for asin in start_url:
            yield Request(url=asin,callback=self.parse)

    def parse(self, response):
        item = reviitem()
        print("HEY")
        for rev in response.css('#cm_cr-review_list [data-hook="review"]'):
            print(rev)
            stars = rev.css('[data-hook="review-star-rating"] ::text').get()
            stars = stars.replace('out of 5 stars', '').strip() if stars else None
            review_date_text = rev.css('[data-hook="review-date"] ::text').get()
            item['ProfileName'] = rev.css('.a-profile-name ::text').get()
            item['Stars'] = stars
            item['StarsText'] = rev.css('[data-hook="review-star-rating"] ::text').get()
            item['Title'] = rev.css('[data-hook="review-title"] span ::text').get()
            review_text = rev.css('[data-hook="review-body"] span::text').getall()
        yield item

