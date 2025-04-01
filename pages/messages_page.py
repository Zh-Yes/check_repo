import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.messages_locators import MessagesLocators

class MessagesPage(BasePage):

    PAGE_URL = Links.MESSAGES_PAGE
    locators = MessagesLocators()

    @allure.step("Enter message")
    def enter_message(self, message):
        self.wait.until(EC.element_to_be_clickable(self.locators.ENTER_MESSAGE)).send_keys(message)

    @allure.step("Click send")
    def click_send(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.SEND_BUTTON)).click()

