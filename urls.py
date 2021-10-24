from os import name
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('contato', views.contato, name='contato'),
    path('esportes', views.esportes, name='esportes'),
    path('login', views.login, name='login')

]