# -*- coding: utf-8 -*-
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from .BasePageObject import BasePageObject


class NewEstimatePageObject(BasePageObject):

    def __init__(self, driver):
        super(NewEstimatePageObject, self).__init__(driver)
        self._add_button = "//button[@id='open-menu-button']"
        self._language_buttons = "//div[@class='adding-area-item']"
        self._client_name_input = "//textarea[@name='customer']"
        self._project_name_input = "//textarea[@ng-model='vm.project.name']"
        self._expert_name_input = "//md-autocomplete-wrap/input"
        self._departments_checkbox = "//li[contains(concat(' ', @ng-repeat ,' '), ' vm.departments ')]"
        self._project_description_input = "//textarea[@name='description']"
        self._submit_button = "//button[@id='edit-about-button']"

    def open_form(self):
        with allure.step("Открываем форму создания заявки"):
            self._driver.find_element_by_xpath(self._add_button).click()
            self._driver.find_elements_by_xpath(self._language_buttons)[0].click()

    def create_estimate(self, client, project, expert, description):
        with allure.step("Заполняем и отправляем форму создания заявки"):
            self._driver.find_element_by_xpath(self._client_name_input).send_keys(client)
            self._driver.find_element_by_xpath(self._project_name_input).send_keys(project)
            self._driver.find_element_by_xpath(self._expert_name_input).send_keys(expert, Keys.ENTER)
            self._driver.find_elements_by_xpath(self._departments_checkbox)[0].click()
            print("Выбран отдел: " + self._driver.find_elements_by_xpath(self._departments_checkbox)[0].text)
            self._driver.find_element_by_xpath(self._project_description_input).send_keys(description)
            self._driver.find_element_by_xpath(self._submit_button).click()

    def get_url(self):
        with allure.step("Получаем текущий адрес страницы"):
            try:
                WebDriverWait(self._driver, 3).until(
                    ec.presence_of_element_located(
                        (By.XPATH, self._client_name_input)))
            except TimeoutException:
                print("Форма создания оценки не открылась")
            return self._driver.current_url

    @property
    def get_client_name_input(self):
        with allure.step("Получаем имя клиента"):
            return self._client_name_input
