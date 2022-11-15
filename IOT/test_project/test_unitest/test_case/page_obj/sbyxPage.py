from time import sleep
from selenium.webdriver.common.by import By
from test_case.page_obj.base import Page


class sbyx(Page):
    """
    设备运行页面
    """

    sbyx_ele = (By.XPATH, '//*[@id="LAY-system-side-menu"]/li[2]/a/cite')   # 定位设备运行元素
    sbyxjk_ele = (By.XPATH, '/html/body/div/div/div[2]/div/ul/li[2]/dl/dd[1]/a/cite')  # 定位设备运行监控元素
    # 定位日稼动状态
    # 定位运行时间
    # 定位趋势
    jjt_ele = (By.XPATH, '/html/body/div/div/div[2]/div/ul/li[2]/dl/dd[5]/a/cite')    # 定位集计图元素
    # 定位每日汇总
    # 定位每月汇总

    # 点击设备运行监控模块
    def sbyxjk_click(self):
        # 点击设备运行
        self.find_element(*self.sbyx_ele).click()
        # 点击设备运行监控
        self.find_element(*self.sbyxjk_ele).click()
        # 切换frame
        self.switch_to(1)
        sleep(1)

    # 点击集计图模块
    def jjt_click(self):
        # 点击设备运行
        self.find_element(*self.sbyx_ele).click()
        # 点击集计图
        self.find_element(*self.jjt_ele).click()
        # 切换frame
        self.switch_to(1)
        sleep(1)
