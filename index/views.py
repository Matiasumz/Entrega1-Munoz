from django.shortcuts import render

def index(request):
    return render(request,"index/index.html")

def plantilla(request):
    return render(request,"index/plantilla.html")

