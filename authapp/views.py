from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from authapp.forms import LoginForm, RegisterForm


def login(request):
    if request.method == 'POST' and request.is_ajax():
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            # return HttpResponseRedirect(reverse('mainapp:index'))
            return JsonResponse({
                'status': True,
                'messages': 'Вы успешно авторизировались!'
            })
        else:
            return JsonResponse({
                'status': False,
                'messages': 'Проверьте имя пользователя и пароль!'
            })
    else:
        form = LoginForm()

    context = {
        'form': form,
        'title': 'авторизация',
    }
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        form = RegisterForm()
    context = {
        'title': 'регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))


