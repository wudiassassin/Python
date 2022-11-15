from selenium.webdriver.common.by import By
from test_case.page_obj.base import Page
from time import sleep


class login(Page):
    """
    用户登录页面
    """

    url = ''

    login_username_ele = (By.ID, "user_id")
    login_password_ele = (By.ID, "LAY-user-login-password")
    login_button_ele = (By.ID, "loginsub")

    # 登录用户名
    def username_input(self, username):
        self.find_element(*self.login_username_ele).send_keys(username)

    # 登录密码
    def password_input(self, password):
        self.find_element(*self.login_password_ele).send_keys(password)

    # 登录按钮
    def login_click(self):
        self.find_element(*self.login_button_ele).submit()

    # 定义统一登录入口
    def user_login(self, username="admin", password="admin"):
        """ 获取的用户名密码登录"""
        self.open()
        self.username_input(username)
        self.password_input(password)
        self.login_click()
        sleep(1)

    user_error_hint_ele = (By.XPATH, '//*[@id="login_form"]/div/div[2]/div[1]/span')
    pawd_error_hint_ele = (By.XPATH, '//*[@id="login_form"]/div/div[2]/div[1]/span')
    user_login_success_ele = (By.XPATH, '//*[@id="LAY_app"]/div/div[2]/div/div/span')

    # 用户名错误提示
    def user_error_text(self):
        return self.find_element(*self.user_error_hint_ele).text

    # 密码错误提示
    def pawd_error_text(self):
        return self.find_element(*self.pawd_error_hint_ele).text

    # 登录成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_ele).text
