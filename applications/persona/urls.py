from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app" # Etiqueta a todo el conjunto de urls, el nombre es una convención 

urlpatterns = [
    path(
        '',
        views.InicioView.as_view(),
        name='inicio'
    ), 
    path('listar-todo-empleados/',
         views.ListAllEmpleados.as_view(),
         name = 'empleados_all'
    ),
    # path('lista-by-area/', views.ListByAreaEmpleado.as_view()),
    path('lista-by-area/<shortname>/',
         views.ListByAreaEmpleado.as_view(),
         name='empleados_area'
    ),   
    path('lista-empleados-admin/',
         views.ListaEmpleadosAdmin.as_view(),
         name='empleados_admin'
    ), 
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),   
    path('lista-habilidades-empleado/', views.ListHabilidadesEmpleado.as_view()),   
    path('ver-empleado/<pk>', #<pk> es obligatorio.. lo exige el DetailView
         views.EmpleadoDetailView.as_view(),
         name='empleado_detail'
    ),
            
    path(
        'add-empleado/',
        views.EmpleadoCreateView.as_view(),   
    # path('success/', views.SuccessView.as_view()),  
        name = 'empleado_add', 
    ),
    path(
        'success/',
        views.SuccessView.as_view(),
        name='correcto'
    ),   
    path(
        'update-empleado/<pk>/',   #<pk> es importante
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
    ),   
     path(
        'delete-empleado/<pk>/',   #<pk> es importante
        views.EmpleadoDeleteView.as_view(),
        name='eliminar_empleado'
    ),  
]