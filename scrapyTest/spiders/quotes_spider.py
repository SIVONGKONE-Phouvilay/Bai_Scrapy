import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://bongdaplus.vn/diem-tin/tin-gio-chot-25-9-van-gaal-canh-bao-de-jong-ve-nguy-co-mat-suat-o-dt-ha-lan-3777342209.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.xpath("//h1[@class='artitle']/text()").get()
        content = response.xpath("//div[@id='postContent']/p[1]").extract_first().strip()
        day = response.xpath("//div[@class='dtepub']/text()").get()
        print('tieu de', title)
        print('content', content)
        print('day', day)


     