from django.contrib import admin
from django.urls import path

from . import views

app_name = "departamento_app" # Etiqueta a todo el conjunto de urls, el nombre es una convención

urlpatterns = [
    path('new-departamento/',
         views.NewDepartamentoView.as_view(),
         name='nuevo_departamento'),
    path('departamento-lista',
         views.DepartamentoListView.as_view(),
         name='departamento_list'),
]