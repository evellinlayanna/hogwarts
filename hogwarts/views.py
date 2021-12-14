from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def addmat(request):
    return render(request, 'addmat.html')

def adm(request):
    return render(request, 'adm.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def contato(request):
    return render(request, 'contato.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def editmat(request):
    return render(request, 'editmat.html')

def esportes(request):
    return render(request, 'esportes.html')

def login(request):
    return render(request, 'login.html')

def nossamissao(request):
    return render(request, 'nossamissao.html')

def quemsomos(request):
    return render(request, 'quemsomos.html')