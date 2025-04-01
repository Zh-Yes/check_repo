import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.settings_locators import SettingsLocators
from faker import Faker

class SettingsPage(BasePage):

    PAGE_URL = Links.SETTINGS_PAGE
    locators = SettingsLocators()

    @allure.step("Enter old password")
    def enter_old_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.locators.OLD_PASSWORD)).send_keys(password)

    @allure.step("Enter new password")
    def enter_new_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.locators.NEW_PASSWORD)).send_keys(password)

    @allure.step("Enter repeat password")
    def enter_repeat_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.locators.REPEAT_PASSWORD)).send_keys(password)

    @allure.step("Click save")
    def click_save_1(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.SAVE_BUTTON_1)).click()
        successfully_text = "Success!"
        assert self.wait.until(EC.text_to_be_present_in_element(self.locators.CHECK_TEXT_1, successfully_text))

    @allure.step("Click done")
    def click_done_1(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.DONE_BUTTON_1)).click()

    @allure.step("Click clear email")
    def click_clear_email(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.CLEAR_EMAIL)).click()

    @allure.step("Enter email")
    def enter_email(self):
        fake = Faker()
        random_email = fake.email()
        self.wait.until(EC.element_to_be_clickable(self.locators.EMAIL_FIELD)).send_keys(random_email)
        return random_email

    @allure.step("Click save")
    def click_save_2(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.SAVE_BUTTON_2)).click()
        text = "Go to the mail to confirm the data change"
        assert self.wait.until(EC.text_to_be_present_in_element(self.locators.CHECK_TEXT_2, text))

    @allure.step("Click done")
    def click_done_2(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.DONE_BUTTON_2)).click()

    @allure.step("Click clear phone number")
    def clear_phone_number(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.PHONE_NUMBER)).clear()

    @allure.step("Enter phone number")
    def enter_phone_number(self, phone_number):
        self.wait.until(EC.element_to_be_clickable(self.locators.PHONE_NUMBER)).send_keys(phone_number)

    @allure.step("Click save")
    def click_save_3(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.SAVE_BUTTON_3)).click()
        text = "Go to the mail to confirm the data change"
        assert self.wait.until(EC.text_to_be_present_in_element(self.locators.CHECK_TEXT_3, text))

    @allure.step("Click done")
    def click_done_3(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.DONE_BUTTON_3)).click()