from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_index, size_index, color_index, quantity):
        # Go to the product page
        product = self.driver.find_element(By.XPATH, f'//*[@id="maincontent"]/div[3]/div/div[2]/div[3]/div/div/ol/li[{product_index}]/div/a/span/span/img')
        product.click()
        time.sleep(5)

        # Select size
        size = self.driver.find_element(By.XPATH, f'//*[@id="option-label-size-143-item-{size_index}"]')
        size.click()
        time.sleep(5)

        # Select color
        color = self.driver.find_element(By.XPATH, f'//*[@id="option-label-color-93-item-{color_index}"]')
        color.click()
        time.sleep(5)

        # Enter quantity
        qty = self.driver.find_element(By.XPATH, '//*[@id="qty"]')
        qty.clear()
        qty.send_keys(quantity)
        time.sleep(5)

        # Click on "Add to Cart" button
        add = self.driver.find_element(By.XPATH, '//*[@id="product-addtocart-button"]')
        add.click()
        time.sleep(5)
    def category_product(self,category_index, sub_category_index, sub_sub_category_index):
        try:
            cursor = ActionChains(self.driver)
            wait = WebDriverWait(self.driver, 10)
            category = self.driver.find_element(By.XPATH, f'//*[@id="ui-id-{category_index}"]/span[2]')
            cursor.move_to_element(category).perform()

            sub_category = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="ui-id-{sub_category_index}"]/span[2]')))
            cursor.move_to_element(sub_category).perform()

            sub_sub_category = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="ui-id-{sub_sub_category_index}"]/span')))
            cursor.move_to_element(sub_sub_category).click().perform()


        except Exception as e:
            print("Element not found or interactable.")        
    def add_to_cart_on_category(self, product_index, size_index, color_index, quantity):
        # Go to the product page
        product = self.driver.find_element(By.XPATH, f'//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[{product_index}]/div/a/span/span/img')
        product.click()
        time.sleep(5)

        # Select size
        size = self.driver.find_element(By.XPATH, f'//*[@id="option-label-size-143-item-{size_index}"]')
        size.click()
        time.sleep(5)

        # Select color
        color = self.driver.find_element(By.XPATH, f'//*[@id="option-label-color-93-item-{color_index}"]')
        color.click()
        time.sleep(5)

        # Enter quantity
        qty = self.driver.find_element(By.XPATH, '//*[@id="qty"]')
        qty.clear()
        qty.send_keys(quantity)
        time.sleep(5)

        # Click on "Add to Cart" button
        add = self.driver.find_element(By.XPATH, '//*[@id="product-addtocart-button"]')
        add.click()
        time.sleep(5)
    def verify_success_message(self):
        response_data = self.driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[1]/div[2]/div/div/div').text
        assert 'to your shopping cart.' in response_data
            
    def verify_error_message_maximum(self):
        response_data = self.driver.find_element(By.XPATH, '//*[@id="qty-error"]').text
        assert 'The maximum you may purchase is 10000' in response_data

    def verify_error_message_zero(self):
        response_data = self.driver.find_element(By.XPATH, '//*[@id="qty-error"]').text
        assert 'Please enter a quantity greater than 0.' in response_data

 
