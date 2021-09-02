import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


# 点赞关注的up主的所有动态
class thumbUp_case(unittest.TestCase):
    option = webdriver.ChromeOptions()
    # 保持浏览器缓存
    # 加载chrome个人资料路径，注意，最好使用‘/’
    option.add_argument('--user-data-dir=C:/Users/wjh/AppData/Local/Google/Chrome/User Data/Default')
    # 加载驱动器路径
    global driver
    driver = webdriver.Chrome(chrome_options=option,
                              executable_path="C:/Users/wjh/Desktop/chromedriver_win32/chromedriver.exe")

    # 提前准备，发现缓存过期需要重新一次
    def test_02_thumbUp_befor(self):
        driver.get("http://bilibili.com")
        driver.maximize_window()
        # 点击首页动态按钮
        driver.find_element_by_xpath(
            '//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/div[4]/div/div[1]/a/span').click()

        # 跳转到新窗口
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        # 动态等待5秒
        driver.implicitly_wait(5)

        t = True
        time.sleep(1)
        i = 1
        while t:
            try:
                driver.find_element_by_xpath(
                    '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[' + str(
                        i) + ']/div/div[1]/div[4]/div[3]').click()
                # 时间长一点，b站保护机制会报错操作过于频繁
                time.sleep(3)
                i = i + 1
            except:
                # 发现没有找到要点赞的元素，下拉页面，用的pagedown按钮
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                ActionChains(driver).key_down(Keys.DOWN).perform()
                time.sleep(2)
            try:
                # 判断是否拉到了页面最下方，不会继续刷新了
                driver.find_element('link_text', '关于我们').click()
                time.sleep(5)
                t = False
            except:
                pass
