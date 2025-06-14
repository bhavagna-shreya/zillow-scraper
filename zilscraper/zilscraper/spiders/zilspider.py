import scrapy
import json

class ZilspiderSpider(scrapy.Spider):
    name = "zillow_playwright"
    allowed_domains = ["zillow.com"]

    def start_requests(self):
        for page in range(1, 21):  # Pages 1 to 20
            url = f"https://www.zillow.com/phoenix-az/{page}_p/"
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                meta={"playwright": True}
            )

    def parse(self, response):
        script = response.xpath("//script[@id='__NEXT_DATA__']/text()").get()
        if script:
            data = json.loads(script)
            listings = (
                data.get("props", {})
                    .get("pageProps", {})
                    .get("searchPageState", {})
                    .get("cat1", {})
                    .get("searchResults", {})
                    .get("listResults", [])
            )
            for item in listings:
                yield {
                    "address": item.get("address"),
                    "price": item.get("price"),
                    "beds": item.get("beds"),
                    "baths": item.get("baths"),
                    "area": item.get("area"),
                    "statusText": item.get("statusText"),
                    "detailUrl": item.get("detailUrl")
                }
