import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# pytest --html=report_functional.html test_functional.py

#Fixture para inicializar y finalizar el driver de Selenium.
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver 
    driver.quit()
   
   
    ############### TEST USANDO performance_glitch_user ####################### 
"""
    Prueba el tiempo que tarda en iniciar sesión en la página.
    Pasos:
    1. Navega a la página principal.
    2. Introduce las credenciales del usuario performance_glitch_user.
    3. Registra el tiempo antes de hacer clic en el botón de login.
    4. Hace clic en el botón de login y espera hasta que la página de inventario esté visible.
    5. Registra el tiempo después de que la página de inventario esté visible.
    6. Verifica que el tiempo total de inicio de sesión sea menor a 4 segundos.
    
    Errores conocidos:
    - Demasiado tiempo al cargar la página al iniciar sesión.
    """
def test_login_time(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("performance_glitch_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    start_time = time.time()
    driver.find_element(By.ID, "login-button").click()
    
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    
    end_time = time.time()
    load_time = end_time - start_time
    assert load_time < 4, f"El tiempo de inicio de sesión es muy alto: {load_time} segundos"



    """
    Prueba el rendimiento de navegación entre diferentes páginas del sitio.

    Pasos:
    1. Navega a la página principal e inicia sesión como performance_glitch_user.
    2. Registra el tiempo, navega al carrito y verifica que la página del carrito esté visible.
    3. Registra el tiempo y verifica que el tiempo total para navegar al carrito sea menor a 4 segundos.
    4. Registra el tiempo, vuelve a la página de inventario y verifica que la página de inventario esté visible.
    5. Registra el tiempo y verifica que el tiempo total para volver al inventario sea menor a 3 segundos.
    
    Errores conocidos:
    - Demasiado tiempo al cargar el inventario al presionar el botón "continuar comprando" desde el carrito de compras.
    """
def test_navigation_performance(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("performance_glitch_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Navegar al carrito
    start_time = time.time()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_list"))
    )
    end_time = time.time()
    navigation_time = end_time - start_time
    assert navigation_time < 4, f"El tiempo de navegación al ir al carrito es muy alto: {navigation_time} segundos"
    
    # Regresar a la página de inventario
    start_time = time.time()
    driver.find_element(By.ID, "continue-shopping").click()
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    end_time = time.time()
    navigation_time = end_time - start_time
    assert navigation_time < 3, f"El tiempo de navegación al volver al inventario es muy alto: {navigation_time} segundos"





##  ERRORS
# Demasiado tiempo al cargar la página al iniciar sesión.
# Demasiado tiempo al cargar el inventario al presionar el botón "continuar comprando" desde el carrito de compras.