import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from login_functions import set_up

driver = selenium.webdriver.Chrome()

set_up(driver)
elements = driver.find_elements(By.XPATH, "html/body/div/div/main/section/div/div/span[@class='tab_tab__1SPyG']")
if len(elements) >= 2:
    elements[0].click()
image = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.TAG_NAME, "img")))
expected_image_src = "https://code.s3.yandex.net/react/code/bun-01.png"
assert image.get_attribute("src") == expected_image_src

driver.quit()
