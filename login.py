import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import HtmlTestRunner
from POM.Login_Page import LoginPage
from POM.Open_Web import OpenWeb

class MagentoLogin(unittest.TestCase):
    
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--log-level=3")  # Mengatur log level menjadi ERROR
        driver_service = Service(executable_path="C:/webdrivers/chromedriver")
        self.driver = webdriver.Chrome(service=driver_service, options=chrome_options)

    
    def test_login(self):
        OpenWeb.go_to_magento(self.driver)
        login_page = LoginPage(self.driver)
        test_data = 'test_login'
        login_page.login(
            LoginPage.test_data[test_data]['email'],
            LoginPage.test_data[test_data]['password']
        )
    def test_login_1(self):
        OpenWeb.go_to_magento(self.driver)
        login_page = LoginPage(self.driver)
        test_data = 'test_login_1'
        login_page.login(
            LoginPage.test_data[test_data]['email'],
            LoginPage.test_data[test_data]['password']
        )
   
    def test_login_2(self):
        OpenWeb.go_to_magento(self.driver)
        login_page = LoginPage(self.driver)
        test_data = 'test_login_2'
        login_page.login(
            LoginPage.test_data[test_data]['email'],
            LoginPage.test_data[test_data]['password']
        )

    
    def test_login_3(self):
        OpenWeb.go_to_magento(self.driver)
        login_page = LoginPage(self.driver)
        test_data = 'test_login_3'
        login_page.login(
            LoginPage.test_data[test_data]['email'],
            LoginPage.test_data[test_data]['password']
        )

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
