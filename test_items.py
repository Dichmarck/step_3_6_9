import time
from selenium.webdriver.common.by import By


def test_product_page_contains_add_to_basket_button(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    browser.get(url)
    browser.implicitly_wait(10)
    btns = browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    time.sleep(1)

    assert len(btns) > 0, "Add-to-basket button no found on product page"
