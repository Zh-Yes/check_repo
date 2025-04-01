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
    @allure.step("Click portfolio")
    def click_portfolio(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.PORTFOLIO_TAB)).click()

    @allure.step("Click add portfolio")
    def click_add_portfolio(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.ADD_PORTFOLIO)).click()

    @allure.step("Enter project title")
    def enter_project_title(self, title):
        self.wait.until(EC.element_to_be_clickable(self.locators.PROJECT_TITLE)).send_keys(title)

    @allure.step("Enter project url")
    def enter_project_url(self, title_url):
        self.wait.until(EC.element_to_be_clickable(self.locators.PROJECT_URL)).send_keys(title_url)

    @allure.step("Enter description")
    def enter_description(self, description):
        self.wait.until(EC.element_to_be_clickable(self.locators.DESCRIPTION)).send_keys(description)

    @allure.step("Click save")
    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.SAVE_BUTTON)).click()

    @allure.step("Check text message")
    def check_message(self):
        successfully_text = "Successfully"
        return self.wait.until(EC.text_to_be_present_in_element(self.locators.CHECK_MESSAGE, successfully_text))

    @allure.step("Click done")
    def click_done(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.DONE_BUTTON)).click()

    #Customer
    @allure.step("Click orders")
    def click_orders(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.ORDERS_TAB)).click()

    #Общее
    @allure.step("Click reviews")
    def click_reviews(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.REVIEWS_TAB)).click()

    @allure.step("Click work")
    def click_work(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.WORK_TAB)).click()

