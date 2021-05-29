from django.shortcuts import render, redirect
#імпортуємо модуль створення форми авторизації користувачів
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def  home(request):
    return render (request, 'todo/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html',  {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html',  {'form':UserCreationForm(), 'error':'Таке ім\'я користувача вже використовується '})
        else:
            print('Привіт')
            #вивести повідомлення про неспівпадання паролів
            return render(request, 'todo/signupuser.html',  {'form':UserCreationForm(), 'error':'Паролі не співпадають'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html',  {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html',  {'form':AuthenticationForm(), 'error':'Пару логін/пароль не знайдено'})
        else:
            login(request, user)
            return redirect('currenttodos')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')
