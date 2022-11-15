import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import json


def browser_initial():
    """"
    进行浏览器初始化
    """
    chrome_options = Options()
    browser = Chrome(options=chrome_options)
    with open('stealth.min.js') as f:
        js = f.read()
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    log_url = 'https://s.taobao.com/'
    return log_url, browser


def get_cookies(log_url, browser):
    """
    获取cookies保存至本地
    """
    browser.get(log_url)
    time.sleep(60)  # 进行登录
    dictCookies = browser.get_cookies()
    jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存

    with open('cookies.txt', 'w') as f:
        f.write(jsonCookies)
    print('cookies保存成功！')

    browser.close()


if __name__ == "__main__":
    tur = browser_initial()
    get_cookies(tur[0], tur[1])
