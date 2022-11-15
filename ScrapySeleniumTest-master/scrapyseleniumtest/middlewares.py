# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
import json
import time


class SeleniumMiddleware:
    def __init__(self, timeout=None, chrome_options=webdriver.ChromeOptions()):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser.set_window_size(1400, 700)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self, request, spider):
        """
        用Chrome(无界面模式)抓取页面
        :param request: Request对象
        :param spider: Spider对象
        :return: HtmlResponse
        """
        self.logger.debug('Chrome is Starting')
        page = request.meta.get('page', 1)
        try:
            self.browser.get('https://s.taobao.com/')
            with open(r'D:\Python\IOT\Demo\cookies.txt', 'r', encoding='utf-8') as f:
                listCookies = json.loads(f.read())

            for cookie in listCookies:
                cookie_dict = {
                    'domain': cookie.get('domain'),
                    'name': cookie.get('name'),
                    'value': cookie.get('value'),
                    'path': '/',
                    "expires": '',
                    'sameSite': 'None',
                    'secure': cookie.get('secure')
                }
                self.browser.add_cookie(cookie_dict)
            time.sleep(2)

            self.browser.get(request.url)
            if page > 1:
                input = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="mainsrp-pager"]/div/div/div/div[2]/input')))
                submit = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="mainsrp-pager"]/div/div/div/div[2]/span[3]')))
                input.clear()
                input.send_keys(page)
                submit.click()
            self.wait.until(
                EC.text_to_be_present_in_element((By.XPATH,
                                            '//*[@id="mainsrp-pager"]//li[@class = "item active"]/span'), str(page)))
            self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                            '//*[@id="mainsrp-itemlist"]/div/div/div[1]/div')))
            return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
                                status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'))

