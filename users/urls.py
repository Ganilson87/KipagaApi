from django.urls import path 
from .views import *
urlpatterns = [
    path('cadastro/', cadastro.as_view(), name="cadastro")
]
