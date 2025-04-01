import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.payments_locators import PaymentsLocators
from faker import Faker

class PaymentsPage(BasePage):

    PAGE_URL = Links.PAYMENTS_PAGE
    locators = PaymentsLocators()

    @allure.step("Click Top up")
    def click_top_up(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.TOP_UP_BUTTON)).click()

    @allure.step("Enter amount")
    def enter_amount(self, amount):
        self.wait.until(EC.element_to_be_clickable(self.locators.AMOUNT_TOP_UP)).send_keys(amount)

    @allure.step("Click close")
    def click_close(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.CLOSE_BUTTON_1)).click()

    @allure.step("Click withdraw")
    def click_withdraw(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.WITHDRAW_BUTTON)).click()

    @allure.step("Enter amount withdraw")
    def enter_amount_withdraw(self, amount):
        self.wait.until(EC.element_to_be_clickable(self.locators.AMOUNT_WITHDRAW)).send_keys(amount)

    @allure.step("Click close")
    def click_close_2(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.CLOSE_BUTTON_2)).click()

    @allure.step("Click promo tab")
    def click_promo_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.PROMO_TAB)).click()

    @allure.step("Click Top Up & Withdraw tab")
    def click_top_up_withdraw_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.TOP_UP_WITHDRAW_TAB)).click()