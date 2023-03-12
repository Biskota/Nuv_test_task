import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver

from tests.ui_tests.pages.cart_page import *
from tests.ui_tests.pages.main_page import *
from utils.base_test import *
from utils.test_data import BASE_URL


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


class TestAmazonShoppingCart:

    def test_shopping_cart(self, driver):
        go_to_page(driver, BASE_URL)
        update_location(driver)

        # Step 2: Search for "hats for men"
        search_items(driver, FIRST_QUERY)
        print("Step 2: Search for 'hats for men'")

        # Step 3: Add first hat to Cart with quantity 2
        title_1 = add_first_item_to_cart(driver, FIRST_QTY)
        print("Step 3: Add first hat to Cart with quantity 2")

        # Step 4: Open cart and assert total price and quantity are correct
        open_cart(driver)
        assert_total_price_and_qty(driver, title_1, FIRST_QTY)
        print("Step 4: Open cart and assert total price and quantity are correct")

        # Step 5: Search for "hats for women"
        search_items(driver, SECOND_QUERY)
        print("Step 5: Search for 'hats for women'")

        # Step 6: Add first hat to Cart with quantity 1
        title_2 = add_first_item_to_cart(driver, SECOND_QTY)
        print("Step 6: Add first hat to Cart with quantity 1")

        # Step 7: Open cart and assert total price and quantity are correct
        open_cart(driver)
        assert_total_price_and_qty(driver, title_2, SECOND_QTY)
        print("Step 7: Open cart and assert total price and quantity are correct")

        # Step 8: Change the quantity for item selected at step 3 from 2 to 1 item in Cart
        change_qty_item_in_cart(driver, SECOND_QTY)
        print("Step 8: Change the quantity for item selected at step 3 from 2 to 1 item in Cart")

        assert_total_price_and_qty(driver, title_1, SECOND_QTY)
        print("Step 9: Assert total price and quantity are changed correctly")


@pytest.fixture()
def tearDown(self):
    self.driver.quit()

