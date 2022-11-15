import requests


class Login(object):
    """模拟登陆"""
    def __init__(self):
        self.base_url = 'http://iot.sot-soft.com/ths-iot/login'
        self.payload = {'username': 'admin', 'password': 'admin'}

    def cookie(self):
        r = requests.post(self.base_url, data=self.payload, allow_redirects=False)
        cookie = requests.utils.dict_from_cookiejar(r.cookies)
        return cookie['JSESSIONID']

    def session(self):
        s = requests.Session()
        s.post(self.base_url, data=self.payload, allow_redirects=False)
        return s
