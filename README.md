Este repositorio contiene pruebas automatizadas utilizando Selenium y Pytest para la aplicación . El conjunto de pruebas abarca el recorrido de un usuario en la aplicación, centrándose en varias funcionalidades.

Prerrequisitos
Python instalado
Biblioteca Selenium
Biblioteca Pytest
Chrome WebDriver
Instalación
Clona el repositorio:
bash
Copy code
git clone
Instala las dependencias:
bash
Copy code
pip install -r requirements.txt
Ejecución de las Pruebas
Asegúrate de que el Chrome WebDriver esté instalado y disponible en el PATH del sistema. Ejecuta el siguiente comando para realizar las pruebas:

bash
Copy code
pytest test_pruebas.py
Detalles de las Pruebas
El script de prueba (test_pruebas.py) realiza las siguientes acciones en la aplicación web de Urban routes:

Abre la aplicación en https://f8b519be-157b-4192-b008-7cd120a03f4c.serverhub.tripleten-services.com?lng=es/.
Navega a través de varios pasos, como seleccionar ubicaciones, ingresar detalles e interactuar con botones.
Valida el recorrido del usuario verificando elementos y comportamientos esperados.
Entorno de Pruebas
Sistema Operativo 
Navegador: Google Chrome (versión del WebDriver X.X.X)
Solución de Problemas
Si las pruebas fallan, asegúrate de que:

La aplicación está en ejecución y es accesible.
Chrome WebDriver está instalado correctamente y en el PATH del sistema.
Las dependencias están instaladas utilizando el archivo requirements.txt proporcionado.
Contribuciones
Siéntete libre de contribuir a este proyecto abriendo problemas o enviando solicitudes de extracción. Tu retroalimentación y contribuciones son muy apreciadas.

¡Felices pruebas!






