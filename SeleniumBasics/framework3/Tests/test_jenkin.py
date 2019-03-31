from selenium import webdriver
# import the respective classes from Pages
from framework3.Pages.LoginPage import LoginPage
from framework3.Pages.LogoutPage import LogoutPage

# import the file test data
from framework3.TestData.data import *
import time
import pytest
import pytest_html


# fixture is used when we want it as a pre-requsite
# The data to such as the Url to open is imported from the Test data folder
# added a classmethod; methods when called individually need not have self; methods within a class needs self defined
class TestLogin:
    @pytest.fixture(
        scope='session')  # ficture is used as a pre-requsite. anything written above yiled is pre and after yield is post req
    def test_launch_browser1(self):
        global driver
        driver = webdriver.Chrome(
            executable_path='C:/python37/NewProjects/SeleniumBasics/framework3/Driver/chromedriver.exe')
        driver.get(URL)
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield  # yield acts like a post- req action
        driver.quit()

    # the Data to be typed in the fields are taken from the test data folder; the same is imported in the login pages
    def test_login(self, test_launch_browser1):
        obj = LoginPage(driver)
        obj.username()
        obj.Passwordfield()
        obj.Submit()

    def test_logout(self, test_launch_browser1):
        time.sleep(5)
        obj2 = LogoutPage(driver)
        obj2.logout()

# reports can be used using python -m pytest -v --html=reports/rep.html
