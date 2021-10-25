from django import forms
from django.db.models import fields
from django.forms.widgets import Textarea
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Problem, Choice


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username']

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['type', 'content', 'made_date', 'correct_choice']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'


ChoiceFormSet = forms.inlineformset_factory(
    parent_model=Problem,
    model=Choice,
    form=ChoiceForm,
    extra=2,
    fields='__all__',
    exclude=None,
)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=Textarea)