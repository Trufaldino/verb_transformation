from django import forms
from .models import VerbTense

class VerbTenseForm(forms.ModelForm):
    class Meta:
        model = VerbTense
        fields = ['tense', 'verb']
