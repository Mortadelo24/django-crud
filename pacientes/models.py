from django.db import models

# Create your models here.
#chises


sexo= [
    ("M", "Masculino"),
    ("F", "Femenino")

]

estado = [
    (True, "Activo"),
    (False, "No activo")

]
class Pacientes(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    peso = models.FloatField()
    sexo = models.CharField(choices=sexo, max_length=1)
    estado = models.BooleanField(choices=estado)

    def __str__(self):
        return f"{self.nombre}{self.apellido}"