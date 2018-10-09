from django.conf.urls import url

from . import views
app_name = "cabeleireira"
urlpatterns = [
    url('^lista-cabeleireira/$', views.lista_cabeleireira, name = 'lista-cabeleireira'),
    url('^nova-cabeleireira/$', views.add_cabeleireira, name = 'nova-cabeleireira'),
    url('^editar-cabeleireira/(?P<id>[0-9]+)/$', views.update_cabeleireira, name = 'editar-cabeleireira'),
    url('^excluir-cabeleireira/(?P<id>[0-9]+)/$', views.delete_cabeleireira, name = 'excluir-cabeleireira'),
    url('^novo-servico-cabeleireira/$', views.add_servicos_cabeleireira, name = 'novo-servico-cabeleireira'),
    url('^lista-servico-cabeleireira/(?P<id>[0-9]+)/$', views.lista_servicos_cabeleireira, name = 'lista-servico-cabeleireira'),
    url('^editar-servico-cabeleireira/(?P<id>[0-9]+)/$', views.update_servico_cabeleireira, name = 'editar-servico-cabeleireira'),
    url('^excluir-servico-cabeleireira/(?P<id>[0-9]+)/$', views.delete_servico_cabeleireira, name = 'excluir-servico-cabeleireira'),
]