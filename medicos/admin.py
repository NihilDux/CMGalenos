from django.contrib import admin

from medicos.models import Especialidad, Medico, Agenda, Centro, Cliente

class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    
class MedicoAdmin(admin.ModelAdmin):
    list_display = [
        'nombre', 'run', 'telefono',
    ]
    
class AgendaAdmin(admin.ModelAdmin):
    list_display = [
        'dia', 'medico', 'horario'
    ]

class CentroAdmin (admin.ModelAdmin):
    list_display = [
        'nombre'
    ]
class ClienteAdmin (admin.ModelAdmin):
    list_display = [
    'nombre'
    ]


admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Centro, CentroAdmin)
admin.site.register(Cliente, ClienteAdmin)