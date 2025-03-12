import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.profile_page_locators import ProfilePageLocators

class ProfilePage(BasePage):

    PAGE_URL = Links.PROFILE_PAGE
    locators = ProfilePageLocators()

    #EDIT_BUTTON = ("xpath", "//span[text()='Edit']")

    @allure.step("Click edit")
    def click_edit(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.EDIT_BUTTON)).click()