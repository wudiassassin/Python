"""
趋势页面
"""
import sys
import pytest
from os.path import dirname, abspath
import time

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.qs_page import QsPage

base_path = dirname(dirname(abspath(__file__)))


class TestQsSearch:

    def test_qs_search1(self, browser, login):
        """
        名称：无效工厂下的设备不应该展示
        步骤：
        1、进入趋势页面
        2、直接点击检索按钮(查询所有工厂下的设备)
        检查点：
        * 检查查询结果左边设备列表是否包含无效工厂的设备。
        """
        page = QsPage(browser)
        page.sbyx_ele.click()
        page.qs_ele.click()
        page.iframe.switch_to_frame()
        page.prompt_close.click()
        page.search_button.click()
        page.prompt_close.click()
        for eqp in page.eqp_list:
            assert eqp.text != "TE-ST-001"

    def test_qs_search2(self, browser, login):
        """
        名称：刷新按钮功能测试(刷新按钮不能和检索按钮功能一样)
        步骤：
        1、进入趋势页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、工厂选择全部(空)
        5、点击刷新按钮
        检查点：
        * 检查查询结果左边设备列表是否还是第一次检索的设备。
        """
        page = QsPage(browser)
        page.sbyx_ele.click()
        page.qs_ele.click()
        page.iframe.switch_to_frame()
        page.prompt_close.click()
        page.affiliationId.select_by_value("TBDG")
        page.areaId.select_by_value("EA-2000")
        page.workShopId.select_by_value("SA-HJCJ")
        page.workLineId.select_by_value("SA-HJ001")
        page.search_button.click()
        page.prompt_close.click()
        page.affiliationId.select_by_index(0)
        page.refresh_button.click()
        page.prompt_close.click()
        assert len(page.eqp_list) == 3

    def test_qs_search3(self, browser, login):
        """
        名称：期间和运行状态切换
        步骤：
        1、进入趋势页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、工厂选择全部(空)
        5、切换设备运行状态
        检查点：
        * 检查查询结果左边设备列表是否还是第一次检索的设备。
        """
        page = QsPage(browser)
        page.sbyx_ele.click()
        page.qs_ele.click()
        page.iframe.switch_to_frame()
        page.prompt_close.click()
        page.affiliationId.select_by_value("TBDG")
        page.areaId.select_by_value("EA-2000")
        page.workShopId.select_by_value("SA-HJCJ")
        page.workLineId.select_by_value("SA-HJ001")
        page.search_button.click()
        page.prompt_close.click()
        page.affiliationId.select_by_index(0)
        page.status_select.select_by_value("02")
        page.prompt_close.click()
        assert len(page.eqp_list) == 3


class TestQsCondition:

    def test_qs_condition1(self, browser, login):
        """
        名称：检索不重置查询条件
        步骤：
        1、进入趋势页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        检查点：
        * 检查查询条件是否被重置。
        """
        page = QsPage(browser)
        page.sbyx_ele.click()
        page.qs_ele.click()
        page.iframe.switch_to_frame()
        page.prompt_close.click()
        page.affiliationId.select_by_value("TBDG")
        page.areaId.select_by_value("EA-2000")
        page.workShopId.select_by_value("SA-HJCJ")
        page.workLineId.select_by_value("SA-HJ001")
        page.search_button.click()
        page.prompt_close.click()
        assert page.affiliationId.first_selected_option == "特变电工"
        assert page.areaId.first_selected_option == "生产2000"
        assert page.workShopId.first_selected_option == "SA-HJCJ : 焊接车间"
        assert page.workLineId.first_selected_option == "SA-HJ001 : APE"

    def test_qs_condition2(self, browser, login):
        """
        名称：刷新还原上一次的检索条件
        步骤：
        1、进入趋势页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、变更检索条件
        5、点击刷新按钮
        检查点：
        * 检查查询条件是否被还原成上一次的检索条件。
        """
        page = QsPage(browser)
        page.sbyx_ele.click()
        page.qs_ele.click()
        page.iframe.switch_to_frame()
        page.prompt_close.click()
        page.affiliationId.select_by_value("TBDG")
        page.areaId.select_by_value("EA-2000")
        page.workShopId.select_by_value("SA-HJCJ")
        page.workLineId.select_by_value("SA-HJ001")
        page.search_button.click()
        page.prompt_close.click()
        page.affiliationId.select_by_value("TBDG3")
        page.refresh_button.click()
        page.prompt_close.click()
        assert page.affiliationId.first_selected_option == "特变电工"
        assert page.areaId.first_selected_option == "生产2000"
        assert page.workShopId.first_selected_option == "SA-HJCJ : 焊接车间"
        assert page.workLineId.first_selected_option == "SA-HJ001 : APE"

    def test_qs_condition3(self, browser, login):
        """
        名称：条件关联测试1
        步骤：
        1、进入趋势页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、变更工厂为工厂三(下面什么都没有)
        检查点：
        * 区域变成全部，车间和产线置灰。
        """
        page = QsPage(browser)
        page.sbyx_ele.click()
        page.qs_ele.click()
        page.iframe.switch_to_frame()
        page.prompt_close.click()
        page.affiliationId.select_by_value("TBDG")
        page.areaId.select_by_value("EA-2000")
        page.workShopId.select_by_value("SA-HJCJ")
        page.workLineId.select_by_value("SA-HJ001")
        page.search_button.click()
        page.prompt_close.click()
        page.affiliationId.select_by_value("TBDG3")
        assert page.affiliationId.first_selected_option == "工厂三"
        assert page.areaId.first_selected_option == "全部"
        assert page.workShopId.is_enabled() is False
        assert page.workLineId.is_enabled() is False

    def test_qs_condition4(self, browser, login):
        """
        名称：条件关联测试2
        步骤：
        1、进入趋势页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、变更工厂为全部(空)
        5、变更工厂为特变电工
        检查点：
        * 工厂变更为全部的时候，区域、车间和产线置灰。
        * 工厂变更特变电工的时候，区域变成全部，车间和产线置灰。
        """
        page = QsPage(browser)
        page.sbyx_ele.click()
        page.qs_ele.click()
        page.iframe.switch_to_frame()
        page.prompt_close.click()
        page.affiliationId.select_by_value("TBDG")
        page.areaId.select_by_value("EA-2000")
        page.workShopId.select_by_value("SA-HJCJ")
        page.workLineId.select_by_value("SA-HJ001")
        page.search_button.click()
        page.prompt_close.click()
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
    pytest.main(["-v", "-s", "test_qs.py"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch::test_baidu_search_case"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearchSettings"])
