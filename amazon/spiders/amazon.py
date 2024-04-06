import scrapy
from pathlib import Path
from ..items import AmazonItem,reviitem
import re
from bs4 import BeautifulSoup


class AmazonSpider(scrapy.Spider):
    
    name = "amazon"
    
    def start_requests(self):
        header={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding':'gzip, deflate, br, zstd',
        'Accept-Language':'en-US,en;q=0.9,hi;q=0.8',
        'Sec-Ch-Ua':'"Google Chrome";v="123","Not:A-Brand";v="8","Chromium";v="123"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Fetch-Dest':'document',
        'Sec-Fetch-Mode':'navigate',
        'Sec-Fetch-Site':'same-origin',
        'Sec-Fetch-User':'?1',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }

        urls = [
            "https://www.amazon.in/s?k=lg+tv+43%2B+inch&crid=2HE0DEB1SSM5B&sprefix=Lg+tv+%2Caps%2C420&ref=nb_sb_ss_ts-doa-p_3_6"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        item=AmazonItem()
        Link = response.css('.a-text-normal').css('a::attr(href)').extract()
        asin=set()
        for result in Link:
            ASIN = re.findall(r"(?<=dp/)[A-Z0-9]{10}",result)
            if len(ASIN)==1:
                asin.add(ASIN[0])
            
        print(asin)
                
                
        for i in asin:
            url=f"https://amazon.in/dp/{i}/"
            yield scrapy.Request(url=f"https://amazon.in/dp/{i}/",callback=self.productpage)
            
            
        
    def productpage(self,response):
        item=AmazonItem()
        
        name=response.css("#productTitle::text").extract()
        
        price=response.css(".a-price-whole::text").extract()
        
        rating=response.css("#cm_cr_dp_d_rating_histogram .a-color-base::text").extract()
        
        no_of_review=response.css("#cm_cr_dp_d_rating_histogram .a-color-secondary::text").extract()
        
        bankoffer_count=response.css("#itembox-InstantBankDiscount .vsx-offers-count::text").extract()
    
        if len(name)>=1 and any(ele.lower()=="lg" for ele in name[0].split(" ")):
            item["product_name"]=name
            item["product_price"]=price
            item['product_rating']=rating
            item['product_rating_count']=no_of_review
            item['product_Bank_offer_cont']=bankoffer_count
        
    
    
            with open("my_file2.txt", "a+") as F:
                for i in range(len(name)):
                    F.write(f'\n NAME:{name[i]}\nprice:{price[i]}\nrating:{rating[i]}\nNo Of Rating :{no_of_review[i]}\n No of bank Offers:{bankoffer_count[i]}')
                    F.write    ("-------------------------------------------------")
                F.close()  

    
    def reviewpage(self,response):
        i=0
        item=AmazonItem()
        title=response.css('.product-title h1 a::text').extract()
        for rev in response.css('#histogramTable .a-histogram-row .a-span10 a'):
            if len(title)>=1 and title[0].split(" ")[0].lower()=="lg":
                for revie in rev.css('a ::attr(title)'):
                    a=revie.extract()
                    b=a.split(" ")
                    item[f"Star_{b[4]}"]=b[0]
        print("--------"*6)
        yield item
        
    
        
    

        
        
        
