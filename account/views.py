from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.utils.datetime_safe import datetime

from account.forms import LoginForm, UserRegistrationForm, UserEditForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
    user_form = UserCreationForm(request.POST)
    if request.method == "POST":  # после отправки формы
        user_form = UserCreationForm(request.POST)
    if user_form.is_valid():  # валидация полей формы
        reg_f = user_form.save(commit=False)  # не сохраняем данные формы
        reg_f.is_staff = False  # запрещен вход в административный раздел
        reg_f.is_active = True  # активный пользователь
        reg_f.is_superuser = False  # не является суперпользователем
        reg_f.date_joined = datetime.now()  # дата регистрации
        reg_f.last_login = datetime.now()  # дата последней авторизации

        reg_f.save()  # сохраняем изменения после добавления данных (добавление пользователя в БД пользователей)

        return render(request, 'account/register_done.html', {'user_form': user_form})
    else:
        user_form = UserCreationForm()  # создание объекта формы для ввода данных нового пользователя
    assert isinstance(request, HttpRequest)
    return render(request, 'account/register.html', {'user_form': user_form, 'year': datetime.now().year, }
                  )


# def edit(request):
#     person = User.objects.get(id=request.user.id)
#     user_form = UserEditForm(
#         initial={'first_name': person.username, 'last_name': person.last_name, 'email': person.email})
#     if request.method == 'POST':
#         if user_form.is_valid():
#             # reg_f = user_form.save(commit=False)  # не сохраняем данные формы
#             person.is_staff = False  # запрещен вход в административный раздел
#             person.is_active = True  # активный пользователь
#             person.is_superuser = False  # не является суперпользователем
#             person.date_joined = datetime.now()  # дата регистрации
#             person.last_login = datetime.now()  # дата последней авторизации
#
#             person.username = request.POST.get('first_name')
#             person.last_name = request.POST.get('last_name')
#             person.email = request.POST.get('email')
#             person.save()  # сохраняем изменения после добавления данных (добавление пользователя в БД пользователей)
#     else:
#         user_form = UserEditForm(
#             initial={'first_name': person.username, 'last_name': person.last_name, 'email': person.email})
#     return render(request, 'account/edit.html', {'user_form': user_form})

def edit(request):
    if request.method == "POST":
        person = User.objects.get(id=request.user.id)
        user_forms = UserEditForm(request.POST, instance=person)
        if user_forms.is_valid():
            user_forms.save(commit=False)
            person.first_name = request.POST.get("first_name")
            person.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_forms = UserEditForm()
    return render(request, 'account/edit.html', {'user_forms': user_forms})
