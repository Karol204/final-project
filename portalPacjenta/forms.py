from django import forms
from django.core.exceptions import ValidationError
from .models import Lekarz, Placówka, Konsultacja, Profil
import datetime

def password_validation(value):
    if len(value) < 8:
        raise ValidationError("za krótkie hasło co najmniej 8 znaków")



class DateInput(forms.DateInput):
    input_type = 'date'

class VisitReservationForm(forms.ModelForm):


    def clean(self):
        clean_data = super().clean()
        data = clean_data['date']
        lekarz = clean_data['doc']
        time = clean_data['time']
        if Konsultacja.objects.filter(date=data, doc=lekarz, time=time).count() > 0:
            raise ValidationError("lekarz zajety")

    class Meta:
        model = Konsultacja
        exclude=['patient']
        widgets ={'date': DateInput}



class profilForm(forms.ModelForm):
    class Meta:
        model = Profil
        exclude = ['user']

