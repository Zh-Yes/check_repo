

class EditProfileLocators:
    #Редактирование имени, чекбокс и сохранение
    CLEAR_FIRST_NAME = ("xpath", "(//span[@class='ant-input-clear-icon'])[1]")
    FIRST_NAME_FIELD = ("xpath", "//input[@type='text']")
    CHECKBOX = ("xpath", "//input[@type='checkbox']")
    SAVE_BUTTON = ("xpath", "//button[@type='submit']")
    DONE_BUTTON = ("xpath", "//button[text()='Done']")
    CHECK_MESSAGE = ("xpath", "//h2[text()='Successfully']")