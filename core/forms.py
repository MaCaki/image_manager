from django import forms

from .models import (
    EyeLid,
    PatientGrade
)


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


class PatientGradeForm(forms.ModelForm):
    """Create a form for all entries required for a Grade object.

    https://jacobian.org/writing/dynamic-form-generation/
    """

    pass