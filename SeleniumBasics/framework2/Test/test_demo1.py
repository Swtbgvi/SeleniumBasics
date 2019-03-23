#framework 2 using decorators

from selenium import webdriver
import time
import pytest
from framework2.Pages.LogOutPage import LogOutPage
from framework2.Pages.LoginPage import LoginPage2


@pytest.fixture(scope='session')
#fixture is used as a pre requisite to perform the further operation. placing the launching in login n logout ; scope ='session'
def test_launch_browser():
    global driver
    driver = webdriver.Chrome(executable_path='C:/python37/NewProjects/SeleniumBasics/framework2/driver/chromedriver.exe')
    driver.get("http://localhost:8080/login")
    driver.maximize_window()
    driver.implicitly_wait(20)

def test_login(test_launch_browser):
    Object = LoginPage2(driver)
    Object.enter_userName()
    Object.enter_pwd()
    Object.signIn()

def test_logout(test_launch_browser):
    time.sleep(10)
    Object2 = LogOutPage(driver)
    Object2.clickLogOut()
