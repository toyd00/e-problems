from typing import Text
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .form import CustomUserCreationForm, ContactForm, ProblemForm, ChoiceForm, ChoiceFormSet
from .models import Problem, Subject

from users.models import CustomUser


def index(request):
    subjects = Subject.objects.all()
    return render(request, 'app/index.html', {'subjects': subjects})

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            input_email = form.cleaned_data['email']
            input_password = form.cleaned_data['password1']
            new_user = authenticate(
                email=input_email,
                password=input_password,
            )
            if new_user is not None:
                login(request, new_user)
                return redirect('app:user', pk=new_user.pk)
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/signup.html', {'form': form})

def user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    return render(request, 'app/user.html', {'user': user})

def subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    return render(request, 'app/subject.html', {'subject': subject})

def problem(request, pk):
    """
    subject = get_object_or_404(Subject, pk=pk)
    problems = subject.objects.all().filter(subject__name=subject.name)
    """
    subject = Subject.objects.get(pk=pk)
    problems = subject.problem_set.all()
    return render(request, 'app/problem.html', {'problems': problems})

def make_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST or None)
        form_set = ChoiceFormSet(request.POST or None)
        context = {
            'form': form,
            'form_set': form_set,
        }
        if all([form.is_valid(), form_set.is_valid()]):
            problem = form.save(commit=False)
            problem.save()
            for form in form_set:
                choice = form.save(commit=False)
                choice.problem = problem
                choice.save()
            return redirect('app:index')
    else:
        context = {
            'form': ProblemForm(),
            'formset': ChoiceFormSet(),
        }
    return render(request, 'app/make_problem.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            recipients = ['taishi.castle@gmail.com']

            send_mail(subject, message, email, recipients)
            return redirect('app:thank')
    else:
        form = ContactForm()
    return render(request, 'app/contact.html', {'form': form})


def thank(request):
    thank_message = "お問い合わせありがとうございました。"
    return render(request, 'app/thank.html', {'thank_message': thank_message})