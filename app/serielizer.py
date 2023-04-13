from rest_framework import serializers
from .models import *
from config.settings import AUTH_USER_MODEL
from users.models import User
from django.utils.translation import gettext_lazy as _

class DepositoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposito
        fields = ['valor', 'timestamp','usuario','id','timestamp']
class TransferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transferencia
        fields = ['valor', 'sender','receptor','id']
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = notify
        fields = ['id','conteudo', 'usuario','lido','timestamp']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id','first_name', 'last_name','foto','bi','Telefone','provincia','endereco1', 'endereco2','gender','email','username', 'saldo','idKipaga']