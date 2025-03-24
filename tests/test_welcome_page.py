import random
import time
import allure
import pytest
from base.base_test import BaseTest
from faker import Faker

@allure.feature("Welcome page")
class TestWelcomePage(BaseTest):

    def test_welcome_page(self):
        self.welcome_page.open()
        self.welcome_page.click_discover_more()
        self.welcome_page.click_for_specialist()
        self.welcome_page.check_header_text()
        self.welcome_page.click_for_employer()
        self.welcome_page.check_header_text_2()
        self.welcome_page.click_faq()
        self.welcome_page.click_first_faq()
        self.welcome_page.click_second_faq()