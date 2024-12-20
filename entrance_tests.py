import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import PASSWORD, EMAIL, BASE_URL
from conftest import login, full_fill_and_login
from locators import LK, REGISTRATION_LINK, ACCOUNT_BUTTON, RESTORE_PASSWORD, AUTH_DIV

ACCOUNT_URL = BASE_URL + '/account'


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_entrance_by_account_profile(driver, setup_driver):
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, LK))).click()
    full_fill_and_login(driver, EMAIL, PASSWORD)
    driver.find_element(By.XPATH, LK).click()

    assert driver.current_url == ACCOUNT_URL


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_entrance_by_button_login_to_account(driver, setup_driver):
    login(driver, EMAIL, PASSWORD)
    driver.find_element(By.XPATH, LK).click()
    assert driver.current_url == ACCOUNT_URL


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_entrance_by_password_recovery(driver, setup_driver):
    driver.find_element(By.CLASS_NAME, ACCOUNT_BUTTON).click()
    driver.find_element(By.XPATH, RESTORE_PASSWORD).click()
    driver.find_element(By.CLASS_NAME, REGISTRATION_LINK).click()
    full_fill_and_login(driver, EMAIL, PASSWORD)


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_entrance_by_registration_form(driver, setup_driver):
    driver.find_element(By.CLASS_NAME, ACCOUNT_BUTTON).click()
    driver.find_element(By.CLASS_NAME, REGISTRATION_LINK).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, AUTH_DIV)))
    driver.find_element(By.CLASS_NAME, REGISTRATION_LINK).click()
    full_fill_and_login(driver, EMAIL, PASSWORD)
