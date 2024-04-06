import scrapy
from ..items import AmazonItem


class AmaprodSpider(scrapy.Spider):
    name = "amaone"
    
    def start_requests(self):
        
        allowed_domains = ["amazon.com"]
        start_urls = ["https://www.amazon.in/LG-inches-Ultra-Smart-65A3PSA/dp/B0C8JN4NX4/ref=sr_1_1?crid=CJ692UKGDIH7&dib=eyJ2IjoiMSJ9.2TjsBeUlfbUHatdkaaF3vQs4KT3_ILOHifuRTobE1YMR2W0nJdqdYfYXj3aNVD2q3R-1OKs7bh6UpDiwzc0cmHK_brLn7DWyPthINuwZt1X4hgUauRGiHQy3l-UM_jbiUUU1j-U53pP9nqwMPlxVFWm5GUpLLCr9gd-CM8y4y9tXPTH_DOt5dtpWN4qT8Cd0nbKAcp_f4OWzo0MhV6Dib64YVitGY7HmnFGaksusTDKem_p4gL5VzaQfQy0j6J9zdDI9AtFb0Po4dNqGZLu-S0CfD6HJ3EI_QNPJlrSJEHg.Fh0F6BSY2v9KDMIIrocxdS6UF48WTicM2RRZW2uIUHk&dib_tag=se&keywords=lg%2Boled%2Bc2x%2B65&qid=1709285912&s=electronics&sprefix=lg%2Boled%2Bc2%2Celectronics%2C558&sr=1-1&th=1"    
    ]
        for i in range(100):
            print(i)
            urls="https://www.amazon.in/LG-inches-Ultra-Smart-65A3PSA/dp/B0C8JN4NX4/ref=sr_1_1?crid=CJ692UKGDIH7&dib=eyJ2IjoiMSJ9.2TjsBeUlfbUHatdkaaF3vQs4KT3_ILOHifuRTobE1YMR2W0nJdqdYfYXj3aNVD2q3R-1OKs7bh6UpDiwzc0cmHK_brLn7DWyPthINuwZt1X4hgUauRGiHQy3l-UM_jbiUUU1j-U53pP9nqwMPlxVFWm5GUpLLCr9gd-CM8y4y9tXPTH_DOt5dtpWN4qT8Cd0nbKAcp_f4OWzo0MhV6Dib64YVitGY7HmnFGaksusTDKem_p4gL5VzaQfQy0j6J9zdDI9AtFb0Po4dNqGZLu-S0CfD6HJ3EI_QNPJlrSJEHg.Fh0F6BSY2v9KDMIIrocxdS6UF48WTicM2RRZW2uIUHk&dib_tag=se&keywords=lg%2Boled%2Bc2x%2B65&qid=1709285912&s=electronics&sprefix=lg%2Boled%2Bc2%2Celectronics%2C558&sr=1-1&th=1"
            yield scrapy.Request(url=urls,dont_filter=True,callback=self.parse)
    
    
    
    def parse(self, response):
        items=AmazonItem()
        #Product title  
        
        name=response.css("#productTitle::text").extract()
        
        #product Price 
        price=response.css(".a-price-whole::text").extract()
        
        
        #product overall Rating 
        rating=response.css("#cm_cr_dp_d_rating_histogram .a-color-base::text").extract()
        
        
        #product Total no of global review 
        no_of_review=response.css("#cm_cr_dp_d_rating_histogram .a-color-secondary::text").extract()
        
        #Product total bank offer at time o f scraping 
        
        bankoffer_count=response.css("#itembox-InstantBankDiscount .vsx-offers-count::text").extract()
    

        
        #Yeilding data in scrapy item dataset 
        items["product_name"]=name
        items["product_price"]=price
        items['product_rating']=rating
        items['product_rating_count']=no_of_review
        items['product_Bank_offer_cont']=bankoffer_count
        
        
        #Saving Product Data Value From sites into Text file
        
        with open("my_file3.txt",'a+') as F:
            for i in range(len(name)):
                F.write(f"Name:{name[i]}\nPrice :{price[i]}\nRating :{rating[i]}\nGlobal rating Count : {no_of_review[i]}\nAvailable bankoffer :{bankoffer_count[i]}\n")
                F.write("---------"*6 +"\n")
            F.close()   
            
        
    
                 
