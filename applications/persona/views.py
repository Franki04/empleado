from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
) 

# models
from .models import Empleado #queryset
# forms
from .forms import EmpleadoForm

# Create your views here.

# Requerimientos proyecto
# 1.- Listar todos los empleados de la empresa
# 2.- Listar todos los empleados que pertenecen a un área de la empresa
# 3.- Listar los empleados por palabra clave
# 4.- Listar habilidades de los empleados
# 5.- Listar empleados por trabajo

class InicioView(TemplateView):
    """ vista que carga la pagina de inicio"""
    template_name = 'inicio.html'


class ListAllEmpleados(ListView): #ListView es la lista generica o toda lista basada en clases django
    template_name = 'persona/list_all.html' # Django busca en las apps la carpeta persona/list_all.html
    # model = Empleado #Con get_queryset ya no haria falta pasar el modelo empleado
    paginate_by = 4 #listar-todo_empleados?page=1
    ordering = 'first_name'
    # context_object_name = 'lista'
    context_object_name = 'empleados' #context_object_name => nos permite acceder a la lista que nos devuelve el queryset
    
    def get_queryset(self):
        print('***********************')
        palabra_clave = self.request.GET.get("kword", '') #Interceptar y traer todas las solicitudes que se han enviado al servidor
        lista = Empleado.objects.filter(
            # jorge = jo
            full_name__icontains=palabra_clave
        )
        # print('=====', palabra_clave)
        # print('lista resultado:', lista)
        return lista
    
    
class ListaEmpleadosAdmin(ListView): #ListView es la lista generica o toda lista basada en clases django
    template_name = 'persona/lista_empleados.html' # Django busca en las apps la carpeta persona/list_all.html
    # model = Empleado #Con get_queryset ya no haria falta pasar el modelo empleado
    paginate_by = 10 #listar-todo_empleados?page=1
    ordering = 'first_name'
    # context_object_name = 'lista'
    context_object_name = 'empleados' #context_object_name => nos permite acceder a la lista que nos devuelve el queryset
    model = Empleado # al no tener el queryset obligatoriamente tenemos que pasarlo 
    
    
class ListByAreaEmpleado(ListView): 
    """ lista empleados de un area """
    template_name = 'persona/list_by_area.html' # Django busca en las apps la carpeta persona/list_all.html
    # queryset = Empleado.objects.filter( # La peor forma de hacer un filtro !!!
    #     departamento__short_name='Contabilidad'
    # )
    context_object_name = 'empleados'
    
    def get_queryset(self):
        # el codigo que yo quiera
        area = self.kwargs['shortname'] # recoge los argumentos que se mandan a traves de la url
        lista = Empleado.objects.filter(
            # departamento__short_name='Contabilidad'
            departamento__short_name= area
        )
        
        return lista #Segun documentacion....este método tiene que retornar una lista

class ListEmpleadosByKword(ListView):
    """ lista empleados por palabra clave """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        print('***********************')
        palabra_clave = self.request.GET.get("kword", '') #Interceptar y traer todas las solicitudes que se han enviado al servidor
        lista = Empleado.objects.filter(
            first_name= palabra_clave
        )
        # print('=====', palabra_clave)
        # print('lista resultado:', lista)
        return lista
    
    
class ListHabilidadesEmpleado(ListView):
    """ lista habilidades de los empleados """
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        empleado = Empleado.objects.get(id=1) # solo quiero un registro, no un conjunto de registros (object.filter())
        print(empleado.habilidades.all())
        return empleado.habilidades.all()
    
    
class EmpleadoDetailView(DetailView):
    model = Empleado # Modelo recuperado por el parametro que se envia por la url <pk>
    template_name = "persona/detail_empleado.html"
    
    def get_context_data(self, **kwargs: Any): #Enviar alguna variable extra al template que no se contemple en los atributos del modelo
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        # toot de un proceso
        context['titulo'] = 'Empleado del mes'
        return context
    

class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    # fields = ['first_name', 'last_name', 'job']
    # fields = ('__all__') # Con esto nos traemos todos los campos del modelo
    # fields = [
    #     'first_name',
    #     'last_name',
    #     'job',
    #     'departamento',
    #     'habilidades',
    #     'avatar',
    # ]
    # success_url = '.' # (importante añadir) Donde redirecciona cuando se ha completado correctamente / '.' signigfica que se redirecciona a la misma pagina
    # success_url = '/success' # (importante añadir) 
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin') # (importante añadir)
    
    def form_valid(self, form): # una forma de interceptar el metodo form_valid o queremos q suceda algo mas despues del guardado o antes del guardado de un registro de nuestro modelo (este ejemplo: actualiza un atributo a partir de otros atributos)
        #logica del proceso
        empleado = form.save(commit=False) # solo realiza la instancia para empleado similar a la que va a ir a la base de datos
        # print(empleado)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save() # guarda el atributo full_name en la base de datos
        return super(EmpleadoCreateView, self).form_valid(form)
    
    
class EmpleadoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin') # (importante añadir)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('************METODO POST************')
        print('===================================')
        print('***********************************')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form): # una forma de interceptar el metodo form_valid o queremos q suceda algo mas despues del guardado o antes del guardado de un registro de nuestro modelo (este ejemplo: actualiza un atributo a partir de otros atributos)
        #logica del proceso
        print('************METODO form valid************')
        print('*****************************************')
        return super(EmpleadoUpdateView, self).form_valid(form)
   
    
class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html" # la funcion del template es la de preguntar al usuario si realmente quiere eliminar el registro
    model = Empleado
    success_url = reverse_lazy('persona_app:empleados_admin') # (importante añadir)