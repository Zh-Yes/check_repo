import pytest
from config.data import Data
from pages.welcome_page import WelcomePage
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from pages.edit_profile_page import ProfileEditPage
from pages.registration_type_page import RegistrationTypePage
from pages.registration_customer_page import RegistrationCustomerPage
from pages.registration_contractor_page import RegistrationContractorPage
from pages.messages_page import MessagesPage
from pages.settings_page import SettingsPage
from pages.payments_page import PaymentsPage

#Расписываем для мультистраничного доступа в тестах
class BaseTest:

    data: Data

    welcome_page: WelcomePage
    home_page: HomePage
    profile_page: ProfilePage
    edit_profile_page: ProfileEditPage
    registration_type_page: RegistrationTypePage
    registration_customer_page: RegistrationCustomerPage
    registration_contractor_page: RegistrationContractorPage
    messages_page: MessagesPage
    settings_page: SettingsPage
    payments_page: PaymentsPage



    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.welcome_page = WelcomePage(driver)
        request.cls.home_page = HomePage(driver)
        request.cls.profile_page = ProfilePage(driver)
        request.cls.edit_profile_page = ProfileEditPage(driver)
        request.cls.registration_type_page = RegistrationTypePage(driver)
        request.cls.registration_customer_page = RegistrationCustomerPage(driver)
        request.cls.registration_contractor_page = RegistrationContractorPage(driver)
        request.cls.messages_page = MessagesPage(driver)
        request.cls.settings_page = SettingsPage(driver)
        request.cls.payments_page = PaymentsPage(driver)