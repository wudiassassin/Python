"""
设备运行监控页面
"""
import sys
import pytest
from os.path import dirname, abspath
import re
from time import sleep
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.sbyxjk_page import SbyxjkPage

base_path = dirname(dirname(abspath(__file__)))
import json


def get_data(file_path):
    """
    读取参数化文件
    :param file_path:
    :return:
    """
    data = []
    with(open(file_path, "r")) as f:
        dict_data = json.loads(f.read())
        for i in dict_data:
            data.append(tuple(i.values()))
    return data


class TestSbyxjkSearch:

    @pytest.mark.parametrize(
        "affiliationId, areaId, workShopId, workLineId",
        get_data(base_path + "/test_dir/data/sbyxjk_file.json"), ids=["case1", "case2", "case3"]
    )
    def test_sbyxjk_search1(self, affiliationId, areaId, workShopId, workLineId, browser, login, sbyxjk_database):
        """
        名称：设备运行监控查询
        步骤：
        1、进入设备运行监控页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        检查点：
        * 检查查询结果是否与数据库结果一致。
        """
        page = SbyxjkPage(browser)
        page.sbyx_ele.click()
        page.sbyxjk_ele.click()
        page.iframe.switch_to_frame()
        page.affiliationId.select_by_value(affiliationId)
        page.areaId.select_by_value(areaId)
        page.workShopId.select_by_value(workShopId)
        page.workLineId.select_by_value(workLineId)
        page.search_button.click()
        web_data = []
        for item in page.eqp_list:
            eqpid = item.text
            color = re.findall('background-color: (.*?);', item.get_attribute('style'))[0]
            web_data.append((eqpid, color))
        # print(web_data)
        # print(sbyxjk_database)
        assert web_data == sbyxjk_database

    def test_sbyxjk_search2(self, browser, login):
        """
        名称：无效工厂下的设备不应该展示
        步骤：
        1、进入设备运行监控页面
        2、直接点击检索按钮(查询所有工厂下的设备)
        检查点：
        * 检查查询结果是否包含无效工厂的设备。
        """
        page = SbyxjkPage(browser)
        page.sbyx_ele.click()
        page.sbyxjk_ele.click()
        page.iframe.switch_to_frame()
        page.search_button.click()
        for eqp in page.eqp_list:
            assert eqp.text != "TE-ST-001"

    def test_sbyxjk_search3(self, browser, test_login):
        """
        名称：默认显示登陆用户所属车间的设备
        步骤：
        1、调用test_login,用test用户登录(下面有设备EM-XL-001,2,3)
        2、进入设备运行监控页面
        检查点：
        * 检查是否默认显示登陆用户所属车间的设备。
        """
        page = SbyxjkPage(browser)
        page.sbyx_ele.click()
        page.sbyxjk_ele.click()
        page.iframe.switch_to_frame()
        web_data = []
        for item in page.eqp_list:
            eqpid = item.text
            web_data.append(eqpid)
        assert web_data == ['EM-XL-001', 'EM-XL-002', 'EM-XL-003']


class TestSbyxjkCondition:

    def test_sbyxjk_condition1(self, browser, login):
        """
        名称：检索不重置查询条件
        步骤：
        1、进入设备运行监控页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        检查点：
        * 检查查询条件是否被重置。
        """
        page = SbyxjkPage(browser)
        page.sbyx_ele.click()
        page.sbyxjk_ele.click()
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

    def test_sbyxjk_condition2(self, browser, login):
        """
        名称：刷新还原上一次的检索条件
        步骤：
        1、进入设备运行监控页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、变更检索条件
        5、点击刷新按钮
        检查点：
        * 检查查询条件是否被还原成上一次的检索条件。
        """
        page = SbyxjkPage(browser)
        page.sbyx_ele.click()
        page.sbyxjk_ele.click()
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

    def test_sbyxjk_condition3(self, browser, login):
        """
        名称：条件关联测试1
        步骤：
        1、进入设备运行监控页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、变更工厂为工厂三(下面什么都没有)
        检查点：
        * 区域变成全部，车间和产线置灰。
        """
        page = SbyxjkPage(browser)
        page.sbyx_ele.click()
        page.sbyxjk_ele.click()
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

    def test_sbyxjk_condition4(self, browser, login):
        """
        名称：条件关联测试2
        步骤：
        1、进入设备运行监控页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、变更工厂为全部(空)
        5、变更工厂为特变电工
        检查点：
        * 工厂变更为全部的时候，区域、车间和产线置灰。
        * 工厂变更特变电工的时候，区域变成全部，车间和产线置灰。
        """
        page = SbyxjkPage(browser)
        page.sbyx_ele.click()
        page.sbyxjk_ele.click()
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


class TestSbyxjkColor:

    def test_sbyxjk_color(self, browser, login):
        """
        名称：自动刷新设备编号字体颜色
        步骤：
        1、进入设备运行监控页面
        2、选择工厂、区域、车间和产线
        3、点击检索按钮
        4、等待40秒自动刷新(自动刷新时间默认30秒)
        检查点：
        * 检查运行中(绿色)设备的设备ID背景色是否变成白色。
        """
        page = SbyxjkPage(browser)
        page.sbyx_ele.click()
        page.sbyxjk_ele.click()
        page.iframe.switch_to_frame()
        page.affiliationId.select_by_value("TBDG")
        page.areaId.select_by_value("EA-2000")
        page.workShopId.select_by_value("SA-HJCJ")
        page.workLineId.select_by_value("SA-HJ001")
        page.search_button.click()
        for k in range(0, 40, 5):
            print(40 - k)
            sleep(5)
        for item in page.eqp_list:
            color = re.findall('background-color: (.*?);', item.get_attribute('style'))[0]
            id_color = re.findall('.*?; color: (.*?);', item.get_attribute('style'))
            if color == "lime":
                if id_color:
                    assert id_color[0] == "black"

                else:
                    id_color = "white"
                    assert id_color == "black"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_sbyxjk.py"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch::test_baidu_search_case"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearch"])
    # pytest.main(["-v", "-s", "test_baidu.py::TestSearchSettings"])
