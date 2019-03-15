# -*- coding: utf-8 -*-
import allure
from selenium import webdriver

from PageObjects.LoginPageObject import LoginPageObject

URL = "http://estimate-qaa.simbirsoft/"


@allure.title("Тест-кейсы QA1-QA4")
class TestS1:

    _driver: webdriver.Chrome  # noqa

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("Проверка авторизации")
    @allure.story("Проверка авторизации с корректными данными")
    def test_login_with_valid_data(self, fixture_driver):
        login_page = LoginPageObject(fixture_driver)
        login_page.login("test_login, "test_password")
        param_url = login_page.get_url()

        assert str(param_url) == URL + "estimates"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature("Проверка авторизации")
    @allure.story("Проверка авторизации с некорректными данными")
    def test_login_with_incorrect_data(self, fixture_driver):
        login_page = LoginPageObject(fixture_driver)
        login_page.login("test", "test")

        assert login_page.get_color_message_error() == "#dd2c00"
        assert login_page.get_message_error() == "User not found"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature("Проверка авторизации")
    @allure.story("Проверка авторизации с корректным логином и пустым паролем")
    def test_login_with_valid_username_blank_password(self, fixture_driver):
        login_page = LoginPageObject(fixture_driver)

        assert login_page.login("test_login", "") == login_page.get_data_input_value()
        assert login_page.button_login_is_present()

        param_url = login_page.get_url()
        assert str(param_url) == URL + "login"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature("Проверка авторизации")
    @allure.story("Проверка авторизации с пустыми полями")
    def test_login_with_blank_data(self, fixture_driver):
        login_page = LoginPageObject(fixture_driver)

        assert login_page.login("", "") == login_page.get_data_input_value()
        assert login_page.button_login_is_present()

        param_url = login_page.get_url()
        assert str(param_url) == URL + "login"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature("Заведомо провальный тест")
    @allure.story("Проверка скриншота")
    def test_fail(self, fixture_driver):
        login_page = LoginPageObject(fixture_driver)

        login_page.login("test_login", "")
        param_url = login_page.get_url()

        assert str(param_url) == URL + "estimates"
