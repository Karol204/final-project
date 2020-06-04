from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import datetime
# Create your models here.

def date_validation(value):
    if value < datetime.date.today():
        raise ValidationError("Wybrana data jest z przeszłości")

class Profil(models.Model):
    name = models.CharField(max_length=24)
    surname = models.CharField(max_length=24)
    mail = models.EmailField()
    phone = models.CharField(max_length=18)
    med_first = models.ForeignKey('Lekarz', on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} {self.surname}"

class Specialization(models.Model):
    name =  models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class Lekarz(models.Model):
    name = models.CharField(max_length=24)
    surname = models.CharField(max_length=24)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"



class Placówka(models.Model):
     city = models.CharField(max_length=64)
     region = models.CharField(max_length=64)
     address = models.CharField(max_length=126, null=True)
     kontakt = models.IntegerField(null=True)
     email = models.EmailField(null=True)
     doc = models.ManyToManyField('Lekarz')
     patient = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

     def __str__(self):
         return f"{self.city} {self.address}"

class Konsultacja(models.Model):
    date = models.DateField(validators=[date_validation])
    time = models.TimeField()
    description = models.CharField(max_length=240, null=True)
    place = models.ForeignKey(Placówka, on_delete=models.CASCADE)
    doc = models.ForeignKey(Lekarz, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)