# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from .BasePageObject import BasePageObject


class ListEstimatePageObject(BasePageObject):

    def __init__(self, driver):
        super(ListEstimatePageObject, self).__init__(driver)
        self._list_estimate = "//div[contains(concat(' ', @class ,' '), ' ng-isolate-scope ')]//strong"
        self._estimate = "//div[contains(concat(' ', @class ,' '), ' task-item ')]"
        self._estimate_href = "//div[contains(concat(' ', @class ,' '), ' task-item ')"
        self._delete_estimate_buttons = "//md-icon[contains(concat(' ', @class ,' '), ' table__remove-icon ')]"
        self._warning_message = "//md-dialog-content[@class='md-dialog-content']/h2"
        self._warning_message_confirm_button = "//div[@class='md-actions']/button[2]"

    def get_first_estimate(self):
        with allure.step("Получаем первый элемент в списке оценок"):
            return self._driver.find_elements_by_xpath(self._list_estimate)[0].text

    def get_first_estimate_attribute_href(self):
        with allure.step("Получаем атрибут href первой оценки в списке оценок"):
            return self._driver.find_elements_by_xpath(self._estimate)[0].get_attribute("href")

    def click_first_delete_estimate_button(self):
        with allure.step("Кликаем по кнопке удалить первую оценку"):
            self._driver.find_elements_by_xpath(self._delete_estimate_buttons)[0].click()

    def get_warning_message(self):
        with allure.step("Получаем предупреждающее сообщение"):
            return WebDriverWait(self._driver, 2).until(
                expected_conditions.visibility_of_element_located((By.XPATH, self._warning_message))).text

    def confirm_delete_estimate(self):
        with allure.step("Кликаем по кнопке подтвердить удаление оценки"):
            WebDriverWait(self._driver, 2).until(
                expected_conditions.element_to_be_clickable((By.XPATH, self._warning_message_confirm_button))).click()

    def attribute_href_is_present(self, href):
        with allure.step("Проверяем наличие атрибута href"):
            WebDriverWait(self._driver, 2).until(
                expected_conditions.invisibility_of_element_located((By.XPATH, self._warning_message)))

            return len(self._driver.find_elements_by_xpath(
                self._estimate_href + "and @href=\"" + href + "\"]"))

    def message_confirm_button_is_present(self):
        with allure.step("Проверяем наличие кнопки подтверждения"):
            try:
                WebDriverWait(self._driver, 2).until(
                    expected_conditions.element_to_be_clickable((By.XPATH, self._warning_message_confirm_button)))
            except TimeoutException:
                print("Закончилось время ожидания элемента кнопка 'OK'")
            return self._driver.find_element_by_xpath(self._warning_message_confirm_button)

    def click_first_estimate(self):
        with allure.step("Кликаем по первой оценки"):
            self._driver.find_elements_by_xpath(self._estimate)[0].click()
