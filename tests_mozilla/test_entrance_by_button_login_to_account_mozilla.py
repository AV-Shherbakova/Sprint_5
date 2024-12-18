import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import EMAIL, PASSWORD
from login_functions import login

driver = selenium.webdriver.Firefox()

login(driver, EMAIL, PASSWORD)
driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account'

driver.quit()

