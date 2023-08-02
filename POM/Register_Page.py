from selenium.webdriver.common.by import By
import time

class RegisterPage:
    test_data = {
        "test_register": {
            "firstname": "Jef",
            "lastname": "Bernart",
            "email": "jefbernart@gmail.com",
            "password": "@Jefbernart12345@",
            "password_confirmation": "@Jefbernart12345@"
        },
        "test_register_1": {
            "firstname": "Alex",
            "lastname": "Grimaldo",
            "email": "jefbernart@gmail.com",
            "password": "@Jefbernart12345@",
            "password_confirmation": "@Jefbernart12345@"
        },
        "test_register_2": {
            "firstname": "Joshua",
            "lastname": "",
            "email": "joshuabernart@gmail.com",
            "password": "@Joshuabernart12345@",
            "password_confirmation": "@Joshuabernart12345@"
        },
        "test_register_3": {
            "firstname": "",
            "lastname": "Lalang",
            "email": "jefflalang@gmail.com",
            "password": "@Jefflalang12345@",
            "password_confirmation": "@Jefflalang12345@"
        },
        "test_register_4": {
            "firstname": "",
            "lastname": "",
            "email": "joshualalang@gmail.com",
            "password": "@Joshualalang12345@",
            "password_confirmation": "@Joshualalang12345@"
        },
        "test_register_5": {
            "firstname": "Jeff",
            "lastname": "Scott",
            "email": "jeffscott.com",
            "password": "@Jeffscott12345@",
            "password_confirmation": "@Jeffscott12345@"
        },
        "test_register_6": {
            "firstname": "Jeff",
            "lastname": "Scott",
            "email": "jeffscott@gmail.com",
            "password": "1",
            "password_confirmation": "@Jeffscott12345@"
        },
        "test_register_7": {
            "firstname": "Jeff",
            "lastname": "Scott",
            "email": "jeffscott@gmail.com",
            "password": "",
            "password_confirmation": "@Jeffscott12345@"
        },
        "test_register_8": {
            "firstname": "Jeff",
            "lastname": "Scott",
            "email": "jeffscott@gmail.com",
            "password": "",
            "password_confirmation": ""
        },
        "test_register_9": {
            "firstname": "Jeff",
            "lastname": "Scott",
            "email": "jeffscott@gmail.com",
            "password": "@Jeffscott12345@",
            "password_confirmation": ""
        },
        "test_register_10": {
            "firstname": "Jeff",
            "lastname": "Scott",
            "email": "",
            "password": "",
            "password_confirmation": ""
        },
        "test_register_11": {
            "firstname": "Jeff",
            "lastname": "Bernart",
            "email": "jeffbernart@gmail.com",
            "password": "@Jefbernart12345@",
            "password_confirmation": "@Jefbernart12345@"
        },                    
    }
    def __init__(self, driver):
        self.driver = driver


    def register_user(self, firstname, lastname, email, password, password_confirmation):
        self.driver.find_element(By.LINK_TEXT, "Create an Account").click()
        time.sleep(5)
        self.driver.find_element(By.NAME, "firstname").send_keys(firstname)
        time.sleep(5)
        self.driver.find_element(By.NAME, "lastname").send_keys(lastname)
        time.sleep(5)
        self.driver.find_element(By.NAME, "email").send_keys(email)
        time.sleep(5)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        time.sleep(5)
        self.driver.find_element(By.NAME, "password_confirmation").send_keys(password_confirmation)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@title='Create an Account']//span[contains(text(),'Create an Account')]").click()
        time.sleep(5)

    def get_register_message(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'page messages')]//div[contains(@class, 'message-success')]//div").text
