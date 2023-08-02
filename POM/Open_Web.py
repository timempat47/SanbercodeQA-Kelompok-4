from selenium.webdriver.common.by import By
import time
class OpenWeb:
    @staticmethod
    def go_to_magento(driver):
        driver.get("https://magento.softwaretestingboard.com/")
        driver.maximize_window()
        time.sleep(5)
