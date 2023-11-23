from django.conf import settings
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.core.validators import RegexValidator
from django.db import models
from medicos.models import Agenda

class Cliente(models.Model):
    name = models.CharField('Nombre', max_length=100)
    email = models.EmailField('E-mail', unique=True)
    GENERO = (
        ("M", "Masculino"),
        ("F", "Femenino")
    )
    
    genero = models.CharField(max_length=9, choices=GENERO,)
    
    phone_regex = RegexValidator(
    regex=r'^\+?56?9?\d{8}$',
    message="El número debe estar en el siguiente formato,  '+56912345678'.")

    telefono = models.CharField(verbose_name="Telefono",
                                validators=[phone_regex],
                                max_length=17, null=True, blank=True)
    run = models.CharField(verbose_name="run",
                    max_length=50,
                    unique=True,)
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuario', 
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f'{self.user.name}'
    
class Consulta(models.Model):
    agenda =  OneToOneField(Agenda, on_delete=models.CASCADE, related_name='consulta')
    cliente = ForeignKey(Cliente, on_delete=models.CASCADE, related_name='consulta')
    
    class Meta:
        unique_together = ('agenda', 'cliente')
        
    def __str__(self):
        return f'{self.agenda} - {self.cliente}'
