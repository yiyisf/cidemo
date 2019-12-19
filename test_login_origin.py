# coding=utf-8
import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(filename="tsg.log", level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')


class TestTsg:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://fxm5547.baobaobooks.com/")
        assert "小明fxm5547" in self.driver.title
        sleep(5)

    def teardown(self):
        self.driver.quit()



    def test_my(self):
        pass
