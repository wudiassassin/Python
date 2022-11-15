import random
import unittest
import base64
from time import sleep
from test_case.models import myunit, function
from test_case.page_obj.loginPage import login


class loginTest(myunit.MyTest):
    """登录测试"""

    # 测试用户登录
    def user_login_verify(self, username="", password=""):
        login(self.driver).user_login(username, password)

    def test_login1(self):
        """用户名、密码为空登录"""
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.user_error_text(), "请输入有效的用户名或密码。")
        # self.assertEqual(po.pawd_error_hint(), "密码不能为空")
        function.insert_img(self.driver, "user_pawd_empty.png")

    def test_login2(self):
        """用户名正确,密码为空登录"""
        self.user_login_verify(username="admin")
        po = login(self.driver)
        self.assertEqual(po.pawd_error_text(), "请输入有效的用户名或密码。")
        function.insert_img(self.driver, "pawd_empty.png")

    def test_login3(self):
        """用户名为空,密码正确"""
        self.user_login_verify(password="admin")
        po = login(self.driver)
        self.assertEqual(po.user_error_text(), "请输入有效的用户名或密码。")
        function.insert_img(self.driver, "user_empty.png")

    def test_login4(self):
        """用户名与密码不匹配"""
        character = random.choice('9876543210')
        username = "admin" + character
        self.user_login_verify(username=username, password="admin")
        po = login(self.driver)
        self.assertEqual(po.pawd_error_text(), "请输入有效的用户名或密码。")
        function.insert_img(self.driver, "user_pawd_error.png")

    def test_login5(self):
        """用户名、密码正确"""
        passFile = open('./test_case/models/password.txt')
        password = base64.b64decode(passFile.read().encode("utf-8")).decode("utf-8")
        self.user_login_verify(username="admin", password=password)
        sleep(2)
        po = login(self.driver)
        self.assertEqual(po.user_login_success(), '工业IOT')
        function.insert_img(self.driver, "user_pawd_ture.png")


if __name__ == "__main__":
    unittest.main()
