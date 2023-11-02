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
  
    
def test_successful_login(driver):
    """
    Verifica que un usuario pueda iniciar sesión exitosamente.

    Pasos:
    1. Navega a la página principal.
    2. Introduce las credenciales válidas de un usuario.
    3. Hace clic en el botón de login.
    4. Verifica que la URL actual sea la de la página de inventario.

    Errores conocidos:
    Ninguno.
    """
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    
    
def test_logout(driver):
    """
    Verifica que un usuario pueda cerrar sesión exitosamente.
    Pasos:
    1. Navega a la página principal e inicia sesión.
    2. Abre el menú lateral.
    3. Hace clic en el enlace de logout.
    4. Verifica que la URL actual sea la de la página principal.

    Errores conocidos:
    Ninguno.
    """
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




    #################### TEST USING PROBLEM_USER ############################ 



def test_successful_checkout(driver):
    """
    Verifica que el usuario 'problem_user' pueda completar el proceso de checkout.

    Pasos:
    1. Navega a la página principal e inicia sesión como 'problem_user'.
    2. Añade un producto al carrito y procede al checkout.
    3. Completa los detalles del checkout y finaliza la compra.
    4. Verifica que la URL actual sea la página de confirmación de checkout.

    Errores conocidos:
    - No se puede agregar el Lastname, por lo que no deja seguir avanzando con el checkout.
    """
    
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("problem_user")  # Modificado
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()  # Añadir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, "button.checkout_button").click()  # Modificado
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    #time.sleep(5); ## para poder ver cuando ocurre el error
    driver.find_element(By.CSS_SELECTOR, "input.cart_button").click()  # Modificado
    driver.find_element(By.ID, "finish").click()
    assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
    #"No se puede agregar el Lastname, por lo que no deja seguir avanzando con el checkout"



def test_filter_functionality(driver):
    """
    Verifica la funcionalidad de filtro en la página de inventario con el usuario 'problem_user'.

    Pasos:
    1. Navega a la página principal e inicia sesión como 'problem_user'.
    2. En la página de inventario, registra el nombre del primer producto.
    3. Aplica un filtro de 'Name (Z to A)'.
    4. Registra nuevamente el nombre del primer producto.
    5. Verifica que el nombre del primer producto haya cambiado, indicando que el filtro se aplicó correctamente.

    Errores conocidos:
    Ningún tipo de filtro disponible funciona con este usuario.
    """
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("problem_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Obtiene el nombre del primer producto antes de aplicar el filtro
    product_name_before = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    
    # Selecciona la opción de filtro 'Name (Z to A)'
    filter_option = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    filter_option.select_by_visible_text("Name (Z to A)")
    
    # Obtiene el nombre del primer producto después de aplicar el filtro
    product_name_after = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    
    # Asegura que el nombre del primer producto haya cambiado después de aplicar el filtro
    assert product_name_before != product_name_after, f"El filtro no funcionó, nombre del ítem antes del filtro: {product_name_before}, es igual a después del filtro: {product_name_after}"





##ERRORES ENCONTRADOS
# Se puede realizar el proceso de compra sin seleccionar ningún artículo.
# No hay restricciones para la información del comprador, ej, la cantidad de caracteres que se pueden ingresar, una combinación de caracteres o números para los nombres.
# No se puede agregar más unidades de los artículos elegidos, solo 1 por artículo.
# Mensajes de errores extraños al iniciar sesión: "Epic sad face: You can only access '/cart.html' when you are logged in." o también
# Epic sad face: You can only access '/inventory.html' when you are logged in.

# Usando el PROBLEM USER se encontró lo siguiente:
# En el checkout no se puede agregar el Lastname, por lo que no deja seguir avanzando y da error.
# El filtro de nombres no funcionó, no se puede aplicar filtro.