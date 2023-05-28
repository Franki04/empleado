from django.db import models

# Create your models here.
class Departamento(models.Model):
    #name = models.CharField('Nombre', max_length=50, blank=True, null=True) #Blank=True hace que el campo no sea obligatorio (blank solo para textos) / Null=True Utilizaremos este parámetro cuando sepamos que este campo no siempre va a traer un valor o cuando nuestro sistema no siempre va a registrar un valor en este campo y puede, en vez de ello, registrar un valor nulo que tal vez más adelante o en un siguiente proceso se actualizará.
    #name = models.CharField('Nombre', max_length=50, editable=False) # editable=False Campo no editable, es decir, que nadie puede acceder desde el administrador.
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre Corto', max_length=20, unique=True) # unique = True Le estoy indicando a Django que no quiero que se repita este campo en otros registros.
    anulate = models.BooleanField('Anulado', default=False)
    
    class Meta:
        verbose_name = 'Mi departamento'
        verbose_name_plural = 'Áreas de la empresa'
        ordering = ['name']
        # ordering = ['-name']
        unique_together = ['name', 'short_name']
    
    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.short_name