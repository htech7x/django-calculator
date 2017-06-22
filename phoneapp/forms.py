from django import forms
from phoneapp.models import Phonebook

class PhonebookForm(forms.ModelForm):

    class Meta:
        model = Phonebook
