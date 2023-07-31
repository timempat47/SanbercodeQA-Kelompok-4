import time
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    test_data = {
        "test_login": {
            "email": "jeffscott@gmail.com",
            "password": "@Jeffscott12345@"
        },
        "test_login_1": {
            "email": "jeffscott",
            "password": "@Jeffscott12345@"
        },
        "test_login_2": {
            "email": "jeffscott@gmail.com",
            "password": "1"
        },
        "test_login_3": {
            "email": "",
            "password": ""
        },
    }
    def login(self, email, password):
        driver = self.driver
        time.sleep(5)
        el = driver.find_element(By.LINK_TEXT, "Sign In")
        el.click()
        time.sleep(5)
        email_input = driver.find_element(By.NAME, "login[username]")
        email_input.send_keys(email)
        time.sleep(5)
        password_input = driver.find_element(By.NAME, "login[password]")
        password_input.send_keys(password)
        time.sleep(5)
        btn_login = driver.find_element(By.NAME, "send")
        btn_login.click()
        time.sleep(5)
