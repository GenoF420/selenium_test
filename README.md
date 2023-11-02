# Testing de la página Sauce Demo con Selenium

## Descripción
Este proyecto contiene una serie de pruebas automatizadas escritas en Python utilizando Selenium WebDriver para verificar la funcionalidad y el rendimiento de la página web Sauce Demo.

## Pruebas Funcionales
Las pruebas funcionales aseguran que las funcionalidades de la página funcionen según lo previsto. Las pruebas incluyen:

- **test_successful_login:** Verifica que un usuario pueda iniciar sesión con credenciales válidas.
- **test_logout:** Verifica que un usuario pueda cerrar sesión exitosamente.
- **test_successful_checkout:** Verifica que un usuario pueda completar el proceso de checkout.
- **test_filter_functionality:** Verifica la funcionalidad de filtrar productos por nombre.

## Pruebas No Funcionales
Las pruebas no funcionales se enfocan en el rendimiento y la estabilidad de la página. Incluyen:

- **test_login_time:** Mide el tiempo que tarda en iniciar sesión en la página y asegura que sea menor a 4 segundos.
- **test_navigation_performance:** Evalúa el tiempo de navegación al carrito y de regreso al inventario, asegurando que sean menores a 4 y 3 segundos respectivamente.

## Errores Conocidos:
- En el checkout no se puede agregar el Lastname, por lo que no deja seguir avanzando y da error.
- El filtro de nombres no funcionó, no se puede aplicar filtro.
- Demasiado tiempo al cargar la página al iniciar sesión.
- Demasiado tiempo al cargar el inventario al presionar el botón "continuar comprando" desde el carrito de compras.
- No se puede agregar el Lastname en el checkout, lo que impide completar el proceso.
- Se puede realizar el proceso de compra sin seleccionar ningún artículo.


## Dependencias
- Python 3.x
- Selenium WebDriver
- pytest (para ejecutar y organizar las pruebas)

## Ejecución de las Pruebas
Para ejecutar las pruebas, usa el siguiente comando en la terminal en la raíz del proyecto:

```bash
pytest --html=report_functional.html test_functional.py
