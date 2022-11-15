import sys
from time import sleep
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.login_page import LoginPage
import random


class TestLogin:
    """登录功能"""

    """用户名、密码为空登录"""
    def test_login1(self, browser, login_url):
        page = LoginPage(browser)
        page.open(login_url)
        page.usrname_input = ""
        page.password_input = ""
        page.login_button.click()
        sleep(2)
        assert page.error_text.text == "请输入有效的用户名或密码。"

    """用户名正确、密码为空"""
    def test_login2(self, browser, login_url):
        page = LoginPage(browser)
        page.open(login_url)
        page.usrname_input = "admin"
        page.password_input = ""
        page.login_button.click()
        sleep(2)
        assert page.error_text.text == "请输入有效的用户名或密码。"

    """用户名为空、密码正确"""
    def test_login3(self, browser, login_url):
        page = LoginPage(browser)
        page.open(login_url)
        page.usrname_input = ""
        page.password_input = "admin"
        page.login_button.click()
        sleep(2)
        assert page.error_text.text == "请输入有效的用户名或密码。"

    """用户名与密码不匹配"""
    def test_login4(self, browser, login_url):
        character = random.choice('9876543210')
        page = LoginPage(browser)
        page.open(login_url)
        page.usrname_input = "admin" + str(character)
        page.password_input = "admin"
        page.login_button.click()
        sleep(2)
        assert page.error_text.text == "请输入有效的用户名或密码。"

    """用户名、密码正确"""
    def test_login5(self, browser, login_url):
        page = LoginPage(browser)
        page.open(login_url)
        page.usrname_input = "admin"
        page.password_input = "admin"
        page.login_button.click()
        sleep(2)
        assert browser.title == "Industrial Internet of Things(IIoT)"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_login.py"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch::test_baidu_search_case"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearchSettings"])
