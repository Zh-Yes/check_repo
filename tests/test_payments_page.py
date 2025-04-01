import random
import time
import allure
import pytest
from base.base_test import BaseTest
from faker import Faker

@allure.feature("Check payments")
class TestPayments(BaseTest):

    def test_payments(self):
        self.welcome_page.open()
        self.welcome_page.click_log_in()
        self.welcome_page.enter_login(self.data.LOGIN_CUSTOMER)
        self.welcome_page.enter_password(self.data.PASSWORD)
        self.welcome_page.press_log_in()
        self.home_page.is_opened()
        self.home_page.click_menu()
        self.home_page.click_payments()
        self.payments_page.click_top_up()
        self.payments_page.enter_amount("999")
        self.payments_page.click_close()
        #self.payments_page.click_withdraw()
        #self.payments_page.enter_amount_withdraw("999")
        #self.payments_page.click_close_2()
        self.payments_page.click_promo_tab()
        self.payments_page.click_top_up_withdraw_tab()

        time.sleep(4)
