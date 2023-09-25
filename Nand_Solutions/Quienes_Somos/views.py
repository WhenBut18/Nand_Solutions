from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Quienes_Somos/index.html")