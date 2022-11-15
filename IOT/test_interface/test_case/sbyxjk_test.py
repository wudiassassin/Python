import requests
import unittest
import bs4
import re
from test_case.login import Login
from lxml import etree


class sbyxjkTest(unittest.TestCase):
    """设备运行监控页面"""

    def setUp(self):
        self.url = "http://iot.sot-soft.com/ths-iot/ScrGraph/09/submit"
        self.login = Login().session()
        """cookie heads"""
        # self.heads = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #               "Cookie": "JSESSIONID=" + Login().cookie()}
        """session heads"""
        self.heads = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        """正则表达式：设备背景色"""
        self.pattern = re.compile('.*?background-color:(.*?);color.*?')

    def tearDown(self):
        print(self.status)
        print(self.web_data)

    def test_sbyxjk(self):
        payload = {'affiliationId': 'TBDG', 'areaId': 'EA-2000', 'workShopId': 'SA-HJCJ', 'workLineId': 'SA-HJ001'}
        """使用cookie"""
        # r = requests.post(url=self.url, data=payload, headers=self.heads, allow_redirects=False)
        """使用session"""
        r = self.login.post(url=self.url, data=payload, headers=self.heads, allow_redirects=False)
        self.status = r.status_code
        """使用正则"""
        # self.soup = bs4.BeautifulSoup(r.text, "lxml")
        # self.web_data = []
        # for eqpid in self.soup.select('#table_height > div'):
        #     # print(eqpid.getText())
        #     style = eqpid.get_attribute_list('style')
        #     for color in re.findall(self.pattern, style[0]):
        #         # print(color)
        #         self.web_data.append((eqpid.getText().replace('\n', ''), color))
        """使用xpath"""
        html = etree.HTML(r.text)
        items = html.xpath('//*[@id="table_height"]/div')
        self.web_data = []
        for item in items:
            eqpid = item.xpath('.//span/text()')[0].strip()
            color = item.xpath(
                "substring-before(substring-after(@style, 'background-color:'), ';')")
            self.web_data.append((eqpid, color))
        self.assertEqual(self.status, 200)
        self.assertEqual(self.web_data, [('EM-XL-001', 'lime'),
                                         ('EM-XL-002', 'silver'),
                                         ('EM-XL-003', 'blue')])

    def test_sbyxjk2(self):
        payload = {'affiliationId': 'TBDG3'}
        """使用cookie"""
        # r = requests.post(url=self.url, data=payload, headers=self.heads, allow_redirects=False)
        """使用session"""
        r = self.login.post(url=self.url, data=payload, headers=self.heads, allow_redirects=False)
        self.status = r.status_code
        html = etree.HTML(r.text)
        items = html.xpath('//*[@id="table_height"]/div')
        self.web_data = []
        for item in items:
            eqpid = item.xpath('.//span/text()')[0].strip()
            color = item.xpath(
                "substring-before(substring-after(@style, 'background-color:'), ';')")
            self.web_data.append((eqpid, color))
        self.assertEqual(self.web_data, [])


if __name__ == '__main__':
    unittest.main()
