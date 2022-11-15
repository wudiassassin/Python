from poium import Page, Element, Elements


class JdtjPage(Page):
    sbyx_ele = Element(xpath='//*[@id="LAY-system-side-menu"]/li[2]/a/cite', describe="设备运行菜单")
    rjdtj_ele = Element(xpath='/html/body/div/div/div[2]/div/ul/li[2]/dl/dd[6]/a/cite', describe="日稼动统计菜单")
    yjdtj_ele = Element(xpath='/html/body/div/div/div[2]/div/ul/li[2]/dl/dd[7]/a/cite', describe="月稼动统计菜单")

    iframe = Element(xpath='//*[@id="LAY_app_body"]/div[2]/iframe', describe="切换frame")

    data_from = Element(xpath='//*[@id="targetDate"]', describe="确认日")
    affiliationId = Element(xpath='//*[@id="sAffiliationID"]', describe="所属工厂下拉框")
    areaId = Element(xpath='//*[@id="sAreaID"]', describe="所属区域下拉框")
    workShopId = Element(xpath='//*[@id="sWorkShopID"]', describe="所属车间下拉框")
    workLineId = Element(xpath='//*[@id="sWorkLineID"]', describe="所属产线下拉框")
    eqp_list = Elements(xpath='//*[@id="edit_id"]/option', describe="设备编号")
    search_button = Element(xpath='//*[@id="table_container"]/div[1]/div[1]/div/button', describe="检索按钮")
    csv_button = Element(xpath='//*[@id="csvButton"]', describe="CSV下载按钮")

    prompt_text = Element(xpath='//*[@id="message"]', describe='无数据提示')
