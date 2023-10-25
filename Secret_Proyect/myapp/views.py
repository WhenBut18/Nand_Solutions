from django.shortcuts import render, redirect
from .models import Denuncia
import googlemaps
from datetime import datetime

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def form(request):
    return render(request, 'form.html')
def create_form(request):
    print(request.POST)
    return redirect('/formulario/')
def map(request):
    return render(request, 'map.html')
def registrar_form(request):
    gmaps = googlemaps.Client(key='AIzaSyBa_xoUht1mXl6xz1J4aMH3DUeEOfjG_5Y')
    prenombres = request.POST['txtNombres']
    preapellidos = request.POST['txtApellidos']
    preedad = request.POST['txtEdad']
    prerut = request.POST['txtRut']
    predireccion = request.POST['txtDireccion']
    prelatitud_longitud = gmaps.geocode(predireccion)
    print(prelatitud_longitud)
    pretelefono = request.POST['txtTelefono']
    precorreo = request.POST['txtCorreo']
    prelatitud_longitud=prelatitud_longitud[0]
    prelatitud_longitud = prelatitud_longitud['geometry']
    prelatitud_longitud = prelatitud_longitud['location']
    prelatitud = prelatitud_longitud['lat']
    prelongitud = prelatitud_longitud['lng']
    premotivo = request.POST.get('TipoMotivo')
    preagresion = request.POST.get('TipoAgresion')
    predireccion_incidente = request.POST['txtDireccionIncidente']
    prefecha = request.POST['txtFechaIncidente']
    prehora = request.POST['txtHoraIncidente']
    denuncia = Denuncia.objects.create(Nombres=prenombres, Apellidos=preapellidos, Edad=preedad, Rut=prerut, Direccion=predireccion, Telefono=pretelefono, Correo=precorreo, Latitud=prelatitud, Longitud=prelongitud, Agresion=preagresion, Motivo=premotivo, Direccion_Agresion=predireccion_incidente, Fecha=prefecha, Hora=prehora)
    return redirect('/formulario')

