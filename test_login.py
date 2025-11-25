import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login = LoginPage(driver)
    login.go_to_login_page()
    login.login("standard_user", "secret_sauce")
    assert "Products" in driver.title
