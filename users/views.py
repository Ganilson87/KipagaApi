from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UsuarioForm
from django.views.generic.edit import CreateView
from .models import *
# Create your views here.



def login(request):
     
    return render(request, 'registration/login.html')

 
class cadastro(CreateView):
    template_name='registration/cadastro.html'
    form_class= UsuarioForm
    model = User
    success_url=reverse_lazy('login')

    def  get_context_data(self, *args, **kwargs):
        context=super().get_context_data(*args,**kwargs) 
        context['Titulo'] = 'Cadastro'
        context['botao'] = 'Cadastrar-me'
        return context
 