from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import UserProfile, Skill, Language, Hobby
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout


def index(request):
    users = UserProfile.objects.all()
    context = {
        'users': users,
    }
    return render(request, template_name='candidates/index.html', context=context)


class ViewUser(DetailView):
    model = UserProfile
    context_object_name = 'user_item'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрированы!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации! Попробуте еще раз!')
    else:
        form = UserRegisterForm()
    return render(request, 'candidates/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm
    return render(request, 'candidates/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')

