from django.db import models

from applications.departamento.models import Departamento

from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'
        
    def __str__(self):
        return str(self.id) + '-' + self.habilidad
    

# Create your models here.
class Empleado(models.Model):
    """ Modelo para empleado """
    
    JOB_CHOICES = (
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','TECNICO'),
        ('4','OTRO'),
    )
    # Contador
    # Administrador
    # Economista
    # Tecnico
    # Otro
    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60) 
    full_name = models.CharField( # la contatenacion de first_name y last_name
        'Nombres Completos',
        max_length=120,
        blank=True #No es obligatorio
    )
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True) # python -m pip install Pillow
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    
    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name