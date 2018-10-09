from django.conf.urls import url

from . import views
app_name = "promoções"
urlpatterns = [
    url('lista/', views.lista_promocoes, name = 'lista-promocoes'),
    url('nova/', views.add_promocao, name = 'nova-promocao'),
    url('editar/(?P<id>[0-9]+)/$', views.update_promocao, name = 'editar-promocao'),
    url('excluir/(?P<id>[0-9]+)/$', views.delete_promocao, name = 'excluir-promocao'),
]