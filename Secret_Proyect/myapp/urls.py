from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("sobre-denunciapp/", views.about),
    path("formulario/", views.form),
]