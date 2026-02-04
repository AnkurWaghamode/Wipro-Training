from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Edge()
driver.get("https://www.amazon.com/")
driver.maximize_window()
print("title is",driver.title)
driver.implicitly_wait(5)
driver.get("https://www.facebook.com/")
print("title is",driver.title)
driver.back()
print("title after back",driver.title)
driver.forward()
print("title after forward",driver.title)
