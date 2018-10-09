from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from .models import Servico
from .forms import ServicoForm

def lista_servico(request):
    servicos = Servico.objects.all()
    return render(request, 'lista_servicos.html', {'servicos': servicos})

@login_required
def add_servico(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ServicoForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Serviço criado com Sucesso!')
                return redirect('servico:novo-servico')
            else:
                messages.error(request, form.errors)
        else:
            form = ServicoForm()
        return render(request, 'add_servico.html', {'form':form})
    else:
        return redirect('error-404')

@login_required
def update_servico(request, id):
    if request.user.is_superuser:
        servico = Servico.objects.get(id=id)
        if request.method == 'POST':
            form = ServicoForm(data=request.POST, instance=servico)
            if form.is_valid():
                form.save()
                messages.success(request, 'Serviço editado com Sucesso!')
                return redirect('servico:editar-servico', id)
            else:
                messages.error(request, form.errors)
        else:
            form = ServicoForm(instance=servico)
            return render(request, 'add_servico.html', {'form':form})
    else:
        return redirect('error-404')

@login_required
def delete_servico(resquest, id):
    if resquest.user.is_superuser:
        servico = Servico.objects.get(id=id)
        servico.delete()
        return redirect('servico:lista-servicos')
    else:
        return redirect('error-404')
