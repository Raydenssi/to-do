# Proyecto Integrador - To Do App Django

## Descripción
Esta aplicación web de lista de tareas está construida con Django y permite a los usuarios gestionar sus tareas diarias. Los usuarios pueden crear, visualizar, editar y eliminar tareas, todo dentro de una interfaz intuitiva y segura.

## Cómo empezar

### Requisitos previos
- Python 3.12 
- pip (Python package installer)

### Configuración del entorno
Para ejecutar este proyecto, instala las dependencias en un entorno virtual:

bash
python -m venv myenv
source myenv/bin/activate # En Windows use `myenv\Scripts\activate`
pip install -r requirements.txt

Configuración de la base de datos

Realiza las migraciones necesarias para configurar la base de datos:

bash

python manage.py makemigrations
python manage.py migrate

Creación de un superusuario

Crea un superusuario para acceder al panel de administración de Django:

bash

python manage.py createsuperuser

Ejecución del servidor de desarrollo

Para iniciar el servidor de desarrollo, ejecuta:

bash

python manage.py runserver
