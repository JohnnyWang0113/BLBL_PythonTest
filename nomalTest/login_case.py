import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

# 登录用例
class login_Case(unittest.TestCase):
    chrome_options = Options()
    global driver
    driver = webdriver.Chrome(options=chrome_options)

    def test_01_login(self):

        driver.get("http://bilibili.com")
        driver.maximize_window()
        # 未登录情况下
        driver.find_element_by_class_name("unlogin-avatar").click()

        # 跳转到新窗口
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//*[@id="login-username"]').send_keys("17826859530")
        driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys("wjh19980808")
        driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()

        # b站有反爬虫图片填充验证，有可跳过的方法，有点复杂，直接使用了浏览器记录的登录信息，见thumbUp_case用例
        driver.quit()
