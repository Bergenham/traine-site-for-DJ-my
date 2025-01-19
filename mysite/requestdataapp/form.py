from django import forms
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile


class UerBioForm(forms.Form):
    username = forms.CharField(label='Username ', min_length=1, max_length=12)
    age = forms.IntegerField(label='Age ', min_value=1, max_value=99)
    bio = forms.CharField(label='Your biography', widget=forms.Textarea)


class UserSendFile(forms.Form):
    file = forms.FileField()

    def validate_F_N(file: InMemoryUploadedFile) -> None:
        if file.name and 'virus' in file.name:
            raise ValidationError('File contains virus')
