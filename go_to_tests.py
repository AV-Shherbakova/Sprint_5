import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import BASE_URL, EMAIL, PASSWORD
from conftest import login, sign_in
from locators import CONSTRUCTOR, LK, BUNS_ELEMENTS, CSS_SELECTOR, FILLINGS_ELEMENTS, IMG_FILLING, SAUCE_ELEMENTS, \
    IMG_SAUCE, ACCOUNT_BUTTON, EXIT_BUTTON, PASSWORD_INPUT, REGISTRATION_BUTTON, ENTER_BUTTON


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_login_and_go_to_constructor(driver, setup_driver):
    login(driver, EMAIL, PASSWORD)
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, LK))).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, CONSTRUCTOR))).click()

    assert driver.current_url == BASE_URL + "/"


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_go_to_buns(driver, setup_driver):
    elements = driver.find_elements(By.XPATH, BUNS_ELEMENTS)
    if len(elements) >= 2:
        elements[0].click()
    image = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.TAG_NAME, "img")))
    expected_image_src = "https://code.s3.yandex.net/react/code/bun-01.png"
    assert image.get_attribute("src") == expected_image_src


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_go_to_sauces(driver, setup_driver):
    elements = driver.find_elements(By.XPATH, SAUCE_ELEMENTS)
    if len(elements) >= 2:
        elements[1].click()
    image = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
        (By.XPATH, IMG_SAUCE)))
    expected_image_src = "https://code.s3.yandex.net/react/code/sauce-02.png"
    assert image.get_attribute("src") == expected_image_src


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_go_to_fillings(driver, setup_driver):
    elements = driver.find_elements(By.XPATH, FILLINGS_ELEMENTS)
    if len(elements) >= 2:
        elements[2].click()
    image = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
        (By.XPATH, IMG_FILLING)))
    expected_image_src = "https://code.s3.yandex.net/react/code/meat-02.png"
    assert image.get_attribute("src") == expected_image_src


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_go_to_constructor_by_logo(driver, setup_driver):
    login(driver, EMAIL, PASSWORD)
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, LK))).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, CSS_SELECTOR))).click()
    assert driver.current_url == BASE_URL + '/'


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_go_to_personal_account(driver, setup_driver):
    login(driver, EMAIL, PASSWORD)
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, LK))).click()
    assert driver.current_url == BASE_URL + '/account'


@pytest.mark.parametrize('driver', [webdriver.Chrome(), webdriver.Firefox()])
def test_logout(driver, setup_driver):
    login(driver, EMAIL, PASSWORD)
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, LK))).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, EXIT_BUTTON))).click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, ACCOUNT_BUTTON)
    assert driver.current_url == BASE_URL + '/login'


@pytest.mark.parametrize('driver', [webdriver.Chrome()])
def test_registration(driver, setup_driver):
    sign_in(driver, "Рахатлукумович", "66raxxxdfgat@example.com", "123")

    error_message = WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "input__error")))
    assert error_message.text == "Некорректный пароль"

    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys("123654")
    driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ENTER_BUTTON))).click()
