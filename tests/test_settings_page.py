import random
import time
import allure
import pytest
from base.base_test import BaseTest
from faker import Faker


class TestSettings(BaseTest):
    @allure.feature("Check settings customer")
    @allure.story("Проверка всех полей")
    def test_settings_customer(self):
        self.welcome_page.open()
        self.welcome_page.click_log_in()
        self.welcome_page.enter_login(self.data.LOGIN_CUSTOMER)
        self.welcome_page.enter_password(self.data.PASSWORD)
        self.welcome_page.press_log_in()
        self.home_page.is_opened()
        self.home_page.click_menu()
        self.home_page.click_settings()
        self.settings_page.enter_old_password(self.data.PASSWORD)
        self.settings_page.enter_new_password(self.data.PASSWORD)
        self.settings_page.enter_repeat_password(self.data.PASSWORD)
        self.settings_page.click_save_1()
        self.settings_page.click_done_1()
        self.settings_page.click_clear_email()
        self.settings_page.enter_email()
        self.settings_page.click_save_2()
        self.settings_page.click_done_2()
        self.settings_page.clear_phone_number()
        self.settings_page.enter_phone_number(self.data.PHONE_NUMBER)
        self.settings_page.click_save_3()
        self.settings_page.click_done_3()

        time.sleep(3)

    @allure.feature("Check settings contractor")
    @allure.story("Проверка всех полей")
    def test_settings_contractor(self):
        self.welcome_page.open()
        self.welcome_page.click_log_in()
        self.welcome_page.enter_login(self.data.LOGIN_CONTRACTOR)
        self.welcome_page.enter_password(self.data.PASSWORD)
        self.welcome_page.press_log_in()
        self.home_page.is_opened()
        self.home_page.click_menu()
        self.home_page.click_settings()
        self.settings_page.enter_old_password(self.data.PASSWORD)
        self.settings_page.enter_new_password(self.data.PASSWORD)
        self.settings_page.enter_repeat_password(self.data.PASSWORD)
        self.settings_page.click_save_1()
        self.settings_page.click_done_1()
        self.settings_page.click_clear_email()
        self.settings_page.enter_email()
        self.settings_page.click_save_2()
        self.settings_page.click_done_2()
        self.settings_page.clear_phone_number()
        self.settings_page.enter_phone_number(self.data.PHONE_NUMBER)
        self.settings_page.click_save_3()
        self.settings_page.click_done_3()

        time.sleep(3)