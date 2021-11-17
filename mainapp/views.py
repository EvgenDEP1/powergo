from django.shortcuts import render

from mainapp.models import Training


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
