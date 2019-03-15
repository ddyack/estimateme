# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver

import settings
from Helpers.DriverHelper import DriverHelper
from PageObjects.LoginPageObject import LoginPageObject


class TestS3:
    _driver: webdriver.Chrome  # noqa

    def setup_method(self):
        self._driver = DriverHelper().get_driver()
        self._driver.get(settings.URL)
        self._driver.implicitly_wait(10)

    def teardown_method(self):
        self._driver.close()

    @pytest.mark.parametrize("test_case, test_login, test_password, expected_url",
                             [
                                 ("test_case1", "test_login", "test_password", settings.URL + "estimates"),
                                 ("test_case2", "test", "test", settings.URL + "login"),
                                 ("test_case3", "test_login", "", settings.URL + "login"),
                                 ("test_case4", "", "", settings.URL + "login")
                             ]
                             )
    def test_login(self, test_login, test_password, expected_url, test_case):
        login_page = LoginPageObject(self._driver)
        login_page.login(test_login, test_password)
        param_url = login_page.get_url()

        if test_case == "test_case1":
            assert str(param_url) == expected_url
        elif test_case == "test_case2":
            assert login_page.get_color_message_error() == "#dd2c00"
            assert login_page.get_message_error() == "User not found"
        elif test_case == "test_case3":
            assert test_login, test_password == login_page.get_data_input_value()
            assert login_page.button_login_is_present()
            assert str(param_url) == expected_url
        elif test_case == "test_case4":
            login_input_value, password_input_value = login_page.get_data_input_value()
            assert test_login == login_input_value and test_password == password_input_value
            assert login_page.button_login_is_present()
            assert str(param_url) == expected_url
