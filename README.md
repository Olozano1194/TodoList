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

1. En la parte superior del repo, de clic al botón '**<> Code**' y copia la url que aparece
2. Abre tu terminal y ejecuta el comando, ojo debe estar en la carpeta donde usted desee que se clone el repo, ejemplo: en el escritorio o en documentos 
    - ```bash
        git clone url-del-repo
      ```
3. Luego de que el repo se clone, existe un archivo requirement.txt donde estará las dependencias que se necesitan para que el proyecto funcione.
4. En la terminal debemos colocar lo siguiente:
 - ```bash
     pip install -r requirements.txt
   ```
5. Tenemos que crear la base de datos en Worbench, nosotros la llamamos 'todolist', si no le gusta ese nombre, puede colocarle el que ustedes deseen, pero si le cambian el nombre más adelante tocará hacerle otras configuraciones.
6. Si le crearon la base de datos con otro nombre, toca dirigirse al archivo **settings.py**, y cambiarle el nombre de la base de datos que aparece en la siguiente parte:
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

### Configuración del proyecto

Si no desea clonar el repo y quiere comenzar desde cero, siga estaos pasos

1. se crea una carpeta raiz, con el nombre que usted desee, en mi caso le coloqué 'TodoList'
2. En la terminal, creamos el entorno virtual de la siguiente manera:
 - ```bash
    python -m venv entorno
   ```
3. Luego de crear el entorno virtual, debemos activarlo, para eso debemos 
 - ```bash
    .\entorno\Scripts\activate
   ```
4. Luego de activar el entorno virtual, procederemos a instalar las dependencias:
 - ```bash
        pip install django
   ```
5. En la terminal, nos dirigimos a la carpeta raiz creada anteriormente, y colocamos lo siguiente:
 - ```bash
    django-admin startproject todoList .
   ```
6. Luego de que termine de crear el proyecto, en el mismo terminar colocamos lo siguiente
 - ```python
    django-admin startapp todoListApp
   ```
7. Tenemos que crear la base de datos en Worbench, nosotros la llamamos 'todolist' o el nombre que ustedes deseen.
8. Nos dirigimos al archivo **settings.py**, buscamos donde dice DATABASE y en él colocamos lo siguiente:
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
9. Para que no nos de error, debemos instalar MySqlClient:
 - ```bash
        pip install mysqlclient
   ```
10. Estando en el archivo, nos dirigimos a **INSTALLED_APPS** y colocamos debajo de ultimas lo siguiente:
 - ```python
        'todoListApp',
   ```
10. Ahora nos apoyamos de los archivos del repo para agilizar las cosas, nos dirigimos a la carpeta todolistApp, que es donde vamos a hacer todas configuraciones de las vistas, las url y los modelos.
11. En el archivo **models.py** es el archivo donde crearemos todas las tablas de la base datos, colocamos lo siguiente:
 - ```python
        # Create your models here.
        class Task(models.Model):
            description = models.CharField(max_length=100)
            completed  = models.BooleanField(default=False)
            created_at = models.DateTimeField(auto_now_add=True)
            
            def __str__(self):
                return self.description
   ```
12. Luego de que termine de hacer las configuracion en ese archivo, nos toca hacer las migraciones:
 - ```bash
        python manage.py makemigrations
    ```
 - ```bash
        python manage.py migrate
    ```
13. Luego nos dirigimos al archivo **views.py** y colocamos lo siguiente:
 - ```python
        from django.shortcuts import render, redirect, get_object_or_404
        #from .forms import TaskForm
        from .models import Task

        # Create your views here.
        def index(request):
            list = Task.objects.all() #cogemos todos los datos de la tabla task y los guardamos en la variable
            taskList_remaining = list.filter(completed=False).count()
            context = {
                'taskList': list,
                'taskList_remaining': taskList_remaining
            }
    
            return render(request, 'index.html', context)

        def insert(request):
            error = None #inicializamos la variable error
            list = Task.objects.all() #cogemos todos los datos de la tabla task y los guardamos en la variable
            taskList_remaining = list.filter(completed=False).count()
            
            if request.method == 'POST': #preguntamos si ya se han enviado los datos
                taskDescription = request.POST.get('description','').strip() #guardamos los datos del input en la variable

                if not taskDescription: 
                    error = 'El Input no puede estar vacio'
                                
                else:
                    try: 
                        task = Task(description=taskDescription) #creamos una tarea, usando la descripcion proporsionada por el user
                        task.save() #se guarda en la bd
                        return redirect('index')
                    except Exception as e:
                        error = f'Ocurrió un error al guardar la tarea: {e}'

            #Definimos el contexto para el render
            context = {
                'taskList': list,
                'taskList_remaining': taskList_remaining,
                'error': error
            }   

            return render(request, 'index.html', context)

        def delete(request, id):
            tarea = Task.objects.get(id=id)
            tarea.delete()

            return redirect('index')

        def update(request, id):
            tarea= Task.objects.get(id=id) #obtenemos la tarea que se va a actualizar

            return render(request, 'update.html', {'tasks': tarea}) #redireccionamos a la pagina principal

        def actualizar(request, id): #esta funcion nos permite actualizar la tarea

            if request.method == "POST": #preguntamos si ya se han enviados los datos
                description = request.POST['description'] #guardamos los datos del input en la variable

                tarea = Task.objects.get(id=id) #obtenemos la tarea que se va a actualizar
                tarea.description = description #actualizamos la tarea
                tarea.save() #guardamos la tarea
                return redirect('index') #redireccionamos a la pagina principal

        def complete_task(request, id): 
            tarea = get_object_or_404(Task, pk=id)
            tarea.completed = not tarea.completed
            tarea.save()

            return redirect('index')
14. Luego creamos un archivo llamado **urls.py** donde tendremos las direcciones que mostraremos en el navegador:
 - ```python
        from django.urls import path
        from .views import index, insert, update, delete,actualizar, complete_task

        urlpatterns = [
            path('', index, name='index'),
            path('insert/', insert, name='insert'),
            path('update/<int:id>', update, name='update'),
            path('updateTask/<int:id>', actualizar, name='actualizarTarea'),
            path('delete/<int:id>', delete, name='delete'),
            path('complete/<int:id>', complete_task, name='completed')
        ]
   ```
15. Ahora creamos una carpeta llamada **static**, en esa carpeta deben ir todos los archivos **Css**, **Js** y **Imagenes**, ojo debemos llamarla así para que Django reconozca los estilos, scripts o imagenes.
16. Ahora creamos una carpeta llamada **templates**, donde van todos los archivos html.
17. Ahora salimos de esa carpeta y nos dirigimos a **todoList**, para hacer una ultima configuración y ejecutar el proyecto.
18. En el archivo **urls.py**, colocamos lo siguiente
 - ```python
        from django.urls import path, include
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('api/', include('todoListApp.urls')),
        ]
20. Luego de terminar esas configuraciones podemos ejecutar el proyecto:
 - ```bash
        python manage.py runserver 
    ```
21. Luego de que termine de ejecutar el proyecto, se abrirá una ventana en
http://127.0.0.1:8000/api/ donde podrá ver el proyecto funcionando. 

22. Dentro de la carpeta raiz, se crea un archivo llamado 'requirements.txt'
23. Dentro del arhivo van a estar las dependencias que se han instalado hasta el momento, para eso ejecutamos el siguiente comando en la terminal:
 - ```bash
        pip freeze > requirements.txt
   ```





 

