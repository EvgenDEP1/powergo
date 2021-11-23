from django.shortcuts import render

from mainapp.models import Training, Weeks, Day, Exercises, Category


def index(request):

    context = {
        'title': 'POWERGO',
    }
    return render(request, 'mainapp/index.html', context)


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
        'title': 'Тренировки',
    }

    return render(request, 'mainapp/training_page.html', context)


def training_day_page(request, pk):
    day = Day.objects.get(pk=pk)
    exercises = Exercises.objects.filter(day_id=pk)
    context = {
        'day': day,
        'exercises': exercises,
        'title': 'Тренировки',
    }

    return render(request, 'mainapp/training_day_page.html', context)
