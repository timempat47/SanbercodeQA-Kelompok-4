import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import HtmlTestRunner
from POM.Login_Page import LoginPage
from POM.Open_Web import OpenWeb
from POM.AddToCart_Page import AddToCartPage

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--log-level=3")  # Set log level to ERROR
        driver_service = Service(executable_path="C:/webdrivers/chromedriver")
        self.driver = webdriver.Chrome(service=driver_service, options=chrome_options)

    def test_add_single_product_to_cart(self):
        OpenWeb.go_to_register_page(self.driver)
        login_page = LoginPage(self.driver)
        test_data = 'test_login'
        login_page.login(
            LoginPage.test_data[test_data]['email'],
            LoginPage.test_data[test_data]['password']
        )        
        add_to_cart_page = AddToCartPage(self.driver)
        add_to_cart_page.add_to_cart(product_index=2, size_index=168, color_index=59, quantity='1')
        add_to_cart_page.verify_success_message()

    def test_add_multiple_products_to_cart(self):
        OpenWeb.go_to_register_page(self.driver)
        login_page = LoginPage(self.driver)
        test_data = 'test_login'
        login_page.login(
            LoginPage.test_data[test_data]['email'],
            LoginPage.test_data[test_data]['password']
        )        
        add_to_cart_page = AddToCartPage(self.driver)
        add_to_cart_page.add_to_cart(product_index=2, size_index=168, color_index=59, quantity='1')
        add_to_cart_page.verify_success_message()
        OpenWeb.go_to_register_page(self.driver)
        add_to_cart_page = AddToCartPage(self.driver)
        add_to_cart_page.add_to_cart(product_index=3, size_index=168, color_index=52, quantity='1')
        add_to_cart_page.verify_success_message()

    def test_add_product_with_large_quantity(self):
        OpenWeb.go_to_register_page(self.driver)
        login_page = LoginPage(self.driver)
        test_data = 'test_login'
        login_page.login(
            LoginPage.test_data[test_data]['email'],
            LoginPage.test_data[test_data]['password']
        )
        add_to_cart_page = AddToCartPage(self.driver)
        add_to_cart_page.add_to_cart(product_index=2, size_index=168, color_index=59, quantity='100000')
        add_to_cart_page.verify_error_message_maximum()        

    def test_add_product_with_zero_quantity(self):
        OpenWeb.go_to_register_page(self.driver)
        login_page = LoginPage(self.driver)
        test_data = 'test_login'
        login_page.login(
            LoginPage.test_data[test_data]['email'],
            LoginPage.test_data[test_data]['password']
        )
        add_to_cart_page = AddToCartPage(self.driver)
        add_to_cart_page.add_to_cart(product_index=2, size_index=168, color_index=59, quantity='0')
        add_to_cart_page.verify_error_message_zero()   

    def test_add_product_to_cart_from_different_pages(self):
        OpenWeb.go_to_register_page(self.driver)
        login_page = LoginPage(self.driver)
        test_data = 'test_login'
        login_page.login(
            LoginPage.test_data[test_data]['email'],
            LoginPage.test_data[test_data]['password']
        )
        addCategory = AddToCartPage(self.driver)
        addCategory.category_product(category_index=4,sub_category_index=9,sub_sub_category_index=11)
        add_to_cart_page = AddToCartPage(self.driver)
        add_to_cart_page.add_to_cart_on_category(product_index=2, size_index=168, color_index=57, quantity='1')
        add_to_cart_page.verify_success_message()

        addCategory = AddToCartPage(self.driver)
        addCategory.category_product(category_index=5,sub_category_index=17,sub_sub_category_index=19)
        add_to_cart_page = AddToCartPage(self.driver)
        add_to_cart_page.add_to_cart_on_category(product_index=1, size_index=168, color_index=50, quantity='1')
        add_to_cart_page.verify_success_message()         

    def test_add_product_with_category_filter(self):
        OpenWeb.go_to_register_page(self.driver)
        login_page = LoginPage(self.driver)
        test_data = 'test_login'
        login_page.login(
            LoginPage.test_data[test_data]['email'],
            LoginPage.test_data[test_data]['password']
        )
        addCategory = AddToCartPage(self.driver)
        addCategory.category_product(category_index=5,sub_category_index=17,sub_sub_category_index=19)
        driver = self.driver
        filter_size = driver.find_element(By.XPATH, '//*[@id="narrow-by-list"]/div[2]/div[1]')
        filter_size.click()
        time.sleep(5)
        input_size = driver.find_element(By.XPATH, '//*[@id="narrow-by-list"]/div[2]/div[2]/div/div/a[3]/div')
        input_size.click()
        time.sleep(5)
        filter_color = driver.find_element(By.XPATH, '//*[@id="narrow-by-list"]/div[3]/div[1]')
        filter_color.click()
        time.sleep(5)
        input_color = driver.find_element(By.XPATH, '//*[@id="narrow-by-list"]/div[3]/div[2]/div/div/a[1]/div')
        input_color.click()
        time.sleep(5)
        add_to_cart_page = AddToCartPage(self.driver)
        add_to_cart_page.add_to_cart_on_category(product_index=1, size_index=168, color_index=50, quantity='1')
        add_to_cart_page.verify_success_message()         


    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
