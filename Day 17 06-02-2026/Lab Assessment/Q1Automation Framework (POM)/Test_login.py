
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# CONFIG SECTION
BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"
# BASE PAGE (Reusable Methods)
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def input_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.text
# LOGIN PAGE (POM)
class LoginPage(BasePage):

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    dashboard_heading = (By.XPATH, "//h6[text()='Dashboard']")

    def login(self, user, pwd):
        self.input_text(self.username, user)
        self.input_text(self.password, pwd)
        self.click(self.login_button)

    def verify_login_success(self):
        return self.get_text(self.dashboard_heading)

# PYTEST FIXTURE
@pytest.fixture
def setup():
    driver = webdriver.Edge()
    driver.get(BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()
# TEST CASE
def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)

    login_page.login(USERNAME, PASSWORD)

    assert login_page.verify_login_success() == "Dashboard"
