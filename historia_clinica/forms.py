from django import forms 
from .models import Historia_Clinica, Motivo_Consulta,Paciente,Medico,Genero, Enfermeria

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = Historia_Clinica
        fields = '__all__'
        exclude = ['flast_historia_clinica']
        widgets = {
            'paciente': forms.Select(attrs={'class':'form-control'}),
            'motivo_consulta': forms.Select(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','rows':3}),
        }
        

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        exclude = ['estado']
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','min_length':3}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'Date','class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control','min_length':3}),
            'telefono': forms.NumberInput(attrs={'class':'form-control'}),
            'genero': forms.Select(attrs={'class':'form-control'}),
            'historia_clinica': forms.TextInput(attrs={'readonly': 'readonly'}),
        
        }


class MedicoForm(forms.ModelForm): 
    class Meta: 
        model = Medico 
        fields = ['nombre', 'apellido', 'especialidad', 'telefono']

        

class Motivo_ConsultaForm(forms.ModelForm):
    class Meta:
        model = Motivo_Consulta
        fields = '__all__'
    
class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'
        
class EnfermeriaForm(forms.ModelForm):
    class Meta:
        model = Enfermeria
        fields = '__all__'
