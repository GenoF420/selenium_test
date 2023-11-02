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
# Demasiado tiempo al presionar el botón continuar comprando desde el carrito de compras.