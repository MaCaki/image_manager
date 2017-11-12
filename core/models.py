from django.db import models
from django.urls import reverse


class Region(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Study(models.Model):
    name = models.CharField(max_length=1000)
    region = models.ForeignKey(Region)
    description = models.TextField()

    def __str__(self):
        return "{}: {}".format(self.name, self.region)

    def get_absolute_url(self):
        return reverse('core:study-detail', kwargs={'pk': self.pk})


class Patient(models.Model):
    """An anonymized subject of a Trachoma study."""
    study = models.ForeignKey(Study)
    uid = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return str(self.uid)

    def get_absolute_url(self):
        return reverse('core:patient-detail', kwargs={'pk': self.pk})


class EyeLid(models.Model):
    """A wrapper around a stored image file of an eyelid."""
    tagline = models.TextField()
    uploaded = models.DateTimeField(auto_now=True)
    # TODO: redirect this to the default file storage for env.
    #  https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html
    image = models.ImageField()
    patient = models.ForeignKey(
        Patient,
        db_index=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "Image: {}, {}, {}".format(
            self.image, self.uploaded, self.patient
        )

    def get_absolute_url(self):
        return reverse('core:eyelid_detail', kwargs={'pk': self.pk})
