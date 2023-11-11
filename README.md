# Testing de la página Sauce Demo con Selenium

## Descripción
Este proyecto contiene una serie de pruebas automatizadas escritas en Python utilizando Selenium WebDriver para verificar la funcionalidad y el rendimiento de la página web Sauce Demo.

## Pruebas Funcionales
Las pruebas funcionales aseguran que las funcionalidades de la página funcionen según lo previsto. Las pruebas incluyen:

- **test_failed_login:** Verifica que un usuario con credenciales inválidas reciba un mensaje de error.
- **test_logout:** Verifica que un usuario pueda cerrar sesión exitosamente.
- **test_failed_login:**     Verifica que un usuario con credenciales inválidas reciba un mensaje de error.
- **test_add_product_to_cart:** Verifica que se pueda añadir un producto al carrito exitosamente.
- **test_remove_product_from_cart:** Verifica que un producto pueda ser removido del carrito exitosamente.
- **test_verify_product_details:** Verifica que el detalle de un producto se muestre correctamente.
- **test_verify_product_price_in_cart:** Verifica que el precio del producto en la página de inventario coincida con el precio mostrado en el carrito.
- **test_verify_continue_shopping_button:** Verifica que el botón 'Continuar comprando' redirija al usuario de vuelta a la página de inventario.
- **test_successful_checkout:** Verifica que el proceso de checkout se complete exitosamente.
- **test_successful_checkout (problem_user):** Verifica que el usuario 'problem_user' pueda completar el proceso de checkout.
- **test_filter_functionality:** Verifica que un usuario pueda cerrar sesión exitosamente.
- **test_logout:** Verifica la funcionalidad de filtro en la página de inventario con el usuario 'problem_user'.


## Pruebas No Funcionales
Las pruebas no funcionales se enfocan en el rendimiento y la estabilidad de la página. Incluyen:

- **test_login_time:** Mide el tiempo que tarda en iniciar sesión en la página y asegura que sea menor a 4 segundos.
- **test_navigation_performance:** Evalúa el tiempo de navegación al carrito y de regreso al inventario, asegurando que sean menores a 4 y 3 segundos respectivamente.

## Errores Conocidos(6):
- En el checkout no se puede agregar el Lastname, por lo que no deja seguir avanzando y da error.
- El filtro de nombres no funcionó, no se puede aplicar filtro.
- Demasiado tiempo al cargar la página al iniciar sesión.
- Demasiado tiempo al cargar el inventario al presionar el botón "continuar comprando" desde el carrito de compras.
- No se puede agregar el Lastname en el checkout, lo que impide completar el proceso.
- Se puede realizar el proceso de compra sin seleccionar ningún artículo.
  
## Dependencias
- Python 3.x
- pytest~=7.4.3
- selenium~=4.15.2
- pytest-html~=3.1.1
- py~=1.11.0

## Ejecución de las Pruebas
Para ejecutar las pruebas, usa el siguiente comando en la terminal en la raíz del proyecto:

Funcional:
```bash
pytest --html=report_functional.html --css=style.css  test_functional.py
```
No Funcional:
```bash
pytest --html=report_functional.html --css=style.css test_functional.py
