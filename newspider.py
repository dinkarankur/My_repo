'''
credited_to : 
[@Author]'Ahmed Rafik Djerah in @'Medium.com'

title : spider fundamentals
writen by nyk
'''
import scrapy

class newspider(scrapy.Spider):
    name = 'newspider'
    allowed_domain = ['www.gsmarena.com']
    start_urls = ['https://www.gsmarena.com/acer-phones-59.php']
    
    def parse(self, response):
        for link in response.xpath('//div[@class="makers"]/ul/li/a/@href').extract():
            yield response.follow(link, callback=self.parse_details)
        next_page = response.xpath('//div[@class="nav-pages"]/a/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_details(self, response):
        memory = response.xpath('//td[@data-spec="internalmemory"]/text()').extract_first()
        camera = response.xpath('//td[@data-spec="cam1modules"]/text()').extract_first()
        battery = response.xpath('//td[@data-spec="batdescription1"]/text()').extract_first()
        price = response.xpath('//td[@data-spec="price"]/text()').extract_first()
        yield {
            'Memory' : memory,
            'Camera' : camera,
            'Battery' : battery,
            'Price' : price
            }

