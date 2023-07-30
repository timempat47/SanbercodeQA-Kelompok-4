import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class MagentoLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Drivers/chromedriver/chromedriver.exe")
    
    def test_register(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        el = driver.find_element(By.LINK_TEXT,"Create an Account")
        el.click()
        firstName = driver.find_element(By.NAME,"firstname")
        firstName.send_keys("Jeff")
        lastName = driver.find_element(By.NAME,"lastname")
        lastName.send_keys("Scott")
        email = driver.find_element(By.NAME,"email")
        email.send_keys("jeffscott@gmail.com")
        password = driver.find_element(By.NAME,"password")
        password.send_keys("@Jeffscott12345@")
        passConfirmation = driver.find_element(By.NAME,"password_confirmation")
        passConfirmation.send_keys("@Jeffscott12345@")
        btnsignUp = driver.find_element(By.XPATH,"//button[@title='Create an Account']//span[contains(text(),'Create an Account')]")
        btnsignUp.click()

    def test_register_1(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        el = driver.find_element(By.LINK_TEXT,"Create an Account")
        el.click()
        firstName = driver.find_element(By.NAME,"firstname")
        firstName.send_keys("Alex")
        lastName = driver.find_element(By.NAME,"lastname")
        lastName.send_keys("Grimaldo")
        email = driver.find_element(By.NAME,"email")
        email.send_keys("jeffscott@gmail.com")
        password = driver.find_element(By.NAME,"password")
        password.send_keys("@Jeffscott12345@")
        passConfirmation = driver.find_element(By.NAME,"password_confirmation")
        passConfirmation.send_keys("@Jeffscott12345@")
        btnsignUp = driver.find_element(By.XPATH,"//button[@title='Create an Account']//span[contains(text(),'Create an Account')]")
        btnsignUp.click()
    
    def test_register_2(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        el = driver.find_element(By.LINK_TEXT,"Create an Account")
        el.click()
        firstName = driver.find_element(By.NAME,"firstname")
        firstName.send_keys("Jeff")
        lastName = driver.find_element(By.NAME,"lastname")
        lastName.send_keys()
        email = driver.find_element(By.NAME,"email")
        email.send_keys("jeffscott@gmail.com")
        password = driver.find_element(By.NAME,"password")
        password.send_keys("@Jeffscott12345@")
        passConfirmation = driver.find_element(By.NAME,"password_confirmation")
        passConfirmation.send_keys("@Jeffscott12345@")
        btnsignUp = driver.find_element(By.XPATH,"//button[@title='Create an Account']//span[contains(text(),'Create an Account')]")
        btnsignUp.click()
    
    def test_register_3(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        el = driver.find_element(By.LINK_TEXT,"Create an Account")
        el.click()
        firstName = driver.find_element(By.NAME,"firstname")
        firstName.send_keys()
        lastName = driver.find_element(By.NAME,"lastname")
        lastName.send_keys("Scott")
        email = driver.find_element(By.NAME,"email")
        email.send_keys("jeffscott@gmail.com")
        password = driver.find_element(By.NAME,"password")
        password.send_keys("@Jeffscott12345@")
        passConfirmation = driver.find_element(By.NAME,"password_confirmation")
        passConfirmation.send_keys("@Jeffscott12345@")
        btnsignUp = driver.find_element(By.XPATH,"//button[@title='Create an Account']//span[contains(text(),'Create an Account')]")
        btnsignUp.click()
    
    def test_register_4(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        el = driver.find_element(By.LINK_TEXT,"Create an Account")
        el.click()
        firstName = driver.find_element(By.NAME,"firstname")
        firstName.send_keys()
        lastName = driver.find_element(By.NAME,"lastname")
        lastName.send_keys()
        email = driver.find_element(By.NAME,"email")
        email.send_keys("jeffscott@gmail.com")
        password = driver.find_element(By.NAME,"password")
        password.send_keys("@Jeffscott12345@")
        passConfirmation = driver.find_element(By.NAME,"password_confirmation")
        passConfirmation.send_keys("@Jeffscott12345@")
        btnsignUp = driver.find_element(By.XPATH,"//button[@title='Create an Account']//span[contains(text(),'Create an Account')]")
        btnsignUp.click()
    
    def test_register_5(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        el = driver.find_element(By.LINK_TEXT,"Create an Account")
        el.click()
        firstName = driver.find_element(By.NAME,"firstname")
        firstName.send_keys("Jeff")
        lastName = driver.find_element(By.NAME,"lastname")
        lastName.send_keys("Scott")
        email = driver.find_element(By.NAME,"email")
        email.send_keys("jeffscott.com")
        password = driver.find_element(By.NAME,"password")
        password.send_keys("@Jeffscott12345@")
        passConfirmation = driver.find_element(By.NAME,"password_confirmation")
        passConfirmation.send_keys("@Jeffscott12345@")
        btnsignUp = driver.find_element(By.XPATH,"//button[@title='Create an Account']//span[contains(text(),'Create an Account')]")
        btnsignUp.click()
    
    def test_register_6(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        el = driver.find_element(By.LINK_TEXT,"Create an Account")
        el.click()
        firstName = driver.find_element(By.NAME,"firstname")
        firstName.send_keys("Jeff")
        lastName = driver.find_element(By.NAME,"lastname")
        lastName.send_keys("Scott")
        email = driver.find_element(By.NAME,"email")
        email.send_keys("jeffscott@gmail.com")
        password = driver.find_element(By.NAME,"password")
        password.send_keys("1")
        passConfirmation = driver.find_element(By.NAME,"password_confirmation")
        passConfirmation.send_keys("@Jeffscott12345@")
        btnsignUp = driver.find_element(By.XPATH,"//button[@title='Create an Account']//span[contains(text(),'Create an Account')]")
        btnsignUp.click()
    
    def test_register_7(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        el = driver.find_element(By.LINK_TEXT,"Create an Account")
        el.click()
        firstName = driver.find_element(By.NAME,"firstname")
        firstName.send_keys("Jeff")
        lastName = driver.find_element(By.NAME,"lastname")
        lastName.send_keys("Scott")
        email = driver.find_element(By.NAME,"email")
        email.send_keys("jeffscott@gmail.com")
        password = driver.find_element(By.NAME,"password")
        password.send_keys()
        passConfirmation = driver.find_element(By.NAME,"password_confirmation")
        passConfirmation.send_keys("@Jeffscott12345@")
        btnsignUp = driver.find_element(By.XPATH,"//button[@title='Create an Account']//span[contains(text(),'Create an Account')]")
        btnsignUp.click()
    
    def test_register_8(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        el = driver.find_element(By.LINK_TEXT,"Create an Account")
        el.click()
        firstName = driver.find_element(By.NAME,"firstname")
        firstName.send_keys("Jeff")
        lastName = driver.find_element(By.NAME,"lastname")
        lastName.send_keys("Scott")
        email = driver.find_element(By.NAME,"email")
        email.send_keys("jeffscott@gmail.com")
        password = driver.find_element(By.NAME,"password")
        password.send_keys()
        passConfirmation = driver.find_element(By.NAME,"password_confirmation")
        passConfirmation.send_keys("@Jeffscott12345@")
        btnsignUp = driver.find_element(By.XPATH,"//button[@title='Create an Account']//span[contains(text(),'Create an Account')]")
        btnsignUp.click()
    
    def test_register_9(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        el = driver.find_element(By.LINK_TEXT,"Create an Account")
        el.click()
        firstName = driver.find_element(By.NAME,"firstname")
        firstName.send_keys("Jeff")
        lastName = driver.find_element(By.NAME,"lastname")
        lastName.send_keys("Scott")
        email = driver.find_element(By.NAME,"email")
        email.send_keys("jeffscott@gmail.com")
        password = driver.find_element(By.NAME,"password")
        password.send_keys("@Jeffscott12345@")
        passConfirmation = driver.find_element(By.NAME,"password_confirmation")
        passConfirmation.send_keys()
        btnsignUp = driver.find_element(By.XPATH,"//button[@title='Create an Account']//span[contains(text(),'Create an Account')]")
        btnsignUp.click()
    
    def test_register_10(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        el = driver.find_element(By.LINK_TEXT,"Create an Account")
        el.click()
        firstName = driver.find_element(By.NAME,"firstname")
        firstName.send_keys("Jeff")
        lastName = driver.find_element(By.NAME,"lastname")
        lastName.send_keys("Scott")
        email = driver.find_element(By.NAME,"email")
        email.send_keys()
        password = driver.find_element(By.NAME,"password")
        password.send_keys()
        passConfirmation = driver.find_element(By.NAME,"password_confirmation")
        passConfirmation.send_keys()
        btnsignUp = driver.find_element(By.XPATH,"//button[@title='Create an Account']//span[contains(text(),'Create an Account')]")
        btnsignUp.click()
    
    def test_register_11(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        el = driver.find_element(By.LINK_TEXT,"Create an Account")
        el.click()
        firstName = driver.find_element(By.NAME,"firstname")
        firstName.send_keys("Jeff")
        lastName = driver.find_element(By.NAME,"lastname")
        lastName.send_keys("Scott")
        email = driver.find_element(By.NAME,"email")
        email.send_keys("jeffscott@gmail.com")
        password = driver.find_element(By.NAME,"password")
        password.send_keys("@Jeffscott12345@")
        passConfirmation = driver.find_element(By.NAME,"password_confirmation")
        passConfirmation.send_keys("@Jeffscott12345@")
        btnsignUp = driver.find_element(By.XPATH,"//button[@title='Create an Account']//span[contains(text(),'Create an Account')]")
        btnsignUp.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()