from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from test_case.page_obj.base import Page
import re


class sbyxjk(Page):
    """
    设备运行监控页面
    """

    eqpgrp_ele = (By.XPATH, '//*[@id="edit_id"]')   # 定位设备组ID下拉框元素

    # 选择设备组ID
    def eqprp_select(self, eqpgrpid):
        Select(self.find_element(*self.eqpgrp_ele)).select_by_value(eqpgrpid)

    search_ele = (By.XPATH, '//*[@id="form"]/div/div[1]/div/button/span')   # 定位检索按钮元素

    # 点击检索按钮
    def search_click(self):
        self.find_element(*self.search_ele).click()

    # 定位所有设备ID及背景色元素
    eqpid_ele = (By.XPATH, '//*[@id="table_height"]/div')

    eqpcolor_ele = (By.XPATH, '//*[@id="table_height"]/div')

    # 获取设备ID
    def eqpid_text(self, i):
        return self.find_elements(*self.eqpid_ele)[i].text

    # 获取背景色
    def eqpcolor_text(self, i):
        return re.findall('background-color:(.*?);',
                          self.find_elements(*self.eqpcolor_ele)[i].get_attribute('style'))[0]
