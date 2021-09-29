from django.shortcuts import redirect, render, get_object_or_404
from .models import Problem, Subject
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def index(request):
    subjects = Subject.objects.all()
    return render(request, 'app/index.html', {'subjects': subjects})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']
            new_user = authenticate(
                username=input_username,
                password=input_password,
            )
            if new_user is not None:
                login(request, new_user)
                return redirect('app:user', pk=new_user.pk)
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})

def user(request, pk):
    user = get_object_or_404(User, pk=pk)
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

