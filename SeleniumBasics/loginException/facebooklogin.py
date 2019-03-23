from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
# driver.find_element_by_id("email").send_keys("kalia")
# driver.find_element_by_id("pass").send_keys("myy")
# driver.find_element_by_id("u_0_2").click()

#driver.find_element_by_xpath("//a[text()='Forgotten account?']").click()
#driver.find_element_by_xpath("//u[text()='Facebook']")
#driver.find_element_by_xpath("//input[@name='reg_email__']").send_keys("888888")
