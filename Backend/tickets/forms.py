from django import forms
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'priority', 'sector', 'status', 'assigned_to']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'priority': forms.Select(),
            'status': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].choices = [
            (value, label) for value, label in self.fields['status'].choices
            if value != 'Resolvido'
        ]
        self.fields['assigned_to'].queryset = User.objects.filter(groups__name='Tecnico')
