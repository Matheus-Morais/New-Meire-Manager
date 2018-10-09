from django.conf.urls import url

from . import views
app_name = "servico"
urlpatterns = [
    url('^all-services/$', views.lista_servico, name = 'lista-servicos'),
    url('^novo-servico/$', views.add_servico, name = 'novo-servico'),
    url('^editar-servico/(?P<id>[0-9]+)/$', views.update_servico, name = 'editar-servico'),
    url('^excluir-servico/(?P<id>[0-9]+)/$', views.delete_servico, name = 'excluir-servico'),
]