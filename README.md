# DWES UT07 Dynamic Web App

*_Nota: La aplicación base se ha extraído de https://github.com/sync-david/curso-dwes/tree/main/UT-07/_

## Ejecución de la aplicación

Al acceder a la aplicación se cargan los datos del usuario por defecto:

![Carga inicial](./docs/imagen-1.png)

Podemos modificar cualquiera de los campos del formulario, incluyendo el número de teléfono, basta con hacer clic en "Click to Edit".

![Edición](./docs/imagen-2.png)

Una vez estamos satisfechos con los cambios, pulsamos el botón "Submit" y se guardan automáticamente.

![Guardado](./docs/imagen-3.png)

## Modificaciones

Se han realizado las modificaciones mínimas necesarias para cumplir con los requisitos de la tarea:

- En el archivo views.py se ha modificado la función de guardado para que recoja el nuevo campo de teléfono.

![Views.py](./docs/imagen-4.png)

- En el archivo models.py se ha incluido el nuevo campo de número de teléfono tanto en el usuario de ejemplo como en la función de update user.

![Models.py](./docs/imagen-5.png)

- En el archivo edit_form.html se ha incluido un nuevo input para el número de teléfono.

![Edit_form.html](./docs/imagen-6.png)

- En el archivo name_display.html se ha incluido una nueva etiqueta para poder mostrar el número de teléfono del usuario

![Name_display.html](./docs/imagen-7.png)