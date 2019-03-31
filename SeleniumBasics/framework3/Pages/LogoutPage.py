class LogoutPage:
    def __init__(self,driver):
        self.driver = driver
        self.logout_locator = "//b[text()='log out']"

    def logout(self):
        self.driver.find_element_by_xpath(self.logout_locator).click()