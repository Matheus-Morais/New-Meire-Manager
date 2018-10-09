from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html') #  Função usada para exibir o home

def error_404(request):
    return render(request, 'core/404.html')

def em_andamento(request):
    return render(request, 'core/em_andamento.html')

def gerencia(request):
    return render (request, 'core/gerencia.html')