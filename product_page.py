from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = (By.CSS_SELECTOR, ".btn_inventory")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_first_item_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
