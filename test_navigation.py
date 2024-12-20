import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import BASE_URL, EMAIL, PASSWORD, sign_in
from conftest import login
from locators import *
from urls import LOGIN_URL, PROFILE_URL


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_login_and_go_to_constructor(driver, setup_driver):
    login(driver, EMAIL, PASSWORD)
    time.sleep(1)
    driver.find_element(By.XPATH, LK).click()
    time.sleep(1)
    driver.find_element(By.XPATH, CONSTRUCTOR).click()
    time.sleep(1)

    assert driver.current_url == BASE_URL + "/"


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_navigate_to_buns(driver, setup_driver):
    bun_tub = driver.find_element(By.XPATH, CURRENT_TAB_SELECTOR)
    span = bun_tub.find_element(By.XPATH, BUNS_SELECTOR)
    assert span.text == "Булки"


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_navigate_to_sauces(driver, setup_driver):
    elements = driver.find_elements(By.XPATH, TAB_SELECTOR)
    sauce_tab = elements[1]
    sauce_tab.click()
    current_tab = driver.find_element(By.XPATH, CURRENT_TAB_SELECTOR)
    sauce_span = current_tab.find_element(By.XPATH, SAUCE_SELECTOR)
    assert sauce_span.text == "Соусы"


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_navigate_to_ingredients(driver, setup_driver):
    elements = driver.find_elements(By.XPATH, TAB_SELECTOR)
    ingredients_tab = elements[len(elements) - 1]
    ingredients_tab.click()
    current_tab = driver.find_element(By.XPATH, CURRENT_TAB_SELECTOR)
    ingredients_span = current_tab.find_element(By.XPATH, INGREDIENTS_SELECTOR)
    assert ingredients_span.text == "Начинки"


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_navigate_constructor_by_logo(driver, setup_driver):
    login(driver, EMAIL, PASSWORD)
    time.sleep(0.5)
    driver.find_element(By.XPATH, LK).click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, CSS_SELECTOR).click()
    time.sleep(0.5)
    assert driver.current_url == BASE_URL + '/'


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_navigate_personal_account(driver, setup_driver):
    login(driver, EMAIL, PASSWORD)
    time.sleep(0.5)
    driver.find_element(By.XPATH, LK).click()
    time.sleep(0.5)
    assert driver.current_url == PROFILE_URL


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_logout(driver, setup_driver):
    login(driver, EMAIL, PASSWORD)
    time.sleep(1)
    driver.find_element(By.XPATH, LK).click()
    time.sleep(1)
    driver.find_element(By.XPATH, EXIT_BUTTON).click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, ACCOUNT_BUTTON)
    time.sleep(1)
    assert driver.current_url == LOGIN_URL


@pytest.mark.parametrize('driver', [webdriver.Chrome()])
def test_registration(driver, setup_driver):
    sign_in(driver, "Рахатлукумович", "62xxxtft@example.com", "123")

    error_message = WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "input__error")))
    assert error_message.text == "Некорректный пароль"

    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys("123654")
    driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()
    time.sleep(1)
    assert driver.current_url == LOGIN_URL
