

class ProfilePageLocators:

    #Кнопка Edit
    EDIT_BUTTON = ("xpath", "//span[text()='Edit']")

    #Contractor
    PORTFOLIO_TAB = ("xpath", "//div[text()='Portfolio']")
    ADD_PORTFOLIO = ("xpath", "//button[@class='PortfolioCard_emptyContainer__ypHSb']")
    UPLOAD_BUTTON = ("xpath", "//span[@class='ant-upload']")
    PROJECT_TITLE = ("xpath", "//input[@id='portfolio_project_title']")
    PROJECT_URL = ("xpath", "//input[@id='portfolio_project_url']")
    DESCRIPTION = ("xpath", "//textarea[@id='portfolio_project_description']")
    SAVE_BUTTON = ("xpath", "//button[text()='Save']")
    CHECK_MESSAGE = ("xpath", "//h2[text()='Successfully']")
    DONE_BUTTON = ("xpath", "//button[text()='Done']")
    REVIEWS_TAB = ("xpath", "//div[text()='Reviews']")
    WORK_TAB = ("xpath", "//div[text()='Work']")

    #Customer
    ORDERS_TAB = ("xpath", "//div[text()='Orders']")
