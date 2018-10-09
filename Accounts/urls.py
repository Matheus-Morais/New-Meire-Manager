from django.conf.urls import url
from . import views

app_name = "accounts"

urlpatterns = [
    url('^login-usuario/$', views.user_login, name='user-login'),
    url('^logout-usuario/$', views.user_logout, name='user-logout'),
    url('^novo-usuario/$', views.add_user, name='add-user'),
    url('^alterar-senha/$', views.change_password, name='change-password'),
    url('^update-dados/$', views.update_dados, name='update-dados'),
    url('^lista-usuarios/$', views.lista_usuarios, name = 'lista-usuarios'),
    url('^delete-usuario/(?P<id>[0-9]+)/$', views.delete_usuario, name = 'delete-usuario'),
    url('^update-usuario/(?P<id>[0-9]+)/$', views.update_usuario, name = 'update-usuario'),
]