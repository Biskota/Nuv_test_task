from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.locators import *
from utils.test_data import *


def update_location(driver):
    driver.find_element(*AmazonMainLocators.CHANGE_DELIVERY_LOCATION).click()
    driver.find_element(*AmazonMainLocators.ZIP_CODE_INPUT).send_keys(ZIP_CODE)
    driver.find_element(*AmazonMainLocators.APPLY_BTN).click()
    driver.find_element(*AmazonMainLocators.CONFIRM_BTN).click()
    driver.refresh()


def search_items(driver, search_query):
    search_bar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AmazonMainLocators.SEARCH_INPUT)))
    WebDriverWait(driver, 3)
    search_bar.send_keys(search_query)
    driver.find_element(*AmazonMainLocators.SEARCH_BTN).click()
    assert (search_query in driver.title)
