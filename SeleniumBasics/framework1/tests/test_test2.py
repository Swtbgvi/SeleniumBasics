# Framework1 for running in pytest

from selenium import webdriver
import time

def test_launch_browser():
    global driver
    driver = webdriver.Chrome(executable_path="C:/python37/NewProjects/SeleniumBasics/loginException/chromedriver.exe")
    driver.get("http://localhost:8080/login")
    driver.maximize_window()
    driver.implicitly_wait(20)

def test_login():
    driver.find_element_by_id("j_username").send_keys("admin")
    driver.find_element_by_name("j_password").send_keys("manager")
    driver.find_element_by_name("Submit").click()
def test_logout():
    time.sleep(10)
    driver.find_element_by_xpath("//b[text()='log out']").click()
