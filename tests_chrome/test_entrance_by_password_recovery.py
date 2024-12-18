import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import EMAIL, PASSWORD
from login_functions import set_up, full_fill_and_login

driver = selenium.webdriver.Chrome()

set_up(driver)
driver.find_element(By.CLASS_NAME, 'button_button__33qZ0').click()
driver.find_element(By.XPATH, ".//a[text()='Восстановить пароль']").click()
driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()
full_fill_and_login(driver, EMAIL, PASSWORD)

driver.quit()
