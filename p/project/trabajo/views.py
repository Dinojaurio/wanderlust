from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"casa.html")

def login(request):
    return render(request,"login.html")

def publicar(request):
    return render(request,"public.html")

def prueba(request):
    return render(request, "prueba.html")