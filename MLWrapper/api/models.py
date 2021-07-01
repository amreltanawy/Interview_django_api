from django.db import models
from jsonfield import JSONField

# Create your models here.

class FeatureSet(models.Model):
    ind_empleado_choices = (
        ('N','N'),
        ('B','B'),
        ('F','F'),
        ('A','A'),
        ('S','S'),
        ('O','default')
    )
    sexo_choices = (
        ('V','V'),
        ('H','H'),
        ('O','default')
        )
    ind_nuevo_choices = (
        ('0',0),
        ('1',1),
        ('default',2) # invalid value
    )
    # starting here
    indrel_choices = (
        ('1',0),
        ('99',1),
        ('O',2)
    )
    indrel_1mes_choices = (
        ('O',0),
        ('1',1),
        ('2',2),
        ('3',3),
        ('4',4),
        ('P',5)
    )
    tiprel_1mes_choices = (
        ('O',0),
        ('I',1),
        ('A',2),
        ('P',3),
        ('R',4),
        ('N',5)
    )
    indresi_choices = (
        ('O',0),
        ('S',1),
        ('N',2)
    )
    indext_choices = (
        ('O',0),
        ('S',1),
        ('N',2)
    )
    conyuemp_choices = (
        ('O',0),
        ('S',1),
        ('N',2)
    )
    indfall_choices = (
        ('O',0),
        ('S',1),
        ('N',2)
    )
    tipodom_choices = (
        ('O',0),
        ('1',1)
    )
    ind_actividad_cliente_choices = (
        ('default',2),
        ('0',0),
        ('1',1)
    )
    segmento_choices = (
        ('default',2),
        ('02 - PARTICULARES',0),
        ('03 - UNIVERSITARIO',1),
        ('01 - TOP', 2)
    )
    
    ind_empleado = models.CharField(max_length=1, choices=ind_empleado_choices, default='X')
    sexo = models.CharField(max_length=1, choices=sexo_choices, default='default')
    ind_nuevo = models.IntegerField(choices=ind_nuevo_choices,default=2)
    pais_residencia = models.CharField(max_length=2, default='NA')
    canal_entrada = models.CharField(max_length=3, default='NA')
    segmento = models.CharField(max_length=40,choices= segmento_choices,default='default')
    ind_actividad_cliente = models.IntegerField(choices=segmento_choices,default=2)
    tipodom = models.IntegerField(choices=tipodom_choices,default=0)
    indfall = models.CharField(max_length=1,choices=indfall_choices, default='O')
    conyuemp = models.CharField(max_length=1,choices=conyuemp_choices, default='O')
    indext = models.CharField(max_length=1,choices=indext_choices, default='O')
    indresi = models.CharField(max_length=1,choices=indresi_choices, default='O')
    tiprel_1mes = models.CharField(max_length=1,choices=tiprel_1mes_choices, default='O')
    indrel_1mes = models.CharField(max_length=1, choices=indrel_1mes_choices, default='O')
    indrel = models.IntegerField(choices=indrel_choices, default=2)
    
    def __str__(self):
        return str(self.id)


class PredictionResult(models.Model):
    feature_set = models.ForeignKey('FeatureSet', blank=False, on_delete=models.CASCADE)
    result = JSONField()

    def __str__(self):
        return str(self.id)
