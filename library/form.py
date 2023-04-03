from django.forms import ModelForm, Form
from django import forms
from .models import Books

class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'


class LoginForm(Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)