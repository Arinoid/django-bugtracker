from django.forms import ModelForm
from .models import *


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['status'].queryset = Status.objects.filter()


class TicketCreateForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'text']