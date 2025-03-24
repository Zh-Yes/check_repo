import random
import time
import allure
import pytest
from base.base_test import BaseTest
from faker import Faker

@allure.feature("Contractor Profile Page")
class TestProfilePage(BaseTest):

    def test_profile_page(self):
        self.welcome_page.open()
        self.welcome_page.click_log_in()
        self.welcome_page.enter_login(self.data.LOGIN_CONTRACTOR)
        self.welcome_page.enter_password(self.data.PASSWORD)
        self.welcome_page.press_log_in()
        self.home_page.is_opened()
        self.home_page.click_menu()
        self.home_page.click_your_profile()
        self.profile_page.is_opened()
        self.profile_page.click_portfolio()
        self.profile_page.click_add_portfolio()
        self.profile_page.enter_project_title(self.data.TITLE)
        self.profile_page.enter_project_url(self.data.SOC_MEDIA_LINKS)
        self.profile_page.enter_description(self.data.COVER_LETTER)
        self.profile_page.click_save()
        self.profile_page.check_message()
        self.profile_page.click_done()
        self.profile_page.click_reviews()
        self.profile_page.click_work()