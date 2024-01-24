from django import forms
from django.contrib.auth.forms import UserCreationForm

from catalog.models import Newspaper, Redactor


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", )
