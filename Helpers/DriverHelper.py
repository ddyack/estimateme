# -*- coding: utf-8 -*-
from selenium import webdriver


class DriverHelper(object):
    def __init__(self):
        self._driver = webdriver.Remote(
            command_executor="http://qaa.simbirsoft:4444/wd/hub",
            desired_capabilities={
                "browserName": "chrome",
                "enableVNC": True}
        )

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._driver.close()

    def get_driver(self):
        return self._driver

    def close(self):
        self._driver.close()
