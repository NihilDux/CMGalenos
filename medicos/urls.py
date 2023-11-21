from django.urls import path
from . import views

app_name = 'medicos'

urlpatterns = [
    path('registro/medico/', views.medico_registro, name='medico_registro'),
    path('registro/especialidad/', views.especialidad_registro, name='especialidad_registro'),
    path('agendar/', views.agenda_registro, name='agendar_consulta'),
    path('agendar/actualizar/<int:pk>/', views.agenda_actualizar, name='agendar_consulta_actualizar'),
    path('agendar/borrar/<int:pk>/', views.agenda_borrar, name='agendar_consulta_borrar'),
    path('mis/consultas/', views.agenda_lista, name="agenda_lista"),
    path('admin/lista/medicos/', views.medico_lista, name="medicos_lista"),
    path('admin/lista/especialidad/', views.especialidad_lista, name="especialidad_lista")
    
]