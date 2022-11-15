from selenium.webdriver.common.by import By
from test_case.page_obj.base import Page
from time import sleep


class xtsz(Page):
    """
    系统设置页面
    """

    xtsz_ele = (By.XPATH, '//*[@id="LAY-system-side-menu"]/li[5]/a/cite')   # 定位系统设置元素
    yhgl_ele = (By.XPATH, '/html/body/div/div/div[2]/div/ul/li[5]/dl/dd[1]/a/cite')   # 定位用户管理元素
    # 定位日稼动状态元素
    # 定位运行时间元素
    # 定位趋势元素
    # 定位每日汇总元素
    # 定位每月汇总元素

    # 点击用户管理模块
    def yhgl_click(self):
        # 点击系统设置
        self.find_element(*self.xtsz_ele).click()
        # 点击用户管理
        self.find_element(*self.yhgl_ele).click()
        # 切换frame
        self.switch_to(1)
        sleep(1)

