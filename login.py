import unittest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 

class SigninMagento(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Drivers/chromedriver/chromedriver.exe")
    
    def test_login(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        el = driver.find_element(By.LINK_TEXT,"Sign In")
        el.click()
        email = driver.find_element(By.NAME,"login[username]")
        email.send_keys("jeffscott@gmail.com")
        password = driver.find_element(By.NAME,"login[password]")
        password.send_keys("@Jeffscott12345@")
        btnLogin = driver.find_element(By.NAME,"send")
        btnLogin.click()

    def test_login_1(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        el = driver.find_element(By.LINK_TEXT,"Sign In")
        el.click()
        email = driver.find_element(By.NAME,"login[username]")
        email.send_keys("jeffscott")
        password = driver.find_element(By.NAME,"login[password]")
        password.send_keys("@Jeffscott12345@")
        btnLogin = driver.find_element(By.NAME,"send")
        btnLogin.click()
    
    def test_login_2(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        el = driver.find_element(By.LINK_TEXT,"Sign In")
        el.click()
        email = driver.find_element(By.NAME,"login[username]")
        email.send_keys("jeffscott@gmail.com")
        password = driver.find_element(By.NAME,"login[password]")
        password.send_keys("1")
        btnLogin = driver.find_element(By.NAME,"send")
        btnLogin.click()
    
    def test_login_3(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        el = driver.find_element(By.LINK_TEXT,"Sign In")
        el.click()
        email = driver.find_element(By.NAME,"login[username]")
        email.send_keys()
        password = driver.find_element(By.NAME,"login[password]")
        password.send_keys()
        btnLogin = driver.find_element(By.NAME,"send")
        btnLogin.click()
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()