import time
import unittest
import redis

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class thumbUp_case(unittest.TestCase):
    option = webdriver.ChromeOptions()
    # 保持浏览器缓存
    # 加载chrome个人资料路径，注意，最好使用‘/’
    option.add_argument('--user-data-dir=C:/Users/wjh/AppData/Local/Google/Chrome/User Data/Default')
    # 加载驱动器路径
    global driver
    driver = webdriver.Chrome(chrome_options=option,
                              executable_path="C:/Users/wjh/Desktop/chromedriver_win32/chromedriver.exe")

    # 查看最近xx条历史记录，记录视频类型
    def test_03_historyRecords(self):
        driver.get("http://bilibili.com")
        driver.maximize_window()

        # 创建连接池,decode_responses=True保证取出的数据不带b（byte）
        r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
        # 点击首页历史按钮
        driver.find_element_by_xpath(
            '//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/div[6]/span/div/span/span').click()

        # 跳转到新窗口
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        # 动态等待5秒
        driver.implicitly_wait(5)

        time.sleep(1)
        # 清除所有key
        r.flushdb()
        # 查看xx条记录，自己修改数目
        for i in range(10):
            try:
                # 获取视频分类标签文本
                text = driver.find_element_by_xpath(
                    '//*[@id="history_list"]/li[' + str(i + 1) + ']/div[2]/div[2]/div/span/span').text.strip()
                n = r.keys('*')
                if text in n:
                    r.set(text, str(int(r.get(text))+1))
                elif text is None:
                    pass
                else:
                    r.set(text, 1)

                time.sleep(0.5)
            except:
                # 发现没有找到元素，下拉页面，用pagedown按钮
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                ActionChains(driver).key_down(Keys.DOWN).perform()
                time.sleep(0.5)
            try:
                # 判断是否拉到了页面最下方，没有新的历史记录
                driver.find_element('link_text', '关于我们').click()
                time.sleep(5)
                break
            except:
                pass

        # 获取所有key和v
        print(r.keys('*'))
        m = r.keys('*')
        l = len(m)
        for p in range(l):
            print(m[p] + ' ' + r.get(m[p]))
