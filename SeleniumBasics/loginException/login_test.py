from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://pypi.org/")
time.sleep(5)
# driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[1]/div/div[1]/input*")
# driver.implicitly_wait(5)

driver.maximize_window()
print(driver.current_url)

expected_url = "https://pypi.org/"
if expected_url == driver.current_url:
    print ("The currect url matched ",driver.current_url)
else:
    print("the current url mismatched", expected_url)
driver.close()
#**********************************************88