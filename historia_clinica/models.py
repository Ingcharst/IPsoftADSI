import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Historia_Clinica(models.Model):
    numeroHclinica = models.CharField(max_length=50)
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            today = datetime.datetime.now().strftime('%d%m%Y')
            last_historia_clinica = Historia_Clinica.objects.all().order_by('id').last()
            if last_historia_clinica:
                new_id = last_historia_clinica.id + 1
            else:
                new_id = 1
            self.flast_historia_clinica = f"{today}-{new_id}"
        super(Historia_Clinica, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.paciente} - {self.fecha_creacion}'
    


class Genero (models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    

class Paciente(models.Model): 
    nombre = models.CharField(max_length=100) 
    fecha_nacimiento = models.DateField() 
    direccion = models.CharField(max_length=255) 
    telefono = models.CharField(max_length=15) 
    edad = models.CharField(max_length=25)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, default='Espera')
    historiaclinica= models.ForeignKey(Historia_Clinica, on_delete=models.CASCADE)

    def __str__(self): return self.nombre 

class Motivo_Consulta(models.Model):
    motivo = models.CharField(max_length=50)

    def __str__(self):
        return self.motivo

class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    

class Enfermeria(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'


