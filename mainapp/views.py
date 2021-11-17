from django.shortcuts import render

from mainapp.models import Training, Weeks


def index(request):

    context = {
        'title': 'POWERGO',
    }
    return render(request, 'mainapp/index.html', context)


def training_list(request):
    traininglist = Training.objects.all()
    context = {
        'traininglist' : traininglist,
        'title': 'POWERGO',
    }
    return render(request, 'mainapp/training_list.html', context)


def training_page(request, pk):
    # items = SubjectCategory.all()
    trainingpage = Training.objects.get(pk=pk)
    weeks = Weeks.objects.filter(training_id=pk)
    context = {
        'trainingpage': trainingpage,
        'weeks': weeks,
        'title': 'Тренировки',
    }

    return render(request, 'mainapp/training_page.html', context)
