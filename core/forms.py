from django import forms


class ImageFieldForm(forms.Form):
    """Form for bulk uploading images."""
    file_field = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )
