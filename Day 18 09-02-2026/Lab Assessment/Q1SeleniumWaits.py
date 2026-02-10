
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Implicit Wait
driver.implicitly_wait(10)
print("Implicit wait set")

driver.get("https://www.selenium.dev/selenium/web/dynamic.html")

# load element
driver.find_element(By.ID, "adder").click()

# Explicit Wait
wait = WebDriverWait(driver, 15)
element = wait.until(
    EC.element_to_be_clickable((By.ID, "box0"))
)
print("Explicit wait: Element is clickable")

# Fluent Wait
fluent_wait = WebDriverWait(
    driver,
    timeout=20,
    poll_frequency=2,
    ignored_exceptions=[NoSuchElementException]
)

fluent_wait.until(
    EC.visibility_of_element_located((By.ID, "box0"))
)

print("Fluent wait: Element is available for interaction")

time.sleep(2)
driver.quit()
