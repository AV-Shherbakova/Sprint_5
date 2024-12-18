import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import EMAIL, PASSWORD
from login_functions import full_fill_and_login

driver = selenium.webdriver.Firefox()

driver.maximize_window()
driver.get('https://stellarburgers.nomoreparties.site')

WebDriverWait(driver, 3).until(
    expected_conditions.element_to_be_clickable((By.XPATH, ".//p[text()='Личный Кабинет']"))).click()
full_fill_and_login(driver, EMAIL, PASSWORD)
driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'

driver.quit()
