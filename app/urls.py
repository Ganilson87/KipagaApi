from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("", index , name="index"),
    path('Depositos', Depositos.as_view(), name="Depositos"),
    path('Transferencias', Transferencias.as_view(), name="Transferencias"),
    path("Token", TokenObtainPairView.as_view()),
    path("Token/Refresh", TokenRefreshView.as_view()),

    path('Deposito/<str:pk>', DepositoDetail.as_view()),
    path('users', Usuario.as_view(), name="users"),
    path('users/<str:pk>', usuarioDetail.as_view(), name="users"),
    path('usersByKI/<str:pk>', usuarioDetailById.as_view(), name="usersByKi"),
    path('notificacoes/<str:pk>', NotificationsDetail.as_view(), name="notificacoes"),
    path('notificacoes', notifys.as_view(), name="notificacoes"),
    
    path('notificacoesLido/<str:pk>', marcarLido.as_view(), name="notificacoes"),    
    ]
