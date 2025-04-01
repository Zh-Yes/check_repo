import random
import time
import allure
import pytest
from base.base_test import BaseTest
from faker import Faker

@allure.feature("Registration Customer")
class TestRegistrationCustomer(BaseTest):

    def test_registration_customer(self):
        self.welcome_page.open()
        self.welcome_page.click_get_started()
        self.registration_type_page.is_opened()
        self.registration_type_page.select_customer_type()
        self.registration_type_page.click_checkbox()
        self.registration_type_page.click_register()
        self.registration_customer_page.is_opened()
        self.registration_customer_page.check_text_step1()
        self.registration_customer_page.enter_first_name(f"Test{random.randint(1, 100)}")
        self.registration_customer_page.enter_last_name(f"Auto{random.randint(1, 100)}")
        self.registration_customer_page.enter_company_name(self.data.COMPANY_NAME)
        self.registration_customer_page.click_job_title()
        self.registration_customer_page.select_job_title()
        self.registration_customer_page.click_country()
        self.registration_customer_page.select_country()
        self.registration_customer_page.enter_city("a")
        self.registration_customer_page.select_city()
        self.registration_customer_page.click_next_step()
        self.registration_customer_page.enter_password(self.data.PASSWORD)
        self.registration_customer_page.enter_repeat_password(self.data.PASSWORD)
        self.registration_customer_page.enter_email()
        self.registration_customer_page.enter_phone_number(self.data.PHONE_NUMBER)
        self.registration_customer_page.click_next_step2()
        self.registration_customer_page.enter_cover_letter(self.data.COVER_LETTER)
        self.registration_customer_page.enter_soc_media_links1(self.data.SOC_MEDIA_LINKS)
        self.registration_customer_page.enter_soc_media_links2(self.data.SOC_MEDIA_LINKS)
        self.registration_customer_page.enter_soc_media_links3(self.data.SOC_MEDIA_LINKS)
        self.registration_customer_page.enter_soc_media_links4(self.data.SOC_MEDIA_LINKS)
        self.registration_customer_page.enter_soc_media_links5(self.data.SOC_MEDIA_LINKS)
        self.registration_customer_page.click_checkbox()
        self.registration_customer_page.click_finish()
        self.home_page.is_opened()

        time.sleep(5)

