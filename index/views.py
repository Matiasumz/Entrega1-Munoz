from django.shortcuts import render, redirect
from django.contrib.auth.forms  import AuthenticationForm
from django.contrib.auth import login as auth_login,authenticate

def index(request):
    return render(request,"index/index.html")

def plantilla(request):
    return render(request,"index/plantilla.html")

def login(request):
    
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password =login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request,user)
                return redirect("index")
            else:
                return render(request,"index/login.html", {"login_form" : login_form ,"Alerta": "El usuario no se pudo autenticar."})
        else:
            return render(request,"index/login.html", {"login_form" : login_form, "Alerta": "Formulario invalido."})
        
    login_form =  AuthenticationForm()
    return render(request,"index/login.html", {"login_form" : login_form})