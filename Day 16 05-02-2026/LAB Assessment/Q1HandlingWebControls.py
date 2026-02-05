from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("file:///C:/Users/User/Desktop/practice_form.html")

# 1. Fill text boxes
driver.find_element(By.ID, "firstName").send_keys("Ankur")
driver.find_element(By.ID, "lastName").send_keys("Waghmode")
driver.find_element(By.ID, "email").send_keys("ankur@test.com")

# 2. Radio button & checkbox
driver.find_element(By.ID, "male").click()
driver.find_element(By.ID, "sports").click()

# 3. Dropdown using Select class
country_dropdown = Select(driver.find_element(By.ID, "country"))
country_dropdown.select_by_visible_text("India")

# 4. Submit form
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(1)

# Verify confirmation message
msg = driver.find_element(By.ID, "message").text
assert "Form submitted successfully!" in msg

print("Test Passed ✔")

driver.quit()
