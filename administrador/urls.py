from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path("usuarios", usuario, name="usuario"),
    path("empresas", empresaView, name="empresa"),
    path("CriarEmpresa", cadastrarEmpresa, name="CriarEmpresa"),
    path("cadastrar", cadastrarUser, name="cadastrarUser"),
    path("usuarios/<str:pk>", UserDetailView, name="UserDetail"),
    path("usuarios/Deposito/<str:pk>", CreateDeposito, name="Deposito"),
    path("Deposito/<str:pk>", CreateDeposito, name="Deposito"),
    path("pdfDownload", pdfDownload, name="pdfDownload"),
    path("envite", envite, name="pdfDownload"),

]
