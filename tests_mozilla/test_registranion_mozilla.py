import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from login_functions import sign_in

driver = selenium.webdriver.Firefox()
sign_in(driver, "Рахатлукумыччч", "raxxxat@example.com", "123")

error_message = WebDriverWait(driver, 3).until(
    expected_conditions.visibility_of_element_located((By.CLASS_NAME, "input__error")))
assert error_message.text == "Некорректный пароль"

driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys("123654")
driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
WebDriverWait(driver, 3).until(
    expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']"))).click()

driver.quit()
