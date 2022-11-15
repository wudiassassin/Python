from poium import Page, Element


class SbyxtjPage(Page):
    sbyx_ele = Element(xpath='//*[@id="LAY-system-side-menu"]/li[2]/a/cite', describe="设备运行菜单")
    sbyxtj_ele = Element(xpath='/html/body/div/div/div[2]/div/ul/li[2]/dl/dd[3]/a/cite', describe="设备运行统计菜单")

    iframe = Element(xpath='//*[@id="LAY_app_body"]/div[2]/iframe', describe="切换frame")

    data_from = Element(xpath='//*[@id="startDateTime"]', describe="开始时间")
    data_to = Element(xpath='//*[@id="finishDateTime"]', describe="结束时间")
    affiliationId = Element(xpath='//*[@id="sAffiliationID"]', describe="所属工厂下拉框")
    areaId = Element(xpath='//*[@id="sAreaID"]', describe="所属区域下拉框")
    workShopId = Element(xpath='//*[@id="sWorkShopID"]', describe="所属车间下拉框")
    workLineId = Element(xpath='//*[@id="sWorkLineID"]', describe="所属产线下拉框")
    search_button = Element(xpath='//*[@id="table_container"]/div[1]/div[1]/div/button', describe="检索按钮")
    refresh_button = Element(xpath='//*[@id="table_div"]/div[1]/div/button', describe="刷新按钮")

    prompt_close = Element(xpath='//*[@id="toast-contain"]/div/button', describe='关闭提示')

    status_button = Element(xpath='//*[@id="01"]', describe="运行状态按钮(运行)")
