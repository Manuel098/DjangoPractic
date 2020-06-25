from django.db import models

class Alumno(models.Model):
    name = models.CharField('nombre', max_length=100)

class Materia(models.Model):
    name = models.CharField('nombre', max_length=100)

class AlMa(models.Model):
    k_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    k_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    calif = models.PositiveIntegerField('calificacion')

