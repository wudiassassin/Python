from poium import Page, Element


class RjdztPage(Page):
    sbyx_ele = Element(xpath='//*[@id="LAY-system-side-menu"]/li[2]/a/cite', describe="设备运行菜单")
    rjdzt_ele = Element(xpath='/html/body/div/div/div[2]/div/ul/li[2]/dl/dd[2]/a/cite', describe="日稼动状态菜单")

    iframe = Element(xpath='//*[@id="LAY_app_body"]/div[2]/iframe', describe="切换frame")

    date_input = Element(xpath='//*[@id="targetDate"]', describe="设备运行时间")
    hour_from = Element(xpath='//*[@id="hFrom"]', describe="开始小时")
    affiliationId = Element(xpath='//*[@id="sAffiliationID"]', describe="所属工厂下拉框")
    areaId = Element(xpath='//*[@id="sAreaID"]', describe="所属区域下拉框")
    workShopId = Element(xpath='//*[@id="sWorkShopID"]', describe="所属车间下拉框")
    workLineId = Element(xpath='//*[@id="sWorkLineID"]', describe="所属产线下拉框")
    search_button = Element(xpath='//*[@id="btn-search"]', describe="检索按钮")
    refresh_button = Element(xpath='//*[@id="table_div"]/div[1]/div/button', describe="刷新按钮")

    prompt_message = Element(xpath='//*[@id="toast-contain"]/div/div[2]', describe="提示信息")
