from selenium import webdriver
qspider = webdriver.Chrome()
qspider.get("file:///C:/python37/htmlPage.html")
qspider.maximize_window()
qspider.implicitly_wait(30)
qspider.find_element_by_id("123").send_keys("admin")
qspider.find_element_by_id("456").send_keys("manager")
qspider.find_element_by_id("111").click()


