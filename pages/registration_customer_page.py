import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.registration_customer_locators import RegistrationCustomerLocators
from faker import Faker

class RegistrationCustomerPage(BasePage):

    PAGE_URL = Links.REGISTRATION_CUSTOMER
    locators = RegistrationCustomerLocators()

    @allure.step("Check text step")
    def check_text_step1(self):
        personalisation_text = "Introduce yourself"
        return self.wait.until(EC.text_to_be_present_in_element(self.locators.CHECK_TEXT_STEP1, personalisation_text))

    @allure.step("Enter first name")
    def enter_first_name(self, first_name):
        self.wait.until(EC.element_to_be_clickable(self.locators.FIRST_NAME_ENTER)).send_keys(first_name)

    @allure.step("Enter last name")
    def enter_last_name(self, last_name):
        self.wait.until(EC.element_to_be_clickable(self.locators.LAST_NAME_ENTER)).send_keys(last_name)

    @allure.step("Enter company name")
    def enter_company_name(self, company_name):
        self.wait.until(EC.element_to_be_clickable(self.locators.COMPANY_NAME)).send_keys(company_name)

    @allure.step("Click job title")
    def click_job_title(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.JOB_TITLE)).click()

    @allure.step("Select job title")
    def select_job_title(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.SELECT_JOB_TITLE)).click()

    @allure.step("Click country")
    def click_country(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.COUNTRY)).click()

    @allure.step("Select country")
    def select_country(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.SELECT_COUNTRY)).click()

    @allure.step("Enter city")
    def enter_city(self, city):
        self.wait.until(EC.element_to_be_clickable(self.locators.CITY)).send_keys(city)

    @allure.step("Select city")
    def select_city(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.SELECT_CITY)).click()

    @allure.step("Click next step")
    def click_next_step(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.NEXT_STEP_BUTTON)).click()

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.locators.PASSWORD_ENTER)).send_keys(password)

    @allure.step("Enter repeat password")
    def enter_repeat_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.locators.REPEAT_PASSWORD_ENTER)).send_keys(password)

    @allure.step("Enter email")
    def enter_email(self):
        fake = Faker()
        random_email = fake.email()
        self.wait.until(EC.element_to_be_clickable(self.locators.EMAIL)).send_keys(random_email)
        return random_email

    @allure.step("Enter phone number")
    def enter_phone_number(self, phone_number):
        self.wait.until(EC.element_to_be_clickable(self.locators.PHONE_NUMBER)).send_keys(phone_number)

    @allure.step("Click next step")
    def click_next_step2(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.NEXT_STEP_BUTTON2)).click()

    @allure.step("Enter cover letter")
    def enter_cover_letter(self, cover_letter):
        self.wait.until(EC.element_to_be_clickable(self.locators.COVER_LETTER)).send_keys(cover_letter)

    @allure.step("Enter social media links")
    def enter_soc_media_links1(self, soc_media1):
        self.wait.until(EC.element_to_be_clickable(self.locators.SOCIAL_MEDIA_LINKS1)).send_keys(soc_media1)

    @allure.step("Enter social media links")
    def enter_soc_media_links2(self, soc_media2):
        self.wait.until(EC.element_to_be_clickable(self.locators.SOCIAL_MEDIA_LINKS2)).send_keys(soc_media2)

    @allure.step("Enter social media links")
    def enter_soc_media_links3(self, soc_media3):
        self.wait.until(EC.element_to_be_clickable(self.locators.SOCIAL_MEDIA_LINKS3)).send_keys(soc_media3)

    @allure.step("Enter social media links")
    def enter_soc_media_links4(self, soc_media4):
        self.wait.until(EC.element_to_be_clickable(self.locators.SOCIAL_MEDIA_LINKS4)).send_keys(soc_media4)

    @allure.step("Enter social media links")
    def enter_soc_media_links5(self, soc_media5):
        self.wait.until(EC.element_to_be_clickable(self.locators.SOCIAL_MEDIA_LINKS5)).send_keys(soc_media5)

    @allure.step("Click checkbox")
    def click_checkbox(self):
        self.wait.until(EC.presence_of_element_located(self.locators.CHECKBOX_REGISTR_FINISH)).click()

    @allure.step("Click finish")
    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.FINISH_BUTTON)).click()



