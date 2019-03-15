# -*- coding: utf-8 -*-
import allure
import pytest

import settings
from Helpers.DriverHelper import DriverHelper


@pytest.fixture(scope="function", autouse=True)
def fixture_driver():
    _driver = DriverHelper().get_driver()
    _driver.get(settings.URL)
    _driver.implicitly_wait(10)
    yield _driver
    if AssertionError:
        allure.attach(_driver.get_screenshot_as_png(), "screen_test", allure.attachment_type.PNG)
    _driver.close()
