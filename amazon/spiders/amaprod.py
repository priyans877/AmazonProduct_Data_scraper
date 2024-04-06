import scrapy
from ..items import AmazonItem


class AmaprodSpider(scrapy.Spider):
    name = "amaprod"
    
    def start_requests(self):
        
        allowed_domains = ["amazon.com"]
        start_urls = ["https://www.amazon.in/LG-inches-Ultra-Smart-65A3PSA/dp/B0C8JN4NX4/ref=sr_1_1?crid=CJ692UKGDIH7&dib=eyJ2IjoiMSJ9.2TjsBeUlfbUHatdkaaF3vQs4KT3_ILOHifuRTobE1YMR2W0nJdqdYfYXj3aNVD2q3R-1OKs7bh6UpDiwzc0cmHK_brLn7DWyPthINuwZt1X4hgUauRGiHQy3l-UM_jbiUUU1j-U53pP9nqwMPlxVFWm5GUpLLCr9gd-CM8y4y9tXPTH_DOt5dtpWN4qT8Cd0nbKAcp_f4OWzo0MhV6Dib64YVitGY7HmnFGaksusTDKem_p4gL5VzaQfQy0j6J9zdDI9AtFb0Po4dNqGZLu-S0CfD6HJ3EI_QNPJlrSJEHg.Fh0F6BSY2v9KDMIIrocxdS6UF48WTicM2RRZW2uIUHk&dib_tag=se&keywords=lg%2Boled%2Bc2x%2B65&qid=1709285912&s=electronics&sprefix=lg%2Boled%2Bc2%2Celectronics%2C558&sr=1-1&th=1",
    "https://www.amazon.in/LG-inches-Ultra-Smart-55UR7500PSC/dp/B0C83J8YF8/ref=sr_1_3?crid=2H8TTF946MG03&dib=eyJ2IjoiMSJ9.yrjK9nP0PQ9oyBZe2UabRpcGBLvroRdtLjKbEDyrF-glePx9r43KXQZjtC0meKVWOAMq4bHx5V6pZi1FfZbct1Q4BlALn6rHTPox6wzbpnmtkTd-stF-ND1h74v4dJzW7FcGDhdJCxR7iIIY2m6rHgqcuE-7NiFvYJeEwIBYV8_kWWG92pcXiHW7heG9SDXJM_n2_hucQaoudexTuUM3ryO5IEzS_hn1wucuCfRkRajR6Nzar5RxMJFYtfwinOqTpM4FnbVWApRCzPUjygAs-ZGygz37YuBKqBJiIrg44G4.5C2EducHkStE5XHMybou7L2Y4dxZlKonQLFutvYwPNA&dib_tag=se&keywords=lg+tv&qid=1711514923&s=electronics&sprefix=lg+tv%2Celectronics%2C275&sr=1-3",
    "https://www.amazon.in/LG-inches-Ready-Smart-32LQ643BPTA/dp/B0CD1S96SM/ref=sr_1_4?crid=2H8TTF946MG03&dib=eyJ2IjoiMSJ9.yrjK9nP0PQ9oyBZe2UabRpcGBLvroRdtLjKbEDyrF-glePx9r43KXQZjtC0meKVWOAMq4bHx5V6pZi1FfZbct1Q4BlALn6rHTPox6wzbpnmtkTd-stF-ND1h74v4dJzW7FcGDhdJCxR7iIIY2m6rHgqcuE-7NiFvYJeEwIBYV8_kWWG92pcXiHW7heG9SDXJM_n2_hucQaoudexTuUM3ryO5IEzS_hn1wucuCfRkRajR6Nzar5RxMJFYtfwinOqTpM4FnbVWApRCzPUjygAs-ZGygz37YuBKqBJiIrg44G4.5C2EducHkStE5XHMybou7L2Y4dxZlKonQLFutvYwPNA&dib_tag=se&keywords=lg+tv&qid=1711514923&s=electronics&sprefix=lg+tv%2Celectronics%2C275&sr=1-4",
    "https://www.amazon.in/LG-inches-Ultra-Smart-43UR7500PSC/dp/B0C82ZHYQ8/ref=sr_1_5?crid=2H8TTF946MG03&dib=eyJ2IjoiMSJ9.yrjK9nP0PQ9oyBZe2UabRpcGBLvroRdtLjKbEDyrF-glePx9r43KXQZjtC0meKVWOAMq4bHx5V6pZi1FfZbct1Q4BlALn6rHTPox6wzbpnmtkTd-stF-ND1h74v4dJzW7FcGDhdJCxR7iIIY2m6rHgqcuE-7NiFvYJeEwIBYV8_kWWG92pcXiHW7heG9SDXJM_n2_hucQaoudexTuUM3ryO5IEzS_hn1wucuCfRkRajR6Nzar5RxMJFYtfwinOqTpM4FnbVWApRCzPUjygAs-ZGygz37YuBKqBJiIrg44G4.5C2EducHkStE5XHMybou7L2Y4dxZlKonQLFutvYwPNA&dib_tag=se&keywords=lg+tv&qid=1711514923&s=electronics&sprefix=lg+tv%2Celectronics%2C275&sr=1-5",
    "https://www.amazon.in/LG-Inches-Ultra-Smart-43UQ7550PSF/dp/B0BFQT9THN/ref=sr_1_6?crid=2H8TTF946MG03&dib=eyJ2IjoiMSJ9.yrjK9nP0PQ9oyBZe2UabRpcGBLvroRdtLjKbEDyrF-glePx9r43KXQZjtC0meKVWOAMq4bHx5V6pZi1FfZbct1Q4BlALn6rHTPox6wzbpnmtkTd-stF-ND1h74v4dJzW7FcGDhdJCxR7iIIY2m6rHgqcuE-7NiFvYJeEwIBYV8_kWWG92pcXiHW7heG9SDXJM_n2_hucQaoudexTuUM3ryO5IEzS_hn1wucuCfRkRajR6Nzar5RxMJFYtfwinOqTpM4FnbVWApRCzPUjygAs-ZGygz37YuBKqBJiIrg44G4.5C2EducHkStE5XHMybou7L2Y4dxZlKonQLFutvYwPNA&dib_tag=se&keywords=lg+tv&qid=1711514923&s=electronics&sprefix=lg+tv%2Celectronics%2C275&sr=1-6",
    "https://www.amazon.in/LG-inches-Ultra-Smart-50UR7500PSC/dp/B0C839R7BY/ref=sr_1_7?crid=2H8TTF946MG03&dib=eyJ2IjoiMSJ9.yrjK9nP0PQ9oyBZe2UabRpcGBLvroRdtLjKbEDyrF-glePx9r43KXQZjtC0meKVWOAMq4bHx5V6pZi1FfZbct1Q4BlALn6rHTPox6wzbpnmtkTd-stF-ND1h74v4dJzW7FcGDhdJCxR7iIIY2m6rHgqcuE-7NiFvYJeEwIBYV8_kWWG92pcXiHW7heG9SDXJM_n2_hucQaoudexTuUM3ryO5IEzS_hn1wucuCfRkRajR6Nzar5RxMJFYtfwinOqTpM4FnbVWApRCzPUjygAs-ZGygz37YuBKqBJiIrg44G4.5C2EducHkStE5XHMybou7L2Y4dxZlKonQLFutvYwPNA&dib_tag=se&keywords=lg+tv&qid=1711514923&s=electronics&sprefix=lg+tv%2Celectronics%2C275&sr=1-7",
    "https://www.amazon.in/LG-inches-Ultra-Smart-65UR7500PSC/dp/B0C834YC4Z/ref=sr_1_9?crid=2H8TTF946MG03&dib=eyJ2IjoiMSJ9.yrjK9nP0PQ9oyBZe2UabRpcGBLvroRdtLjKbEDyrF-glePx9r43KXQZjtC0meKVWOAMq4bHx5V6pZi1FfZbct1Q4BlALn6rHTPox6wzbpnmtkTd-stF-ND1h74v4dJzW7FcGDhdJCxR7iIIY2m6rHgqcuE-7NiFvYJeEwIBYV8_kWWG92pcXiHW7heG9SDXJM_n2_hucQaoudexTuUM3ryO5IEzS_hn1wucuCfRkRajR6Nzar5RxMJFYtfwinOqTpM4FnbVWApRCzPUjygAs-ZGygz37YuBKqBJiIrg44G4.5C2EducHkStE5XHMybou7L2Y4dxZlKonQLFutvYwPNA&dib_tag=se&keywords=lg+tv&qid=1711514923&s=electronics&sprefix=lg+tv%2Celectronics%2C275&sr=1-9",
    "https://www.amazon.in/LG-Inches-Ultra-Smart-OLED55C2PSC/dp/B0B5H3BWSB/ref=sr_1_10?crid=2H8TTF946MG03&dib=eyJ2IjoiMSJ9.yrjK9nP0PQ9oyBZe2UabRpcGBLvroRdtLjKbEDyrF-glePx9r43KXQZjtC0meKVWOAMq4bHx5V6pZi1FfZbct1Q4BlALn6rHTPox6wzbpnmtkTd-stF-ND1h74v4dJzW7FcGDhdJCxR7iIIY2m6rHgqcuE-7NiFvYJeEwIBYV8_kWWG92pcXiHW7heG9SDXJM_n2_hucQaoudexTuUM3ryO5IEzS_hn1wucuCfRkRajR6Nzar5RxMJFYtfwinOqTpM4FnbVWApRCzPUjygAs-ZGygz37YuBKqBJiIrg44G4.5C2EducHkStE5XHMybou7L2Y4dxZlKonQLFutvYwPNA&dib_tag=se&keywords=lg+tv&qid=1711514923&s=electronics&sprefix=lg+tv%2Celectronics%2C275&sr=1-10",
    "https://www.amazon.in/LG-inches-Collection-OLEDevo-55LX1QPSA/dp/B0BM4PM1HW/ref=sr_1_13?crid=2H8TTF946MG03&dib=eyJ2IjoiMSJ9.yrjK9nP0PQ9oyBZe2UabRpcGBLvroRdtLjKbEDyrF-glePx9r43KXQZjtC0meKVWOAMq4bHx5V6pZi1FfZbct1Q4BlALn6rHTPox6wzbpnmtkTd-stF-ND1h74v4dJzW7FcGDhdJCxR7iIIY2m6rHgqcuE-7NiFvYJeEwIBYV8_kWWG92pcXiHW7heG9SDXJM_n2_hucQaoudexTuUM3ryO5IEzS_hn1wucuCfRkRajR6Nzar5RxMJFYtfwinOqTpM4FnbVWApRCzPUjygAs-ZGygz37YuBKqBJiIrg44G4.5C2EducHkStE5XHMybou7L2Y4dxZlKonQLFutvYwPNA&dib_tag=se&keywords=lg+tv&qid=1711514923&s=electronics&sprefix=lg+tv%2Celectronics%2C275&sr=1-13",
    "https://www.amazon.in/LG-Smart-WebOS-Active-43UR8040PSB_Black/dp/B0CCJ6RRQ5/ref=sr_1_14?crid=2H8TTF946MG03&dib=eyJ2IjoiMSJ9.yrjK9nP0PQ9oyBZe2UabRpcGBLvroRdtLjKbEDyrF-glePx9r43KXQZjtC0meKVWOAMq4bHx5V6pZi1FfZbct1Q4BlALn6rHTPox6wzbpnmtkTd-stF-ND1h74v4dJzW7FcGDhdJCxR7iIIY2m6rHgqcuE-7NiFvYJeEwIBYV8_kWWG92pcXiHW7heG9SDXJM_n2_hucQaoudexTuUM3ryO5IEzS_hn1wucuCfRkRajR6Nzar5RxMJFYtfwinOqTpM4FnbVWApRCzPUjygAs-ZGygz37YuBKqBJiIrg44G4.5C2EducHkStE5XHMybou7L2Y4dxZlKonQLFutvYwPNA&dib_tag=se&keywords=lg+tv&qid=1711514923&s=electronics&sprefix=lg+tv%2Celectronics%2C275&sr=1-14"
    
    ]
        for urls in start_urls:
            yield scrapy.Request(url=urls,callback=self.parse)
    
    
    
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
        
        with open("my_file1.txt",'a+') as F:
            for i in range(len(name)):
                F.write(f"\nName : {name[i]}\nPrice :{price[i]}\nRating :{rating[i]}\nGlobal rating Count : {no_of_review[i]}\nAvailable bankoffer :{bankoffer_count[i]}\n")
                F.write("---------"*6)
            F.close()   
            
        
    
                 
