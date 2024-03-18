from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

try:

    butoonFirst = browser.find_element(By.ID, "book")
    # Задаем счетчик ожидания
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    butoonFirst.click()
   

    box = browser.find_element(By.ID, 'input_value')
    x = box.text

    element_1 = browser.find_element(By.ID, 'answer')
    element_1.send_keys(calc(x))

    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()