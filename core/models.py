from django.db import models

# Create your models here.

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=200)
    experience=models.IntegerField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    number=models.CharField(max_length=15)

    def __str__(self):
        return self.name
    

class Appointment(models.Model):
    Patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Date=models.DateField()
    Time=models.TimeField()

    def __str__(self):
        return f"{self.Patient}-{self.Doctor}"