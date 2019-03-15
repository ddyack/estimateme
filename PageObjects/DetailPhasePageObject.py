# -*- coding: utf-8 -*-

import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from .BasePageObject import BasePageObject


class DetailPhasePageObject(BasePageObject):

    def __init__(self, driver):
        super(DetailPhasePageObject, self).__init__(driver)
        self._add_menu_button = "//button[@aria-label='menu']"
        self._add_feature_button = "//div[@ng-click='vm.addNewFeature($event)']"
        self._add_task_button = "//div[@ng-click='vm.addNewTask($event)']"
        self._add_feature_or_task_window = "//md-dialog[contains(concat(' ', @class ,' '), ' addingModal ')]"
        self._list_features_or_tasks = "//div[@class='md-label']//div[contains(concat(' ', @class ,' '), ' name ')]"
        self._confirm_add_feature_button = "//button[@id='save-adding-features-button']"
        self._confirm_add_task_button = "//button[@id='save-adding-tasks-button']"
        self._names_feature = "//*[@id='feature-name-textarea' and text() = "
        self._names_task = "//*[@id='task-name-textarea' and text() = "
        self._add_custom_feature_or_task_input = "//div[contains(concat(' ', @class ,' '), ' new-task-row ')]//textarea"
        self._add_description_button = "//md-icon[contains(concat(' ', @ng-if ,' '), ' vm.item.description ')]"
        self._add_description_input = "//div[@ng-if='vm.descriptionOpen']//textarea"
        self._add_min_time_input = "//input[@id='min-hours-input']"
        self._add_max_time_input = "//input[@id='max-hours-input']"
        self._total_min_time_phase = "//div[contains(concat(' ', @class ,' '), ' phase-total-time ')]/div[1]"
        self._total_max_time_phase = "//div[contains(concat(' ', @class ,' '), ' phase-total-time ')]/div[3]"
        self._page_phase = "//div[@ui-view='phase']"
        self._edit_phase_button = "//button[@ng-click='vm.openEditPhase()']"
        self._del_phase_button = "//button[@id='delete-phase-button']"
        self._del_phase_tooltip = "//md-tooltip/div/span"
        self._del_phase_window = "//div[@class='md-actions']"
        self._del_phase_cancel_button = "//md-dialog//button[@ng-click='dialog.abort()']"
        self._del_phase_confirm_button = "//div[@class='md-actions']/button[2]"
        self._save_edit_phase_button = "//button[@id='save-phase-button']"

    def open_add_feature_window(self):
        with allure.step("Открываем меню добавления фичи"):
            self._driver.find_element_by_xpath(self._add_menu_button).click()
            self._driver.find_element_by_xpath(self._add_feature_button).click()

    def open_add_task_window(self):
        with allure.step("Открываем меню добавления задачи"):
            self._driver.find_element_by_xpath(self._add_menu_button).click()
            self._driver.find_element_by_xpath(self._add_task_button).click()

    def check_feature_or_task_window(self):
        with allure.step("Проверяем наличие окна добавления задачи или фичи"):
            return self._driver.find_element_by_xpath(self._add_feature_or_task_window)

    def add_feature(self, n):
        with allure.step("Добавляем фичу из списка"):
            name_feature = self._driver.find_elements_by_xpath(self._list_features_or_tasks)[n].get_attribute("innerText")
            name_feature = name_feature.split("chevron_right")[1]
            self._driver.find_elements_by_xpath(self._list_features_or_tasks)[n].click()
            self._driver.find_element_by_xpath(self._confirm_add_feature_button).click()
            return name_feature

    def add_task(self, n):
        with allure.step("Добавляем задачу из списка"):
            name_task = self._driver.find_elements_by_xpath(self._list_features_or_tasks)[n].text
            self._driver.find_elements_by_xpath(self._list_features_or_tasks)[n].click()
            self._driver.find_element_by_xpath(self._confirm_add_task_button).click()
            return name_task

    def search_feature(self, text):
        with allure.step("Ищем добавленную фичу в списке"):
            return self._driver.find_element_by_xpath((self._names_feature + "\'{}\']").format(text))

    def search_task(self, text):
        with allure.step("Ищем добавленную задачу в списке"):
            return self._driver.find_element_by_xpath((self._names_task + "\'{}\']").format(text))

    def add_custom_feature(self, text):
        with allure.step("Добавляем пользовательскую фичу"):
            self._driver.find_element_by_xpath(self._add_custom_feature_or_task_input).send_keys(text)
            self._driver.find_element_by_xpath(self._confirm_add_feature_button).click()
            return text

    def add_custom_task(self, text):
        with allure.step("Добавляем пользовательскую задачу"):
            self._driver.find_element_by_xpath(self._add_custom_feature_or_task_input).send_keys(text)
            self._driver.find_element_by_xpath(self._confirm_add_task_button).click()
            return text

    def click_description_feature_or_task(self, n):
        with allure.step("Кликаем по кнопке добавить описание"):
            self._driver.find_elements_by_xpath(self._add_description_button)[n].click()

    def get_description_feature_or_task_input_count(self):
        with allure.step("Проверяем наличие input описание на странице"):
            return len(self._driver.find_elements_by_xpath(self._add_description_input))

    def enter_description_feature_or_task(self, text):
        with allure.step("Вводим текст описания"):
            self._driver.find_element_by_xpath(self._add_description_input).send_keys(text)
            return text

    def get_current_description_feature_or_task_input_text(self):
        with allure.step("Получаем текущий текст описания задачи или фичи"):
            return self._driver.find_element_by_xpath(self._add_description_input).text

    def input_min_time(self, time):
        with allure.step("Вводим время ОТ"):
            self._driver.find_element_by_xpath(self._add_min_time_input).send_keys(time)
            self._driver.find_element_by_xpath(self._page_phase).click()
            return time

    def input_max_time(self, time):
        with allure.step("Вводим время ДО"):
            self._driver.find_element_by_xpath(self._add_max_time_input).send_keys(time)
            self._driver.find_element_by_xpath(self._page_phase).click()
            return time

    def get_current_min_time(self):
        with allure.step("Получаем текущее время ОТ"):
            return self._driver.find_element_by_xpath(self._add_min_time_input).get_attribute("value")

    def get_current_max_time(self):
        with allure.step("Получаем текущее время ДО"):
            return self._driver.find_element_by_xpath(self._add_max_time_input).get_attribute("value")

    def get_total_min_time_phase(self):
        with allure.step("Получаем общее время ОТ"):
            return self._driver.find_element_by_xpath(self._total_min_time_phase).text

    def get_total_max_time_phase(self):
        with allure.step("Получаем общее время ДО"):
            return self._driver.find_element_by_xpath(self._total_max_time_phase).text

    def click_edit_phase_button(self):
        with allure.step("Кликаем по кнопке редактирования фазы"):
            self._driver.find_element_by_xpath(self._edit_phase_button).click()

    def del_phase_buttons_is_present(self):
        with allure.step("Проверяем наличие кнопки удалить фазу"):
            return len(self._driver.find_elements_by_xpath(self._del_phase_button))

    def get_del_phase_button(self):
        with allure.step("Получаем кнопку удаления фазы"):
            return self._driver.find_element_by_xpath(self._del_phase_button)

    def get_tooltip_del_phase(self):
        with allure.step("Получаем всплывающее сообщения кнопки удаления фазы"):
            return self._driver.find_element_by_xpath(self._del_phase_tooltip)

    def hover_to(self, element):
        with allure.step("Наводим мышь на элемент"):
            ActionChains(self._driver).move_to_element(element).perform()

    def del_phase(self, n):
        with allure.step("Удаляем фазу"):
            self._driver.find_elements_by_xpath(self._del_phase_button)[n].click()

    def get_del_phase_window(self):
        with allure.step("Получаем окно удаления фазы"):
            return self._driver.find_element_by_xpath(self._del_phase_window)

    def get_del_phase_cancel_button(self):
        with allure.step("Получаем кнопку отмены удаления фазы"):
            return self._driver.find_element_by_xpath(self._del_phase_cancel_button)

    def get_del_phase_confirm_button(self):
        with allure.step("Получаем кнопку подтверждения удаления фазы"):
            return self._driver.find_element_by_xpath(self._del_phase_confirm_button)

    def click_del_phase_confirm_button(self):
        with allure.step("Кликаем по кнопке подтверждения удаления фазы"):
            WebDriverWait(self._driver, 2).until(ec.visibility_of_element_located((
                By.XPATH, self._del_phase_window)))

            WebDriverWait(self._driver, 2).until(ec.element_to_be_clickable((
                By.XPATH, self._del_phase_confirm_button))).click()

    def click_save_edit_phase_button(self):
        with allure.step("Кликаем по кнопке сохранения редактирования фазы"):
            self._driver.find_element_by_xpath(self._save_edit_phase_button).click()

    def get_attribute_display_from_save_edit_phase_button(self):
        with allure.step("Проверяем видимость кнопки сохранения редактирования фазы"):
            return self._driver.find_element_by_xpath(self._save_edit_phase_button).get_attribute("display")
