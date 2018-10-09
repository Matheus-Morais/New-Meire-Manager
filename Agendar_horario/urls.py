from django.conf.urls import url

from . import views
app_name = "agenda"
urlpatterns = [
    url('^lista/$', views.lista_agenda, name = 'lista-horario'),
    url('^novo-horario/$', views.add_horario, name = 'novo-horario'),
    url('^editar-horario/(?P<id>[0-9]+)/$', views.update_horario, name = 'editar-horario'),
    url('^excluir-horario/(?P<id>[0-9]+)/$', views.delete_horario, name = 'excluir-horario'),
]