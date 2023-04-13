from django.db import models
import uuid
from config.settings import AUTH_USER_MODEL
# Produtos

class Deposito(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    usuario = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    valor = models.FloatField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "Deposito"
        ordering = ['-timestamp']

        def __str__(self) -> str:
            return self.usuario.name
        
class empresa(models.Model):
    logo = models.ImageField( upload_to="static/images")
    nome = models.CharField( max_length=50)
    nif = models.CharField( max_length=50)
    usuario = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    tipo = models.CharField( max_length=50)
    Servico = models.CharField( max_length=50)
    provincia = models.CharField( max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    saldo = models.FloatField(default=0)
    isestado = models.BooleanField(default=False)
    idKipaga = models.CharField( max_length=50)

    class Meta:
        db_table = "empresa"
        ordering = ['-timestamp']

        def __str__(self) -> str:
            return self.nome    
    
class Transferencia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    sender = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='sender')
    receptor = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receptor')
    valor = models.FloatField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (" {} enviou Para {}".format(self.sender,self.receptor))
    class Meta:
        ordering = ['-timestamp']

    
class notify(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    conteudo = models.CharField(max_length=50)
    usuario = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    lido = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "notify"
        ordering = ['-timestamp']
