import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.home_page_locators import HomePageLocators

class HomePage(BasePage):

    PAGE_URL = Links.HOME_PAGE
    locators = HomePageLocators()

    #DROPDOWN_BUTTON = ("xpath", "//button[@class='ant-dropdown-trigger position-relative cursor-pointer']")
    #YOUR_PROFILE = ("xpath", "(//span[@class='ant-dropdown-menu-title-content'])[1]")

    @allure.step("Click menu")
    def click_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.DROPDOWN_BUTTON)).click()

    @allure.step("Click Your profile")
    def click_your_profile(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.YOUR_PROFILE)).click()