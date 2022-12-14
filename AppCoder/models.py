from django.db import models
from django.contrib.auth.models import User

"""
Estudiantes (nombre, apellido, email)
Profesor (nombre, apellido, email, profesión)
Entregable (nombre, fechaDeEntrega,entregado)
Curso (nombre, comisión)
"""


class Estudiante(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'


class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()
    profesion = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'


class Curso(models.Model):
    nombre = models.CharField(max_length=128)
    comision = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.comision}'


class Entregable(models.Model):
    nombre = models.CharField(max_length=128)
    entregado = models.BooleanField()
    fecha_de_entrega = models.DateField()

    def __str__(self):
        return f'Se ve como dice el metodo __str__'


class Avatar(models.Model):
    # Vinculo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Subcaperta avatares de media :)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user}"
