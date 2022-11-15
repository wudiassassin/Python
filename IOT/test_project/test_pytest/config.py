import os
PRO_PATH = os.path.dirname(os.path.abspath(__file__))


class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    cases_path = os.path.join(PRO_PATH, "test_dir")
    # cases_path = os.path.join(PRO_PATH, "test_dir", "test_qs.py::TestQsCondition")
    # cases_path = os.path.join(PRO_PATH, "test_dir", "test_qs.py::TestQsSearch::test_qs_search2")

    # 配置浏览器驱动类型(chrome/Edge/firefox/chrome-headless/firefox-headless)。
    # driver_type = "Edge"
    driver_type = "chrome-headless"

    # 失败重跑次数
    rerun = "0"

    # 当达到最大失败数，停止执行
    max_fail = "100"

    # 浏览器驱动（不需要修改）
    driver = None

    # 报告路径（不需要修改）
    NEW_REPORT = None
