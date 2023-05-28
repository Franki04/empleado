from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from applications.persona.models import Empleado
from .models import Departamento

from .forms import NewDepartamentoForm

# Create your views here.


class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name = 'departamentos'


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'
    
    def form_valid(self, form):
        print('************METODO form valid************')
        print('*****************************************')
        
        depa = Departamento( # crear una instancia de departamento porque es una foreighkey
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['shortname'],
        )
        depa.save()
        
        nombre = form.cleaned_data['nombre'] 
        apellido = form.cleaned_data['apellidos'] 
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1', # 1 = ADMINISTRADOR
            departamento=depa
        )
        return super(NewDepartamentoView, self).form_valid(form)