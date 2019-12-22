# coding=utf-8
import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(filename="tsg.log", level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')


class TestTsg:
    def setup(self):

        # opt = Options()
        # # opt.set_headless()
        # opt.add_argument('--no-sandbox')
        # # 让Chrome在root权限下跑
        # opt.add_argument('--disable-dev-shm-usage')
        # opt.add_argument('--headless')
        # opt.add_argument('blink-settings=imagesEnabled=false')
        # opt.add_argument('--disable-gpu')
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)


        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://fxm5547.baobaobooks.com/")
        assert "小明fxm5547" in self.driver.title
        sleep(5)

    def teardown(self):
        self.driver.quit()



    def test_my(self):
        pass
