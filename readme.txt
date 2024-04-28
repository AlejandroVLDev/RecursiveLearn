Este proyecto es el código recoge el código utilizado para el desarrollo de la práctica.

Se han realizado modificaciones en el archivo settings.py para que se pueda ejecutar el proyecto de forma fácil.

Cambios de seguridad: Se ha modificado el valor de DEBUG a True para que pueda servir los ficheros estáticos el programa.
Cambios en Apache y base de datos: Se ha eliminado la variable ALLOWED_HOSTS para el servidor Apache en settings.py, se ha sustituido la 
    variable DATABASES > default por una SqLite para poder tener los datos precargados en el proyecto.

Finalmente para ejecutar el proyecto seguir los siguientes pasos: en un equipo con Python instalado ejecutar:
    1º python -m venv env        # Este comando crea un entorno virtual para ejecutar python
    2º - ./env/Scripts/Activate.ps1         # Activa el entorno virtual en Sistema Opertivo Windows
       - source env/bin/activate            # Activa el entorno virtual en Sistema Opertivo Linux
    3º python .\recursive_learn\manage.py runserver         # ejecuta el servidor por defecto en el puerto 8000
    4º En un navegador acceder a http://localhost:8000
