from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://phptravels.com/")
driver.maximize_window()
driver.implicitly_wait(30)
cur_win_id= driver.current_window_handle
time.sleep(5)
driver.find_element_by_xpath("//span[text()='Login']").click()
mul_win = driver.window_handles
driver.refresh()
# print(mul_win)
# print(type(mul_win))
for id in mul_win:
    print(id)
    if(cur_win_id!= id):
        driver.switch_to.window(id)
        driver.find_element_by_id("inputEmail").send_keys("test")
        driver.find_element_by_id("inputPassword").send_keys("pass")
        driver.find_element_by_name("rememberme").click()
    # else:
    #     driver.switch_to.window(id)
    #     driver.find_element_by_link_text("https://phptravels.com/assets/img/quotation.svg")
driver.implicitly_wait(10)
#driver.close()
driver.close()



