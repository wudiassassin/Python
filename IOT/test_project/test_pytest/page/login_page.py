from poium import Page, Element
import time


class LoginPage(Page):
    usrname_input = Element(id_="user_id", describe="用户名")
    password_input = Element(id_="LAY-user-login-password", describe="密码")
    login_button = Element(xpath="//*[@id='loginsub']/span", describe="登录按钮")
    error_text = Element(xpath="//*[@id='login_form']/div/div[2]/div[1]/span", describe="错误提示")