from django import forms
from .models import Nota, Observacion

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ('identificacion', 'historia',  'nota_enfermeria','usuario')

class ObservacionForm(forms.ModelForm):
    class Meta:
        model = Observacion
        fields = ['texto',]
        labels = {'texto': 'Nueva Observación'}
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 4, 'cols': 40,}),
            
        }
 
