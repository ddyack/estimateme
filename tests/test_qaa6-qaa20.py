# -*- coding: utf-8 -*-

import allure

import settings
from PageObjects.DetailEstimatePageObject import DetailEstimatePageObject
from PageObjects.DetailPhasePageObject import DetailPhasePageObject
from PageObjects.ListEstimatePageObject import ListEstimatePageObject
from PageObjects.LoginPageObject import LoginPageObject


class TestS6:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("Проверка сценария создания фазы")
    @allure.story("Проверка сценария создания фазы из списка")
    def test_add_phase_for_estimate(self, fixture_driver):
        login_page = LoginPageObject(fixture_driver)
        login_page.login(settings.LOGIN, settings.PASSWORD)

        list_estimate_page = ListEstimatePageObject(fixture_driver)
        list_estimate_page.click_first_estimate()

        detail_estimate_page = DetailEstimatePageObject(fixture_driver)
        detail_estimate_page.click_add_phase_button()
        add_phase = detail_estimate_page.select_phase_buttons()
        assert detail_estimate_page.phase_window_is_present()

        detail_estimate_page.confirm_add_phase()
        current_added_phase = detail_estimate_page.get_text_added_phase()
        assert add_phase.lower() == current_added_phase.lower()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("Проверка сценария создания фичи")
    @allure.story("Проверка сценария создания фичи из списка")
    def test_add_feature_for_phase(self, fixture_driver):
        login_page = LoginPageObject(fixture_driver)
        login_page.login(settings.LOGIN, settings.PASSWORD)

        list_estimate_page = ListEstimatePageObject(fixture_driver)
        list_estimate_page.click_first_estimate()

        detail_estimate_page = DetailEstimatePageObject(fixture_driver)
        detail_estimate_page.click_add_phase_button()
        detail_estimate_page.select_phase_buttons()
        assert detail_estimate_page.phase_window_is_present()
        detail_estimate_page.confirm_add_phase()

        detail_phase_page = DetailPhasePageObject(fixture_driver)
        detail_phase_page.open_add_feature_window()
        assert detail_phase_page.check_feature_or_task_window()

        name_feature = detail_phase_page.add_feature(0)
        assert detail_phase_page.search_feature(name_feature)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("Проверка сценария создания фазы")
    @allure.story("Проверка сценария создания пользовательской фазы")
    def test_add_custom_phase_for_estimate(self, fixture_driver):
        login_page = LoginPageObject(fixture_driver)
        login_page.login(settings.LOGIN, settings.PASSWORD)

        list_estimate_page = ListEstimatePageObject(fixture_driver)
        list_estimate_page.click_first_estimate()

        detail_estimate_page = DetailEstimatePageObject(fixture_driver)
        detail_estimate_page.click_add_phase_button()
        add_phase = detail_estimate_page.send_custom_name_phase(settings.CUSTOM_NAME_PHASE)
        assert detail_estimate_page.phase_window_is_present()

        detail_estimate_page.confirm_add_phase()
        current_added_phase = detail_estimate_page.get_text_added_phase()
        assert add_phase.lower() == current_added_phase.lower()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("Проверка сценария создания фичи")
    @allure.story("Проверка сценария создания пользовательской фичи")
    def test_add_custom_feature_for_phase(self, fixture_driver):
        login_page = LoginPageObject(fixture_driver)
        login_page.login(settings.LOGIN, settings.PASSWORD)

        list_estimate_page = ListEstimatePageObject(fixture_driver)
        list_estimate_page.click_first_estimate()

        detail_estimate_page = DetailEstimatePageObject(fixture_driver)
        detail_estimate_page.click_add_phase_button()
        detail_estimate_page.select_phase_buttons()
        assert detail_estimate_page.phase_window_is_present()
        detail_estimate_page.confirm_add_phase()

        detail_phase_page = DetailPhasePageObject(fixture_driver)
        detail_phase_page.open_add_feature_window()
        assert detail_phase_page.check_feature_or_task_window()

        name_feature = detail_phase_page.add_custom_feature(settings.CUSTOM_NAME_FEATURE)
        assert detail_phase_page.search_feature(name_feature)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature("Проверка сценария добавления описания")
    @allure.story("Проверка сценария добавления описания к фиче")
    def test_add_description_feature(self, fixture_driver):
        login_page = LoginPageObject(fixture_driver)
        login_page.login(settings.LOGIN, settings.PASSWORD)

        list_estimate_page = ListEstimatePageObject(fixture_driver)
        list_estimate_page.click_first_estimate()

        detail_estimate_page = DetailEstimatePageObject(fixture_driver)
        detail_estimate_page.click_add_phase_button()
        detail_estimate_page.send_custom_name_phase(settings.CUSTOM_NAME_PHASE)
        detail_estimate_page.confirm_add_phase()

        detail_phase_page = DetailPhasePageObject(fixture_driver)
        detail_phase_page.open_add_feature_window()
        detail_phase_page.add_custom_feature(settings.CUSTOM_NAME_FEATURE)

        detail_phase_page.click_description_feature_or_task(0)
        assert detail_phase_page.get_description_feature_or_task_input_count()

        description_feature_text = detail_phase_page.enter_description_feature_or_task(settings.DESCRIPTION_FEATURE)
        detail_phase_page.click_description_feature_or_task(0)
        assert not detail_phase_page.get_description_feature_or_task_input_count()

        detail_phase_page.click_description_feature_or_task(0)
        assert detail_phase_page.get_description_feature_or_task_input_count()

        current_description_feature_text = detail_phase_page.get_current_description_feature_or_task_input_text()
        assert description_feature_text == current_description_feature_text

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("Проверка сценария создания задачи")
    @allure.story("Проверка сценария создания задачи из списка")
    def test_add_task_for_phase(self, fixture_driver):
        login_page = LoginPageObject(fixture_driver)
        login_page.login(settings.LOGIN, settings.PASSWORD)

        list_estimate_page = ListEstimatePageObject(fixture_driver)
        list_estimate_page.click_first_estimate()

        detail_estimate_page = DetailEstimatePageObject(fixture_driver)
        detail_estimate_page.click_add_phase_button()
        detail_estimate_page.send_custom_name_phase(settings.CUSTOM_NAME_PHASE)
        detail_estimate_page.confirm_add_phase()

        detail_phase_page = DetailPhasePageObject(fixture_driver)
        detail_phase_page.open_add_task_window()
        assert detail_phase_page.check_feature_or_task_window()

        name_task = detail_phase_page.add_task(0)
        assert detail_phase_page.search_task(name_task)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("Проверка сценария создания задачи")
    @allure.story("Проверка сценария создания пользовательской задачи")
    def test_add_custom_task_for_phase(self, fixture_driver):
        login_page = LoginPageObject(fixture_driver)
        login_page.login(settings.LOGIN, settings.PASSWORD)

        list_estimate_page = ListEstimatePageObject(fixture_driver)
        list_estimate_page.click_first_estimate()

        detail_estimate_page = DetailEstimatePageObject(fixture_driver)
        detail_estimate_page.click_add_phase_button()
        detail_estimate_page.select_phase_buttons()
        detail_estimate_page.confirm_add_phase()

        detail_phase_page = DetailPhasePageObject(fixture_driver)
        detail_phase_page.open_add_task_window()
        assert detail_phase_page.check_feature_or_task_window()

        name_task = detail_phase_page.add_custom_task(settings.CUSTOM_NAME_TASK)
        assert detail_phase_page.search_task(name_task)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature("Проверка сценария добавления описания")
    @allure.story("Проверка сценария добавления описания к задачи")
    def test_add_description_task(self, fixture_driver):
        login_page = LoginPageObject(fixture_driver)
        login_page.login(settings.LOGIN, settings.PASSWORD)

        list_estimate_page = ListEstimatePageObject(fixture_driver)
        list_estimate_page.click_first_estimate()

        detail_estimate_page = DetailEstimatePageObject(fixture_driver)
        detail_estimate_page.click_add_phase_button()
        detail_estimate_page.send_custom_name_phase(settings.CUSTOM_NAME_PHASE)
        detail_estimate_page.confirm_add_phase()

        detail_phase_page = DetailPhasePageObject(fixture_driver)
        detail_phase_page.open_add_task_window()
        detail_phase_page.add_custom_task(settings.CUSTOM_NAME_TASK)

        detail_phase_page.click_description_feature_or_task(0)
        assert detail_phase_page.get_description_feature_or_task_input_count()

        description_task_text = detail_phase_page.enter_description_feature_or_task(settings.DESCRIPTION_TASK)
        detail_phase_page.click_description_feature_or_task(0)
        assert not detail_phase_page.get_description_feature_or_task_input_count()

        detail_phase_page.click_description_feature_or_task(0)
        assert detail_phase_page.get_description_feature_or_task_input_count()

        current_description_task_text = detail_phase_page.get_current_description_feature_or_task_input_text()
        assert description_task_text == current_description_task_text

    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature("Проверка сценария добавления времени")
    @allure.story("Проверка сценария добавления времени 'ОТ' к задаче")
    def test_add_min_time_for_task(self, fixture_driver):
        login_page = LoginPageObject(fixture_driver)
        login_page.login(settings.LOGIN, settings.PASSWORD)

        list_estimate_page = ListEstimatePageObject(fixture_driver)
        list_estimate_page.click_first_estimate()

        detail_estimate_page = DetailEstimatePageObject(fixture_driver)
        detail_estimate_page.click_add_phase_button()
        detail_estimate_page.send_custom_name_phase(settings.CUSTOM_NAME_PHASE)
        detail_estimate_page.confirm_add_phase()

        detail_phase_page = DetailPhasePageObject(fixture_driver)
        detail_phase_page.open_add_task_window()
        detail_phase_page.add_custom_task(settings.CUSTOM_NAME_TASK)

        min_time = detail_phase_page.input_min_time(10)
        assert float(detail_phase_page.get_current_min_time()) == float(min_time)
        total_min_time = detail_phase_page.get_total_min_time_phase()
        assert float(min_time) == float(total_min_time)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.feature("Проверка сценария добавления времени")
    @allure.story("Проверка сценария добавления времени 'ДО' к задаче")
    def test_add_max_time_for_task(self, fixture_driver):
        login_page = LoginPageObject(fixture_driver)
        login_page.login(settings.LOGIN, settings.PASSWORD)

        list_estimate_page = ListEstimatePageObject(fixture_driver)
        list_estimate_page.click_first_estimate()

        detail_estimate_page = DetailEstimatePageObject(fixture_driver)
        detail_estimate_page.click_add_phase_button()
        detail_estimate_page.send_custom_name_phase(settings.CUSTOM_NAME_PHASE)
        detail_estimate_page.confirm_add_phase()

        detail_phase_page = DetailPhasePageObject(fixture_driver)
        detail_phase_page.open_add_task_window()
        detail_phase_page.add_custom_task(settings.CUSTOM_NAME_TASK)

        max_time = detail_phase_page.input_max_time(10)
        assert float(detail_phase_page.get_current_max_time()) == max_time
        total_max_time = detail_phase_page.get_total_max_time_phase()
        assert float(max_time) == float(total_max_time)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.feature("Проверка сценария удаления фазы")
    @allure.story("Проверка сценария удаления фазы из списка")
    def test_del_phase(self, fixture_driver):
        login_page = LoginPageObject(fixture_driver)
        login_page.login(settings.LOGIN, settings.PASSWORD)

        list_estimate_page = ListEstimatePageObject(fixture_driver)
        list_estimate_page.click_first_estimate()

        detail_estimate_page = DetailEstimatePageObject(fixture_driver)
        detail_estimate_page.click_add_phase_button()
        detail_estimate_page.send_custom_name_phase(settings.CUSTOM_NAME_PHASE)
        detail_estimate_page.confirm_add_phase()

        detail_phase_page = DetailPhasePageObject(fixture_driver)
        detail_phase_page.click_edit_phase_button()
        assert detail_phase_page.get_del_phase_button()

        del_phase_button = detail_phase_page.get_del_phase_button()
        detail_phase_page.hover_to(del_phase_button)
        assert detail_phase_page.get_tooltip_del_phase()

        detail_phase_page.del_phase(0)
        assert detail_phase_page.get_del_phase_window()
        assert detail_phase_page.get_del_phase_cancel_button()
        assert detail_phase_page.get_del_phase_confirm_button()

        detail_phase_page.click_del_phase_confirm_button()
        assert not detail_estimate_page.check_added_phase()

        detail_phase_page.click_save_edit_phase_button()
        assert not detail_phase_page.get_attribute_display_from_save_edit_phase_button()
        assert detail_estimate_page.check_add_phase_button()
