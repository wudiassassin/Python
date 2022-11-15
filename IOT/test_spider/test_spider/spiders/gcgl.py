from scrapy import Spider, Request
from scrapy.http import FormRequest, Request
from test_spider.items import GcglItem


def gcgl(response):
    result = response.xpath('//*[@id="dynamic-table"]//tbody/tr')[1:]
    for items in result:
        item = GcglItem()
        item['affiliationID'] = items.xpath('./td[2]/text()').extract_first().strip()
        item['affiliation'] = items.xpath('./td[3]/text()').extract_first().strip()
        item['remarks'] = items.xpath('./td[4]/text()').extract_first().strip()
        item['delFlg'] = items.xpath(
            "substring-after(./td[5]/i/@class,'bigger-130 icon-')").extract_first()
        yield item


class GcglSpider(Spider):
    name = 'gcgl'
    allowed_domains = ['iot.sot-soft.com']
    start_urls = ['http://iot.sot-soft.com/ths-iot/index']
    function_url = 'http://iot.sot-soft.com/ths-iot/ScrMaster/22'
    login_url = 'http://iot.sot-soft.com/ths-iot/login'

    def start_requests(self):
        yield Request(self.login_url, callback=self.login)

    def login(self, response):
        data = {'username': 'admin', 'password': 'admin'}
        yield FormRequest.from_response(response=response, formdata=data, callback=self.parse_login)

    def parse_login(self, response):
        yield from super().start_requests()

    def parse(self, response):
        playload = {
            'affiliationID': '',
            'affiliation': '',
            'delFlg': '',
            'limit': '10',
            'pageNo': '1',
            'sortStatus': '',
            'sortId': '',
            'oldSortId': ''
        }
        yield FormRequest(url=self.function_url, formdata=playload, callback=gcgl)
