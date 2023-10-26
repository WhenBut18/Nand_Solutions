from django.urls import path
from . import views
from .views import registrar_form
urlpatterns = [
    path("", views.index),
    path("sobre-denunciapp/", views.about),
    path("formulario/", views.form),
    path("mapa/", views.map),
    path("registrarform/", registrar_form),
    path('preguntas-frecuentes/', views.questions)
]