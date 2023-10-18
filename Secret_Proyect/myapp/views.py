from django.shortcuts import render, redirect

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