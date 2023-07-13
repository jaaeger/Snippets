from django.forms import ModelForm
from MainApp.models import Snippet
from django.forms.widgets import TextInput, Textarea, CheckboxInput
from django import forms
from django.contrib.auth.models import User


class SnippetForm(ModelForm):

    class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code', 'is_published', 'private']
       widgets = {
           'name': TextInput(attrs={"class": "form-control form-control-lg", 'placeholder': 'Название сниппета'}),
           'lang': TextInput(attrs={"class": "btn btn-secondary dropdown-toggle", 'placeholder': 'Название языка'}),
           'code': Textarea(attrs={"class": "col", 'placeholder': 'Код сниппета'}),
       }
       labels = {
           'name': ''
       }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']: raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    class Meta:
        model = User
        fields = ['username']
