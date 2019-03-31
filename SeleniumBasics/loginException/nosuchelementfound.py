from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/python37/NewProjects/SeleniumBasics/chromedriver.exe")
driver.get("file:///C:/python37/htmlPage.html")
driver.maximize_window()
#driver.implicitly_wait(30)
driver.find_element_by_class_name("user").send_keys("email@gmail.com")
driver.find_element_by_id("pwd").send_keys("password")
driver.find_element_by_id("login1").click()
#driver.find_element_by_xpath("//button[@id='login']").click()

#when the id in the webpage gest changed the error we get is : NoSuchElementException
val =driver.find_element_by_class_name("user").get_attribute("class")
print(val)

val1 = driver.find_element_by_class_name("user").text
print(val1)



