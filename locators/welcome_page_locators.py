

class WelcomePageLocators:

    #Авторизация
    BUTTON_LOG = ("xpath", "//button[contains(@class, 'Button')][1]")
    LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
    PASSWORD_FIELD = ("xpath", "//input[@id='login_password']")
    BUTTON_LOG_IN = ("xpath", "//button[@type='submit']")

    #Регистрация
    GET_STARTED_BUTTON = ("xpath", "//button[text()='Get started']")

    #Разделы в Welcome page
    DISCOVER_MORE_BUTTON = ("xpath", "(//button[text()='Discover more'])[1]")
    FOR_SPECIALIST = ("xpath", "//p[text()='For specialist']")
    TEXT1 = ("xpath", "//h1[text()='Empower your independence, unleash your creativity!']")
    FOR_EMPLOYER = ("xpath", "//p[text()='For employer']")
    TEXT2 = ("xpath", "//h1[text()='Find the best talent, get the job done']")
    FAQ = ("xpath", "//p[text()='FAQs']")
    FIRST_FAQ = ("xpath", "//p[text()='Are there any fees to post a job or bid for one?']")
    SECOND_FAQ = ("xpath", "//p[text()='Will booster.site provide work for me?']")