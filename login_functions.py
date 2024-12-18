from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import BASE_URL


def login(driver, email, password):
    # функция логина для переиспользования
    set_up(driver)
    driver.find_element(By.CLASS_NAME, 'button_button__33qZ0').click()
    full_fill_and_login(driver, email, password)


def sign_in(driver, username, email, password):
    # функция регистрации для переиспользования
    set_up(driver)

    driver.find_element(By.CLASS_NAME, 'button_button__33qZ0').click()
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input").send_keys(username)
    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()


def set_up(driver):
    # на весь экран и перейти на сайт
    driver.maximize_window()
    # driver.implicitly_wait(3)
    driver.get(BASE_URL)


def full_fill_and_login(driver, email, password):
    # функция заполнения полей логина

    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
