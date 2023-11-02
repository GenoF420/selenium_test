#### Future Test ########

# def test_failed_login(driver):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("invalid_user")
#     driver.find_element(By.ID, "password").send_keys("invalid_password")
#     driver.find_element(By.ID, "login-button").click()
#     assert driver.find_element(By.XPATH, "//div[@class='error-message-container error']").is_displayed()

# def test_add_product_to_cart(driver):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     driver.find_element(By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]/ancestor::div[@class='inventory_item']//button").click()
#     assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"


# def test_remove_product_from_cart(driver):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     # Añadir producto al carrito
#     driver.find_element(By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]/ancestor::div[@class='inventory_item']//button").click()
#     # Ir al carrito y remover el producto
#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
#     # Verificar que el carrito esté vacío
#     cart_badge_elements = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
#     assert len(cart_badge_elements) == 0


# def test_order_products(driver):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     driver.find_element(By.XPATH, "//select/option[text()='Price (high to low)']").click()
#     products_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
#     prices = [float(price.text[1:]) for price in products_prices]
#     assert prices == sorted(prices, reverse=True)

# # test ver detalle sauce labs backpack, tiene id = 4
# def test_verify_product_details(driver):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']").click()
#     assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"

# def test_successful_checkout(driver):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     driver.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()  # Añadir al carrito
#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     driver.find_element(By.CSS_SELECTOR, "button.checkout_button").click()  # Modificado
#     driver.find_element(By.ID, "first-name").send_keys("John")
#     driver.find_element(By.ID, "last-name").send_keys("Doe")
#     driver.find_element(By.ID, "postal-code").send_keys("12345")
#     driver.find_element(By.CSS_SELECTOR, "input.cart_button").click()  # Modificado
#     driver.find_element(By.ID, "finish").click()
#     assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"


# def test_verify_product_price_in_cart(driver):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     product_price = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
#     driver.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()
#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     cart_price = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
#     assert product_price == cart_price


# def test_verify_continue_shopping_button(driver):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     driver.find_element(By.CSS_SELECTOR, "button.btn_inventory").click() #hace click en el primer botón "btn_inventory"
#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     driver.find_element(By.ID, "continue-shopping").click()  # Modificado
#     assert driver.current_url == "https://www.saucedemo.com/inventory.html"



