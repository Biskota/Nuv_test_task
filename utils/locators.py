from selenium.webdriver.common.by import By


class AmazonCartLocators:
    ITEMS = (By.CSS_SELECTOR,
             "#search > div div span.rush-component.s-latency-cf-section > div.s-search-results > div:nth-child(3)")
    ITEM_TITLE = (By.ID, "productTitle")
    ITEM_QTY = (By.ID, "quantity")
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
    GO_TO_CART = (By.CSS_SELECTOR, "#sw-gtc > span > a")
    ITEMS_CART = (By.CSS_SELECTOR, ".a-row.sc-list-item")
    ITEM_CART_TITLE = (By.CSS_SELECTOR,
                       " .sc-product-title> span > .a-truncate-cut")
    ITEM_PRICE = (By.CSS_SELECTOR, ".sc-product-price.a-text-bold")
    ITEM_CART_QTY = (By.CSS_SELECTOR, ".a-dropdown-prompt")


class AmazonMainLocators:
    CHANGE_DELIVERY_LOCATION = (By.ID, "nav-global-location-popover-link")
    ZIP_CODE_INPUT = (By.ID, "GLUXZipUpdateInput")
    APPLY_BTN = (By.CSS_SELECTOR, "#GLUXZipUpdate > span > input")
    CONFIRM_BTN = (By.CSS_SELECTOR,
                   ".a-popover-footer span.a-button-span4")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input#twotabsearchtextbox")
    SEARCH_BTN = (By.ID, "nav-search-submit-button")
