"""
日稼动状态页面
"""
import sys
import pytest
from os.path import dirname, abspath
import time
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.rjdzt_page import RjdztPage

base_path = dirname(dirname(abspath(__file__)))


class TestRjdztSearch:

    def test_rjdzt_search1(self, browser, login):
        """
        名称：无目标数据的检索、刷新
        步骤：
        1、进入日稼动状态页面
        2、工厂选择工厂三
        3、点击检索按钮
        4、点击刷新按钮
        检查点：
        * 检查是否有相应提示“目标数据不存在。”
        """
        page = RjdztPage(browser)
        page.sbyx_ele.click()
        page.rjdzt_ele.click()
        page.iframe.switch_to_frame()
        page.affiliationId.select_by_value("TBDG3")
        page.search_button.click()
        assert page.prompt_message.text == "目标数据不存在。"
        page.refresh_button.click()
        assert page.prompt_message.text == "目标数据不存在。"

    @pytest.mark.xfail()
    def test_rjdzt_search2(self, browser, login):
        """
        名称：开始小时大于当前时间检索
        步骤：
        1、进入日稼动状态页面
        2、开始小时选择大于系统当前时间
        3、点击检索按钮
        检查点：
        * 检查是否有相应提示“目标数据不存在。”或“无法指定未来日子。”
        """
        page = RjdztPage(browser)
        page.sbyx_ele.click()
        page.rjdzt_ele.click()
        page.iframe.switch_to_frame()
        now_hour = time.localtime().tm_hour
        page.hour_from.select_by_index(now_hour+1)
        page.search_button.click()
        assert page.prompt_message.text == "目标数据不存在。" or "无法指定未来日子。"
        
        
class TestRjdztCondition:

    def test_rjdzt_condition1(self, browser, login):
        """
        名称：检索不重置查询条件
        步骤：
        1、进入日稼动状态页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        检查点：
        * 检查查询条件是否被重置。
        """
        page = RjdztPage(browser)
        page.sbyx_ele.click()
        page.rjdzt_ele.click()
        page.iframe.switch_to_frame()
        page.affiliationId.select_by_value("TBDG")
        page.areaId.select_by_value("EA-2000")
        page.workShopId.select_by_value("SA-HJCJ")
        page.workLineId.select_by_value("SA-HJ001")
        page.search_button.click()
        assert page.affiliationId.first_selected_option == "特变电工"
        assert page.areaId.first_selected_option == "生产2000"
        assert page.workShopId.first_selected_option == "SA-HJCJ : 焊接车间"
        assert page.workLineId.first_selected_option == "SA-HJ001 : APE"

    def test_rjdzt_condition2(self, browser, login):
        """
        名称：刷新还原上一次的检索条件
        步骤：
        1、进入日稼动状态页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、变更检索条件
        5、点击刷新按钮
        检查点：
        * 检查查询条件是否被还原成上一次的检索条件。
        """
        page = RjdztPage(browser)
        page.sbyx_ele.click()
        page.rjdzt_ele.click()
        page.iframe.switch_to_frame()
        page.affiliationId.select_by_value("TBDG")
        page.areaId.select_by_value("EA-2000")
        page.workShopId.select_by_value("SA-HJCJ")
        page.workLineId.select_by_value("SA-HJ001")
        page.search_button.click()
        page.affiliationId.select_by_value("TBDG3")
        page.refresh_button.click()
        assert page.affiliationId.first_selected_option == "特变电工"
        assert page.areaId.first_selected_option == "生产2000"
        assert page.workShopId.first_selected_option == "SA-HJCJ : 焊接车间"
        assert page.workLineId.first_selected_option == "SA-HJ001 : APE"

    def test_rjdzt_condition3(self, browser, login):
        """
        名称：条件关联测试1
        步骤：
        1、进入日稼动状态页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、变更工厂为工厂三(下面什么都没有)
        检查点：
        * 区域变成全部，车间和产线置灰。
        """
        page = RjdztPage(browser)
        page.sbyx_ele.click()
        page.rjdzt_ele.click()
        page.iframe.switch_to_frame()
        page.affiliationId.select_by_value("TBDG")
        page.areaId.select_by_value("EA-2000")
        page.workShopId.select_by_value("SA-HJCJ")
        page.workLineId.select_by_value("SA-HJ001")
        page.search_button.click()
        page.affiliationId.select_by_value("TBDG3")
        assert page.affiliationId.first_selected_option == "工厂三"
        assert page.areaId.first_selected_option == "全部"
        assert page.workShopId.is_enabled() is False
        assert page.workLineId.is_enabled() is False

    def test_rjdzt_condition4(self, browser, login):
        """
        名称：条件关联测试2
        步骤：
        1、进入日稼动状态页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、变更工厂为全部(空)
        5、变更工厂为特变电工
        检查点：
        * 工厂变更为全部的时候，区域、车间和产线置灰。
        * 工厂变更特变电工的时候，区域变成全部，车间和产线置灰。
        """
        page = RjdztPage(browser)
        page.sbyx_ele.click()
        page.rjdzt_ele.click()
        page.iframe.switch_to_frame()
        page.affiliationId.select_by_value("TBDG")
        page.areaId.select_by_value("EA-2000")
        page.workShopId.select_by_value("SA-HJCJ")
        page.workLineId.select_by_value("SA-HJ001")
        page.search_button.click()
        page.affiliationId.select_by_index(0)
        assert page.affiliationId.first_selected_option == ""
        assert page.areaId.is_enabled() is False
        assert page.workShopId.is_enabled() is False
        assert page.workLineId.is_enabled() is False
        page.affiliationId.select_by_value("TBDG")
        assert page.affiliationId.first_selected_option == "特变电工"
        assert page.areaId.first_selected_option == "全部"
        assert page.workShopId.is_enabled() is False
        assert page.workLineId.is_enabled() is False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_rjdzt.py"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch::test_baidu_search_case"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearchSettings"])
