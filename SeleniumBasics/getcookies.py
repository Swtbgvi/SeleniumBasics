from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://pypi.org/")
time.sleep(5)
# print(driver.get_cookies(),'\n')
# expected = str(driver.get_cookies())
# if expected == driver.get_cookies():
#     print("Get cookies matched")
# else:
#     print("get cookies mismatched",'\n',expected)
# driver.close()
print(driver.get_window_size())
print(driver)


