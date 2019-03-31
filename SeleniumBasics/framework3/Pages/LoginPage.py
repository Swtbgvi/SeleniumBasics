from framework3.TestData.data import *


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_locator = "j_username"
        self.passwd_locator = "j_password"
        self.submit = "Submit"

    # the send_keys has the constants that are defied from the test data folder
    def username(self):
        self.driver.find_element_by_id(self.user_locator).send_keys(UN)

    def Passwordfield(self):
        self.driver.find_element_by_name(self.passwd_locator).send_keys(PWD)

    def Submit(self):
        self.driver.find_element_by_name(self.submit).click()
