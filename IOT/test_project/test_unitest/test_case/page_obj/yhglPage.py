from selenium.webdriver.common.by import By
from test_case.page_obj.base import Page


class yhgl(Page):
    """
    用户管理页面
    """

    adduser_ele = (By.XPATH, '//*[@id="table_container"]/div[2]/div/div[1]/div/button[1]')   # 定位添加按钮元素
    change_ele = (By.XPATH, '//*[@id="dynamic-table"]/tbody/tr[4]/td[8]/div/a[1]/i')    # 定位修改按钮
    delete_ele = (By.XPATH, '//*[@id="dynamic-table"]/tbody/tr[4]/td[8]/div/a[2]/i')    # 定位删除按钮

    # 点击添加按钮
    def adduser_click(self):
        self.find_element(*self.adduser_ele).click()

    # 点击修改按钮
    def change_click(self):
        self.find_element(*self.change_ele).click()

    # 点击删除按钮
    def delete_click(self):
        self.find_element(*self.delete_ele).click()

    userid_ele = (By.XPATH, '//*[@id="userID"]')    # 定位用户ID输入框元素
    username_ele = (By.XPATH, '//*[@id="userName"]')  # 定位用户名输入框元素
    password_ele = (By.XPATH, '//*[@id="password"]')    # 定位密码输入框元素

    # 输入用户ID
    def userid_input(self, userid):
        self.find_element(*self.userid_ele).send_keys(userid)

    # 输入用户名
    def username_input(self, username):
        self.find_element(*self.username_ele).send_keys(username)

    # 清空用户名
    def username_clear(self):
        self.find_element(*self.username_ele).clear()

    # 输入密码
    def password_input(self, password):
        self.find_element(*self.password_ele).send_keys(password)

    save_ele = (By.XPATH, '//*[@id="adbtnConfirm"]/span')   # 定位保存按钮元素
    close_ele = (By.XPATH, '//*[@id="adbtn"]/span')    # 定位关闭按钮元素
    add_confirm_ele = (By.XPATH, '/html/body/div[5]/div[7]/button[2]')  # 定位添加确认按钮元素
    add_cancel_ele = (By.XPATH, '/html/body/div[5]/div[7]/button[1]')   # 定位添加取消按钮元素
    canceled_ele = (By.XPATH, '/html/body/div[5]/div[7]/button[2]')  # 定位已取消确认按钮元素
    delete_confirm_ele = (By.XPATH, '/html/body/div[4]/div[7]/button[2]')   # 定位删除确认按钮元素

    # 点击保存按钮
    def save_click(self):
        self.find_element(*self.save_ele).click()

    # 点击关闭按钮
    def close_click(self):
        self.find_element(*self.close_ele).click()

    # 点击添加确认按钮
    def add_confirm_click(self):
        self.find_element(*self.add_confirm_ele).click()

    # 点击添加取消按钮
    def add_cancel_click(self):
        self.find_element(*self.add_cancel_ele).click()

    # 点击已取消确认按钮
    def canceled_click(self):
        self.find_element(*self.canceled_ele).click()

    # 点击删除确认按钮
    def delete_confirm_click(self):
        self.find_element(*self.delete_confirm_ele).click()













