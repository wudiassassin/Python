from poium import Page, Element, Elements


class QsPage(Page):
    sbyx_ele = Element(xpath='//*[@id="LAY-system-side-menu"]/li[2]/a/cite', describe="设备运行菜单")
    qs_ele = Element(xpath='/html/body/div/div/div[2]/div/ul/li[2]/dl/dd[4]/a/cite', describe="趋势菜单")

    iframe = Element(xpath='//*[@id="LAY_app_body"]/div[2]/iframe', describe="切换frame")

    data_from = Element(xpath='//*[@id="datetimeStart"]', describe="开始时间")
    data_to = Element(xpath='//*[@id="datetimeEnd"]', describe="结束时间")
    status_select = Element(xpath='//*[@id="status"]', describe="运行状态")
    affiliationId = Element(xpath='//*[@id="sAffiliationID"]', describe="所属工厂下拉框")
    areaId = Element(xpath='//*[@id="sAreaID"]', describe="所属区域下拉框")
    workShopId = Element(xpath='//*[@id="sWorkShopID"]', describe="所属车间下拉框")
    workLineId = Element(xpath='//*[@id="sWorkLineID"]', describe="所属产线下拉框")
    eqp_list = Elements(xpath='//*[@id="eqpIDCheck"]', describe="设备列表")
    search_button = Element(xpath='//*[@id="table_container"]/div[1]/div[1]/div/button', describe="检索按钮")
    refresh_button = Element(xpath='//*[@id="table_div"]/div[1]/div/button', describe="刷新按钮")

    prompt_close = Element(xpath='//*[@id="toast-contain"]/div/button', describe='关闭提示')
