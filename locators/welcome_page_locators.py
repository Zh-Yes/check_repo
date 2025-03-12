

class WelcomePageLocators:

    #Авторизация
    BUTTON_LOG = ("xpath", "//button[contains(@class, 'Button')][1]")
    LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
    PASSWORD_FIELD = ("xpath", "//input[@id='login_password']")
    BUTTON_LOG_IN = ("xpath", "//button[@type='submit']")

    GET_STARTED_BUTTON = ("xpath", "//button[text()='Get started']")