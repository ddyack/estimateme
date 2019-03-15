# -*- coding: utf-8 -*-
class BasePageObject(object):
    def __init__(self, driver):
        self._driver = driver

    def title(self):
        return self._driver.title

    def page_source(self):
        return self._driver.page_source
