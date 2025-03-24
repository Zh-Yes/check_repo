import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.welcome_page_locators import WelcomePageLocators

class WelcomePage(BasePage):

    PAGE_URL = Links.WELCOME_PAGE
    locators = WelcomePageLocators()

    #Авторизация
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

    #Регистрация
    @allure.step("Click Get Started")
    def click_get_started(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.GET_STARTED_BUTTON)).click()

    def click_discover_more(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.DISCOVER_MORE_BUTTON)).click()

    def click_for_specialist(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.FOR_SPECIALIST)).click()

    def check_header_text(self):
        text_header = "Empower your independence, unleash your creativity!"
        return self.wait.until(EC.text_to_be_present_in_element(self.locators.TEXT1, text_header))

    def click_for_employer(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.FOR_EMPLOYER)).click()

    def check_header_text_2(self):
        text_header = "Find the best talent, get the job done"
        return self.wait.until(EC.text_to_be_present_in_element(self.locators.TEXT2, text_header))

    def click_faq(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.FAQ)).click()

    def click_first_faq(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.FIRST_FAQ)).click()

    def click_second_faq(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.SECOND_FAQ)).click()
