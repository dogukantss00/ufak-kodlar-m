from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

url="http://github.com"
driver.get(url)

searchInput = driver.find_element_by_name("")

time.sleep(2)
searchInput.send_keys("python")

time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)

result = driver.find_elements_by_css_selector("")
driver.close()

