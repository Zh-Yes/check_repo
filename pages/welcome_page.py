import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.welcome_page_locators import WelcomePageLocators

class WelcomePage(BasePage):

    PAGE_URL = Links.WELCOME_PAGE
    locators = WelcomePageLocators()

    #BUTTON_LOG = ("xpath", "//button[contains(@class, 'Button')][1]")
    #LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
    #PASSWORD_FIELD = ("xpath", "//input[@id='login_password']")
    #BUTTON_LOG_IN = ("xpath", "//button[@type='submit']")

    @allure.step("Click Log In")
    def click_log_in(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.BUTTON_LOG)).click()

    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.locators.LOGIN_FIELD)).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.locators.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click submit button")
    def press_log_in(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.BUTTON_LOG_IN)).click()

    @allure.step("Click Get Started")
    def click_get_started(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.GET_STARTED_BUTTON)).click()