<h1 aling='center'>To Do List</h1>

Este proyecto fue desarrollado como parte de una Prueba técnica. Se centra en la creación de una aplicación web de gestión de tareas, que permite a los usuarios gestionar efectivamente las tareas diarias, mejorando la organizaión y productividad.

La aplicación permite a los usuarios:

- Crear tareas
- Eliminar tareas
- Marcar tareas como completadas
- Actualizar la descripción de las tareas
- Leer la lista de las tareas existentes

## Tecnologías Utilizadas

- HTML5
- CSS3
- Django
- Python
- MySql

## Tutorial: Creación de una Aplicación de Lista de Tareas con Django y MySql

### Requisitos Previos

Antes de comenzar, asegurate de tener instalado lo siguiente:

- Python
- Editor de texto o IDE "Visual Studio Code"
- Conocimientos básicos de Html y Css
- Conocimientos básicos de Django y MySql
- Instalar MySql (Worbench) en tu sistema operativo.

## Clonar Repositorio

Si quiere clonar el repositorio para no tener que empezar desde cero, haga lo siguiente:

1. En la parte superior del repo, de clic al botón '<> Code' y copia la url que aparece
2. Abre tu terminal y ejecuta el comando, ojo debe estar en la carpeta donde usted desee que se clone el repo, ejemplo: en el escritorio o en documentos 
    - ```bash
        git clone url-del-repo
      ```
3. Luego de que el repo se clone, dejaré un archivo requirement.txt donde estará las dependencias que se necesitan para que el proyecto funcione.
4. En la terminal debemos colocar lo siguiente:
 - ```bash
     pip install -r requirements.txt
   ```
5. Tenemos que crear la base de datos en Worbench, nosotros la llamamos 'todolist', si no le gusta ese nombre, puede colocarle el que ustedes deseen, pero si le cambian el nombre más adelante tocará hacerle otras configuraciones.
6. Si le crearon la base de datos con otro nombre, toca dirijirse al archivo **settings.py**, y cambiarle el nombre de la base de datos que aparece en la siguiente parte:
 - ```bash
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'nombre-de-la-base-de-datos', # nombre de la base de datos
                'USER': 'nombre-de-usuario', # nombre de usuario
                'PASSWORD': 'contraseña', # contraseña
                'HOST': 'localhost', # servidor
                'PORT': '3306', # puerto
            }
        }
   ```

7. Luego de que termine de hacer las configuracion en ese archivo, nos toca hacer las migraciones:
 - ```bash
        python manage.py makemigrations
    ```
 - ```bash
        python manage.py migrate
    ```

8. Luego de terminar esas configuraciones podemos ejecutar el proyecto:
 - ```bash
        python manage.py runserver 
    ```
9. Luego de que termine de ejecutar el proyecto, se abrirá una ventana en
http://127.0.0.1:8000/api/ donde podrá ver el proyecto funcionando.

### Instalación de Dependencias

Si no desea clonar el repo y quiere comenzar desde cero, siga estaos pasos

1. se crea una carpeta raiz, con el nombre que usted desee, en mi caso le coloqué 'TodoList'
2. En la terminal, nos dirigimos a la carpeta que acabamos de crear, y colocamos los siguiente:
 - ```bash
    django-admin startproject todoList .
   ```
3. Luego de que termine de crear el proyecto, en el mismo terminar colocamos lo siguiente
 - ```python
    python manage.py startapp todoListApp
   ```


2. Dentro de la carpeta raiz, se crea un archivo llamado 'requirements.txt'




 

