from django import forms 
from .models import Receta, Medicamento


class RecetaForm(forms.ModelForm): 
    class Meta: 
      model = Receta 
      fields = ['medicamento', 'fecha', 'tratamiento', 'cantidad','cantidad_entregada']
     
class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = "__all__"

   