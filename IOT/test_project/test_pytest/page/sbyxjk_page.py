from poium import Page, Element, Elements


class SbyxjkPage(Page):
    sbyx_ele = Element(xpath='//*[@id="LAY-system-side-menu"]/li[2]/a/cite', describe="设备运行菜单")
    sbyxjk_ele = Element(xpath='/html/body/div/div/div[2]/div/ul/li[2]/dl/dd[1]/a/cite', describe="设备运行监控菜单")

    iframe = Element(xpath='//*[@id="LAY_app_body"]/div[2]/iframe', describe="切换frame")

    affiliationId = Element(xpath='//*[@id="sAffiliationID"]', describe="所属工厂下拉框")
    areaId = Element(xpath='//*[@id="sAreaID"]', describe="所属区域下拉框")
    workShopId = Element(xpath='//*[@id="sWorkShopID"]', describe="所属车间下拉框")
    workLineId = Element(xpath='//*[@id="sWorkLineID"]', describe="所属产线下拉框")
    search_button = Element(xpath='//*[@id="form"]/div/div[1]/div/button', describe="检索按钮")
    refresh_button = Element(xpath='//*[@id="table_div"]/div[1]/div/button', describe="刷新按钮")

    eqp_list = Elements(xpath='//*[@id="table_height"]/div', describe="设备信息")
