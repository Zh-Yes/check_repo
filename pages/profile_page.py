import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.profile_page_locators import ProfilePageLocators

class ProfilePage(BasePage):

    PAGE_URL = Links.PROFILE_PAGE
    locators = ProfilePageLocators()

    @allure.step("Click edit")
    def click_edit(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.EDIT_BUTTON)).click()

    #Contractor
    def click_portfolio(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.PORTFOLIO_TAB)).click()

    def click_add_portfolio(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.ADD_PORTFOLIO)).click()

    def enter_project_title(self, title):
        self.wait.until(EC.element_to_be_clickable(self.locators.PROJECT_TITLE)).send_keys(title)

    def enter_project_url(self, title_url):
        self.wait.until(EC.element_to_be_clickable(self.locators.PROJECT_URL)).send_keys(title_url)

    def enter_description(self, description):
        self.wait.until(EC.element_to_be_clickable(self.locators.DESCRIPTION)).send_keys(description)

    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.SAVE_BUTTON)).click()

    def check_message(self):
        successfully_text = "Successfully"
        return self.wait.until(EC.text_to_be_present_in_element(self.locators.CHECK_MESSAGE, successfully_text))

    def click_done(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.DONE_BUTTON)).click()

    #Customer
    def click_orders(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.ORDERS_TAB)).click()

    #Общее
    def click_reviews(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.REVIEWS_TAB)).click()

    def click_work(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.WORK_TAB)).click()

