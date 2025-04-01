import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.registration_contractor_locators import RegistrationContractorLocators
from faker import Faker

class RegistrationContractorPage(BasePage):

    PAGE_URL = Links.REGISTRATION_CONTRACTOR
    locators = RegistrationContractorLocators()

    @allure.step("Enter first name")
    def enter_first_name(self, first_name):
        self.wait.until(EC.element_to_be_clickable(self.locators.FIRST_NAME_ENTER)).send_keys(first_name)

    @allure.step("Enter last name")
    def enter_last_name(self, last_name):
        self.wait.until(EC.element_to_be_clickable(self.locators.LAST_NAME_ENTER)).send_keys(last_name)

    @allure.step("Click main specialization")
    def click_main_specialization(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.MAIN_SPECIALIZATION_1)).click()

    @allure.step("Select specialization")
    def select_specialization(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.SELECT_SPECIALIZATION_1)).click()

    @allure.step("Enter years experience")
    def enter_years_experience(self, years_experience):
        self.wait.until(EC.element_to_be_clickable(self.locators.SPECIALIZATION_YEARS_EXPERIENCE)).send_keys(years_experience)

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

    @allure.step("Click add specialization")
    def click_add_specialization(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.ADD_SPECIALIZATION)).click()

    @allure.step("Click main specialization")
    def click_main_specialization_2(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.MAIN_SPECIALIZATION_2)).click()

    @allure.step("Select specialization")
    def select_specialization_2(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.SELECT_SPECIALIZATION_2)).click()

    @allure.step("Enter years experience")
    def enter_years_experience_2(self, years_experience):
        self.wait.until(EC.element_to_be_clickable(self.locators.SPECIALIZATION_YEARS_EXPERIENCE_2)).send_keys(years_experience)

    @allure.step("Click skills")
    def click_skills_1(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.SKILLS_1)).click()

    @allure.step("Select skills")
    def select_skills_1(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.SELECT_SKILLS_1)).click()

    @allure.step("Enter skills years experience")
    def enter_skills_years_exper_1(self, years):
        self.wait.until(EC.element_to_be_clickable(self.locators.SKILLS_YEARS_EXPERIENCE_1)).send_keys(years)

    @allure.step("Click skills")
    def click_skills_2(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.SKILLS_2)).click()

    @allure.step("Select skills")
    def select_skills_2(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.SELECT_SKILLS_2)).click()

    @allure.step("Enter skills years experience")
    def enter_skills_years_exper_2(self, years):
        self.wait.until(EC.element_to_be_clickable(self.locators.SKILLS_YEARS_EXPERIENCE_2)).send_keys(years)

    @allure.step("Click skills")
    def click_skills_3(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.SKILLS_3)).click()

    @allure.step("Select skills")
    def select_skills_3(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.SELECT_SKILLS_3)).click()

    @allure.step("Enter skills years experience")
    def enter_skills_years_exper_3(self, years):
        self.wait.until(EC.element_to_be_clickable(self.locators.SKILLS_YEARS_EXPERIENCE_3)).send_keys(years)

    @allure.step("Click language")
    def click_language(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.LANGUAGE)).click()

    @allure.step("Select language")
    def select_language(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.SELECT_LANGUAGE)).click()

    @allure.step("Click level")
    def click_level(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.LEVEL)).click()

    @allure.step("Select level")
    def select_level(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.SELECT_LEVEL)).click()

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
