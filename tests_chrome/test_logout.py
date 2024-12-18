import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import EMAIL, PASSWORD
from login_functions import login

driver = selenium.webdriver.Chrome()

login(driver, EMAIL, PASSWORD)
WebDriverWait(driver, 3).until(
    expected_conditions.element_to_be_clickable((By.XPATH, ".//p[text()='Личный Кабинет']"))).click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
    (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']"))).click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')  # .click()
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

driver.quit()
