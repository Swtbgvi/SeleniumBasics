class LoginPage2:
    def __init__ (self,driver):
        self.driver =driver
        self.us_locator ="j_username"
        self.paswd_locator ="j_password"
        self.submit ="Submit"

    def enter_userName(self):
        self.driver.find_element_by_id(self.us_locator).send_keys("admin")

    def enter_pwd(self):
        self.driver.find_element_by_name(self.paswd_locator).send_keys("manager")

    def signIn(self):
        self.driver.find_element_by_name(self.submit).click()
