from socket import fromshare
from LAB.models import Appointment
from django import forms


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
