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
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument('--no-sandbox')
        chromeOptions.add_argument('--disable-dev-shm-usage')
        chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('blink-settings=imagesEnabled=false')
        chromeOptions.add_argument('--disable-gpu')
        chromeOptions.binary_location = r""
        # self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chromeOptions)
        self.driver = webdriver.Chrome(options=chromeOptions, executable_path='/usr/bin/chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.get("https://fxm5547.baobaobooks.com/")
        assert "小明fxm5547" in self.driver.title
        sleep(5)

    def teardown(self):
        self.driver.quit()



    def test_my(self):
        pass
