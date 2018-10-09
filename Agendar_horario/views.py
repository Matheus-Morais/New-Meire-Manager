from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from .models import Agendar
from .forms import AgendarForm, AgendarAdminForm

from Accounts.models import Usuario

@login_required
def lista_agenda(request):
    if request.user.is_superuser:
        agenda = Agendar.objects.filter(status='SO')
        return render(request, 'lista_horarios.html', {'agenda': agenda})
    else:
        usuarios = Usuario.objects.all()
        for usuario in usuarios:
            if usuario.user == request.user:
                u = usuario

        agenda = Agendar.objects.filter(cliente=u)

        return render(request, 'lista_horarios.html', {'agenda': agenda})

@login_required
def add_horario(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = AgendarAdminForm(request.POST)
            if form.is_valid():
                h = form.save(commit=False)
                h.usuario = request.user
                h.save()
                messages.success(request, 'Horario agendado com Sucesso!')
                return redirect('agenda:lista-horario')
            else:
                messages.error(request, form.errors)
        else:
            form = AgendarAdminForm()
            return render(request, 'add_horario.html', {'form':form})
    else:
        if request.method == 'POST':
            form = AgendarForm(request.POST)
            if form.is_valid():
                h = form.save(commit=False)
                usuarios = Usuario.objects.all()

                for usuario in usuarios:
                    if usuario.user == request.user:
                        u = usuario

                h.cliente = u
                h.usuario = request.user
                h.save()
                messages.success(request, 'Horario agendado com Sucesso!')
                return redirect('agenda:lista-horario')
            else:
                messages.error(request, form.errors)
        else:
            form = AgendarForm()
            return render(request, 'add_horario.html', {'form':form})

@login_required
def update_horario(request, id):
    if request.user.is_superuser:
        horario = Agendar.objects.get(id=id)
        if request.method == 'POST':
            form = AgendarAdminForm(data=request.POST, instance=horario)
            if form.is_valid():
                form.save()
                messages.success(request, 'Horario editado com Sucesso!')
                return redirect('agenda:lista-horario')
            else:
                messages.error(request, form.errors)
        else:
            form = AgendarAdminForm(instance=horario)
        return render(request, 'add_horario.html', {'form':form})
    else:
        user = request.user
        cliente = Usuario.objects.get(user=user)
        horario = Agendar.objects.get(id=id)
        if horario.cliente == cliente:
            if request.method == 'POST':
                form = AgendarForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Horario agendado com Sucesso!')
                    return redirect('agenda:lista-horario')
                else:
                    messages.error(request, form.errors)
            else:
                form = AgendarForm()
            return render(request, 'add_horario.html', {'form':form})
        else:
            return redirect('error-404')

@login_required
def delete_horario(request, id):
    if request.user.is_superuser:
        horario = Agendar.objects.get(id=id)
        horario.delete()
    else:
        user = request.user
        cliente = Usuario.objects.get(user=user)
        horario = Agendar.objects.get(id=id)
        if horario.cliente == cliente:
            horario.delete()
        else:
            return redirect('error-404')