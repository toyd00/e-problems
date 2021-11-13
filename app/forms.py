from django import forms
from django.db.models import fields
from django.forms import BaseFormSet
from django.forms.models import modelformset_factory
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
        fields = ['content']

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=Textarea)


class RequiredFormset(forms.BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormset, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False