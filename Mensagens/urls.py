from django.conf.urls import url

from . import views
app_name = "msg"
urlpatterns = [
    url('^mensagens/$', views.lista_mensagens, name = 'lista-mensagens'),
    url('^delete-mensagem/(?P<id>[0-9]+)/$', views.delete_mensagem, name = 'delete-mensagem'),
]