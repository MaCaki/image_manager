from django.db import models
from django.urls import reverse

class Region(models.Model):
    name = models.CharField(max_length=1000)


class Study(models.Model):
    name = models.CharField(max_length=1000)
    location = models.ForeignKey(Region)
    description = models.TextField()


class Patient(models.Model):
    """An anonymized subject of a Trachoma study."""
    study = models.ForeignKey(Study)
    patient_uid = models.IntegerField(default=0)


class EyeLid(models.Model):
    """A wrapper around a stored image file of an eyelid."""
    tagline = models.TextField()
    uploaded = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('core:eyelid_detail', kwargs={'pk': self.pk})
