import pytest
from selenium import webdriver
from framework3.TestData.data import *


@pytest.fixture(
    scope='class')  # ficture is used as a pre-requsite. anything written above yiled is pre and after yield is post req
def test_launch_browser(request):
    global driver
    driver = webdriver.Chrome(
        executable_path='C:/python37/NewProjects/SeleniumBasics/framework3/Driver/chromedriver.exe')
    driver.get(URL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield  # yield acts like a post- req action
    driver.quit()
