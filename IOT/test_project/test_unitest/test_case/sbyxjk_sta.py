import unittest
from time import sleep
from test_case.models import myunit, function
from test_case.page_obj.loginPage import login
from test_case.page_obj.sbyxPage import sbyx
from test_case.page_obj.sbyxjkPage import sbyxjk
from test_case.data.sbyxjkData import sbyxjkdata


class sbyxjkTest(myunit.MyTest):
    """设备运行监控测试"""
    eqpgrpid = input("输入设备组ID：")

    def test_sbyxjk(self):
        # 调用统一登录入口方法
        login(self.driver).user_login()
        # 调用点击设备运行监控模块方法
        sbyx(self.driver).sbyxjk_click()
        po = sbyxjk(self.driver)
        # 调用选择设备组ID方法
        po.eqprp_select(self.eqpgrpid)
        # 调用点击检索按钮方法
        po.search_click()
        sleep(1)
        # 通过调用获取设备ID和背景色方法，组成列表
        web_data = []
        for i in range(sbyxjkdata().eqp_sta_data(self.eqpgrpid)[1]):
            web_data.append((po.eqpid_text(i), po.eqpcolor_text(i)))
        print(web_data)
        # 调用查询数据库设备ID和状态方法
        database_data = sbyxjkdata().eqp_sta_data(self.eqpgrpid)[0]
        print(database_data)
        # 断言
        self.assertEqual(web_data, database_data)
        # 截图
        function.insert_img(self.driver, "sbyxjk_hint.png")


if __name__ == "__main__":
    unittest.main()
