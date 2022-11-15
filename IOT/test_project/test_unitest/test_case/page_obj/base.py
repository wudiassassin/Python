class Page(object):
    """
    页面基础类，用于所有页面的继承
    """

    # iot_url = 'http://192.168.3.167:8080/ths-iot/login'
    # iot_url = 'https://www.baidu.com'
    iot_url = 'http://iot.sot-soft.com/ths-iot/login'

    def __init__(self, selenium_driver, base_url=iot_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def find_element(self, *ele):
        return self.driver.find_element(*ele)

    def find_elements(self, *ele):
        return self.driver.find_elements(*ele)

    def switch_to(self, frame):
        return self.driver.switch_to.frame(frame)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, src):
        return self.driver.execute_script(src)
