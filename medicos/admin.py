from django.contrib import admin

from medicos.models import Especialidad, Medico, Agenda

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
    
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Agenda, AgendaAdmin)