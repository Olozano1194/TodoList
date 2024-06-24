from django.shortcuts import render, redirect, get_object_or_404
from . forms import TaskForm
from . models import Task

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

    return render(request, 'index.html', {'error': error})

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