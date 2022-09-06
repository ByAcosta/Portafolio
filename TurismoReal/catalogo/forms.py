from django import forms
from django.forms import fields
from .models import Depto


class DeptoForm(forms.ModelForm):

    class Meta:
        model = Depto
        fields = '__all__'