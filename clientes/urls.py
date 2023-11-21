from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('registro/', views.cliente_registro, name='cliente_registro'),
    path('atualizar/', views.cliente_actualizar, name='cliente_actualizar'),
    path('consultas/', views.consulta_lista, name='consulta_list'),
    path('consultas/crear/', views.consulta_registro, name='consulta_create'),
    path('consultas/editar/<int:pk>/', views.consulta_actualizar, name='consulta_update'),
    path('consultas/borrar/<int:pk>/', views.consulta_borrar, name='consulta_delete'),
]