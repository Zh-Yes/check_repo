

class RegistrationTypeLocators:

    #Customer
    SELECT_CUSTOMER_TYPE = ("xpath", "(//input[@class='ant-radio-input'])[1]")
    #Contractor
    SELECT_CONTRACTOR_TYPE = ("xpath", "(//input[@class='ant-radio-input'])[2]")

    CHECKBOX_REGISTR = ("xpath", "//input[@type='checkbox']")
    REGISTER_BUTTON = ("xpath", "//button[@type='button']")