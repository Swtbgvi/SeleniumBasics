#framework 2 using decorators

from selenium import webdriver
import time
import  pytest

@pytest.fixture(scope='function')
#fixture is used as a pre requisite to perform the further operation. placing the launching in login n logout ; scope ='session'
def test_launch_browser():
    global driver
    driver = webdriver.Chrome(executable_path='C:/python37/NewProjects/SeleniumBasics/framework2/driver/chromedriver.exe')
    driver.get("http://localhost:8080/login")
    driver.maximize_window()
    driver.implicitly_wait(20)

def test_login(test_launch_browser):
    driver.find_element_by_id("j_username").send_keys("admin")
    driver.find_element_by_name("j_password").send_keys("manager")
    driver.find_element_by_name("Submit").click()

def test_logout(test_launch_browser):
    time.sleep(10)
    driver.find_element_by_xpath("//b[text()='log out']").click()


# to run use
#python -m pytest -v
#-m - module ; -v is vergos