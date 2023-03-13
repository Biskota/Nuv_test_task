import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from tests.ui_tests.pages.cart_page import *
from tests.ui_tests.pages.main_page import *
from utils.base_test import *
from utils.logger import logger2
from utils.test_data import BASE_URL


@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


class TestAmazonShoppingCart:

    def test_shopping_cart(self, driver):
        logger2.info(f"Step 1: Open amazon main page and update location")
        go_to_page(driver, BASE_URL)
        update_location(driver)

        search_items(driver, FIRST_QUERY)
        logger2.info(f"Step 2: Search for 'hats for men'")

        title_1 = add_first_item_to_cart(driver, FIRST_QTY)
        logger2.info(f"Step 3: Add first hat to Cart with quantity 2")

        open_cart(driver)
        assert_total_price_and_qty(driver, title_1, FIRST_QTY)
        logger2.info(f"Step 4: Open cart and assert total price and quantity are correct")

        search_items(driver, SECOND_QUERY)
        logger2.info(f"Step 5: Search for 'hats for women'")

        title_2 = add_first_item_to_cart(driver, SECOND_QTY)
        logger2.info(f"Step 6: Add first hat to Cart with quantity 1")

        open_cart(driver)
        assert_total_price_and_qty(driver, title_2, SECOND_QTY)
        logger2.info(f"Step 7: Open cart and assert total price and quantity are correct")

        change_qty_item_in_cart(driver, title_1, SECOND_QTY)
        logger2.info(f"Step 8: Change the quantity for item selected at step 3 from 2 to 1 item in Cart")

        assert_total_price_and_qty(driver, title_1, SECOND_QTY)
        logger2.info(f"Step 9: Assert total price and quantity are changed correctly")


@pytest.fixture()
def tearDown(self):
    self.driver.quit()
