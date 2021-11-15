import copy

from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from .forms import CustomUserCreationForm, ContactForm, ProblemForm, ChoiceForm, RequiredFormset
from .models import Subject, Problem, Choice, Like

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
    problemID_list = []
    for problem in problems:
        problemID_list.append(problem.id)
    context = {
        'subject': subject,
        'problems': problems,
        'problemID_list': problemID_list,
    }
    return render(request, 'app/mini_test.html', context)


def score_test(request, problem_count):
    if request.method == 'POST':
        correct_count = 0
        problems = []
        isCorrect_list1 = [False for _ in range(problem_count)]
        selected_choice_list = [-1 for _ in range(problem_count)]
        for p_c in range(problem_count):
            problem_id = request.POST.get('problemID-' + str(p_c + 1), False)
            selected_choice = int(request.POST.get('choice-' + str(p_c + 1), -1))
            selected_choice_list[p_c] = selected_choice
            if problem_id:
                problem = Problem.objects.get(id=problem_id)
                problems.append(problem)
                if problem.correct_choice == selected_choice:
                    correct_count += 1
                    isCorrect_list1[p_c] = True
        isCorrect_list2 = copy.deepcopy(isCorrect_list1)
        isCorrect_list1.reverse()
        isCorrect_list2.reverse()
        selected_choice_list.reverse()
        context = {
            'correct_count': correct_count,
            'problems': problems,
            'isCorrect_list1': isCorrect_list1,
            'isCorrect_list2': isCorrect_list2,
            'selected_choice_list': selected_choice_list,
        }
        return render(request, 'app/test_result.html', context)
    else:
        return redirect('app:index')


def like(request, pk):
    problem = Problem.objects.get(pk=pk)
    print(request.user.id)
    query = Like.objects.filter(user__id=request.user.id, problem__id=pk)
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

@login_required
def make_problem(request, pk):
    subject = Subject.objects.get(pk=pk)
    form = ProblemForm(request.POST or None)
    ChoiceFormSet = formset_factory(
        form=ChoiceForm,
        formset=RequiredFormset,
        extra=2,
    )
    print(request.POST)
    formset = ChoiceFormSet(request.POST or None)
    context = {
        'form': form,
        'formset': formset,
        'subject': subject,
    }
    print(formset.is_valid())
    if all([form.is_valid(), formset.is_valid()]):
        problem = form.save(commit=False)
        problem.user = request.user
        problem.subject = subject
        problem.like = Like.objects.create()
        problem.save()
        for form in formset:
            choice = form.save(commit=False)
            choice.problem = problem
            choice.save()
        return redirect('app:index')

    return render(request, 'app/make_problem.html', context)


def edit_problem(request):
    user = request.user
    problems = user.problem_set.all()
    print(problems)
    context = {'problems': problems}
    return render(request, 'app/my_problem.html', context)



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