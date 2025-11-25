Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:47) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from selenium.webdriver.common.by import By
... 
... class LoginPage:
...     def __init__(self, driver):
...         self.driver = driver
...         self.username_input = (By.ID, "user-name")
...         self.password_input = (By.ID, "password")
...         self.login_button = (By.ID, "login-button")
... 
...     def go_to_login_page(self):
...         self.driver.get("https://www.saucedemo.com/")
... 
...     def login(self, username, password):
...         self.driver.find_element(*self.username_input).send_keys(username)
...         self.driver.find_element(*self.password_input).send_keys(password)
...         self.driver.find_element(*self.login_button).click()
