from django.shortcuts import render
from django.db import connection
import cx_Oracle
from .forms import registrocliente,CustomUserForm,FormCheckIn
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from datetime import datetime


# Create your views here.

def index(request):
    #print(listar_departamentos())
    data={
        'departamentos':listar_departamentos(),
    }
    return render(request,'core/index.html',data)

def depa1(request):
    #print(listar_departamentos())

    dt = datetime(2019,5,1)
    dt1 = datetime(2020,6,1)

    print(dt)
    agregar_reserva(12,dt,dt1,50000,1,1,1,1)
    return render(request,'core/departamentos/departamento_1.html')

#Departamentos

def Test(request):
    
    return render(request,'core/Test.html')

def departamento1(request):
    data={
        'departamentos':listar_departamentos(),
    }
    return render(request,'core/departamentos/departamento_1.html',data)

def departamento2(request):
    return render(request,'core/departamentos/departamento_2.html')
def departamento3(request):
    return render(request,'core/departamentos/departamento_3.html')
def departamento4(request):
    return render(request,'core/departamentos/departamento_4.html')
def departamento5(request):
    return render(request,'core/departamentos/departamento_5.html')
def departamento6(request):
    return render(request,'core/departamentos/departamento_6.html')
def departamento7(request):
    return render(request,'core/departamentos/departamento_7.html')
def departamento8(request):
    return render(request,'core/departamentos/departamento_8.html')
def departamento9(request):
    return render(request,'core/departamentos/departamento_9.html')
def departamento10(request):
    return render(request,'core/departamentos/departamento_10.html')

def numero():
    numero=1
    return numero

def listar_departamentos():
    django_cursor= connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_DEPARTAMENTOS_WEB2",[out_cur])

    lista=[]
    for fila in out_cur:
        lista.append(fila)

    return lista

def datos_departamento():
    django_cursor= connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_DATOS_DEPARTAMENTO_WEB",[out_cur])

    lista=[]
    for fila in out_cur:
        lista.append(fila)

    return lista


def registro_usuario(request):

    data={
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect(to='index')

    return render(request, 'Registration/registrar.html',data)

def registro_cliente(request):
    data = {
        'forma':  registrocliente(),
    }
    data["mensaje"] = ""
    if request.method == 'POST':
        formulario = registrocliente(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "bien"
        else:
            data["mensaje"] = "mal"
    
    return render(request, 'Registration/registroCliente.html',data)

def Checkin(request):

    form = FormCheckIn()

    if request.method == 'POST':
        form = FormCheckIn(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'core/ChechIn.html', context)

def agregar_reserva(id_reserva,fecha_ini,fecha_fin,total,pago_id_pago,estado_reserva_id_estreserva,cliende_id_cliente,departamento_id_depa):
    django_cursor= connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_RESERVADEPARTAMENTO',[id_reserva,fecha_ini,fecha_fin,total,pago_id_pago,estado_reserva_id_estreserva,cliende_id_cliente,departamento_id_depa])
    return salida.getvalue()