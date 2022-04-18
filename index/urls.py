from django.urls import path
from .views import index , plantilla,login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",index, name="index"),
    path("login/",login, name="login"),
    path("logout/",LogoutView.as_view(template_name ="index\logout.html" ), name="logout"),
    path("plantilla/",plantilla,name="plantilla"),
]
