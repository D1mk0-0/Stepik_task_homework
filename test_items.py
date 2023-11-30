import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url_link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_button(browser):
    try:
        browser.get(url_link)
        # time.sleep(30)
        WebDriverWait(browser, 10).until(
                 EC.visibility_of_element_located((By.CSS_SELECTOR, '#add_to_basket_form button'))
             )
        button_basket = True
    except:
        button_basket = False
    assert button_basket, r'Кнопка не обнаружена ¯\_(ツ)_/¯'
