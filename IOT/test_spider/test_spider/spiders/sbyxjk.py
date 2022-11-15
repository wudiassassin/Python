from scrapy import Spider, Request
from scrapy.http import FormRequest, Request
from test_spider.items import SbyxjkItem


def sbyxjk(response):
    result = response.xpath('//*[@id="table_height"]/div')
    for items in result:
        item = SbyxjkItem()
        item['eqpid'] = items.xpath('.//span/text()').extract_first().strip()
        item['color'] = items.xpath("substring-before(substring-after(@style, 'background-color:'), ';')").extract_first()
        yield item


class SbyxjkSpider(Spider):
    name = 'sbyxjk'
    allowed_domains = ['iot.sot-soft.com']
    start_urls = ['http://iot.sot-soft.com/ths-iot/index']
    function_url = 'http://iot.sot-soft.com/ths-iot/ScrGraph/09/submit'
    login_url = 'http://iot.sot-soft.com/ths-iot/login'

    def start_requests(self):
        yield Request(self.login_url, callback=self.login)

    def login(self, response):
        data = {'username': 'admin', 'password': 'admin'}
        yield FormRequest.from_response(response=response, formdata=data, callback=self.parse_login)

    def parse_login(self, response):
        yield from super().start_requests()

    def parse(self, response):
        playload = {'affiliationId': ''}
        yield FormRequest(url=self.function_url, formdata=playload, callback=sbyxjk)



