from selenium import webdriver

# driver = webdriver.(executable_path="C:\\Users\\ss035878\\Downloads\\geckodriver-v0.24.0-win64")
# driver.get("https://www.google.com/")

# driver = webdriver.Firefox(executable_path="C:\\Users\\ss035878\\Downloads\\geckodriver-v0.24.0-win64\\\\\\geckodriver.exe")
# driver.get("https://www.google.com/")

driver = webdriver.Ie(executable_path="C:\\Users\\ss035878\\Downloads\\IEDriverServer_x64_3.14.0\\IEDriverServer.exe")
driver.get("https://google.com")
