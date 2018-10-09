"""New_Meire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from core import views
from Mensagens import views as mensagens_views
from Accounts import urls as accounts_urls
from Mensagens import urls as mensagens_urls
from Servico import urls as servico_urls
from Promocao import urls as promocao_urls
from cabeleireira import urls as cabeleireira_urls
from Agendar_horario import urls as agenda_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'core'),
    path('404', views.error_404, name ='error-404'),
    path('em-andamento', views.em_andamento, name ='em-andamento'),
    path('gerencia', views.gerencia, name='gerencia'),
    path('contato/', mensagens_views.nova_mensagem, name = 'contato'),
    path('accounts/', include(accounts_urls)),
    path('msg/', include(mensagens_urls)),
    path('servico/', include(servico_urls)),
    path('promocoes/', include(promocao_urls)),
    path('cabeleireira/', include(cabeleireira_urls)),
    path('agenda/', include(agenda_urls)),
]
