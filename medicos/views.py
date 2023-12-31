from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Medico, Agenda, Especialidad, Centro

from email.message import EmailMessage
import smtplib

class TestMixinIsAdmin(UserPassesTestMixin):
    def test_func(self):
        is_admin_or_is_staff = self.request.user.is_superuser or \
            self.request.user.is_staff
        return bool(is_admin_or_is_staff)

    def handle_no_permission(self):
        messages.error(
            self.request, "No tienes los permisos!"
        )
        return redirect("accounts:index")

class MedicoCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Medico
    login_url = 'accounts:login'
    template_name = 'medicos/registro.html'
    fields = ['nombre', 'run', 'email', 'telefono', 'especialidad']
    success_url = reverse_lazy('medicos:medicos_lista')
    
class MedicoListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'medicos/medicos_list.html'

    def get_queryset(self):
        return Medico.objects.all().order_by('-pk')
    
class EspecialidadCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Especialidad
    login_url = 'accounts:login'
    template_name = 'medicos/registro.html'
    fields = ['nombre',]
    success_url = reverse_lazy('medicos:especialidad_lista')
    
class EspecialidadListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'medicos/especialidad_list.html'

    def get_queryset(self):
        return Especialidad.objects.all().order_by('-pk')
############################################    
class CentroCreateView(LoginRequiredMixin, TestMixinIsAdmin, CreateView):

    model = Centro
    login_url = 'accounts:login'
    template_name = 'medicos/registro.html'
    fields = ['nombre',]
    success_url = reverse_lazy('medicos:centro_lista')
    
class CentroListView(LoginRequiredMixin, TestMixinIsAdmin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'medicos/centro_list.html'

    def get_queryset(self):
        return Centro.objects.all().order_by('-pk')
##########################################################

class AgendaCreateView(CreateView):

    model = Agenda
    template_name = 'medicos/agenda_registro.html'
    #form_class = TuFormulario
    fields = ['centro', 'medico', 'dia', 'horario', 'nombre', 'email', 'genero', 'telefono', 'run']
    success_url = reverse_lazy('medicos:agenda_lista')
    
    def form_valid(self, form):

        if not self.request.user.is_anonymous:
            form.instance.user = self.request.user
        else:
            form.instance.user = None
        
        horario_value = form.cleaned_data['horario']
        horario_display = dict(form.fields['horario'].choices).get(horario_value)

        self.enviar_correo(form.cleaned_data['nombre'], form.cleaned_data['email'], form.cleaned_data['medico'],form.cleaned_data['dia'] , horario_display, form.cleaned_data['centro'])
        messages.success(self.request, 'Agenda creada exitosamente.')

        return super().form_valid(form)
    
    def enviar_correo(self, nombre, email, medico, dia, horario, centro):
        print(f'Dia: {dia}')
        print(f'Horario: {horario}')
        


        remitente = 'cmgalenosaws@gmail.com'
        destinatario = email
        mensaje = f'Hola {nombre}, se ha agendado exitosamente su hora médica con el Médico {medico}, con fecha {dia} desde las {horario} en el Centro Médico ubicado en {centro}'

        email = EmailMessage()
        email["From"] = remitente
        email["To"] = destinatario
        email["Subject"] = "Prueba de correo"
        email.set_content(mensaje)

        smtp = smtplib.SMTP_SSL('smtp.gmail.com')
        smtp.login(remitente, "ughp nbhq gmxm actu")
        smtp.sendmail(remitente, destinatario, email.as_string())
        print("Correo enviado")
        smtp.quit()
    
class AgendaUpdateView(LoginRequiredMixin, TestMixinIsAdmin, UpdateView):

    model = Agenda
    login_url = 'accounts:login'
    template_name = 'medicos/agenda_registro.html'
    fields = ['centro', 'medico', 'dia', 'horario']
    success_url = reverse_lazy('medicos:agenda_lista')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AgendaDeleteView(LoginRequiredMixin, TestMixinIsAdmin, DeleteView):
    model = Agenda
    success_url = reverse_lazy('medicos:agenda_lista')
    template_name = 'form_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Consulta eliminada exitosamente!")
        return reverse_lazy('medicos:agenda_lista')


class AgendaListView(ListView):
    
    login_url = 'accounts:login'
    template_name = 'medicos/agenda_list.html'

    def get_queryset(self):
        return Agenda.objects.filter().order_by('-pk')
    
medico_registro = MedicoCreateView.as_view()
medico_lista = MedicoListView.as_view()
especialidad_registro = EspecialidadCreateView.as_view()
especialidad_lista = EspecialidadListView.as_view()
agenda_registro = AgendaCreateView.as_view()
agenda_actualizar = AgendaUpdateView.as_view()
agenda_lista = AgendaListView.as_view()
agenda_borrar = AgendaDeleteView.as_view()
centro_registro = CentroCreateView.as_view()
centro_lista = CentroListView.as_view()