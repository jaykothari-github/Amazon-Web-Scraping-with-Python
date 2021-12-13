import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'Amazon'
    # allowed_domains = ['Amazon.in']
    start_urls = ['https://www.amazon.in/s?k=mobile+phone&i=electronics&crid=8JAMGTSNJLC5&sprefix=mobil%2Celectronics%2C527&ref=nb_sb_ss_ts-doa-p_3_5']

    def parse(self, response):
        
        val = response.css('.s-border-top')
        
        for div in val:

            title = div.css('.a-text-normal::text')[0].extract()
            price = div.css('.a-price-whole::text')[0].extract()
            try:
                img = div.css('.s-image::attr(src)')[0].extract()

            except: 
                img = 'No Image'

            yield {'title':title,'price':price,'img':img}
