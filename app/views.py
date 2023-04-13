from django.shortcuts import render
from rest_framework.response import Response
from config.settings import AUTH_USER_MODEL
from django.contrib.auth.decorators import login_required
from rest_framework import status, generics
from .models import *
from .serielizer import *
import math
from datetime import datetime
from users.models import User
# Create your views here.
@login_required()
def index(request):
    
    
    return render(request, "index.html")
class usuarioDetail(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_usuario(self, pk):
        try:
            return User.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        usuario = self.get_usuario(pk=pk)
        if usuario == None:
            return Response({"status": "fail", "message": f"usuario with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(usuario)
        return Response({"status": "success", "User": serializer.data})
class usuarioDetailById(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_usuario(self, pk):
        try:
            return User.objects.filter(idKipaga=pk).get()

        except:
            return None

    def get(self, request, pk):
        usuario = self.get_usuario(pk=pk)
        if usuario == None:
            return Response({"status": "fail", "message": f"usuario with KipagaID: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(usuario)
        return Response({"status": "success", "User": serializer.data})
class Usuario(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        Users = User.objects.all()
        total_Users = Users.count()
        if search_param:
            se = Users.filter(usuario__icontains=search_param)
        serializer = self.serializer_class(Users[start_num:end_num], many=True)
        return Response({
            "User": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"User": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
class Depositos(generics.GenericAPIView):
    serializer_class = DepositoSerializer
    queryset = Deposito.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("usuario")
        Depositos = Deposito.objects.all()
        total_Depositos = Depositos.count()
        if search_param:
            Depositos = Depositos.filter(usuario=search_param)
        serializer = self.serializer_class(Depositos[start_num:end_num], many=True)
        return Response({
            "Depositos": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            valor = dict(serializer.data).get('valor')
            user_id = dict(serializer.data).get('usuario')
            print(valor,user_id)
            usuario = User.objects.filter(id=user_id)
            # print(usuario.get().saldo)
            dados_user = usuario.get()
            dados_user.saldo += valor
            dados_user.save()
            print(usuario.get().saldo)

            return Response({"Deposito": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
class DepositosByUsuario(generics.GenericAPIView):
    serializer_class = DepositoSerializer
    queryset = Deposito.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("usuario")
        Depositos = Deposito.objects.all()
        total_Depositos = Depositos.count()
        if search_param:
            Depositos = Depositos.filter(usuario__icontains=search_param)
        serializer = self.serializer_class(Depositos[start_num:end_num], many=True)
        return Response({
            # "status": "success",
            # "total": total_Depositos,
            # "page": page_num,
            # "last_page": math.ceil(total_Depositos / limit_num),
            "Depositos": serializer.data
        })

class DepositoDetail(generics.GenericAPIView):
    queryset = Deposito.objects.all()
    serializer_class = DepositoSerializer

    def get_Deposito(self, pk):
        try:
            return Deposito.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        Deposito = self.get_Deposito(pk=pk)
        if Deposito == None:
            return Response({"status": "fail", "message": f"Deposito with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(Deposito)
        return Response({"status": "success", "Deposito": serializer.data})

    def patch(self, request, pk):
        Deposito = self.get_Deposito(pk)
        if Deposito == None:
            return Response({"status": "fail", "message": f"Deposito with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            Deposito, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "Deposito": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Deposito = self.get_Deposito(pk)
        if Deposito == None:
            return Response({"status": "fail", "message": f"Deposito with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        Deposito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Depositos FIM


#TRANFERENCIAS INICIO

class Transferencias(generics.GenericAPIView):
    serializer_class = TransferenciaSerializer
    queryset = Transferencia.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        Transferencias = Transferencia.objects.all()
        total_Transferencias = Transferencias.count()
        if search_param:
            Transferencias = Transferencias.filter(usuario__icontains=search_param)
        serializer = self.serializer_class(Transferencias[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_Transferencias,
            "page": page_num,
            "last_page": math.ceil(total_Transferencias / limit_num),
            "Transferencias": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            valor = dict(serializer.data).get('valor')
            sender_id = dict(serializer.data).get('sender')
            receiver_id = dict(serializer.data).get('receptor')
            sender = User.objects.filter(id=sender_id)
            receiver = User.objects.filter(id=receiver_id)
            # print(usuario.get().saldo)
            print("De ",sender,"para",receiver)

            dados_sender = sender.get()
            if(dados_sender.saldo < valor):
                return Response({"status": "saldo", "message": f"insuficiente"}, status=status.HTTP_404_NOT_FOUND)
            if(sender_id == receiver_id ):
                return Response({"status": "dados", "message": f"Está usando mesmo a ID Kipaga!"}, status=status.HTTP_401_UNAUTHORIZED)
            
            dados_receiver = receiver.get()
            dados_sender.saldo -= valor
            dados_receiver.saldo += valor
            dados_sender.save()
            dados_receiver.save()
            
            notifyTitle = "{} {} fez uma transferencia de {} Kz para a sua conta!".format(dados_sender.first_name, dados_sender.last_name,valor)

            notificacao = notify()
            notificacao.conteudo = notifyTitle
            notificacao.usuario = receiver.get()
            notificacao.save()
            notifyTitle2 = "Transferencia realizada com sucesso!"

            notificacao2 = notify()
            notificacao2.conteudo = notifyTitle2
            notificacao2.usuario = sender.get()
            notificacao2.save()
            print("Uma transferencia realizada!")
            return Response({"Transferencia": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


#TRANSFERENCIAS FIM
#Notificações
class notifys(generics.GenericAPIView):
    serializer_class = NotificationSerializer
    queryset = notify.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("usuario")
        notifys = notify.objects.all()
        total_notifys = notifys.count()
        if search_param:
            notifys = notifys.filter(usuario=search_param)
        serializer = self.serializer_class(notifys[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_notifys,
            "page": page_num,
            "last_page": math.ceil(total_notifys / limit_num),
            "notifys": serializer.data,
        },status=status.HTTP_200_OK
)

class NotificationsDetail(generics.GenericAPIView):
    serializer_class = NotificationSerializer
    queryset = notify.objects.all()

    def get_Notifications(self, pk):
        try:
            return notify.objects.filter(usuario=pk).all()

        except:
            return None

    def get(self, request, pk):
        Notifications = self.get_Notifications(pk=pk)
        if Notifications == None:
            return Response({"status": "fail", "message": f"Não foi encontrada nenuma notificação com o Id: {pk} "}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(Notifications)
        return Response({"status": "success", "notify": serializer.data})
class marcarLido(generics.GenericAPIView):
    serializer_class = NotificationSerializer
    queryset = notify.objects.all()

    def get_Notifications(self, pk):
        try:
            data = notify.objects.filter(id=pk)
            data.lido = True
            data.save()
            return notify.objects.filter(id=pk).get()

        except:
            return None

    def get(self, request, pk):
        Notifications = self.get_Notifications(pk=pk)
        if Notifications == None:
            return Response({"status": "fail", "message": f"Não foi encontrada nenuma notificação com o Id: {pk} "}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(Notifications)
        return Response({"status": "success", "notify": serializer.data})
#Notificações FIM