from django.db import models


class Image(models.Model):

    name = models.CharField(max_length=200)
    tagline = models.TextField()
    uploaded = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to="")


class Patient(models.Model):

    patient_id = models.Integer()