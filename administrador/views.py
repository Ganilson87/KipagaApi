from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
import qrcode
import os
from django.shortcuts import redirect
from reportlab.lib.units import cm
from reportlab.lib import colors
from rest_framework import status, generics
from app.serielizer import UserSerializer
from django.shortcuts import redirect

# Create your views here.
from config.settings import EMAIL_HOST_USER
import random
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from app.models import Transferencia, Deposito, notify, empresa
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


@login_required()
def index(request):
    users = User.objects.filter(nivel="App")

    n_user = len(users)
    context = {
        "users": users,
        "n_user": n_user,
    }
    return render(request, "index.html", context=context)


@login_required()
def usuario(request):
    users = User.objects.filter(nivel="App")

    n_user = len(users)
    print(n_user)

    context = {
        "users": users,
        "n_user": n_user,
    }

    return render(request, "user.html", context=context)


@login_required()
def empresaView(request):
    
    empresas = empresa.objects.all()
    context= {
        "empresas":empresas
    }
    return render(request, "empresa.html", context=context)


@login_required()
def transferencia(request):
    return render(request, "empresa.html")


def send_email(to, subject, template_name, context):
    html_message = render_to_string(template_name, context)
    send_mail(
        subject,
        '',
        EMAIL_HOST_USER,
        [to],
        html_message=html_message,
    )
    print("ENVIADO")


@login_required()
def cadastrarUser(request):
    context = {}
    if request.method == "POST":
        data = request.POST.copy()
        print(data)
        numero = random.randint(100000, 500000)
        numero2 = random.randint(100000, 500000)
        ki = "Ki{}".format(numero2)
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        image = data.get('image')
        email = data.get('email')
        bi = data.get('bi')
        telefone = data.get('telefone')
        provincia = data.get('provincia')
        nivel = data.get('nivel')
        gender = data.get('gender')
        endereco1 = data.get('endereco1')
        endereco2 = data.get('endereco2')
        novo = User()
        novo.first_name = first_name
        novo.foto = image
        novo.username = email
        novo.last_name = last_name
        novo.email = email
        novo.bi = bi
        novo.set_password("{}".format(numero))
        novo.Telefone = telefone
        novo.provincia = provincia
        novo.nivel = nivel
        novo.idKipaga = ki
        novo.gender = gender
        novo.endereco1 = endereco1
        print(numero)
        novo.endereco2 = endereco2
        novo.save()
        notifyTitle = "Olá {} seja bem vindo ao Universo Kipaga!".format(
            novo.first_name)

        notificacao = notify()
        notificacao.conteudo = notifyTitle
        notificacao.usuario = novo
        notificacao.save()
        para = email
        subject = ("Kipaga - Seja bem vindo!")
        template_name = "emailWelcome.html"

        imagem = qrcode.make('{}'.format(novo.idKipaga))

        imagem.save('static/images/{}.png'.format(bi))
        dados = {
            "password": numero,
            "nome": novo.first_name,
        }
        # send_email(
        #     to=para,
        #     subject=subject,
        #     template_name=template_name,
        #     context=dados,
        # )
        return redirect("usuario")

    return render(request, "userCadastro.html")

# class UserDetailView(DetailView):
#     model = User()
#     template_name = "UserDetial.html"


def UserDetailView(request, pk):

    Usuario = User.objects.get(id=pk)
    transferencias = Transferencia.objects.filter(sender=pk)

    context = {
        "object": Usuario,
        "transferencias": transferencias,
    }

    return render(request, "UserDetial.html", context=context)


def CreateDeposito(request, pk):

    Usuario = User.objects.get(id=pk)

    context = {
        "object": Usuario,
    }

    if request.method == "POST":
        data = request.POST.copy()
        print(data)
        user_id = Usuario.id
        valor = data.get("valor")
        print(valor)
        novo = Deposito()
        novo.usuario = Usuario
        novo.valor = valor
        novo.save()
        saldo_user = novo.usuario.saldo
        deposito = novo.valor
        convert = float(deposito)
        # saldo_user += deposito
        novo.usuario.saldo += convert
        novo.usuario.save()
        print(type(saldo_user))
        print(type(convert))

        notifyTitle = "{} um deposito foi realizado para a sua conta Kipaga com o valor de {} AOA!".format(
            novo.usuario.first_name, novo.valor)

        notificacao = notify()
        notificacao.conteudo = notifyTitle
        notificacao.usuario = Usuario
        notificacao.save()
        para = novo.usuario.email
        subject = (
            "Kipaga - Um novo deposito foi realizado!".format(novo.first_name))
        template_name = "emailDeposito.html"
        dados = {
            "valor": novo.valor,
            "nome": novo.first_name,
        }
        # send_email(
        #     to=para,
        #     subject=subject,
        #     template_name=template_name,
        #     context=dados,
        # )
        print("Sucesso!")

    return render(request, "Deposito.html", context=context)


def pdfDownload(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    pdf = canvas.Canvas(buffer)
    pdf.translate(cm, cm)
    pdf.setPageSize((2480, 3508))
    # template 1
    pdf.setStrokeColor(colors.gray)
    pdf.setFillColor(colors.gray)
    pdf.rect(40, 60, 900, 100, stroke=1, fill=1)
    pdf.setStrokeColor(colors.red)
    pdf.setFillColor(colors.red)
    pdf.rect(40, 30, 900, 500, stroke=1, fill=1)

    pdf.setStrokeColor(colors.gray)
    pdf.setFillColor(colors.gray)
    pdf.rect(40, 30, 900, 500, stroke=1, fill=1)

    pdf.save()

    # template 2
    # pdf.setStrokeColor(colors.green)
    # pdf.setFillColor(colors.green)
    # pdf.rect(40,560,900,100,stroke=1,fill=1)

    # pdf.setStrokeColor(colors.blueviolet)
    # pdf.setFillColor(colors.blueviolet)
    # pdf.rect(40,100,900,420,stroke=1,fill=1)

    # pdf.setStrokeColor(colors.red)
    # pdf.setFillColor(colors.red)
    # pdf.rect(40,20,900,50,stroke=1,fill=1)
    # pdf.save()
    # tutorial 3
    # pdf.setStrokeColor(colors.green)
    # pdf.setFillColor(colors.green)
    # pdf.rect(40,560,900,100,stroke=1,fill=1)

    # pdf.setStrokeColor(colors.blueviolet)
    # pdf.setFillColor(colors.blueviolet)
    # pdf.rect(40,100,200,420,stroke=1,fill=1)

    # pdf.setStrokeColor(colors.blueviolet)
    # pdf.setFillColor(colors.blueviolet)
    # pdf.rect(260,100,680,420,stroke=1,fill=1)

    # pdf.setStrokeColor(colors.red)
    # pdf.setFillColor(colors.red)
    # pdf.rect(40,20,900,50,stroke=1,fill=1)
    # pdf.save()

    # tutorial 4
    # pdf.setStrokeColor(colors.green)
    # pdf.setFillColor(colors.green)
    # pdf.rect(40,560,900,100,stroke=1,fill=1)

    # pdf.setStrokeColor(colors.blueviolet)
    # pdf.setFillColor(colors.blueviolet)
    # pdf.rect(40,100,200,420,stroke=1,fill=1)

    # pdf.setStrokeColor(colors.blueviolet)
    # pdf.setFillColor(colors.blueviolet)
    # pdf.rect(260,100,680,220,stroke=1,fill=1)

    # pdf.setStrokeColor(colors.blueviolet)
    # pdf.setFillColor(colors.blueviolet)
    # pdf.rect(260,330,680,190,stroke=1,fill=1)

    # pdf.setStrokeColor(colors.red)
    # pdf.setFillColor(colors.red)
    # pdf.rect(40,20,900,50,stroke=1,fill=1)
    # pdf.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='Comprovativo de Deposito - Conta Kipaga.pdf')


def envite(request):

    link = request.GET
    link = request.GET.get('link')
    if link != '' and link is not None:
        try:
            Searchdata = User.objects.get(id=link)
        except:
            return redirect("/notFound")
    context = {
        "object": Searchdata
    }

    return render(request, "linkCompartilavel.html", context=context)


def cadastrarEmpresa(request):
    Users = User.objects.all()
    if request.method == "POST":
        data = request.POST.copy()
        print(data)
        numero = random.randint(100000, 500000)
        numero2 = random.randint(100000, 500000)
        ki = "Ki{}".format(numero2)
        image = data.get('image')
        nome = data.get('nome')
        usuario = data.get('usuario')
        userAnexado = User.objects.filter(id=usuario).get()
        NIF = data.get('nif')
        provincia = data.get('provincia')
        servico = data.get('servico')
        novo = empresa()
        novo.nome = nome
        novo.nif = NIF
        novo.usuario = userAnexado
        novo.tipo = servico
        novo.provincia = provincia
        novo.idKipaga = ki
        novo.save()
        notifyTitle = "{} a sua conta foi Anexada a uma conta empresa, verfique o seu !".format(
            userAnexado.first_name)

        notificacao = notify()
        notificacao.conteudo = notifyTitle
        notificacao.usuario = userAnexado
        notificacao.save()
        para = userAnexado.email
        subject = ("Kipaga - Seja bem vindo!")
        template_name = "AnexEmail.html"

        imagem = qrcode.make('{}'.format(novo.idKipaga))

        imagem.save('static/images/{}.png'.format(NIF))
        dados = {
            "empresa": novo,
            "user": userAnexado,
        }
        send_email(
            to=para,
            subject=subject,
            template_name=template_name,
            context=dados,
        )
        return redirect("empresa")
    context = {
        "users":Users,
    }

    return render(request, "createEmpresa.html", context=context)
