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
