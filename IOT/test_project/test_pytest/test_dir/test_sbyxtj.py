"""
设备运行统计页面
"""
import sys
import pytest
from os.path import dirname, abspath
import time

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.sbyxtj_page import SbyxtjPage

base_path = dirname(dirname(abspath(__file__)))


class TestSbyxtjCondition:

    def test_sbyxtj_condition1(self, browser, login):
        """
        名称：检索不重置查询条件
        步骤：
        1、进入设备运行统计页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        检查点：
        * 检查查询条件是否被重置。
        """
        page = SbyxtjPage(browser)
        page.sbyx_ele.click()
        page.sbyxtj_ele.click()
        page.iframe.switch_to_frame()
        page.prompt_close.click()
        page.affiliationId.select_by_value("TBDG")
        page.areaId.select_by_value("EA-2000")
        page.workShopId.select_by_value("SA-HJCJ")
        page.workLineId.select_by_value("SA-HJ001")
        page.search_button.click()
        assert page.affiliationId.first_selected_option == "特变电工"
        assert page.areaId.first_selected_option == "生产2000"
        assert page.workShopId.first_selected_option == "SA-HJCJ : 焊接车间"
        assert page.workLineId.first_selected_option == "SA-HJ001 : APE"

    def test_sbyxtj_condition2(self, browser, login):
        """
        名称：刷新还原上一次的检索条件
        步骤：
        1、进入设备运行统计页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、变更检索条件
        5、点击刷新按钮
        检查点：
        * 检查查询条件是否被还原成上一次的检索条件。
        """
        page = SbyxtjPage(browser)
        page.sbyx_ele.click()
        page.sbyxtj_ele.click()
        page.iframe.switch_to_frame()
        page.prompt_close.click()
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

    def test_sbyxtj_condition3(self, browser, login):
        """
        名称：条件关联测试1
        步骤：
        1、进入设备运行统计页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、变更工厂为工厂三(下面什么都没有)
        检查点：
        * 区域变成全部，车间和产线置灰。
        """
        page = SbyxtjPage(browser)
        page.sbyx_ele.click()
        page.sbyxtj_ele.click()
        page.iframe.switch_to_frame()
        page.prompt_close.click()
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

    def test_sbyxtj_condition4(self, browser, login):
        """
        名称：条件关联测试2
        步骤：
        1、进入设备运行统计页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、变更工厂为全部(空)
        5、变更工厂为特变电工
        检查点：
        * 工厂变更为全部的时候，区域、车间和产线置灰。
        * 工厂变更特变电工的时候，区域变成全部，车间和产线置灰。
        """
        page = SbyxtjPage(browser)
        page.sbyx_ele.click()
        page.sbyxtj_ele.click()
        page.iframe.switch_to_frame()
        page.prompt_close.click()
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

    def test_sbyxtj_condition5(self, browser, login):
        """
        名称：按运行状态排序
        步骤：
        1、进入设备运行统计页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、点击运行状态进行排序
        检查点：
        * 检查条件是否被重置。
        """
        page = SbyxtjPage(browser)
        page.sbyx_ele.click()
        page.sbyxtj_ele.click()
        page.iframe.switch_to_frame()
        page.prompt_close.click()
        page.affiliationId.select_by_value("TBDG")
        page.areaId.select_by_value("EA-2000")
        page.workShopId.select_by_value("SA-HJCJ")
        page.workLineId.select_by_value("SA-HJ001")
        page.search_button.click()
        page.status_button.click()
        assert page.affiliationId.first_selected_option == "特变电工"
        assert page.areaId.first_selected_option == "生产2000"
        assert page.workShopId.first_selected_option == "SA-HJCJ : 焊接车间"
        assert page.workLineId.first_selected_option == "SA-HJ001 : APE"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_sbyxtj.py"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch::test_baidu_search_case"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearchSettings"])
