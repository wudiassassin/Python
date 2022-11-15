from scrapy import Spider, Request
from doubanTop250.items import DaoubanItem


class DoubanSpider(Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/']

    def start_requests(self):
        base_url = 'https://movie.douban.com/top250?start={start}&filter='
        for page in range(self.settings.get('MAX_PAGE')):
            start = page * 25
            yield Request(base_url.format(start=start), callback=self.parse)

    def parse(self, response):
        result = response.xpath('//ol[@class="grid_view"]/li')
        for items in result:
            item = DaoubanItem()
            item['index'] = items.xpath('.//div[@class="item"]//em/text()').extract_first().strip()
            item['image'] = items.xpath('.//div[@class="pic"]//img/@src').extract().strip()
            item['title'] = items.xpath('.//span[1][@class="title"]/text()').extract_first().strip()
            item['director'] = items.xpath('.//div[@class="bd"]/p/text()[1]').extract_first().strip().replace(u'\xa0', u' ')
            item['time'] = items.xpath('.//div[@class="bd"]/p/text()[2]').extract_first().strip()[:4]
            item['score'] = items.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract_first().strip()
            yield item
