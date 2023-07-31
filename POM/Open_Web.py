from selenium.webdriver.common.by import By

class OpenWeb:
    @staticmethod
    def go_to_register_page(driver):
        driver.get("https://magento.softwaretestingboard.com/")
        driver.maximize_window()
