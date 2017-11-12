from django import forms

from .models import EyeLid


class EyelidForm(forms.ModelForm):
    """Form for bulk uploading images."""
    class Meta:
        model = EyeLid
        fields = ['image']


class UploadImageForm(forms.Form):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={'multiple': True}
        )
    )
