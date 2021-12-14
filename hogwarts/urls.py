from os import name
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('addmat', views.addmat, name='addmat'),
    path('adm', views.adm, name='adm'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('contato', views.contato, name='contato'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('editmat', views.editmat, name='editmat'),
    path('esportes', views.esportes, name='esportes'),
    path('login', views.login, name='login'),
    path('nossamissao', views.nossamissao, name='nossamissao'),
    path('quemsomos', views.quemsomos, name='quemsomos'),

]