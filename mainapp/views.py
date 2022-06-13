from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from powergo import settings

from django.shortcuts import render

from mainapp.models import Training, Weeks, Day, Exercises, Category

from mainapp.forms import MailForm


def index(request):

    context = {
        'title': 'POWERGO',
    }
    return render(request, 'mainapp/index.html', context)


@login_required
def support(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            message = f'От: {form.name} ({form.email})\nСообщение: {form.text}\n'
            send_mail(settings.EMAIL_TITLE, message, settings.EMAIL_HOST_USER, ['jen_dostovalov@mail.ru'])
            if send_mail:
                form.save()
                messages.success(request, 'Вы успешно отправили письмо!')
                return HttpResponseRedirect(reverse('index'))
    else:
        form = MailForm()
    context = {
        'title': 'POWERGO',
        'form': form,
    }
    return render(request, 'mainapp/support.html', context)


def training_list(request):
    traininglist = Training.objects.all()
    context = {
        'traininglist': traininglist,
        'title': 'POWERGO',
    }
    return render(request, 'mainapp/training_list.html', context)


def training_page(request, pk):
    trainingpage = Training.objects.get(pk=pk)
    weeks = Weeks.objects.filter(training_id=pk)
    day = Day.objects.filter(training_id=pk)
    exercises = Exercises.objects.filter(day_id=pk)
    cat = Category
    context = {
        'trainingpage': trainingpage,
        'weeks': weeks,
        'day': day,
        'exercises': exercises,
        'cat': cat,
        'title': 'POWERGO',
    }

    return render(request, 'mainapp/training_page.html', context)


@login_required
def training_day_page(request, pk):
    day = Day.objects.get(pk=pk)
    exercises = Exercises.objects.filter(day_id=pk)
    # trainingpage = Training.objects.get(pk=pk)
    context = {
        'day': day,
        'exercises': exercises,
        # 'trainingpage': trainingpage,
        'title': 'Тренировки',
    }

    return render(request, 'mainapp/training_day_page.html', context)
