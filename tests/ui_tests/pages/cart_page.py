import allure
from selenium.webdriver.support.select import Select

from utils.locators import AmazonCartLocators
from utils.test_data import *


@allure.step('Add first item to cart')
def add_first_item_to_cart(driver, quantity):
    items = driver.find_elements(*AmazonCartLocators.ITEMS)
    items[0].click()

    title = driver.find_element(*AmazonCartLocators.ITEM_TITLE).text

    select = Select(driver.find_element(*AmazonCartLocators.ITEM_QTY))
    select.select_by_value(quantity)

    add_to_cart_button = driver.find_element(*AmazonCartLocators.ADD_TO_CART_BTN)
    add_to_cart_button.click()

    return title


@allure.step('Open cart')
def open_cart(driver):
    # Click on cart button
    cart_button = driver.find_element(*AmazonCartLocators.GO_TO_CART)
    cart_button.click()
    assert (SHOPPING_CART in driver.title)


@allure.step('Assert total price and quantity')
def assert_total_price_and_qty(driver, product_name, qty):
    total_price = 0.0
    cart_items = driver.find_elements(*AmazonCartLocators.ITEMS_CART)
    for i in range(len(cart_items)):
        cart_item = cart_items[i]
        title = cart_item.find_elements(*AmazonCartLocators.ITEM_CART_TITLE)[0]
        if product_name == title:
            cart_item.find_elements(*AmazonCartLocators.ITEMS_CART)[0].text
            for i in range(len(cart_items)):
                cart_item = cart_items[i]
                item_price = float(
                    cart_item.find_elements(*AmazonCartLocators.ITEM_PRICE)[0].text.replace('$', ''))
                item_quantity = float(cart_item.find_elements(*AmazonCartLocators.ITEM_CART_QTY)[0].text)
                total_price += item_price * item_quantity
                assert (item_quantity == qty, QTY_ERROR_MSG)
                assert (float(total_price) == (float(item_price) * float(item_quantity)), PRICE_ERROR_MSG)


@allure.step('Change item qty in cart')
def change_qty_item_in_cart(driver, product_name, quantity):
    cart_items = driver.find_elements(*AmazonCartLocators.ITEMS_CART)
    for i in range(len(cart_items)):
        cart_item = cart_items[i]
        title = cart_item.find_elements(*AmazonCartLocators.ITEM_CART_TITLE)[0]
        if product_name == title:
            select = Select(cart_items[i].find_element(*AmazonCartLocators.ITEM_QTY))
            select.select_by_value(quantity)