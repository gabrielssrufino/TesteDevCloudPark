from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Ticket(models.Model):


    class Priority(models.TextChoices):
        BAIXA = 'Baixa',
        MEDIA = 'Média',
        ALTA = 'Alta'


    class Status(models.TextChoices):
        ABERTO = 'Aberto',
        PROGRESSO = 'Em Atendimento',
        RESOLVIDO = 'Resolvido',
        CANCELADO = 'Cancelado',

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=521, null=True, blank=True)
    priority = models.CharField(max_length=10, choices=Priority.choices)
    sector = models.CharField(max_length=120, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tickets')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_assigned_tickets')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_updated_tickets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.pk}. {self.title}'