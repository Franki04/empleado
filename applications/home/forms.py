from django import forms

from .models import Prueba


class PruebaForm(forms.ModelForm):
    
    class Meta:
        model = Prueba
        # fields = ('__all__') #utilizar todos los atributos del modelo Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad'
        )
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese texto aqui',
                    'class': 'titulo'
                }
            )
        }
        
    def clean_cantidad(self): # la palabra clean_ es obligatorio
        cantidad = self.cleaned_data['cantidad'] # recuperar el valor cantidad que hay dentro del formulario
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un número mayor a 10')
        
        return cantidad