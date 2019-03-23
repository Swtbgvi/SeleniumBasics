from selenium import webdriver

driver = webdriver.Chrome()
driver.get(file:///C:/python37/myWebtable.html)
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='cric']/tbody/tr[3]/td[1]")
print(type)