from django.db import models


class Nota(models.Model):
    identificacion = models.IntegerField(null=True, blank=True)
    historia = models.IntegerField(null=True, blank=True)
    fecha_hora = models.DateTimeField(auto_now_add=True,null=True)
    nota_enfermeria = models.CharField(max_length=500, null=True, blank=True)
    usuario = models.CharField(max_length=500, null=True)
    medicamento=models.CharField(max_length=50,null=True)

    def __str__(self):
        return str(self.identificacion)

class Observacion(models.Model):
     nota = models.ForeignKey('Nota', related_name='observaciones', on_delete=models.CASCADE)
     texto = models.CharField(max_length=500, null=True, blank=True)
     fecha_horas=models.DateTimeField(auto_now_add=True,null=True)
     def __str__(self):
       return self.texto 
     


     
    






    