import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# pytest --html=report_functional.html test_functional.py

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver 
    driver.quit()
    
    ################ WORKING TEST  ########################
    
def test_logout(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
    )
    driver.find_element(By.ID, "logout_sidebar_link").click()
    assert driver.current_url == "https://www.saucedemo.com/"


# def test_successful_login(driver):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     assert driver.current_url == "https://www.saucedemo.com/inventory.html"

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




    ############## TEST USING PROBLEM_USER ############################ 

# def test_successful_checkout(driver):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("problem_user")  # Modificado
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     driver.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()  # Añadir al carrito
#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     driver.find_element(By.CSS_SELECTOR, "button.checkout_button").click()  # Modificado
#     driver.find_element(By.ID, "first-name").send_keys("John")
#     driver.find_element(By.ID, "last-name").send_keys("Doe")
#     driver.find_element(By.ID, "postal-code").send_keys("12345")
#     time.sleep(5); ## para poder ver cuando ocurre el error
#     driver.find_element(By.CSS_SELECTOR, "input.cart_button").click()  # Modificado
#     driver.find_element(By.ID, "finish").click()
#     assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
#     #no se puede agregar el Lastname, por lo que no deja seguir avanzando con el checkout

# def test_filter_functionality(driver):
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("problem_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
    
#     # Obtiene el nombre del primer producto antes de aplicar el filtro
#     product_name_before = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    
#     # Selecciona la opción de filtro 'Name (Z to A)'
#     filter_option = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
#     filter_option.select_by_visible_text("Name (Z to A)")
    
#     # Obtiene el nombre del primer producto después de aplicar el filtro
#     product_name_after = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    
#     # Asegura que el nombre del primer producto haya cambiado después de aplicar el filtro
#     assert product_name_before != product_name_after, f"El filtro no funcionó, nombre del ítem antes del filtro: {product_name_before}, es igual a después del filtro: {product_name_after}"
    
    
    
######################  TO TEST ###########################










##ERRORS
# Se puede realizar el proceso de compra sin seleccionar ningún artículo.
# No hay restricciones para la información del comprador, ej, la cantidad de caracteres que se pueden ingresar, una combinación de caracteres o números para los nombres.
# No se puede agregar más unidades de los artículos elegidos, solo 1 por artículo.
# Mensajes de errores extraños al iniciar sesión: "Epic sad face: You can only access '/cart.html' when you are logged in." o también
# Epic sad face: You can only access '/inventory.html' when you are logged in.

# Usando el PROBLEM USER se encontró lo siguiente:
# En el checkout no se puede agregar el Lastname, por lo que no deja seguir avanzando y da error.
# El filtro de nombres no funcionó, no se puede aplicar filtro.