from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import UserForm, UsuarioForm, UpdateUsuarioForm, UpdateUserForm, AdminUsuarioForm, AdminUserForm
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, 'Usuario ou senha invalidos!')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('core')

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        formUsuario = UsuarioForm(request.POST)
        if formUsuario.is_valid():
            if form.is_valid():
                u = form.save()
                u.set_password(u.password)
                u.save()
                u2 = formUsuario.save(commit=False)
                u2.user = u #User.objects.get(pk = u.id)
                u2.save()
                messages.success(request, 'Usuário criado com sucesso! Utilize o formulario abaixo para fazer login!')
                return redirect('accounts:user-login')
            else:
                messages.error(request, form.errors)
        else:
            messages.error(request, formUsuario.errors)
    else:
        form = UserForm()
        formUsuario = UsuarioForm()
    return render(request, 'accounts/add_user.html', {'form':form, 'form1':formUsuario})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('accounts:change-password')
        else:
            messages.error(request, 'Não foi possivel alterar sua senha, verifique os dados!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form':form})

@login_required
def update_dados(request):
    for u in Usuario.objects.all():
        if u.user == request.user:
            usuario = u
    
    if request.method == 'POST':
        usuario_form = UpdateUsuarioForm(data=request.POST, instance=usuario)
        user_form = UpdateUserForm(data=request.POST, instance=request.user)

        if usuario_form.is_valid():
            if user_form.is_valid():

                usuario_form.save()
                user_form.save()
                return redirect('accounts:update-dados')
            else:
                messages.error(request, user_form.errors)
        else:
            messages.error(request, usuario_form.errors)
    else:
        usuario_form = UpdateUsuarioForm(instance=usuario)
        user_form = UpdateUserForm(instance=request.user)
        return render(request, 'accounts/update_dados.html', {'usuario_form':usuario_form, 'user_form':user_form, 'usuario':usuario})

@login_required
def lista_usuarios(request):
    if request.user.is_superuser:
        usuarios = Usuario.objects.all()
        return render(request, 'accounts/lista_usuarios.html', {'usuarios': usuarios})
    else:
        return redirect('error-404')

@login_required
def delete_usuario(request, id):
    if request.user.is_superuser:
        usuario = Usuario.objects.get(pk=id)
        u = usuario.user
        usuario.delete()
        u.delete()
        return redirect('accounts:lista-usuarios')
    else:
        return redirect('error-404')

@login_required
def update_usuario(request, id):
    if request.user.is_superuser:
        usuario = Usuario.objects.get(pk = id)
        user = User.objects.get(pk = usuario.user.pk)
        if request.method == 'POST':
            usuario_form = UsuarioForm(data=request.POST, instance=usuario)
            user_form = AdminUserForm(data=request.POST, instance=user)
            if usuario_form.is_valid():
                if user_form.is_valid():
                    usuario_form.save()
                    user_form.save()
                    return redirect('accounts:lista-usuarios')
                else:
                    messages.error(request, user_form.errors)
                    return redirect('accounts:lista-usuarios')
            else:
                messages.error(request, usuario_form.errors)
                return redirect('accounts:lista-usuarios')
        else:
            usuario_form = UsuarioForm(instance=usuario)
            user_form = AdminUserForm(instance=user)
            return render(request, 'accounts/update_usuario.html', {'usuario_form':usuario_form, 'user_form':user_form})
    else:
        return redirect('error-404')