from django import forms

from landing.models import Address
from .models import Reservation


class ReservationForm(forms.ModelForm):
    name = forms.CharField(required=False)
    guests = forms.IntegerField(required=False)
    address = forms.ModelChoiceField(queryset=Address.objects.all(), required=False)

    class Meta:
        model = Reservation
        fields = forms.ALL_FIELDS
