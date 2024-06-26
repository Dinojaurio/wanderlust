from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('public', views.publicar, name="publicar"),
    path('prueba', views.prueba, name="prueba")
]