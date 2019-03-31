# Framework1 using different classes ( login n logout classes from different pages)
#
from selenium import webdriver
import time
from framework1.Pages.LoginPage import Loginpage1 # import the file to use the class funtion
from framework1.Pages.LogoutPage import LogoutPage1

def launch_browser():
    global driver
    driver = webdriver.Chrome(executable_path="C:/python37/NewProjects/SeleniumBasics/loginException/chromedriver.exe")
    driver.get("http://localhost:8080/login")
    driver.maximize_window()
    driver.implicitly_wait(20)

def login():
    #driver.find_element_by_id("j_username").send_keys("admin")
    #driver.find_element_by_name("j_password").send_keys("manager")
    Lp=Loginpage1(driver)
    Lp.enter_username()
    Lp.enter_pwd()
    driver.find_element_by_name("Submit").click()
def logout():
    time.sleep(10)
    Lo =LogoutPage1(driver)
    Lo.clicklogout()
    #driver.find_element_by_xpath("//b[text()='log out']").click()

launch_browser()
login()
logout()