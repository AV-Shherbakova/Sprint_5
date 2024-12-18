import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import EMAIL, PASSWORD
from login_functions import set_up, login

driver = selenium.webdriver.Firefox()

set_up(driver)
login(driver, EMAIL, PASSWORD)
WebDriverWait(driver, 3).until(
    expected_conditions.element_to_be_clickable((By.XPATH, ".//p[text()='Личный Кабинет']"))).click()
WebDriverWait(driver, 3).until(
    expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, "#root > div > header > nav > div > a > svg"))).click()

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

driver.quit()