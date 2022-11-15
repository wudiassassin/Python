"""
日稼动统计页面
"""
import sys
import pytest
from os.path import dirname, abspath
import time

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.jdtj_page import JdtjPage

base_path = dirname(dirname(abspath(__file__)))


class TestRjdtjCondition:

    def test_rjdtj_condition1(self, browser, login):
        """
        名称：检索不重置查询条件
        步骤：
        1、进入日稼动统计页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        检查点：
        * 检查查询条件是否被重置。
        """
        page = JdtjPage(browser)
        page.sbyx_ele.click()
        page.rjdtj_ele.click()
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

    def test_rjdtj_condition2(self, browser, login):
        """
        名称：条件关联测试1
        步骤：
        1、进入日稼动统计页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、变更工厂为工厂三(下面什么都没有)
        检查点：
        * 区域变成全部，车间和产线置灰。
        """
        page = JdtjPage(browser)
        page.sbyx_ele.click()
        page.rjdtj_ele.click()
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

    def test_rjdtj_condition3(self, browser, login):
        """
        名称：条件关联测试2
        步骤：
        1、进入日稼动统计页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、变更工厂为全部(空)
        5、变更工厂为特变电工
        检查点：
        * 工厂变更为全部的时候，区域、车间和产线置灰。
        * 工厂变更特变电工的时候，区域变成全部，车间和产线置灰。
        """
        page = JdtjPage(browser)
        page.sbyx_ele.click()
        page.rjdtj_ele.click()
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


class TestRjdtjCsvButton:

    def test_rjdtj_csvbutton(self, browser, login):
        """
        名称：检索结果无数据
        步骤：
        1、进入日稼动统计页面
        2、直接点击检索按钮(查询结果无数据)
        检查点：
        * CSV按钮不可用
        """
        page = JdtjPage(browser)
        page.sbyx_ele.click()
        page.rjdtj_ele.click()
        page.iframe.switch_to_frame()
        page.search_button.click()
        assert page.prompt_text.text == "目标数据不存在。"
        assert page.csv_button.is_enabled() is False


class TestYjdtjCondition:

    def test_yjdtj_condition1(self, browser, login):
        """
        名称：检索不重置查询条件
        步骤：
        1、进入月稼动统计页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        检查点：
        * 检查查询条件是否被重置。
        """
        page = JdtjPage(browser)
        page.sbyx_ele.click()
        page.yjdtj_ele.click()
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

    @pytest.mark.xfail()
    def test_yjdtj_condition2(self, browser, login):
        """
        名称：条件关联测试1
        步骤：
        1、进入月稼动统计页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、变更工厂为工厂三(下面什么都没有)
        检查点：
        * 区域变成全部，车间和产线置灰。
        """
        page = JdtjPage(browser)
        page.sbyx_ele.click()
        page.yjdtj_ele.click()
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

    def test_yjdtj_condition3(self, browser, login):
        """
        名称：条件关联测试2
        步骤：
        1、进入月稼动统计页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、变更工厂为全部(空)
        5、变更工厂为特变电工
        检查点：
        * 工厂变更为全部的时候，区域、车间和产线置灰。
        * 工厂变更特变电工的时候，区域变成全部，车间和产线置灰。
        """
        page = JdtjPage(browser)
        page.sbyx_ele.click()
        page.yjdtj_ele.click()
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

    def test_yjdtj_condition4(self, browser, login):
        """
        名称：无效工厂下的设备不应该显示
        步骤：
        1、进入月稼动统计页面
        2、工厂选择全部(空)
        检查点：
        * 检查设备编号下拉列表中是否有无效工厂的设备
        """
        page = JdtjPage(browser)
        page.sbyx_ele.click()
        page.yjdtj_ele.click()
        page.iframe.switch_to_frame()
        for eqp in page.eqp_list:
            assert eqp.text != "TE-ST-001 : 测试001"

    def test_yjdtj_condition5(self, browser, login):
        """
        名称：工厂下拉框选项
        步骤：
        1、进入月稼动统计页面
        检查点：
        * 检查工厂下拉框选项是否包含工厂三
        """
        page = JdtjPage(browser)
        page.sbyx_ele.click()
        page.yjdtj_ele.click()
        page.iframe.switch_to_frame()
        page.affiliationId.select_by_index(0)
        assert page.affiliationId.first_selected_option == ""
        page.affiliationId.select_by_index(1)
        assert page.affiliationId.first_selected_option == "特变电工"
        page.affiliationId.select_by_index(2)
        assert page.affiliationId.first_selected_option == "工厂三"


class TestYjdtjCsvButton:

    def test_yjdtj_csvbutton(self, browser, login):
        """
        名称：检索结果无数据
        步骤：
        1、进入月稼动统计页面
        2、直接点击检索按钮(查询结果无数据)
        检查点：
        * CSV按钮不可用
        """
        page = JdtjPage(browser)
        page.sbyx_ele.click()
        page.yjdtj_ele.click()
        page.iframe.switch_to_frame()
        page.search_button.click()
        assert page.prompt_text.text == "目标数据不存在。"
        assert page.csv_button.is_enabled() is False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_rjdtj.py::TestJdtjConditionSort"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch::test_baidu_search_case"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearchSettings"])
