from django.shortcuts import render, redirect
from .models import Denuncia
import googlemaps
from datetime import date
import json
import os

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def form(request):
    return render(request, 'form.html')
def questions(request):
    return render(request, 'questions.html')
def create_form(request):
    print(request.POST)
    return redirect('/formulario/')
def map(request):
    return render(request, 'map.html')
def coficador(dato1,dato2,dato3,dato4,dato5,dato6, dato7):
    return {"properties":{"mag":"Motivo {}, registrado el dia {} a las {}, en {}".format(dato1, dato2, dato3, dato4),"place":"Agresion del tipo {}".format(dato5)},"geometry":{"coordinates":[float(dato6), float(dato7),16.4]}}
def codificador2(datos1):
    return {"features":datos1}
def coder2(datos1):
    return "eqfeed_callback({})".format(datos1)
def registrar_form(request):
    gmaps = googlemaps.Client(key='AIzaSyBa_xoUht1mXl6xz1J4aMH3DUeEOfjG_5Y')
    premotivo = request.POST.get('TipoMotivo')
    preagresion = request.POST.get('TipoAgresion')
    predireccion_incidente = request.POST['txtDireccionIncidente']
    prefecha = request.POST['txtFechaIncidente']
    prehora = request.POST['txtHoraIncidente']
    prenombres = request.POST['txtNombres']
    preapellidos = request.POST['txtApellidos']
    preedad = request.POST['txtEdad']
    prerut = request.POST['txtRut']
    predireccion = request.POST['txtDireccion']
    prelatitud_longitud = gmaps.geocode(predireccion_incidente)
    pretelefono = request.POST['txtTelefono']
    precorreo = request.POST['txtCorreo']
    prelatitud_longitud=prelatitud_longitud[0]
    prelatitud_longitud = prelatitud_longitud['geometry']
    prelatitud_longitud = prelatitud_longitud['location']
    prelatitud = prelatitud_longitud['lat']
    prelongitud = prelatitud_longitud['lng']
    prelatitud_longitud = "{},{}".format(prelongitud, prelatitud)
    denuncia = Denuncia.objects.create(Nombres=prenombres, Apellidos=preapellidos, Edad=preedad, Rut=prerut, Direccion=predireccion, Telefono=pretelefono, Correo=precorreo, Latitud=prelatitud, Longitud=prelongitud, Agresion=preagresion, Motivo=premotivo, Direccion_Agresion=predireccion_incidente, Fecha=prefecha, Hora=prehora, Longitud_Latitud=prelatitud_longitud)
    cosas = Denuncia.objects.all().values("Longitud_Latitud","Agresion","Motivo","Fecha","Hora","Direccion_Agresion","Longitud","Latitud")
    nuevo_json = []
    for d in cosas:
        temp_json = coficador(d['Motivo'],d['Fecha'],d['Hora'],d['Direccion_Agresion'],d['Agresion'],d['Longitud'],d['Latitud'])
        nuevo_json.append(temp_json)
    nuevo_json = codificador2(nuevo_json)
    nuevo_json = coder2(nuevo_json)
    folder = os.path.join("myapp","static","json","datos2.txt")
    p = open(folder, "w")
    p.write(nuevo_json)
    return redirect('/formulario')

