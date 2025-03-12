import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.edit_profile_locators import EditProfileLocators

class ProfileEditPage(BasePage):

    PAGE_URL = Links.EDIT_PROFILE
    locators = EditProfileLocators()

    # CLEAR_FIRST_NAME = ("xpath", "(//span[@class='ant-input-clear-icon'])[1]")
    # FIRST_NAME_FIELD = ("xpath", "//input[@type='text']")
    # CHECKBOX = ("xpath", "//input[@type='checkbox']")
    # SAVE_BUTTON = ("xpath", "//button[@type='submit']")
    # DONE_BUTTON = ("xpath", "//button[text()='Done']")
    # CHECK_MESSAGE = ("xpath", "//h2[text()='Successfully']")

    @allure.step("Click clear name")
    def click_clear(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.CLEAR_FIRST_NAME)).click()

    def change_name(self, new_name):
        with allure.step(f"Change name on '{new_name}'"):
            self.wait.until(EC.element_to_be_clickable(self.locators.FIRST_NAME_FIELD)).send_keys(new_name)

    @allure.step("Click checkbox")
    def click_checkbox(self):
        #self.wait.until(EC.element_to_be_clickable(self.CHECKBOX)).click()
        checkbox = self.wait.until(EC.presence_of_element_located(self.locators.CHECKBOX))
        self.driver.execute_script("arguments[0].click();", checkbox)

    @allure.step("Save changes")
    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.SAVE_BUTTON)).click()

    @allure.step("Click Done")
    def click_done(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.DONE_BUTTON)).click()

    @allure.step("Check message")
    def check_message(self):
        successfully_text = "Successfully"
        return self.wait.until(EC.text_to_be_present_in_element(self.locators.CHECK_MESSAGE, successfully_text))

