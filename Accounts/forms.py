from django import forms
from django.contrib.auth.models import User
from .models import Usuario

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ('user',)

class UpdateUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ('cpf', 'rg', 'user',)

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class AdminUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class AdminUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')