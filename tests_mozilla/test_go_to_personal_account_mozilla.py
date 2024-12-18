import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import EMAIL, PASSWORD
from login_functions import login

driver = selenium.webdriver.Firefox()

login(driver, EMAIL, PASSWORD)
WebDriverWait(driver, 3).until(
    expected_conditions.element_to_be_clickable((By.XPATH, ".//p[text()='Личный Кабинет']"))).click()
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'

driver.quit()