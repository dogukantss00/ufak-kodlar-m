from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


email="gmail"
password="password"
class Instagram:
    def __init__(self,email,password):
        self.browser=webdriver.Firefox()
        self.email=email
        self.password=password

    def signIn(self):
        self.browser.get("https://www.instagram.com")
        time.sleep(3)
        emailInput=self.browser.find_element_by_name("")
        passwordInput=self.browser.find_element_by_xpath("")

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

instagram=Instagram(email,password)
instagram.signIn()