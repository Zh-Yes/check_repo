import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.registration_type_locators import RegistrationTypeLocators

class RegistrationTypePage(BasePage):

    PAGE_URL = Links.REGISTRATION_TYPE
    locators = RegistrationTypeLocators()

    @allure.step("Select Customer type")
    def select_customer_type(self):
        self.wait.until(EC.presence_of_element_located(self.locators.SELECT_CUSTOMER_TYPE)).click()

    @allure.step("Select Contractor type")
    def select_contractor_type(self):
        self.wait.until(EC.presence_of_element_located(self.locators.SELECT_CONTRACTOR_TYPE)).click()

    @allure.step("Click checkbox")
    def click_checkbox(self):
        self.wait.until(EC.presence_of_element_located(self.locators.CHECKBOX_REGISTR)).click()

    @allure.step("Click register")
    def click_register(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.REGISTER_BUTTON)).click()