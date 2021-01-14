from django import forms
from django.forms import ModelForm

from apps.models import Person


class UserForm(forms.Form):
    name = forms.CharField(label_suffix="_Имя", help_text="Введите свое имя", min_length=2, max_length=20,
                           widget=forms.TextInput(attrs={"class": "myfield"}))
    age = forms.IntegerField(label="Возраст", help_text="Введите свой возраст", max_value=100, min_value=18)
    # time = forms.SplitDateTimeField()
    # comment = forms.CharField(label="Комментарий", widget=forms.Textarea)
    field_order = ["age", "name"]


class PersonUserForm(forms.Form):
    name = forms.CharField(label="Введите имя")
    age = forms.IntegerField(label="Возраст")
    field_order = ["age", "name"]
