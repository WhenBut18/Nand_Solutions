from django.urls import path
from . import views
from .views import create_form
urlpatterns = [
    path("", views.index),
    path("sobre-denunciapp/", views.about),
    path("formulario/", views.form),
    path('formulario/new/', create_form),
    path("mapa/", views.map),
]