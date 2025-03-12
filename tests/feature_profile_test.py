import random
import time
import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.welcome_page.open()
        self.welcome_page.click_log_in()
        self.welcome_page.enter_login(self.data.LOGIN)
        self.welcome_page.enter_password(self.data.PASSWORD)
        self.welcome_page.press_log_in()
        self.home_page.is_opened()
        self.home_page.click_menu()
        self.home_page.click_your_profile()
        self.profile_page.is_opened()
        self.profile_page.click_edit()
        self.edit_profile_page.is_opened()
        self.edit_profile_page.click_clear()
        self.edit_profile_page.change_name(f"Test {random.randint(1, 100)}")
        #time.sleep(2)
        self.edit_profile_page.click_checkbox()
        #time.sleep(3)
        self.edit_profile_page.click_save()
        self.edit_profile_page.check_message()
        self.edit_profile_page.click_done()