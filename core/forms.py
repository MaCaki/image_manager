from django import forms

from .models import EyeLid


class EyelidForm(forms.ModelForm):
    """Form for bulk uploading images."""
    class Meta:
        model = EyeLid
        fields = ['image', 'tagline', 'patient']


class UploadImageForm(forms.Form):
    image = forms.ImageField()
    enctype = "multipart/form-data"
