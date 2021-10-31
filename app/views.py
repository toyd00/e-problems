from typing import Text
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404

from .forms import CustomUserCreationForm, ContactForm, ProblemForm, ChoiceForm, ChoiceFormSet
from .models import Problem, Subject, Like

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


def miniTest(request, pk):
    subject = Subject.objects.get(pk=pk)
    problems = subject.problem_set.all()
    context = {
        'subject': subject,
        'problems': problems,
    }
    return render(request, 'app/problem.html', context)


def like(request, pk):
    problem = Problem.objects.get(pk=pk)
    print(request.user.id)
    query = Like.objects.filter(user__id=request.user.id, problem__id=pk)
    #print(query)
    response = {'button': 'いいね'}
    like = problem.like
    if query.count() == 0:
        like.count += 1
        like.user.add(request.user)
        like.save()
        response['button'] = 'いいね取り消し'
    else:
        like.count -= 1
        like.user.remove(request.user)
        like.save()

    response['like_count'] = like.count
    print(response)
    return JsonResponse(response)


def make_problem(request, pk):
    subject = Subject.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProblemForm(request.POST or None)
        form_set = ChoiceFormSet(request.POST or None)
        context = {
            'form': form,
            'form_set': form_set,
            'subject': subject,
        }
        if all([form.is_valid(), form_set.is_valid()]):
            problem = form.save(commit=False)
            problem.subject = subject
            problem.like = Like.objects.create()
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
            'subject': subject,
        }
    return render(request, 'app/make_problem.html', context)


def score_test(request):
    if request.method == 'POST':
        choices = request.POST.getlist('choice')
        count = 0
        for choice in choices:
            problem_id, selected_choice = map(int, choice.split('/'))
            problem = Problem.objects.get(id=problem_id)
            if problem.correct_choice == selected_choice:
                count += 1
        context = {'count': count}
        return render(request, 'app/test_result.html', context)
    else:
        return redirect('app:index')


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