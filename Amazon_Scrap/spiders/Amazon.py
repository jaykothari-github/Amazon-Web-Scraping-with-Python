import scrapy
from ..items import AmazonScrapItem


class AmazonSpider(scrapy.Spider):
    name = 'Amazon'
    # allowed_domains = ['Amazon.in']
    start_urls = ['https://www.amazon.in/s?k=mobile+phone&i=electronics&crichd=8JAMGTSNJLC5&sprefix=mobil%2Celectronics%2C527&ref=nb_sb_ss_ts-doa-p_3_5']
    k = 2

    def parse(self, response):
        items = AmazonScrapItem()
        
        val = response.css('.s-border-top')
        
        for div in val:

            title = div.css('.a-text-normal::text')[0].extract()
            price = div.css('.a-price-whole::text')[0].extract()
            try:
                img = div.css('.s-image::attr(src)')[0].extract()

            except: 
                img = 'No Image'
                
            items['title'] = title
            items['price'] = price
            items['img'] = img

            yield items

        # check = response.css('.a-pagination a::attr(href)').get()

        if self.k < 7:
            
            next_url = f'https://www.amazon.in/s?k=mobile+phone&i=electronics&page={self.k}&crichd=8JAMGTSNJLC5&qid=1639909083&sprefix=mobil%2Celectronics%2C527&ref=sr_pg_{self.k-1}'
            print(f'----------Upto Next page > {self.k} ---------------------------------')
            self.k += 1
            yield response.follow(next_url,callback = self.parse)
