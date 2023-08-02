import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import HtmlTestRunner
from POM.Register_Page import RegisterPage
from POM.Open_Web import OpenWeb

class MagentoRegister(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--log-level=3")  # Mengatur log level menjadi ERROR
        driver_service = Service(executable_path="C:/webdrivers/chromedriver")
        self.driver = webdriver.Chrome(service=driver_service, options=chrome_options)

    
    def test_register(self):
        OpenWeb.go_to_magento(self.driver)
        test_data = 'test_register'
        register_page = RegisterPage(self.driver)
        register_page.register_user(
            register_page.test_data[test_data]["firstname"],
            register_page.test_data[test_data]["lastname"],
            register_page.test_data[test_data]["email"],
            register_page.test_data[test_data]["password"],
            register_page.test_data[test_data]["password_confirmation"]
        )

    def test_register_1(self):
        OpenWeb.go_to_magento(self.driver)
        test_data = 'test_register_1'
        register_page = RegisterPage(self.driver)
        register_page.register_user(
            register_page.test_data[test_data]["firstname"],
            register_page.test_data[test_data]["lastname"],
            register_page.test_data[test_data]["email"],
            register_page.test_data[test_data]["password"],
            register_page.test_data[test_data]["password_confirmation"]
        )
    
    def test_register_2(self):
        OpenWeb.go_to_magento(self.driver)
        test_data = 'test_register_2'
        register_page = RegisterPage(self.driver)
        register_page.register_user(
            register_page.test_data[test_data]["firstname"],
            register_page.test_data[test_data]["lastname"],
            register_page.test_data[test_data]["email"],
            register_page.test_data[test_data]["password"],
            register_page.test_data[test_data]["password_confirmation"]
        )
    
    def test_register_3(self):
        OpenWeb.go_to_magento(self.driver)
        test_data = 'test_register_3'
        register_page = RegisterPage(self.driver)
        register_page.register_user(
            register_page.test_data[test_data]["firstname"],
            register_page.test_data[test_data]["lastname"],
            register_page.test_data[test_data]["email"],
            register_page.test_data[test_data]["password"],
            register_page.test_data[test_data]["password_confirmation"]
        )
    
    def test_register_4(self):
        OpenWeb.go_to_magento(self.driver)
        test_data = 'test_register_4'
        register_page = RegisterPage(self.driver)
        register_page.register_user(
            register_page.test_data[test_data]["firstname"],
            register_page.test_data[test_data]["lastname"],
            register_page.test_data[test_data]["email"],
            register_page.test_data[test_data]["password"],
            register_page.test_data[test_data]["password_confirmation"]
        )
    
    def test_register_5(self):
        OpenWeb.go_to_magento(self.driver)
        test_data = 'test_register_5'
        register_page = RegisterPage(self.driver)
        register_page.register_user(
            register_page.test_data[test_data]["firstname"],
            register_page.test_data[test_data]["lastname"],
            register_page.test_data[test_data]["email"],
            register_page.test_data[test_data]["password"],
            register_page.test_data[test_data]["password_confirmation"]
        )
    
    def test_register_6(self):
        OpenWeb.go_to_magento(self.driver)
        test_data = 'test_register_6'
        register_page = RegisterPage(self.driver)
        register_page.register_user(
            register_page.test_data[test_data]["firstname"],
            register_page.test_data[test_data]["lastname"],
            register_page.test_data[test_data]["email"],
            register_page.test_data[test_data]["password"],
            register_page.test_data[test_data]["password_confirmation"]
        )
    
    def test_register_7(self):
        OpenWeb.go_to_magento(self.driver)
        test_data = 'test_register_7'
        register_page = RegisterPage(self.driver)
        register_page.register_user(
            register_page.test_data[test_data]["firstname"],
            register_page.test_data[test_data]["lastname"],
            register_page.test_data[test_data]["email"],
            register_page.test_data[test_data]["password"],
            register_page.test_data[test_data]["password_confirmation"]
        )
    
    def test_register_8(self):
        OpenWeb.go_to_magento(self.driver)
        test_data = 'test_register_8'
        register_page = RegisterPage(self.driver)
        register_page.register_user(
            register_page.test_data[test_data]["firstname"],
            register_page.test_data[test_data]["lastname"],
            register_page.test_data[test_data]["email"],
            register_page.test_data[test_data]["password"],
            register_page.test_data[test_data]["password_confirmation"]
        )
    
    def test_register_9(self):
        OpenWeb.go_to_magento(self.driver)
        test_data = 'test_register_9'
        register_page = RegisterPage(self.driver)
        register_page.register_user(
            register_page.test_data[test_data]["firstname"],
            register_page.test_data[test_data]["lastname"],
            register_page.test_data[test_data]["email"],
            register_page.test_data[test_data]["password"],
            register_page.test_data[test_data]["password_confirmation"]
        )
    
    def test_register_10(self):
        OpenWeb.go_to_magento(self.driver)
        test_data = 'test_register_10'
        register_page = RegisterPage(self.driver)
        register_page.register_user(
            register_page.test_data[test_data]["firstname"],
            register_page.test_data[test_data]["lastname"],
            register_page.test_data[test_data]["email"],
            register_page.test_data[test_data]["password"],
            register_page.test_data[test_data]["password_confirmation"]
        )
    def test_register_11(self):
        OpenWeb.go_to_magento(self.driver)
        test_data = 'test_register_11'
        register_page = RegisterPage(self.driver)
        register_page.register_user(
            register_page.test_data[test_data]["firstname"],
            register_page.test_data[test_data]["lastname"],
            register_page.test_data[test_data]["email"],
            register_page.test_data[test_data]["password"],
            register_page.test_data[test_data]["password_confirmation"]
        )

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))