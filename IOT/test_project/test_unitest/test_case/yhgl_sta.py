import unittest
from time import sleep
from test_case.models import myunit, function
from test_case.page_obj.loginPage import login
from test_case.page_obj.xtszPage import xtsz
from test_case.page_obj.yhglPage import yhgl


class sbyxjkTest(myunit.MyTest):
    """用户管理测试"""

    # 添加用户
    def test_adduser1(self):
        # 调用统一登录入口方法
        login(self.driver).user_login()
        # 调用点击用户管理模块方法
        xtsz(self.driver).yhgl_click()
        po = yhgl(self.driver)
        # 调用点击添加按钮方法
        po.adduser_click()
        sleep(1)
        # 调用输入用户ID方法
        po.userid_input("test")
        # 调用输入用户名方法
        po.username_input("测试")
        # 调用输入密码方法
        po.password_input("123456")
        sleep(1)
        # 调用点击保存按钮方法
        po.save_click()
        sleep(1)
        # 调用点击添加确认按钮方法
        po.add_confirm_click()
        sleep(5)
        # 截图
        function.insert_img(self.driver, "test_adduser1.png")

    # 取消添加用户
    def test_adduser2(self):
        login(self.driver).user_login()
        xtsz(self.driver).yhgl_click()
        po = yhgl(self.driver)
        po.adduser_click()
        sleep(1)
        po.userid_input("test")
        po.username_input("测试")
        po.password_input("123456")
        sleep(1)
        po.save_click()
        sleep(1)
        # 调用点击添加取消按钮方法
        po.add_cancel_click()
        sleep(1)
        # 调用点击取消确认按钮方法
        po.canceled_click()
        sleep(1)
        # 调用点击关闭按钮方法
        po.close_click()
        sleep(5)
        function.insert_img(self.driver, "test_adduser2.png")

    # 修改用户名
    def test_adduser3(self):
        login(self.driver).user_login()
        xtsz(self.driver).yhgl_click()
        po = yhgl(self.driver)
        # 调用点击修改按钮方法
        po.change_click()
        sleep(1)
        # 调用清空用户名方法
        po.username_clear()
        po.username_input("测试123")
        sleep(1)
        po.save_click()
        sleep(1)
        po.add_confirm_click()
        sleep(5)
        function.insert_img(self.driver, "test_adduser3.png")

    # 删除用户
    def test_adduser4(self):
        login(self.driver).user_login()
        xtsz(self.driver).yhgl_click()
        po = yhgl(self.driver)
        # 调用点击删除按钮方法
        po.delete_click()
        sleep(1)
        # 调用点击删除确认按钮方法
        po.delete_confirm_click()
        sleep(5)
        function.insert_img(self.driver, "test_adduser4.png")

        # 断言
        # self.assertEqual(web_data, database_data)


if __name__ == "__main__":
    unittest.main()
