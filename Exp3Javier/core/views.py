from django.shortcuts import redirect, render
from django.views.decorators import csrf
from .models import Cliente, Producto
from django.contrib import messages


# Create your views here.

def index (request):
    return render(request, 'index.html')

def somos (request):
    return render(request, 'somos.html')

def galeria (request):
    return render(request, 'galeria.html')

def formularioregistro(request):
    return render(request, 'formularioregistro.html')

def formulariocontacto(request):
    return render(request, 'formulariocontacto.html')


#-------------------------------    

def clientesadmin(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientesadmin.html', {"clientes": clientes})

#-----------------------------


def RegistrarClientes(request):
    rut = request.POST['txtrut']
    nombrec = request.POST['txtnombre']
    correo = request.POST['txtcorreo']
    direccion = request.POST['txtdireccion']
    telefono = request.POST['numbertelefono']
    cliente =Cliente.objects.create(rut=rut, nombrec = nombrec, correo=correo, direccion=direccion, telefono=telefono)
    messages.success(request, '!Cliente agregado¡')
    return redirect('clientesadmin')


def editarCliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    return render(request, "editarCliente.html", {"cliente": cliente})


def modificarClientes(request):
    rut = request.POST['txtrut']
    nombrec = request.POST['txtnombre']
    cliente = Cliente.objects.get(rut=rut)
    cliente.nombrec = nombrec
    cliente.save()
    messages.success(request, '!Cliente modificado¡')
    return redirect('clientesadmin') 



def eliminarCliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    messages.success(request, '!Cliente eliminado¡')

    return redirect ('clientesadmin')


#--------------

#Productos---------

def productosadmin(request):
    productos = Producto.objects.all()
    return render(request, 'productosadmin.html', {"productos": productos})

#Registros-------

def RegistrarProductos(request):
    idProducto = request.POST['txtidproducto']
    nombreProducto = request.POST['txtproducto']
    imagen = request.FILES['txtImagen']
    producto =Producto.objects.create(idProducto=idProducto, nombreProducto = nombreProducto, imagen = imagen)
    messages.success(request, '!Producto agregado¡')
    return redirect('productosadmin')

def editarProducto(request, id):
    producto = Producto.objects.get(idProducto=id)
    return render(request, "editarProducto.html", {"producto": producto})


def modificarProducto(request):
    idProducto = request.POST['txtidproducto']
    nombreProducto = request.POST['txtproducto']
    producto = Producto.objects.get(idProducto=idProducto)
    producto.nombreProducto = nombreProducto
    producto.save()
    messages.success(request, '!Producto modificado¡')
    return redirect('productosadmin') 

def eliminarProducto(request, id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    messages.success(request, '!Producto eliminado¡')

    return redirect ('productosadmin')



