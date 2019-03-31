from selenium import webdriver
from selenium.webdriver.support.select import Select # needed for select function
from selenium.webdriver.common.keys import Keys # needed for enter keyboard functions
import time

driver = webdriver.Chrome(executable_path="C:/python37/NewProjects/SeleniumBasics/chromedriver.exe")
driver.get("https://jqueryui.com/datepicker/#dropdown-month-year")
driver.maximize_window()

Ele =driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(Ele)
driver.find_element_by_xpath("//input[@id='datepicker']").click()

# To select the 7th date of august for ANY year
month_val = "7" #august
Year_val = "2009"
date_val = "15"

#case1 : By typing the date in the text field
driver.find_element_by_id('datepicker').send_keys(month_val+"/"+date_val+"/"+Year_val)
driver.find_element_by_id('datepicker').send_keys(Keys.ENTER)

#Clears the date field and tries the dynamic xpath method of dropdown
driver.implicitly_wait(10)
driver.find_element_by_id('datepicker').clear()
#switches back to iframe
driver.implicitly_wait(20)
driver.switch_to.default_content()
Ele=driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(Ele)
driver.find_element_by_id('datepicker').click()

#case2 : ***** dynamic xpath ******
#xpath got from coping the xpath direct;y =//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a[text()='3']

xp1= "//*[@id='ui-datepicker-div']/table/tbody/tr/td/a[text()="
xp2="'"
xp3="'"
xp4="]"
fxp = xp1+xp2+date_val+ xp3+xp4

month = driver.find_element_by_class_name("ui-datepicker-month")
sel_mon= Select(month)
sel_mon.select_by_value(month_val)

#time.sleep(5)
year = driver.find_element_by_class_name("ui-datepicker-year")
sel_year = Select(year)
sel_year.select_by_visible_text(Year_val)
driver.find_element_by_xpath(fxp).click()


#****to switch between frames ******

#driver.switch_to.default_content()
#driver.switch_to.parent_frame()
#driver.find_element_by_xpath("//a[text()='Draggable']").click()
