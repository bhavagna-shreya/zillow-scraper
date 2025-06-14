import scrapy

class ZilspiderSpider(scrapy.Spider):

    name = "zilspider"
    allowed_domains = ["zillow.com"]
    url = "https://www.zillow.com/phoenix-az/"

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
