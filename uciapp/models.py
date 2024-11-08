from django.db import models
import random
import time

# Create your models here.

class SignosVitales(models.Model):
    frecuencia_cardiaca = models.IntegerField()
    tension_arterial_sistolica = models.IntegerField()
    tension_arterial_diastolica = models.IntegerField()
    saturacion_oxigeno = models.IntegerField()
    frecuencia_respiratoria = models.IntegerField()
    temperatura = models.DecimalField(max_digits=4, decimal_places=1)
    urgencia = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def simular_signos(self):
        self.frecuencia_cardiaca = random.randint(60, 100) + random.randint(-3, 3)
        self.tension_arterial_sistolica = random.randint(100, 140) + random.randint(-3, 3)
        self.tension_arterial_diastolica = random.randint(60, 90) + random.randint(-3, 3)
        self.saturacion_oxigeno = random.randint(95, 100) + random.randint(-1, 1)
        self.frecuencia_respiratoria = random.randint(10, 20) + random.randint(-1, 1)
        self.temperatura = round(random.uniform(36.5, 37.5), 1) + random.uniform(-0.3, 0.3)
        
        if self.urgencia:
            self.frecuencia_cardiaca = random.randint(150, 180)
            self.tension_arterial_sistolica = random.randint(180, 220)
            self.tension_arterial_diastolica = random.randint(120, 150)
            self.saturacion_oxigeno = random.randint(80, 90)
            self.frecuencia_respiratoria = random.randint(12, 18) + random.randint(-1, 1)
            self.temperatura = round(random.uniform(39.0, 40.0), 1)
            
        return self

    def __str__(self):
        return f"Signos vitales: FC={self.frecuencia_cardiaca} Tensión={self.tension_arterial_sistolica}/{self.tension_arterial_diastolica}mmHg SpO2={self.saturacion_oxigeno}% FR={self.frecuencia_respiratoria} Temp={self.temperatura}°C"
