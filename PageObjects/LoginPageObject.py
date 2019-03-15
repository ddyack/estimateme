# -*- coding: utf-8 -*-
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait

from .BasePageObject import BasePageObject


class LoginPageObject(BasePageObject):

    def __init__(self, driver):
        super(LoginPageObject, self).__init__(driver)
        self._input_login = "//input[@ng-model = 'vm.login']"
        self._input_pass = "//input[@ng-model = 'vm.password']"
        self._button_login = "//button['login-btn']"
        self._button_rating_in_title = "//button[@id='toggle-side-nav-button']"
        self._message_error = "//div[contains(concat(' ', @class ,' '), ' error-msg ')]"

    def login(self, login, passwd):
        with allure.step("Проходим авторизацию"):
            self._driver.find_element_by_xpath(self._input_login).send_keys(login)
            self._driver.find_element_by_xpath(self._input_pass).send_keys(passwd)
            self._driver.find_element_by_xpath(self._button_login).click()
            return login, passwd

    def get_data_input_value(self):
        with allure.step("Получаем значения вводимые в поля при авторизации"):
            value_login = self._driver.find_element_by_xpath(self._input_login).get_attribute("value")
            value_password = self._driver.find_element_by_xpath(self._input_pass).get_attribute("value")
            return value_login, value_password

    def get_url(self):
        with allure.step("Получаем текущий адрес страницы"):
            try:
                WebDriverWait(self._driver, 3).until(
                    expected_conditions.presence_of_element_located(
                        (By.XPATH, self._button_rating_in_title)))
            except TimeoutException:
                print("Вход на сайт не осуществлен")
            return self._driver.current_url

    def get_message_error(self):
        try:
            WebDriverWait(self._driver, 1).until(
                expected_conditions.text_to_be_present_in_element(
                    (By.XPATH, self._message_error), "User not found"))
        except TimeoutException:
            print("Закончилось время ожидания элемента 'User not found'")
        return str(self._driver.find_elements_by_xpath(self._message_error)[0].text)

    def get_color_message_error(self):
        try:
            WebDriverWait(self._driver, 1).until(
                expected_conditions.text_to_be_present_in_element(
                    (By.XPATH, self._message_error), "User not found"))
        except TimeoutException:
            print("Закончилось время ожидания элемента 'User not found'")
        rgb = self._driver.find_elements_by_xpath(self._message_error)[0].value_of_css_property("color")
        return Color.from_string(rgb).hex

    def button_login_is_present(self):
        try:
            WebDriverWait(self._driver, 1).until(
                expected_conditions.text_to_be_present_in_element(
                    (By.XPATH, self._button_login), "User not found"))
        except TimeoutException:
            print("Закончилось время ожидания элемента кнопка 'LOGIN'")
        return self._driver.find_element_by_xpath(self._button_login)
