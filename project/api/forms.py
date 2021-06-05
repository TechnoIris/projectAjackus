from .models import *
from django import forms

class UserRegister(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('email', 'password', 'fullName', 'phone', 'city', 'state', 'country', 'pincode')

class UploadItem(forms.ModelForm):
    class Meta:
        model = Contitem
        fields = ('title', 'body', 'summary', 'pdf')
