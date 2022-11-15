import json

import requests
import unittest
import bs4
import re
import time
from test_case.login import Login


class gcglTest(unittest.TestCase):
    """工厂管理页面"""

    def setUp(self):
        self.add_url = "http://iot.sot-soft.com/ths-iot/ScrMaster/22/factorySave"
        self.del_url = "http://iot.sot-soft.com/ths-iot/ScrMaster/22/del"
        self.add_heads = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        self.del_heads = {'Content-Type': 'application/json'}
        self.login = Login().session()

    def tearDown(self):
        print(self.status)
        print(self.json)

    """正确添加工厂"""
    def test_gcgl_add1(self):
        payload = {'affiliationID': 'TBDG7', 'affiliation': '工厂七', 'type': '01', 'remarks': '公司', 'delFlg': '0',
                   'updateDate': ''}
        r = self.login.post(url=self.add_url, data=payload, headers=self.add_heads, allow_redirects=False)
        self.status = r.status_code
        self.json = r.json()
        self.assertEqual(self.status, 200)
        self.assertEqual(self.json['affiliationID'], 'TBDG7')
        self.assertEqual(self.json['affiliation'], '工厂七')

    """正确修改工厂"""
    def test_gcgl_change1(self):
        payload = {'affiliationID': 'TBDG7', 'affiliation': '工厂七7', 'type': '01', 'remarks': '公司', 'delFlg': '0',
                   'updateDate': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}
        r = self.login.post(url=self.add_url, data=payload, headers=self.add_heads, allow_redirects=False)
        self.status = r.status_code
        self.json = r.json()
        self.assertEqual(self.status, 200)
        self.assertEqual(self.json['affiliationID'], 'TBDG7')
        self.assertEqual(self.json['affiliation'], '工厂七7')

    """修改不存在的工厂(工厂ID)"""
    def test_gcgl_change2(self):
        payload = {'affiliationID': 'TBDG10', 'affiliation': '工厂十', 'type': '01', 'remarks': '公司',
                   'delFlg': '0',
                   'updateDate': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}
        r = self.login.post(url=self.add_url, data=payload, headers=self.add_heads, allow_redirects=False)
        self.status = r.status_code
        self.json = r.json()
        self.assertEqual(self.status, 500)

    """正确删除工厂"""
    def test_gcgl_delete1(self):
        payload = [{"affiliationID": "TBDG7"}]
        r = self.login.post(url=self.del_url, data=json.dumps(payload), headers=self.del_heads, allow_redirects=False)
        self.status = r.status_code
        self.json = r.json()
        self.assertEqual(self.status, 200)
        self.assertEqual(self.json['success'], 'true')

    """删除不存在的工厂(工厂ID)"""
    def test_gcgl_delete2(self):
        payload = [{"affiliationID": "TBDG7"}]
        r = self.login.post(url=self.del_url, data=json.dumps(payload), headers=self.del_heads, allow_redirects=False)
        self.status = r.status_code
        self.json = r.json()
        self.assertEqual(self.json['message'], '4002')


if __name__ == '__main__':
    unittest.main()
