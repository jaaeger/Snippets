from django.forms import ModelForm
from MainApp.models import Snippet
from django.forms.widgets import TextInput, Textarea


class SnippetForm(ModelForm):

    class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code', 'is_published']
       widgets = {
           'name': TextInput(attrs={"class": "form-control form-control-lg", 'placeholder': 'Название сниппета'}),
           'lang': TextInput(attrs={"class": "btn btn-secondary dropdown-toggle", 'placeholder': 'Название языка'}),
           'code': Textarea(attrs={"class": "col", 'placeholder': 'Код сниппета'}),
       }
       labels = {
           'name': ''
       }
