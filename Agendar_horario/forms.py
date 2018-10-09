from django import forms
from .models import Agendar

class AgendarForm(forms.ModelForm):
    class Meta:
        model = Agendar
        exclude = ('usuario', 'status', 'cliente',)

class AgendarAdminForm(forms.ModelForm):
    class Meta:
        model = Agendar
        exclude = ('usuario',)
