from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from test_case.page_obj.base import Page


class jjt(Page):
    """
    集计图页面
    """
    datafrom_ele = (By.XPATH, '//*[@id="datetimeStart"]')   # 定位开始时间元素
    datato_ele = (By.XPATH, '//*[@id="datetimeEnd"]')   # 定位结束时间元素
    eqpgrp_ele = (By.XPATH, '//*[@id="eqpGrpID"]')   # 定位设备组ID下拉框元素
    targeteqp_ele = (By.XPATH, '//*[@id="edit_id"]')    # 定位目标设备下拉框元素
    blank_ele = (By.XPATH, '//*[@id="table_container"]/div[1]/div[1]/span')    # 定位不能操作的元素，模拟空白区域

    # 点击空白区域
    def blank_click(self):
        # ActionChains(self.driver).move_by_offset(400, 700).click().perform()
        # ActionChains(self.driver).release().perform()
        self.find_element(*self.blank_ele).click()

    # 输入开始时间
    def datafrom_input(self, datafrom):
        self.find_element(*self.datafrom_ele).send_keys(datafrom)

    # 输入结束时间
    def datato_input(self, datato):
        self.find_element(*self.datato_ele).send_keys(datato)

    # 选择设备组ID
    def eqprp_select(self):
        Select(self.find_element(*self.eqpgrp_ele)).select_by_value('CF-CM-001')  # 数控火焰切割机

    # 选择目标设备ID
    def targeteqp_select(self):
        Select(self.find_element(*self.targeteqp_ele)).select_by_value('EM-XL-001')  # 数控火焰切割机1

    # 定位时间
    list_time_ele = []
    for i in range(4):
        time_ele = (By.XPATH, '//*[@id="table_div"]/div[2]/table/tbody/tr/td[1]/table/tbody/tr[' + str(i + 2) + ']/td[2]')
        list_time_ele.append(time_ele)

    # 获取时间
    def time_text(self, i):
        return self.find_element(*self.list_time_ele[i]).text
