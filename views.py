from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def contato(request):
    return render(request, 'contato.html')

def esportes(request):
    return render(request, 'esportes.html')

def login(request):
    return render(request, 'login.html')