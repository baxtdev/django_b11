from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from accounts.models import CustomUser as User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, 'Пароли не совпадают')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже есть')
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, 'Регистрация успешна! Теперь войдите.')
        return redirect('login')

    return render(request, 'accounts/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('news-list')
        else:
            messages.error(request, 'Неверный логин или пароль')
            return redirect('login')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


