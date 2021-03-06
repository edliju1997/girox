from django.db import models
from django.shortcuts import resolve_url as r
from django.conf import settings
from girox.event.validators import validate_cpf


class Event(models.Model):
    title = models.CharField('título', max_length=255)
    description = models.TextField('descrição')
    resume = models.TextField('resumo', blank=True, null=True)
    date = models.DateTimeField('data do evento')
    date_limit_subscription = models.DateTimeField('data limite de inscrição')
    number_limit_subscription = models.PositiveIntegerField('quantidade limite de inscrições', help_text='Zero para quantidade ilimitada!', default=0)
    image = models.ImageField('imagem', upload_to='events/', null=True, blank=True)
    organizers = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='organizadores')

    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'
        ordering = ('-date',)

    def __str__(self):
        return self.title


class EventSponsorsImage(models.Model):
    event = models.ForeignKey(Event, related_name='sponsors')
    image = models.ImageField('imagem', upload_to='events/sponsors/')

    class Meta:
        verbose_name = 'patrocinador'
        verbose_name_plural = 'patrocinadores'

    def __str__(self):
        return self.image.url


class Subscription(models.Model):
    name = models.CharField('nome', max_length=255)
    rg = models.CharField('RG', max_length=20)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf], help_text='(Necessário para o seguro)', db_index=True)
    date_of_birth = models.DateField('data nascimento', help_text='(Necessário para o seguro)')
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20)
    address = models.CharField('endereço', max_length=255)
    city = models.CharField('cidade-UF', max_length=255)
    team = models.CharField('equipe', null=True, blank=True, max_length=255)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    event = models.ForeignKey('Event', verbose_name='evento', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'
        ordering = ('-created_at',)
        unique_together = (("rg", "event"), ("cpf", "event"))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('events:subscription_detail', self.event.pk, self.pk)


class SubscriptionProxy(Subscription):
    class Meta:
        proxy = True
        verbose_name = 'participante'
        verbose_name_plural = 'participantes'
