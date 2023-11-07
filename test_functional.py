import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

#comando para correr el script
# pytest --html=report_functional.html test_functional.py

#Fixture para inicializar y finalizar el driver de Selenium.
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver 
    driver.quit()
  
    
# def test_failed_login(driver):
#     """
#     Verifica que un usuario con credenciales inválidas reciba un mensaje de error.

#     Pasos:
#     1. Navega a la página de inicio de sesión.
#     2. Introduce un nombre de usuario y contraseña inválidos.
#     3. Hace clic en el botón de login.
#     4. Verifica que el mensaje de error se muestre correctamente.

#     Errores conocidos:
#     Ninguno.
#     """
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("invalid_user")
#     driver.find_element(By.ID, "password").send_keys("invalid_password")
#     driver.find_element(By.ID, "login-button").click()
#     error_message = driver.find_element(By.CSS_SELECTOR, "div.error-message-container.error")
#     assert error_message.is_displayed()

    
# def test_logout(driver):
#     """
#     Verifica que un usuario pueda cerrar sesión exitosamente.
#     Pasos:
#     1. Navega a la página principal e inicia sesión.
#     2. Abre el menú lateral.
#     3. Hace clic en el enlace de logout.
#     4. Verifica que la URL actual sea la de la página principal.

#     Errores conocidos:
#     Ninguno.
#     """
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()
#     driver.find_element(By.ID, "react-burger-menu-btn").click()
#     WebDriverWait(driver, 5).until(
#         EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
#     )
#     driver.find_element(By.ID, "logout_sidebar_link").click()
#     assert driver.current_url == "https://www.saucedemo.com/"
    

# def test_failed_login(driver):
#     """
#     Verifica que un usuario con credenciales inválidas reciba un mensaje de error.

#     Pasos:
#     1. Navega a la página de inicio de sesión.
#     2. Introduce un nombre de usuario y contraseña inválidos.
#     3. Hace clic en el botón de login.
#     4. Verifica que el mensaje de error se muestre correctamente.

#     Errores conocidos:
#     Ninguno.
#     """
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("invalid_user")
#     driver.find_element(By.ID, "password").send_keys("invalid_password")
#     driver.find_element(By.ID, "login-button").click()
#     error_message = driver.find_element(By.CSS_SELECTOR, "div.error-message-container.error")
#     assert error_message.is_displayed()
    


# def test_add_product_to_cart(driver):
#     """
#     Verifica que se pueda añadir un producto al carrito exitosamente.

#     Pasos:
#     1. Navega a la página de inicio de sesión.
#     2. Introduce las credenciales de un usuario estándar.
#     3. Hace clic en el botón de inicio de sesión.
#     4. Busca el botón de añadir al carrito para el producto "Sauce Labs Backpack".
#     5. Hace clic en el botón de añadir al carrito.
#     6. Verifica que el contador del carrito se actualice a "1".

#     Errores conocidos:
#     Ninguno.
#     """
#     driver.get("https://www.saucedemo.com/")
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     driver.find_element(By.ID, "login-button").click()

#     # Suponiendo que 'Sauce Labs Backpack' tiene un botón con un ID o una clase única, actualizamos el siguiente selector.
#     driver.find_element(By.CSS_SELECTOR, "button[name='add-to-cart-sauce-labs-backpack']").click()

#     # Verifica que el ícono del carrito muestre "1"
#     assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"

    
    
# def test_remove_product_from_cart(driver):
#     """
#     Verifica que un producto pueda ser removido del carrito exitosamente.

#     Pasos:
#     1. Navega a la página de inicio de sesión.
#     2. Inicia sesión con credenciales válidas.
#     3. Añade un producto al carrito.
#     4. Navega al carrito de compras.
#     5. Remueve el producto del carrito.
#     6. Verifica que el contador del carrito no esté presente, indicando que está vacío.

#     Errores conocidos:
#     Ninguno.
#     """
#     # Navegar a la página de inicio de sesión
#     driver.get("https://www.saucedemo.com/")
#     # Ingresar usuario y contraseña
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     # Iniciar sesión
#     driver.find_element(By.ID, "login-button").click()
#     # Añadir producto al carrito
#     driver.find_element(By.CSS_SELECTOR, "button[name='add-to-cart-sauce-labs-backpack']").click()
#     # Navegar al carrito de compras
#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     # Remover producto del carrito
#     driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
#     # Verificar que el carrito esté vacío
#     cart_badge_elements = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
#     assert len(cart_badge_elements) == 0, "El carrito no está vacío después de remover el producto."

    
    
# def test_verify_product_details(driver):
#     """
#     Verifica que el detalle de un producto se muestre correctamente.

#     Pasos:
#     1. Navega a la página de inicio de sesión.
#     2. Inicia sesión con credenciales válidas.
#     3. Selecciona el producto 'Sauce Labs Backpack' para ver los detalles.
#     4. Verifica que la URL actual contenga el ID correcto del producto.

#     Errores conocidos:
#     Ninguno.
#     """
#     # Navegar a la página de inicio de sesión
#     driver.get("https://www.saucedemo.com/")
#     # Ingresar usuario y contraseña
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     # Iniciar sesión
#     driver.find_element(By.ID, "login-button").click()
#     # Seleccionar el producto 'Sauce Labs Backpack' para ver los detalles
#     driver.find_element(By.ID, "item_4_title_link").click()  # Usamos el ID que es más específico y menos propenso a cambios que un XPath
#     # Verificar que la URL actual contenga el ID correcto del producto
#     assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4", "La URL no coincide con la esperada para los detalles del producto."


# def test_successful_checkout(driver):
#     """
#     Verifica que el proceso de checkout se complete exitosamente.

#     Pasos:
#     1. Navega a la página de inicio de sesión.
#     2. Inicia sesión con credenciales válidas.
#     3. Añade un producto al carrito.
#     4. Navega al carrito de compras.
#     5. Inicia el proceso de checkout.
#     6. Completa los datos de facturación.
#     7. Finaliza el proceso de checkout.
#     8. Verifica que la URL actual sea la de la página de confirmación de checkout.

#     Errores conocidos:
#     Ninguno.
#     """
#     # Navegar a la página de inicio de sesión
#     driver.get("https://www.saucedemo.com/")
#     # Ingresar usuario y contraseña
#     driver.find_element(By.ID, "user-name").send_keys("standard_user")
#     driver.find_element(By.ID, "password").send_keys("secret_sauce")
#     # Iniciar sesión
#     driver.find_element(By.ID, "login-button").click()
#     # Añadir el primer producto disponible al carrito
#     driver.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()
#     # Navegar al carrito de compras
#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     # Iniciar el proceso de checkout
#     driver.find_element(By.CSS_SELECTOR, "button.checkout_button").click()
#     # Completar información del comprador
#     driver.find_element(By.ID, "first-name").send_keys("John")
#     driver.find_element(By.ID, "last-name").send_keys("Doe")
#     driver.find_element(By.ID, "postal-code").send_keys("12345")
#     # Continuar con el checkout
#     driver.find_element(By.CSS_SELECTOR, "input.cart_button").click()
#     # Finalizar el proceso de checkout
#     driver.find_element(By.ID, "finish").click()
#     # Verificar que se haya redirigido a la página de confirmación de checkout
#     assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html", "La URL no coincide con la esperada después del checkout."

    
def test_verify_product_price_in_cart(driver):
    """
    Verifica que el precio del producto en la página de inventario coincida con el precio mostrado en el carrito.

    Pasos:
    1. Navega a la página de inicio de sesión.
    2. Inicia sesión con credenciales válidas.
    3. Obtiene el precio del primer producto listado.
    4. Añade ese producto al carrito.
    5. Navega al carrito de compras.
    6. Obtiene el precio del producto dentro del carrito.
    7. Compara ambos precios para asegurarse de que coinciden.

    Errores conocidos:
    Ninguno.
    """
    # Navegar a la página de inicio de sesión
    driver.get("https://www.saucedemo.com/")
    # Ingresar usuario y contraseña
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    # Iniciar sesión
    driver.find_element(By.ID, "login-button").click()
    # Obtener precio del primer producto en la página de inventario
    product_price = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
    # Añadir el primer producto al carrito
    driver.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()
    # Navegar al carrito de compras
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    # Obtener precio del producto en el carrito de compras
    cart_price = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
    # Asegurarse de que los precios coinciden
    assert product_price == cart_price, "El precio del producto en la página de inventario no coincide con el del carrito."

    

    #################### TEST USING PROBLEM_USER ############################ 



# def test_successful_checkout(driver):
#     """
#     Verifica que el usuario 'problem_user' pueda completar el proceso de checkout.

#     Pasos:
#     1. Navega a la página principal e inicia sesión como 'problem_user'.
#     2. Añade un producto al carrito y procede al checkout.
#     3. Completa los detalles del checkout y finaliza la compra.
#     4. Verifica que la URL actual sea la página de confirmación de checkout.

#     Errores conocidos:
#     - No se puede agregar el Lastname, por lo que no deja seguir avanzando con el checkout.
#     """
    
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
#     #time.sleep(5); ## para poder ver cuando ocurre el error
#     driver.find_element(By.CSS_SELECTOR, "input.cart_button").click()  # Modificado
#     driver.find_element(By.ID, "finish").click()
#     assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
#     #"No se puede agregar el Lastname, por lo que no deja seguir avanzando con el checkout"



# def test_filter_functionality(driver):
#     """
#     Verifica la funcionalidad de filtro en la página de inventario con el usuario 'problem_user'.

#     Pasos:
#     1. Navega a la página principal e inicia sesión como 'problem_user'.
#     2. En la página de inventario, registra el nombre del primer producto.
#     3. Aplica un filtro de 'Name (Z to A)'.
#     4. Registra nuevamente el nombre del primer producto.
#     5. Verifica que el nombre del primer producto haya cambiado, indicando que el filtro se aplicó correctamente.

#     Errores conocidos:
#     Ningún tipo de filtro disponible funciona con este usuario.
#     """
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





##ERRORES ENCONTRADOS
# Se puede realizar el proceso de compra sin seleccionar ningún artículo.
# No hay restricciones para la información del comprador, ej, la cantidad de caracteres que se pueden ingresar, una combinación de caracteres o números para los nombres.
# No se puede agregar más unidades de los artículos elegidos, solo 1 por artículo.
# Mensajes de errores extraños al iniciar sesión: "Epic sad face: You can only access '/cart.html' when you are logged in." o también
# Epic sad face: You can only access '/inventory.html' when you are logged in.

# Usando el PROBLEM USER se encontró lo siguiente:
# En el checkout no se puede agregar el Lastname, por lo que no deja seguir avanzando y da error.
# El filtro de nombres no funcionó, no se puede aplicar filtro.