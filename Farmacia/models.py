import datetime
from django.db import models
from historia_clinica.models import Paciente
from django.contrib.auth.models import User
# Create your models here.

class Proveedores(models.Model):
     nit = models.CharField(max_length=20)
     proveedor = models.CharField(max_length=50)
     direccion = models.CharField(max_length=100)
     telefono = models.CharField(max_length=50)
     celular = models.CharField(max_length=50)
     email = models.EmailField(max_length=100)

     def _str_(self):
         return self.proveedor


class Laboratorio(models.Model):
    cod_lab = models.CharField(max_length=10)
    laboratorio = models.CharField(max_length=50)
    def _str_(self):
        return self.laboratorio


    
class Presentacion(models.Model):
   cod_presentacion = models.CharField(max_length=5)
   presentacion = models.CharField(max_length=20)
   def _str_(self):
      return self.presentacion
   
class Unidad(models.Model):
    cod_und = models.CharField(max_length=5)
    nombre_und = models.CharField(max_length=20)

    def _str_(self):
         return self.nombre_und


class Categoria(models.Model):
     cod_Cat = models.CharField(max_length=10)
     categoria = models.CharField(max_length=50)

     def _str_(self):
         return self.categoria


class Medicamento(models.Model): 
    nombre = models.CharField(max_length=100) 
    referencia = models.CharField(max_length=10)
    descripcion = models.TextField() 
    componente = models.CharField(max_length=100)
    concentracion = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
    stock = models.IntegerField() 
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    lote = models.CharField(max_length=10)
    vencimiento = models.DateTimeField()
    def __str__(self): 
       return self.nombre 
        
    class Meta: 
       permissions = [ ("can_access_farmacia", "Can access farmacia module"), ]




    



    
class Receta(models.Model): 
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE) 
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE) 
    fecha = models.DateTimeField()
    cantidad = models.CharField(max_length=50)
    tratamiento = models.TextField()
    estado = models.CharField(max_length=50, default='Falta de medicamento')
    cantidad_entregada = models.CharField(max_length=50, default=0)
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    
    def __str__(self): 
        return f'{self.paciente} - {self.medicamento} - {self.cantidad_entregada}'

class Tipo_mov(models.Model):
   cod_tipo = models.SmallIntegerField()
   tipo = models.CharField(max_length=20)

   def _str_(self):
     return self.tipo

class Movimientos(models.Model):
    num_factura = models.IntegerField()
    tipo = models.ForeignKey(Tipo_mov, on_delete=models.CASCADE)
    usuario = models.IntegerField()
    tercero = models.IntegerField()
    referencia = models.IntegerField()
    cantidad = models.IntegerField()
    fecha = models.DateField()

    def _str_(self):
        return self.num_factura + " " + self.fecha

class Insumos(models.Model):
    nombre = models.CharField(max_length=100)
    referencia = models.CharField(max_length=10)
    descripcion = models.TextField()
    

class Factura(models.Model): 
    numero_factura = models.CharField(max_length=50)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medicamentos = models.ManyToManyField(Medicamento) 
    fecha = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            today = datetime.datetime.now().strftime('%d%m%Y')
            last_numero_factura = Factura.objects.all().order_by('id').last()
            if last_numero_factura:
                new_id = last_numero_factura.id + 1
            else:
                new_id = 1
            self.factura_medicamento = f"{today}-{new_id}"
        super(Factura, self).save(*args, **kwargs)
    

# ////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#                          Modulos de Yorla 
# ////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# from django.db import models # type: ignore

# # Create your models here.
#






    


# class Tipo_mov(models.Model):
#     cod_tipo = models.SmallIntegerField()
#     tipo = models.CharField(max_length=20)

#     def _str_(self):
#         return self.tipo
    




# class Movimientos(models.Model):
#     num_factura = models.IntegerField()
#     tipo = models.ForeignKey(Tipo_mov, on_delete=models.CASCADE)
#     usuario = models.IntegerField()
#     tercero = models.IntegerField()
#     referencia = models.IntegerField()
#     cantidad = models.IntegerField()
#     fecha = models.DateField()

#     def _str_(self):
#         return self.num_factura + " " + self.fecha