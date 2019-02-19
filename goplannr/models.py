from django.db import models
# Create your models here.

class DoctorsDb(models.Model):

    doc_name = models.CharField(max_length=50, primary_key=True)
    specialization = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    availability = models.CharField(max_length=50)
    rating = models.FloatField()
    desc = models.TextField()

    def __str__(self):

        return self.doc_name

class Appointment(models.Model):

    patient = models.CharField(max_length=50)
    doc_name = models.ForeignKey(DoctorsDb, on_delete=models.CASCADE)

    def __str__(self):

        return self.patient
