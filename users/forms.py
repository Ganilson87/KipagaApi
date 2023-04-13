from django.contrib import auth
from django.forms import *
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
class UsuarioForm(UserCreationForm):
    email= EmailField(max_length=50 )
    first_name= CharField(max_length=50)
    last_name= CharField(max_length=50)
    nivel_choices = [
        ('Tecnico de Manutençao','tec'),
        ('CEO','ceo'),
        ('Funcionario','Funcionario')
    ]
    Nivel = ChoiceField(choices=nivel_choices)    
    class Meta:
        model = User
        fields= ['username','first_name','Nivel','last_name','email']

    

 
class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        Model = User


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        Model = User
        