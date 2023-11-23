from datetime import date
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db.models.fields.related import ForeignKey
import re

INVALID_RUTS = [
    "11.111.111-1",
    "22.222.222-2",
    "33.333.333-3",
    "44.444.444-4",
    "55.555.555-5",
    "66.666.666-6",
    "77.777.777-7",
    "88.888.888-8",
    "99.999.999-9",
    "00.000.000-0",
    # Otros RUTs inválidos...
]

def validate_rut(value):
    rut_pattern = re.compile(r'^\d{1,2}\.\d{3}\.\d{3}-[\dkK]$')
    if not rut_pattern.match(value):
        raise ValidationError("El formato del RUT no es válido.")

    # Extraer el dígito verificador y los números del RUT
    rut_digits, verificador = value[:-2].replace('.', ''), value[-1].lower()
    
    # Calcular el dígito verificador esperado
    expected_verificador = str((11 - int(rut_digits[::-1]) % 11) % 11)
    if expected_verificador == '10':
        expected_verificador = 'k'
    
    # Comparar el dígito verificador ingresado con el esperado
    if verificador != expected_verificador:
        raise ValidationError("El RUT ingresado no es válido.")
    
    if value in INVALID_RUTS:
        raise ValidationError("El RUT ingresado está en la lista de RUTs inválidos.")


class Especialidad(models.Model):
    nombre = models.CharField(verbose_name="nombre", max_length=200)

    unique_together = ('nombre')

    def __str__(self):
        return f'{self.nombre}'

class Centro(models.Model):
    nombre = models.CharField(verbose_name="nombre", max_length=200)

    unique_together = ('nombre')

    def __str__(self):
        return f'{self.nombre}'
    
class Medico(models.Model):
    nombre = models.CharField(verbose_name="nombre", max_length=200)
    email = models.EmailField(verbose_name="Email")
    run_regex = RegexValidator(
    regex=r'^\d{1,2}\.\d{3}\.\d{3}-\d{1}$',
    message="El número debe estar en el algunos de los siguientes formatos: '1.111.111-1' o '11.111.111-1'.")
    run = models.CharField(
        verbose_name="run",
        validators=[run_regex],
        max_length=12,
        null=True,
        blank=True)
    phone_regex = RegexValidator(
    regex=r'^\+569\d{8}$',
    message="El número debe estar en el siguiente formato,  '+56912345678'.")


    telefono = models.CharField(verbose_name="telefono",
                                validators=[phone_regex],
                                max_length=17, null=True, blank=True)
    especialidad = ForeignKey(Especialidad,
                               on_delete=models.CASCADE,
                               related_name='medicos')
    
    unique_together = ('run')

    
    def __str__(self):
        return f'{self.nombre}'

def validar_dia(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()

    if value < today:
        raise ValidationError('No es posible elegir una fecha anterior.')
    if (weekday == 5) or (weekday == 6):
        raise ValidationError('Elija un día laboral de la semana.')
    
def validate_real_rut(value):
    """
    Valida que el RUT ingresado sea un RUT válido y real.
    """
    if not validate_rut(value):
        raise ValidationError(_("El RUT ingresado no es válido."))

class Agenda(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    email = models.EmailField('E-mail')

    GENERO = (
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otro"),
        ("T", "Tanque T-64")
    )
    
    genero = models.CharField(max_length=11, choices=GENERO,)
    
    phone_regex = RegexValidator(
    regex=r'^\+569\d{8}$',
    message="El número debe estar en el siguiente formato,  '+56912345678'.")

    telefono = models.CharField(verbose_name="Telefono",
                                validators=[phone_regex],
                                max_length=17)
    run_regex = RegexValidator(
    regex=r'^\d{1,2}\.\d{3}\.\d{3}-\d{1}$',
    message="El número debe estar en el algunos de los siguientes formatos: '1.111.111-1' o '11.111.111-1'.")
    run = models.CharField(
        verbose_name="run",
        validators=[run_regex],
        max_length=12)
    centro = ForeignKey(Centro, on_delete=models.CASCADE, related_name='agenda')
    medico = ForeignKey(Medico, on_delete=models.CASCADE, related_name='agenda')
    dia = models.DateField(help_text="Introduzca una fecha para el calendario", validators=[validar_dia])
    
    HORARIOS = (
        ("1", "07:00 a 08:00"),
        ("2", "08:00 a 09:00"),
        ("3", "09:00 a 10:00"),
        ("4", "10:00 a 11:00"),
        ("5", "11:00 a 12:00"),
        ("6", "13:00 a 14:00"),
        ("7", "16:00 a 17:00"),
    )
    horario = models.CharField(max_length=10, choices=HORARIOS)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuario', 
        on_delete=models.CASCADE,
        null = True,
        blank = True,
        related_name='agendas'
    )
    class Meta:
        unique_together = ('centro','medico','horario', 'dia')

    @property
    def clean_run(self):
        try:
            validate_rut(self.run)
        except ValidationError as e:
            raise ValidationError({'run': e.message})
        
    def __str__(self):
        return f'{self.dia.strftime("%b %d %Y")} - {self.get_horario_display()} - {self.medico} - {self.centro}'