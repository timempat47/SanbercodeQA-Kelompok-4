import unittest 
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from Object import data
import time
import tracemalloc

tracemalloc.start()

class inputan():
    valid_user = "jeffscott@gmail.com"
    valid_passw = "@Jeffscott12345@"
    email = "mynameisjeff@gmail.com"
    product1 = "Argus All-Weather Tank"
    product2 = "Breathe-Easy Tank"
    warna1 = "Gray"
    warna2 = "White"
    ukuran1 = "M"
    ukuran2 = "S"
    First_Name = "Iko"
    Last_Name = "Utomo"
    Company = "TimEmpat"
    StreetAddress_1 = "Villa Serpong Damai"
    StreetAddress_2 = "Blok D1/3"
    StreetAddress_3 = "Serpong"
    StreetAddress1_1 = "Villa Jombang Permai"
    StreetAddress1_2 = "Blok D2/4"
    StreetAddress1_3 = "Ciputat"
    City = "Tangerang Selatan"
    Province = "Banten"
    Province1 = "Alabama"
    Zip_Code_valid = "15411"
    Zip_Code_invalid = "POS-ABC"
    Country = "Indonesia"
    Country1 = "United States"
    Phone_Number = "0878787895"

class CheckoutMagento_1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.url = "https://magento.softwaretestingboard.com/"

    def test_1_proceed_to_checkout(self):
        driver = self.driver
        driver.get(self.url)
        data.test_product(driver, inputan.product1, inputan.ukuran1, inputan.warna1)
        time.sleep(2)
        data.test_product(driver, inputan.product2, inputan.ukuran1, inputan.warna2)
        time.sleep(2)
        driver.find_element(By.CLASS_NAME,"minicart-wrapper").click()
        time.sleep(3)
        driver.find_element(By.ID,"top-cart-btn-checkout").click()
        time.sleep(3)
        #validasi
        self.assertIn('/checkout/#shipping', driver.current_url)

    def test_2_isi_form_lengkap(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_2(driver)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        time.sleep(3)
        shipping.find_element(By.ID,"customer-email").send_keys(inputan.email)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//option[@data-title='"+inputan.Country+"']").click()
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='firstname']").send_keys(inputan.First_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='lastname']").send_keys(inputan.Last_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='company']").send_keys(inputan.Company)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[0]']").send_keys(inputan.StreetAddress_1)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[1]']").send_keys(inputan.StreetAddress_2)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[2]']").send_keys(inputan.StreetAddress_3)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='city']").send_keys(inputan.City)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='region']").send_keys(inputan.Province)
        time.sleep(2)
        shipping.find_element(By.XPATH,"//input[@name='postcode']").send_keys(inputan.Zip_Code_valid)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='telephone']").send_keys(inputan.Phone_Number)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//button[@data-role='opc-continue']").click()
        time.sleep(2)
        #validasi
        self.assertIn('/checkout/#payment', driver.current_url)

    def test_3_isi_form_login(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_2(driver)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        time.sleep(3)
        shipping.find_element(By.ID,"customer-email").send_keys(inputan.valid_user)
        time.sleep(4)
        shipping.find_element(By.ID,"customer-password").send_keys(inputan.valid_passw)
        time.sleep(4)
        shipping.find_element(By.XPATH,"//button[@data-action='checkout-method-login']").click()
        time.sleep(10)
        driver.find_element(By.XPATH,"//button[@data-role='opc-continue']").click()
        time.sleep(3)
        #validasi
        self.assertIn('/checkout/#payment', driver.current_url)

    def test_4_isi_form_tanpa_FirstName(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_1(driver)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        time.sleep(3)
        shipping.find_element(By.ID,"customer-email").send_keys(inputan.email)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//option[@data-title='"+inputan.Country+"']").click()
        time.sleep(3)
        #shipping.find_element(By.XPATH,"//input[@name='firstname']").send_keys(inputan.First_Name)
        #time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='lastname']").send_keys(inputan.Last_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='company']").send_keys(inputan.Company)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[0]']").send_keys(inputan.StreetAddress_1)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[1]']").send_keys(inputan.StreetAddress_2)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[2]']").send_keys(inputan.StreetAddress_3)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='city']").send_keys(inputan.City)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='region']").send_keys(inputan.Province)
        time.sleep(2)
        shipping.find_element(By.XPATH,"//input[@name='postcode']").send_keys(inputan.Zip_Code_valid)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='telephone']").send_keys(inputan.Phone_Number)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//button[@data-role='opc-continue']").click()
        time.sleep(3)
        #validasi
        response = driver.find_element(By.XPATH,"//span[@data-bind='text: element.error']").text
        self.assertIn('This is a required field.', response)

    def tearDown(self):
        self.driver.close()

class CheckoutMagento_2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.url = "https://magento.softwaretestingboard.com/"

    def test_5_isi_form_tanpa_LastName(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_1(driver)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        time.sleep(3)
        shipping.find_element(By.ID,"customer-email").send_keys(inputan.email)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//option[@data-title='"+inputan.Country+"']").click()
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='firstname']").send_keys(inputan.First_Name)
        time.sleep(1)
        #shipping.find_element(By.XPATH,"//input[@name='lastname']").send_keys(inputan.Last_Name)
        #time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='company']").send_keys(inputan.Company)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[0]']").send_keys(inputan.StreetAddress_1)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[1]']").send_keys(inputan.StreetAddress_2)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[2]']").send_keys(inputan.StreetAddress_3)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='city']").send_keys(inputan.City)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='region']").send_keys(inputan.Province)
        time.sleep(2)
        shipping.find_element(By.XPATH,"//input[@name='postcode']").send_keys(inputan.Zip_Code_valid)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='telephone']").send_keys(inputan.Phone_Number)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//button[@data-role='opc-continue']").click()
        time.sleep(3)
        #validasi
        response = driver.find_element(By.XPATH,"//span[@data-bind='text: element.error']").text
        self.assertIn('This is a required field.', response)
    
    def setUp(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.url = "https://magento.softwaretestingboard.com/"

    def test_6_isi_form_tanpa_Company(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_2(driver)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        time.sleep(3)
        shipping.find_element(By.ID,"customer-email").send_keys(inputan.email)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//option[@data-title='"+inputan.Country+"']").click()
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='firstname']").send_keys(inputan.First_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='lastname']").send_keys(inputan.Last_Name)
        time.sleep(1)
        #shipping.find_element(By.XPATH,"//input[@name='company']").send_keys(inputan.Company)
        #time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[0]']").send_keys(inputan.StreetAddress_1)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[1]']").send_keys(inputan.StreetAddress_2)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[2]']").send_keys(inputan.StreetAddress_3)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='city']").send_keys(inputan.City)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='region']").send_keys(inputan.Province)
        time.sleep(2)
        shipping.find_element(By.XPATH,"//input[@name='postcode']").send_keys(inputan.Zip_Code_valid)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='telephone']").send_keys(inputan.Phone_Number)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//button[@data-role='opc-continue']").click()
        time.sleep(3)
        #validasi
        self.assertIn('/checkout/#payment', driver.current_url)

    def test_7_isi_form_tanpa_Address1(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_1(driver)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        time.sleep(3)
        shipping.find_element(By.ID,"customer-email").send_keys(inputan.email)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//option[@data-title='"+inputan.Country+"']").click()
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='firstname']").send_keys(inputan.First_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='lastname']").send_keys(inputan.Last_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='company']").send_keys(inputan.Company)
        time.sleep(1)
        #shipping.find_element(By.XPATH,"//input[@name='street[0]']").send_keys(inputan.StreetAddress_1)
        #time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[1]']").send_keys(inputan.StreetAddress_2)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[2]']").send_keys(inputan.StreetAddress_3)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='city']").send_keys(inputan.City)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='region']").send_keys(inputan.Province)
        time.sleep(2)
        shipping.find_element(By.XPATH,"//input[@name='postcode']").send_keys(inputan.Zip_Code_valid)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='telephone']").send_keys(inputan.Phone_Number)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//button[@data-role='opc-continue']").click()
        time.sleep(3)
        #validasi
        response = driver.find_element(By.XPATH,"//span[@data-bind='text: element.error']").text
        self.assertIn('This is a required field.', response)

    def test_8_isi_form_tanpa_Address2(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_2(driver)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        time.sleep(3)
        shipping.find_element(By.ID,"customer-email").send_keys(inputan.email)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//option[@data-title='"+inputan.Country+"']").click()
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='firstname']").send_keys(inputan.First_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='lastname']").send_keys(inputan.Last_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='company']").send_keys(inputan.Company)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[0]']").send_keys(inputan.StreetAddress_1)
        time.sleep(1)
        #shipping.find_element(By.XPATH,"//input[@name='street[1]']").send_keys(inputan.StreetAddress_2)
        #time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[2]']").send_keys(inputan.StreetAddress_3)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='city']").send_keys(inputan.City)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='region']").send_keys(inputan.Province)
        time.sleep(2)
        shipping.find_element(By.XPATH,"//input[@name='postcode']").send_keys(inputan.Zip_Code_valid)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='telephone']").send_keys(inputan.Phone_Number)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//button[@data-role='opc-continue']").click()
        time.sleep(3)
        #validasi
        self.assertIn('/checkout/#payment', driver.current_url)

    def tearDown(self):
        self.driver.close()

class CheckoutMagento_3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.url = "https://magento.softwaretestingboard.com/"

    def test_9_isi_form_tanpa_Address3(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_2(driver)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        time.sleep(3)
        shipping.find_element(By.ID,"customer-email").send_keys(inputan.email)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//option[@data-title='"+inputan.Country+"']").click()
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='firstname']").send_keys(inputan.First_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='lastname']").send_keys(inputan.Last_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='company']").send_keys(inputan.Company)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[0]']").send_keys(inputan.StreetAddress_1)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[1]']").send_keys(inputan.StreetAddress_2)
        time.sleep(1)
        #shipping.find_element(By.XPATH,"//input[@name='street[2]']").send_keys(inputan.StreetAddress_3)
        #time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='city']").send_keys(inputan.City)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='region']").send_keys(inputan.Province)
        time.sleep(2)
        shipping.find_element(By.XPATH,"//input[@name='postcode']").send_keys(inputan.Zip_Code_valid)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='telephone']").send_keys(inputan.Phone_Number)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//button[@data-role='opc-continue']").click()
        time.sleep(3)
        #validasi
        self.assertIn('/checkout/#payment', driver.current_url)

    def test_10_isi_form_tanpa_City(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_1(driver)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        time.sleep(3)
        shipping.find_element(By.ID,"customer-email").send_keys(inputan.email)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//option[@data-title='"+inputan.Country+"']").click()
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='firstname']").send_keys(inputan.First_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='lastname']").send_keys(inputan.Last_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='company']").send_keys(inputan.Company)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[0]']").send_keys(inputan.StreetAddress_1)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[1]']").send_keys(inputan.StreetAddress_2)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[2]']").send_keys(inputan.StreetAddress_3)
        time.sleep(1)
        #shipping.find_element(By.XPATH,"//input[@name='city']").send_keys(inputan.City)
        #time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='region']").send_keys(inputan.Province)
        time.sleep(2)
        shipping.find_element(By.XPATH,"//input[@name='postcode']").send_keys(inputan.Zip_Code_valid)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='telephone']").send_keys(inputan.Phone_Number)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//button[@data-role='opc-continue']").click()
        time.sleep(3)
        #validasi
        response = driver.find_element(By.XPATH,"//span[@data-bind='text: element.error']").text
        self.assertIn('This is a required field.', response)

    def test_11_isi_form_tanpa_Province(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_2(driver)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        time.sleep(3)
        shipping.find_element(By.ID,"customer-email").send_keys(inputan.email)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//option[@data-title='"+inputan.Country+"']").click()
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='firstname']").send_keys(inputan.First_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='lastname']").send_keys(inputan.Last_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='company']").send_keys(inputan.Company)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[0]']").send_keys(inputan.StreetAddress_1)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[1]']").send_keys(inputan.StreetAddress_2)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[2]']").send_keys(inputan.StreetAddress_3)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='city']").send_keys(inputan.City)
        time.sleep(1)
        #shipping.find_element(By.XPATH,"//input[@name='region']").send_keys(inputan.Province)
        #time.sleep(2)
        shipping.find_element(By.XPATH,"//input[@name='postcode']").send_keys(inputan.Zip_Code_valid)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='telephone']").send_keys(inputan.Phone_Number)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//button[@data-role='opc-continue']").click()
        time.sleep(3)
        #validasi
        self.assertIn('/checkout/#payment', driver.current_url)

    def tearDown(self):
        self.driver.close()

class CheckoutMagento_4(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.url = "https://magento.softwaretestingboard.com/"

    def test_12_isi_form_tanpa_ZipCode(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_1(driver)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        time.sleep(3)
        shipping.find_element(By.ID,"customer-email").send_keys(inputan.email)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//option[@data-title='"+inputan.Country+"']").click()
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='firstname']").send_keys(inputan.First_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='lastname']").send_keys(inputan.Last_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='company']").send_keys(inputan.Company)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[0]']").send_keys(inputan.StreetAddress_1)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[1]']").send_keys(inputan.StreetAddress_2)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[2]']").send_keys(inputan.StreetAddress_3)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='city']").send_keys(inputan.City)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='region']").send_keys(inputan.Province)
        time.sleep(2)
        #shipping.find_element(By.XPATH,"//input[@name='postcode']").send_keys(inputan.Zip_Code_valid)
        #time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='telephone']").send_keys(inputan.Phone_Number)
        time.sleep(5)
        shipping.find_element(By.XPATH,"//button[@data-role='opc-continue']").click()
        time.sleep(3)
        #validasi
        response = driver.find_element(By.XPATH,"//span[@data-bind='text: element.error']").text
        self.assertIn('This is a required field.', response)

    def test_13_isi_form_invalid_ZipCode(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_1(driver)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        time.sleep(3)
        shipping.find_element(By.ID,"customer-email").send_keys(inputan.email)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//option[@data-title='"+inputan.Country+"']").click()
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='firstname']").send_keys(inputan.First_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='lastname']").send_keys(inputan.Last_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='company']").send_keys(inputan.Company)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[0]']").send_keys(inputan.StreetAddress_1)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[1]']").send_keys(inputan.StreetAddress_2)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[2]']").send_keys(inputan.StreetAddress_3)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='city']").send_keys(inputan.City)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='region']").send_keys(inputan.Province)
        time.sleep(2)
        shipping.find_element(By.XPATH,"//input[@name='postcode']").send_keys(inputan.Zip_Code_invalid)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='telephone']").send_keys(inputan.Phone_Number)
        time.sleep(1)
        #validasi
        response = driver.find_element(By.XPATH,"//div[@name='shippingAddress.postcode']/div/div/span").text
        self.assertIn('Provided Zip/Postal Code seems to be invalid.', response)

    def test_14_isi_form_tanpa_Country(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_1(driver)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        time.sleep(3)
        shipping.find_element(By.ID,"customer-email").send_keys(inputan.email)
        time.sleep(3)
        select_country = Select(driver.find_element(By.XPATH,"//select[@name='country_id']"))
        select_country.select_by_index(0)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='firstname']").send_keys(inputan.First_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='lastname']").send_keys(inputan.Last_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='company']").send_keys(inputan.Company)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[0]']").send_keys(inputan.StreetAddress_1)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[1]']").send_keys(inputan.StreetAddress_2)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[2]']").send_keys(inputan.StreetAddress_3)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='city']").send_keys(inputan.City)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='region']").send_keys(inputan.Province)
        time.sleep(2)
        shipping.find_element(By.XPATH,"//input[@name='postcode']").send_keys(inputan.Zip_Code_valid)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='telephone']").send_keys(inputan.Phone_Number)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//button[@data-role='opc-continue']").click()
        time.sleep(3)
        #validasi
        response = driver.find_element(By.XPATH,"//span[@data-bind='text: element.error']").text
        self.assertIn('This is a required field.', response)

    def test_15_isi_form_tanpa_PhoneNumber(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_1(driver)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        time.sleep(3)
        shipping.find_element(By.ID,"customer-email").send_keys(inputan.email)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//option[@data-title='"+inputan.Country+"']").click()
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='firstname']").send_keys(inputan.First_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='lastname']").send_keys(inputan.Last_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='company']").send_keys(inputan.Company)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[0]']").send_keys(inputan.StreetAddress_1)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[1]']").send_keys(inputan.StreetAddress_2)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[2]']").send_keys(inputan.StreetAddress_3)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='city']").send_keys(inputan.City)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='region']").send_keys(inputan.Province)
        time.sleep(2)
        shipping.find_element(By.XPATH,"//input[@name='postcode']").send_keys(inputan.Zip_Code_valid)
        time.sleep(6)
        #shipping.find_element(By.XPATH,"//input[@name='telephone']").send_keys(inputan.Phone_Number)
        #time.sleep(1)
        shipping.find_element(By.XPATH,"//button[@data-role='opc-continue']").click()
        time.sleep(3)
        #validasi
        response = driver.find_element(By.XPATH,"//span[@data-bind='text: element.error']").text
        self.assertIn('This is a required field.', response)
    
    def tearDown(self):
        self.driver.close()
    
class CheckoutMagento_5(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.url = "https://magento.softwaretestingboard.com/"

    def test_16_isi_form_ganti_Province_di_US(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_2(driver)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        time.sleep(3)
        shipping.find_element(By.ID,"customer-email").send_keys(inputan.email)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//option[@data-title='"+inputan.Country1+"']").click()
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='firstname']").send_keys(inputan.First_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='lastname']").send_keys(inputan.Last_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='company']").send_keys(inputan.Company)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[0]']").send_keys(inputan.StreetAddress_1)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[1]']").send_keys(inputan.StreetAddress_2)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[2]']").send_keys(inputan.StreetAddress_3)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='city']").send_keys(inputan.City)
        time.sleep(1)
        province_select = shipping.find_element(By.XPATH,"//select[@name='region_id']")
        province_select.find_element(By.XPATH,"//option[@data-title='"+inputan.Province1+"']").click()
        time.sleep(2)
        shipping.find_element(By.XPATH,"//input[@name='postcode']").send_keys(inputan.Zip_Code_valid)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='telephone']").send_keys(inputan.Phone_Number)
        time.sleep(3)
        #validasi
        province_select_name = shipping.find_element(By.XPATH,"//select[@name='region_id']").text
        self.assertIn(inputan.Province1, province_select_name)

    def test_17_isi_form_ganti_ShippingMethods(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_2(driver)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        time.sleep(3)
        shipping.find_element(By.ID,"customer-email").send_keys(inputan.email)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//option[@data-title='"+inputan.Country1+"']").click()
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='firstname']").send_keys(inputan.First_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='lastname']").send_keys(inputan.Last_Name)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='company']").send_keys(inputan.Company)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[0]']").send_keys(inputan.StreetAddress_1)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[1]']").send_keys(inputan.StreetAddress_2)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='street[2]']").send_keys(inputan.StreetAddress_3)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@name='city']").send_keys(inputan.City)
        time.sleep(1)
        province_select = shipping.find_element(By.XPATH,"//select[@name='region_id']")
        province_select.find_element(By.XPATH,"//option[@data-title='"+inputan.Province1+"']").click()
        time.sleep(2)
        shipping.find_element(By.XPATH,"//input[@name='postcode']").send_keys(inputan.Zip_Code_valid)
        time.sleep(3)
        shipping.find_element(By.XPATH,"//input[@name='telephone']").send_keys(inputan.Phone_Number)
        time.sleep(1)
        shipping.find_element(By.XPATH,"//input[@aria-labelledby='label_method_bestway_tablerate label_carrier_bestway_tablerate']").click()
        time.sleep(3)
        shipping.find_element(By.XPATH,"//button[@data-role='opc-continue']").click()
        time.sleep(3)
        #validasi
        self.assertIn('/checkout/#payment', driver.current_url)

    def test_18_tooltip_PhoneNumber(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_1(driver)
        time.sleep(5)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        shipping.find_element(By.XPATH,"//div[@name='shippingAddress.telephone']/div/div").click()
        time.sleep(3)

        #validasi
        response = driver.find_element(By.XPATH,"//div[@name='shippingAddress.telephone']/div/div/div").text
        self.assertIn('For delivery questions.', response)
    
    def test_19_order_summary(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_1(driver)
        time.sleep(3)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        shipping.find_element(By.XPATH,"//div[@class='block items-in-cart']").click()
        time.sleep(3)

        #validasi
        response = driver.find_element(By.XPATH,"//strong[@class='product-item-name']").text
        self.assertIn('Argus All-Weather Tank', response)

    def test_20_order_summary_details(self):
        driver = self.driver
        driver.get(self.url)
        data.test_checkout_1(driver)
        time.sleep(3)
        shipping = driver.find_element(By.ID,"checkout-step-shipping")
        shipping.find_element(By.XPATH,"//div[@class='block items-in-cart']").click()
        time.sleep(2)
        shipping.find_element(By.XPATH,"//div[@class='product options']").click()
        time.sleep(3)

        #validasi
        response = driver.find_element(By.XPATH,"//dd[@class='values']").text
        self.assertIn(inputan.ukuran1, response)

    def tearDown(self):
        self.driver.close()

class PaymentMagento(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.url = "https://magento.softwaretestingboard.com/"

    def test_21_place_order(self):
        driver = self.driver
        driver.get(self.url)
        data.test_isi_form(driver)
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@class='payment-method-content']/div[4]/div").click()
        time.sleep(9)
        #validasi
        self.assertIn("/checkout/onepage/success/", driver.current_url)
    
    def test_22_different_billing(self):
        driver = self.driver
        driver.get(self.url)
        data.test_isi_form(driver)
        driver.find_element(By.XPATH,"//div[@class='billing-address-same-as-shipping-block field choice']/input").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//li[@id='payment']//div[@name='billingAddresscheckmo.country_id']//option[@data-title='"+inputan.Country+"']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//div[@class='billing-address-form']/form/fieldset/div[1]/div/input").send_keys(inputan.First_Name)
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@class='billing-address-form']/form/fieldset/div[2]/div/input").send_keys(inputan.Last_Name)
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@class='billing-address-form']/form/fieldset/div[3]/div/input").send_keys(inputan.Company)
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@class='billing-address-form']/form/fieldset/fieldset/div/div[1]/div/input").send_keys(inputan.StreetAddress1_1)
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@class='billing-address-form']/form/fieldset/fieldset/div/div[2]/div/input").send_keys(inputan.StreetAddress1_2)
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@class='billing-address-form']/form/fieldset/fieldset/div/div[3]/div/input").send_keys(inputan.StreetAddress1_3)
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@class='billing-address-form']/form/fieldset/div[4]/div/input").send_keys(inputan.City)
        time.sleep(1)
        driver.find_element(By.XPATH,"//li[@id='payment']//div[@class='billing-address-form']/form/fieldset/div[6]/div/input").send_keys(inputan.Province)
        time.sleep(1)
        driver.find_element(By.XPATH,"//li[@id='payment']//div[@class='billing-address-form']/form/fieldset/div[7]/div/input").send_keys(inputan.Zip_Code_valid)
        time.sleep(3)
        driver.find_element(By.XPATH,"//li[@id='payment']//div[@class='billing-address-form']/form/fieldset/div[9]/div/input").send_keys(inputan.Phone_Number)
        time.sleep(3)
        driver.find_element(By.XPATH,"//div//button[@class='action action-update']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//div//button[@class='action primary checkout']").click()
        time.sleep(10)

        #validasi
        self.assertIn("/checkout/onepage/success/", driver.current_url)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()