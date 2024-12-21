import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import ACCOUNT_BUTTON, NAME_INPUT, EMAIL_INPUT, PASSWORD_INPUT, REGISTRATION_BUTTON, ENTER_BUTTON, \
    AUTH_DIV
from urls import BASE_URL

EMAIL = "Alyona_Shherbakova_1988_16_py@yandex.ru"
PASSWORD = "aaa666"


@pytest.fixture
def setup_driver(driver):
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


def login(driver, email, password):
    # функция логина для переиспользования
    driver.find_element(By.CLASS_NAME, ACCOUNT_BUTTON).click()
    full_fill_and_login(driver, email, password)


def sign_in(driver, username, email, password):
    # функция регистрации для переиспользования
    driver.find_element(By.CLASS_NAME, ACCOUNT_BUTTON).click()
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, AUTH_DIV)))
    driver.find_element(By.XPATH, NAME_INPUT).send_keys(username)
    driver.find_element(By.XPATH, EMAIL_INPUT).send_keys(email)
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys(password)
    driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()


def full_fill_and_login(driver, email, password):
    # функция заполнения полей логина
    driver.find_element(By.XPATH, EMAIL_INPUT).send_keys(email)
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys(password)
    driver.find_element(By.XPATH, ENTER_BUTTON).click()
