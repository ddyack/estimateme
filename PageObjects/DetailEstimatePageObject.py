# -*- coding: utf-8 -*-
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from .BasePageObject import BasePageObject


class DetailEstimatePageObject(BasePageObject):

    def __init__(self, driver):
        super(DetailEstimatePageObject, self).__init__(driver)
        self._about_view_window = "//md-content[@ng-show='!vm.preloader']/div[1]"
        self._close_message_button = "//md-dialog[contains(concat(' ', @class ,' '), ' phaseModal ')]/md-icon"
        self._phase_window = "//md-dialog[contains(concat(' ', @class ,' '), ' phaseModal ')]"
        self._bread_crumbs = "//h2//a[@ui-sref='index.estimates']"
        self._add_phase_button = "//button[@id='add-phase-button']"
        self._list_phase_buttons = "//ul[@class='phase-list']/li"
        self._confirm_add_phase_button = "//button[contains(concat(' ', @class ,' '), ' md-primary ')]/span"
        self._added_phase = "//md-tab-item[last()]/label[@tab-editable='phase.name']"
        self._add_custom_phase_input = "//input[@id='save-adding-phases-button']"
        self._del_phase_window = "//md-dialog"

    def close_message(self):
        with allure.step("Закрываем всплывающее окно создания фазы"):
            WebDriverWait(self._driver, 2).until(
                ec.element_to_be_clickable((By.XPATH, self._close_message_button))).click()

    def click_bread_crumbs(self):
        with allure.step("Переходим на страницу Оценки"):
            WebDriverWait(self._driver, 2).until(ec.invisibility_of_element_located((By.XPATH, self._phase_window)))
            WebDriverWait(self._driver, 2).until(ec.element_to_be_clickable((By.XPATH, self._bread_crumbs))).click()

    def phase_window_is_present(self):
        with allure.step("Получаем всплывающее окно создания фазы"):
            try:
                WebDriverWait(self._driver, 3).until(
                    ec.presence_of_element_located(
                        (By.XPATH, self._phase_window)))
            except TimeoutException:
                print("Форма создания фазы не открылась")
            return self._driver.find_element_by_xpath(self._phase_window)

    def get_about_window(self):
        with allure.step("Получаем информацию о созданной оценке"):
            return self._driver.find_element_by_xpath(self._about_view_window)

    def click_add_phase_button(self):
        self._driver.find_element_by_xpath(self._add_phase_button).click()

    def select_phase_buttons(self):
        phase = self._driver.find_elements_by_xpath(self._list_phase_buttons)[0].text
        self._driver.find_elements_by_xpath(self._list_phase_buttons)[0].click()
        return phase

    def confirm_add_phase(self):
        self._driver.find_element_by_xpath(self._confirm_add_phase_button).click()

    def get_text_added_phase(self):
        WebDriverWait(self._driver, 2).until(ec.invisibility_of_element_located((By.XPATH, self._phase_window)))
        return self._driver.find_element_by_xpath(self._added_phase).text

    def send_custom_name_phase(self, custom_name_phase):
        self._driver.find_element_by_xpath(self._add_custom_phase_input).send_keys(custom_name_phase)
        return custom_name_phase

    def check_added_phase(self):
        WebDriverWait(self._driver, 2).until(ec.invisibility_of_element_located((
            By.XPATH, self._del_phase_window)))

        return len(self._driver.find_elements_by_xpath(self._added_phase))

    def check_add_phase_button(self):
        return len(self._driver.find_elements_by_xpath(self._add_phase_button))
