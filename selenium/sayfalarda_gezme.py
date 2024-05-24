# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 14:21:39 2023

@author: DOĞUKAN TAŞ
"""

from selenium import webdriver
import time

#istenen tarayıcı import edilir
driver = webdriver.Firefox()

#gidilecek url yazılır
url="http://github.com"

#url ye götürür
driver.get(url)

#2 saniye bekletir
time.sleep(2)

#tam ekran yapar sayfayı
driver.maximize_window()

#ekran görüntüsü alır
driver.save_screenshot("github.png")
#terminale sayfanın başlıgını yazdırır
print(driver.title)

#sayfayı geri alır
driver.back()

#sonraki sayfaya geçer
driver.forward()
time.sleep(2)
#sayfayı kapatır
driver.close()
