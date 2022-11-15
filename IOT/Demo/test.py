from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--window-size=1920x1080")
browser = webdriver.Chrome(chrome_options=chrome_options)
# browser = webdriver.Edge()

browser.get("http://iot.sot-soft.com/ths-iot/login")

browser.find_element(By.ID, "user_id").send_keys("test")
browser.find_element(By.ID, "LAY-user-login-password").send_keys("test")
browser.find_element(By.XPATH, "//*[@id='loginsub']/span").click()

browser.find_element(By.XPATH, '//*[@id="LAY-system-side-menu"]/li[2]/a/cite').click()
browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/ul/li[2]/dl/dd[1]/a/cite').click()
browser.switch_to.frame(1)

items = browser.find_elements(By.XPATH, '//*[@id="table_height"]/div')
for item in items:
    print(item.text)
