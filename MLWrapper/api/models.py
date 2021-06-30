from django.db import models

# Create your models here.

class FeatureSet(models.Model):
    ind_empleado_choices = (
        ('N',1),
        ('B',2),
        ('F',3),
        ('A',4),
        ('S',5),
        ('X',0)
    )
    sexo_choices = (
        ('V',0),
        ('H',1),
        ('O',2)
        )
    ind_nuevo_choices = (
        ('0',0),
        ('1',1),
        ('9',2) # invalid value

    )
    ind_empleado = models.CharField(max_length=1, choices=ind_empleado_choices, default='X')
    sexo = models.CharField(max_length=1, choices=sexo_choices, default='O')
    ind_nuevo = models.IntegerField(choices=ind_nuevo_choices,default=2)


class PredictionResult(models.Model):
    pass