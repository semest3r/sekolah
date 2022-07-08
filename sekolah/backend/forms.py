from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm



class FormProfile(forms.ModelForm):
    class Meta:
        Model = User
        fields = ['username', 'first_name', 'last_name']