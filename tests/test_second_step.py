# -*- coding: utf-8 -*-
import allure
from selenium import webdriver

import settings
from Helpers.DriverHelper import DriverHelper
from PageObjects.DetailEstimatePageObject import DetailEstimatePageObject
from PageObjects.ListEstimatePageObject import ListEstimatePageObject
from PageObjects.LoginPageObject import LoginPageObject
from PageObjects.NewEstimatePageObject import NewEstimatePageObject


@allure.title("Тест-кейсы QA5")
class TestS2:

    _driver: webdriver.Chrome  # noqa

    def setup_method(self):
        self._driver = DriverHelper().get_driver()
        self._driver.get(settings.URL)
        self._driver.implicitly_wait(10)

    def teardown_method(self):
        self._driver.close()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("Проверка сценария создания оценки")
    @allure.story("Проверка сценария создания оценки c произвольными данными")
    def test_create_estimate(self):
        LoginPageObject(self._driver).login(settings.LOGIN, settings.PASSWORD)

        new_estimate_page = NewEstimatePageObject(self._driver)

        new_estimate_page.open_form()
        assert "edit" in new_estimate_page.get_url()

        new_estimate_page.create_estimate(
            settings.NAME_CLIENT, settings.NAME_PROJECT, settings.NAME_EXPERT, settings.DESCRIPTION_PROJECT)
        detail_estimate_page = DetailEstimatePageObject(self._driver)
        assert detail_estimate_page.phase_window_is_present()

        detail_estimate_page.close_message()
        assert detail_estimate_page.get_about_window()

        detail_estimate_page.click_bread_crumbs()
        list_estimate_page = ListEstimatePageObject(self._driver)

        assert str(list_estimate_page.get_first_estimate()) == settings.NAME_CLIENT
