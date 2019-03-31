from selenium import webdriver
# import the respective classes from Pages
from framework3.Pages.LoginPage import LoginPage
from framework3.Pages.LogoutPage import LogoutPage

# import the file test data
from framework3.TestData.data import *
import time
import pytest
import pytest_html


# request is used
@pytest.mark.usefixtures("test_launch_browser")
class TestLogin:
    def test_login(self):
        driver = self.driver
        obj = LoginPage(driver)
        obj.username()
        obj.Passwordfield()
        obj.Submit()


    def test_logout(self):
        driver = self.driver
        time.sleep(5)
        obj2 = LogoutPage(driver)
        obj2.logout()

# reports can be used using python -m pytest -v --html=reports/rep.html
