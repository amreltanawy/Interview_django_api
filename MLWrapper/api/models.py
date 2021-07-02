from django.db import models
from django.contrib.auth.models import AbstractUser


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
    ind_actividad_cliente = models.IntegerField(choices=ind_actividad_cliente_choices,default=2)
    tipodom = models.IntegerField(choices=tipodom_choices,default=0)
    indfall = models.CharField(max_length=1,choices=indfall_choices, default='O')
    conyuemp = models.CharField(max_length=1,choices=conyuemp_choices, default='O')
    indext = models.CharField(max_length=1,choices=indext_choices, default='O')
    indresi = models.CharField(max_length=1,choices=indresi_choices, default='O')
    tiprel_1mes = models.CharField(max_length=1,choices=tiprel_1mes_choices, default='O')
    indrel_1mes = models.CharField(max_length=1, choices=indrel_1mes_choices, default='O')
    indrel = models.IntegerField(choices=indrel_choices, default=2)
    age = models.FloatField(default=20)
    antiguedad = models.FloatField(default=0)
    rent = models.FloatField(default=101850)
    def __str__(self):
        return str(self.id)


class PredictionResult(models.Model):
    feature_set = models.ForeignKey('FeatureSet', blank=False, on_delete=models.CASCADE)
    # ind_ahor_fin_ult1= models.FloatField(default=0)
    # ind_aval_fin_ult1= models.FloatField(default=0)
    ind_cco_fin_ult1= models.FloatField(default=0)
    ind_cder_fin_ult1= models.FloatField(default=0)
    ind_cno_fin_ult1= models.FloatField(default=0)
    ind_ctju_fin_ult1= models.FloatField(default=0)
    ind_ctma_fin_ult1= models.FloatField(default=0)
    ind_ctop_fin_ult1= models.FloatField(default=0)
    ind_ctpp_fin_ult1= models.FloatField(default=0)
    ind_deco_fin_ult1= models.FloatField(default=0)
    ind_deme_fin_ult1= models.FloatField(default=0)
    ind_dela_fin_ult1= models.FloatField(default=0)
    ind_ecue_fin_ult1= models.FloatField(default=0)
    ind_fond_fin_ult1= models.FloatField(default=0)
    ind_hip_fin_ult1= models.FloatField(default=0)
    ind_plan_fin_ult1= models.FloatField(default=0)
    ind_pres_fin_ult1= models.FloatField(default=0)
    ind_reca_fin_ult1= models.FloatField(default=0)
    ind_tjcr_fin_ult1= models.FloatField(default=0)
    ind_valo_fin_ult1= models.FloatField(default=0)
    ind_viv_fin_ult1= models.FloatField(default=0)
    ind_nomina_ult1= models.FloatField(default=0)
    ind_nom_pens_ult1= models.FloatField(default=0)
    ind_recibo_ult1= models.FloatField(default=0)

    def __str__(self):
        return str(self.id)


class User(AbstractUser):
    """
    Overriding Abstract User
    """
    SUPER_ADMIN = 1
    STAFF = 2
    USER = 3

    USER_ROLE = (
        (SUPER_ADMIN, "super_admin"),
        (STAFF, 'staff'),
        (USER, 'user')
    )
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=USER_ROLE, default=3)
    username = models.EmailField(max_length=254, blank=False, null=False, unique=True)
    email = models.EmailField(max_length=254, blank=False, null=False, unique=True)
    is_email_verified = models.BooleanField(null=False, blank=False, default=False)
    is_blocked = models.BooleanField(null=False, blank=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.username)
