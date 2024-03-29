import time

from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_code_functionality_languages(browser):
    browser.get(link)

    button_add = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    time.sleep(3)
    assert len(button_add.text) > 0
