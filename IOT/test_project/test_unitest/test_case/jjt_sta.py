import unittest
from time import sleep
from test_case.models import myunit, function
from test_case.page_obj.loginPage import login
from test_case.page_obj.sbyxPage import sbyx
from test_case.page_obj.jjtPage import jjt
from test_case.data.jjtData import jjt_data


class jjtTest(myunit.MyTest):
    """集计图测试"""
    def test_jjt(self):
        # 调用统一登录入口方法
        login(self.driver).user_login()
        # 调用点击集计图模块方法
        sbyx(self.driver).jjt_click()
        po = jjt(self.driver)
        # 调用输入开始时间
        po.datafrom_input("2022-08-01")
        # 调用点击空白区域方法
        po.blank_click()
        sleep(1)
        # 调用输入结束时间
        po.datato_input("2022-08-01")
        # 调用点击空白区域方法
        po.blank_click()
        sleep(1)
        # 调用选择设备组ID方法
        po.eqprp_select()
        sleep(1)
        # 调用选择目标设备ID方法
        po.targeteqp_select()
        sleep(1)
        # 通过获取时间方法
        web_data = []
        for i in range(4):
            web_data.append(po.time_text(i))
        # 调用查询数据库时间方法
        database_data = jjt_data()
        # 断言
        self.assertEqual(web_data, database_data)
        # 截图
        function.insert_img(self.driver, "jjt_hint.png")


if __name__ == "__main__":
    unittest.main()
