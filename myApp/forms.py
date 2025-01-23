from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, FormMaker
from django import forms



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('name','email',)


class FormMakerForm(forms.ModelForm):
    class Meta:
        model = FormMaker
        fields = ('image',
                  'mobile',
                  'objective',
                  'skills',
                  'tools',
                  'projects',
                  'education',
                  'customuser',
                  )

