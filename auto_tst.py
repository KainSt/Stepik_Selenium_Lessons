import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.smoke
def test_guest_should_see_login_link(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    time.sleep(3)

    browser.find_element(By.CSS_SELECTOR, '#ember33').click()
    time.sleep(3)

    new_window = browser.window_handles[0]
    browser.switch_to.window(new_window)

    browser.find_element(By.CSS_SELECTOR, '#id_login_email').send_keys('kainst83@mail.ru')
    browser.find_element(By.CSS_SELECTOR, '#id_login_password').send_keys('m919stepik4126')
    time.sleep(10)

    browser.find_element(By.CSS_SELECTOR, '#login_form > button').click()
    time.sleep(5)

