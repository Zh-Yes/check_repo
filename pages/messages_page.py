import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.messages_locators import MessagesLocators

class ProfileEditPage(BasePage):

    PAGE_URL = Links.EDIT_PROFILE
    locators = MessagesLocators()

