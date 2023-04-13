from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    bi = models.CharField(max_length=15,blank=True)
    foto = models.ImageField(verbose_name="", upload_to="static/images")
    # data = models.DateField( blank=True)
    provincia_choices = [
        ('Huila','huila'),
        ('Luanda','luanda'),
        ('Benguela','benguela'),
        ('Namibe','Namibe'),
    ]
    nivelChoices = [
        ('Ceo','Ceo'),
        ('Agente','Agente'),
        ('App','App'),
    
    ]
    genderChoices = [
        ('Masculino','Masculino'),
        ('Feminino','Feminino'),
    ]
    Telefone = models.CharField(max_length=14, unique=True)
    provincia = models.CharField( max_length=50)
    idKipaga = models.CharField( max_length=50)
    nivel = models.CharField(choices= nivelChoices , max_length=50)
    gender = models.CharField(choices= genderChoices , max_length=50)
    saldo = models.FloatField(default=0)
    endereco1 = models.CharField(max_length=50,blank=True)
    endereco2 = models.CharField(max_length=50,blank=True)
    verificado = models.BooleanField(default=False)
    isempresa = models.BooleanField(default=False)
    
      