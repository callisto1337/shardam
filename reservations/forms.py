from django import forms

from .models import Reservation


class ReservationForm(forms.ModelForm):
    name = forms.CharField(required=False)
    guests = forms.IntegerField(required=False)
    address = forms.IntegerField(required=False)

    class Meta:
        model = Reservation
        fields = forms.ALL_FIELDS
